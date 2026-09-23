from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app=FastAPI()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

fake_user = {
    "username": "rahma",
    "password": "1234",
    "role": "admin"
}


@app.get("/")
def home():
    return {"message": "AI Agent Platform Security API is running"}



@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if(
        form_data.username != fake_user["username"] or
        form_data.password != fake_user["password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": "my-secret-token",
        "token_type": "bearer",
        "role": fake_user["role"]
    }


@app.get("/admin")
def admin_route(token: str = Depends(oauth2_scheme)):

    if fake_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return {
        "message": "Welcome to the admin area"
    }



@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {
        "message": "You have access to the protected route",
        "token": token
    }