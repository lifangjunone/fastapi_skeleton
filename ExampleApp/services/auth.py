import os
import jwt
import time
import binascii
from conf.default import config
from typing import Union, Tuple, Any
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from utils.time_utils import convert_iso_to_custom_format


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_secret(random = 24) -> bytes:
    """
    获取 secret
    :param random: 随机数
    """
    return binascii.hexlify(os.urandom(random))


def sign_jwt(user_id: Union[str, int], username: str = None, expires_in: timedelta = timedelta(minutes=10)) -> Union[str, None]:
    """
    生成 JWT 签名
    :param user_id: 用户ID
    :param username: 用户名
    :param expires_in: JWT 过期时间间隔，默认为 10 分钟
    :return: JWT token 或 None
    """
    if not user_id:
        return None
    # 设置 JWT 过期时间
    expiration = datetime.now(timezone(timedelta(hours=8))) + expires_in
    payload = {
        "user_id": str(user_id),
        "username": username or str(user_id),
        "expires": expiration.isoformat(),  # 使用 ISO 格式保存时间
        "date_format": convert_iso_to_custom_format(expiration.isoformat())
    }
    # 生成并返回 JWT token
    return jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)


def decode_jwt(token: str) -> Tuple[bool, Any]:
    """
    解码JWT令牌并验证其有效性。
    :param token: JWT token,要解码的JWT令牌。
    :return
        Tuple[bool, Any]:
            - 布尔值，指示解码是否成功。
            - 解码后的token字典，如果失败，返回错误信息。
    """
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
        # Extract expiration time and convert it to a datetime object
        expiration = datetime.fromisoformat(decoded_token["expires"]).replace(tzinfo=timezone.utc)
        # Check if the token is expired
        if expiration >= datetime.now(timezone.utc):
            return True, decoded_token  # Success, return decoded token
        else:
            return False, "Token has expired"  # Failure due to expiration
    except jwt.ExpiredSignatureError:
        return False, "Token has expired"  # Specific error message for expired token
    except jwt.InvalidTokenError:
        return False, "Invalid token"  # Specific error message for invalid token
    except Exception as e:
        return False, str(e)  # Return a generic error message


def verify_password(plain_password, hashed_password) -> bool:
    """
    验证密码是否正确
    :param plain_password: <PASSWORD> 明文密码
    :param hashed_password: <PASSWORD> 哈希密码
    :returns bool, 验证是否通过
    """
    if not plain_password: return False
    if not isinstance(plain_password, str):
        plain_password = str(plain_password)
    return pwd_context.verify(plain_password, hashed_password)


def password_hash(password: Any) -> str:
    """
    生成密码对应的hash值
    :param password: <PASSWORD> 明文密码
    :returns str: 密码hash值
    """
    return pwd_context.hash(str(password))


if __name__ == '__main__':
    # token_ = sign_jwt(1)
    # print(token_)
    # print(decode_jwt(token_)[1].get("date_format"))
    ph = password_hash(12345)
    print(ph)
    print(verify_password(12345, ph))
