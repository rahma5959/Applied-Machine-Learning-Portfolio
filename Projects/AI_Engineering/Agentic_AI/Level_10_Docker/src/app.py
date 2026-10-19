from fastapi import FastAPI

app=FastAPI(title="docker Demo app")

@app.get("/")
def home():
    return{
        "message":"hello from fast api running from "
    }

@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }