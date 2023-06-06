from fastapi import APIRouter
import httpx

api = APIRouter()


@api.get("/")
async def home():
    return {"message": "FastApi Home"}


@api.get("/foobar")
async def foobar():
    return {"message": "hello world"}


@api.get("/call-google")
def call_google():
    with httpx.Client() as client:
        response = client.get("https://www.google.com")
    return response.status_code
