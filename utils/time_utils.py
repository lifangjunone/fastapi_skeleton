import time
from datetime import datetime


def current_timestamp() -> int:
    """
    获取当前的时间戳（毫秒级）
    """
    return int(time.time() * 1000)


def timestamp_to_date_str(timestamp, format_string="%Y-%m-%d %H:%M:%S") -> str:
    """
    时间戳转日期字符串
    """
    if not timestamp:
        timestamp = time.time()
    if not isinstance(timestamp, int):
        try:
            timestamp = int(timestamp)
        except ValueError:
            timestamp = time.time()
    if timestamp > 1e10:
        timestamp = timestamp / 1000
    time_array = time.localtime(timestamp)
    date = time.strftime(format_string, time_array)
    return date


def convert_iso_to_custom_format(iso_time_str: str) -> str:
    """
    将ISO格式的时间字符串转换为指定格式：年-月-日 时：分：秒

    :param iso_time_str: ISO格式的时间字符串
    :return: 格式化后的时间字符串
    """
    # 将ISO格式字符串解析为datetime对象
    dt = datetime.fromisoformat(iso_time_str)
    # 转换为指定格式
    formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time


def format_datetime(datetime_obj: datetime = None) -> str:
    """
    datetime格式化
    """
    if not datetime_obj: return ""
    if isinstance(datetime_obj, datetime):
        return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(datetime_obj, str):
        return datetime_obj


if __name__ == '__main__':
    # iso_time_str_ = '2024-10-04T22:37:08.236543+08:00'
    # formatted_time_ = convert_iso_to_custom_format(iso_time_str_)
    # print(formatted_time_)
    print(current_timestamp())