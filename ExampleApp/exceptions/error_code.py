from enum import Enum


class ErrorCode(Enum):
    ACCOUNT_OR_PASSWORD_ERROR = 10010
    TOKEN_MISS_ERROR = 10101
    TOKEN_INVALID_ERROR = 10102


ERROR_CODE = ErrorCode