from enum import Enum


class HTTPMethods(str, Enum):
    CONNECT = 'CONNECT'
    DELETE = 'DELETE'
    GET = 'GET'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'
    TRACE = 'TRACE'

class FormConstants(str, Enum):
    EMAIL_TITLECASE = 'Email'
    EMAIL_LOWERCASE = 'email'
    PASSWORD_TITLECASE = 'Password'
    PASSWORD_LOWERCASE = 'password'

    LOGIN_CREDENTIALS_ERROR_MSG = 'Invalid email or password'
    LOGIN_SUCCESS_MSG = 'Account created for %s'

class URL_ROUTES(str, Enum):
    BASE_URL = '/'

    HOME_URL = BASE_URL + 'home'
    LOGIN_URL = BASE_URL + 'login'
    REGISTRATION_URL = BASE_URL + 'registration'