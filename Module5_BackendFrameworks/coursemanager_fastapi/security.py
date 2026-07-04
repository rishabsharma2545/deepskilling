# 87. In a security.py utility file, implement: get_password_hash(password: str) -> str using passlib's 
# CryptContext with bcrypt scheme, and verify_password(plain_password, hashed_password) -> bool.

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# 91. Creates a JWT token using python-jose with an expiry of 30 minutes, and returns {'access_token': token, 'token_type': 'bearer'}.

from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

'''
Passwords are hashed using bcrypt instead of MD5 or SHA-256.
bcrypt is specifically designed for password storage because it
automatically uses a salt and is intentionally slow, making
brute-force and rainbow-table attacks much harder. MD5 and SHA-256
are fast hashing algorithms intended for data integrity, not for
securely storing passwords.
'''