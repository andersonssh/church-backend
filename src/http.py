"""
Validadores http e constantes
"""
from functools import wraps
from enum import Enum
from flask import request, abort
import jsonschema


HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
HTTP_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_INTERNAL_ERROR = 500


class MimeTypes(Enum):
    """[summary]

    Args:
        Enum ([type]): [description]
    """
    JSON = "application/json"


def validate_content(schema: dict, content_type: MimeTypes):
    """
    Valida a requisicao
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.content_type != content_type.value:
                abort(HTTP_UNSUPPORTED_MEDIA_TYPE)

            try:
                jsonschema.validate(instance=request.json, schema=schema)
            except jsonschema.ValidationError as validation_error:
                return {"message": validation_error.message}, HTTP_BAD_REQUEST

            return func(*args, **kwargs)

        return wrapper
    return decorator
