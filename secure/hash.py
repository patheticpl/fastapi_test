import bcrypt
from passlib.context import CryptContext
from fastapi.security import APIKeyHeader

context = CryptContext(schemes=["bcrypt"], deprecated="auto")
apikey_header = APIKeyHeader(name="Authorization")