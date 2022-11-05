from rest_framework import status
from rest_framework.exceptions import APIException

from menel.api.error_codes import ErrorCode


class CoreAPIException(APIException):
    def __init__(self, code=None, message=None, **kwargs) -> None:
        detail = {
            "code": code,
            "message": message,
            "extra": kwargs,
        }

        self.detail = {"detail": detail}


class APINotImplemented(CoreAPIException):
    status_code = status.HTTP_501_NOT_IMPLEMENTED
    code = ErrorCode.APINotImplemented
    message = "API not implemented."

    def __init__(self, message=message, code=code, **kwargs) -> None:
        super().__init__(message=message, code=code, **kwargs)
