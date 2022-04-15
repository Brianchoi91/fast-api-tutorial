from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password:str):
    return pwd_context.hash(password)

#Take in the raw password and hash and check against the hashed pw from db
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
