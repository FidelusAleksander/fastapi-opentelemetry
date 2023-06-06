import fastapi
from app.utils.otel import instrument_opentelemetry
from app.router import api


def create_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    instrument_opentelemetry(app)

    app.include_router(api)
    return app
