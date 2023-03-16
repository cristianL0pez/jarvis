from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
import os

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
JWT_SECRET = os.environ["JWT_SECRET"]

# Mock user database
USERS = {
    "user1": {
        "username": "user1",
        "password": "password1",
        "is_active": True,
        "is_paid": True,
    },
    "user2": {
        "username": "user2",
        "password": "password2",
        "is_active": True,
        "is_paid": False,
    },
}

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    is_active: bool = True
    is_paid: bool = False

# Endpoint para generar token de acceso
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    if not user.get("is_active"):
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    if not user.get("is_paid"):
        raise HTTPException(status_code=400, detail="Pago pendiente")
    if user.get("password") != form_data.password:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    token_data = {"sub": user["username"]}
    access_token = jwt.encode(token_data, JWT_SECRET)
    return {"access_token": access_token, "token_type": "bearer"}

# Decorador de autenticación
def authenticate_user(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        username = payload["sub"]
        user = USERS.get(username)
        if not user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        return User(**user)
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Decorador de autorización
def require_payment(user: User = Depends(authenticate_user)):
    if not user.is
