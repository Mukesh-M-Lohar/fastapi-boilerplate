from starlette import status

from core.exceptions import CustomException


class UnauthorizedException(CustomException):
    code = status.HTTP_401_UNAUTHORIZED
    error_code = "UNAUTHORIZED"
    message = ""
