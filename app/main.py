from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from DevOps Multi-Cloud Demo!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/env")
def env():
    # exposes non-sensitive environment info if present
    return {
        "ENV": os.getenv("ENV", "dev"),
        "VERSION": os.getenv("VERSION", "v1")
    }

