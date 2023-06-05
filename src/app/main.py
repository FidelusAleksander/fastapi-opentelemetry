import fastapi
import httpx
from app.utils.otel import instrument_opentelemetry
import uvicorn

app = fastapi.FastAPI()
instrument_opentelemetry(app)


@app.get("/")
async def home():
    return {"message": "FastApi Home"}


@app.get("/foobar")
async def foobar():
    return {"message": "hello world"}


@app.get('/call-google')
def call_google():
    with httpx.Client() as client:
        response = client.get("https://www.google.com")
    return response.status_code


if __name__ == "__main__":
    uvicorn.run(app)
