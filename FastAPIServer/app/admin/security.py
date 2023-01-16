import secrets
import string
from typing import Union, Any
from datetime import datetime, timedelta

import jwt
import shortuuid
from passlib.context import CryptContext
from app.admin.utils import utc_seoul


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']     # should be kept secret
JWT_SECRET_KEY = "JWT_SECRET_KEY"
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = "JWT_REFRESH_SECRET_KEY"
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def myuuid():
    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)
    return su.random(length=8)


def get_hashed_password(plain_password: str) -> str:
    return password_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    return password_context.verify(plain_password, hashed_password)


def generate_token(subject: Union[str, Any], expires_delta: int = None):
    if expires_delta is not None:
        expires_delta = utc_seoul() + expires_delta
    else:
        expires_delta = utc_seoul() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {'exp': expires_delta, 'sub': str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    print(f'발급된 토큰 {encoded_jwt}')
    return encoded_jwt


def generate_token_secrets():
    return secrets.token_urlsafe(32)    # python 3.8 기준으로 DEFAULT_ENTROPY == 32


def refresh_token(subject: Union[str, Any], expires_delta: int = None):
    pass


def get_expiration_data():
    return utc_seoul() + timedelta(dats=3)

