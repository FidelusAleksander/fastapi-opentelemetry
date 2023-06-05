import pytest
from fastapi.testclient import TestClient
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from unittest.mock import patch
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

@pytest.fixture
def client():
    from app.main import app
    yield TestClient(app)


@pytest.fixture(scope="function")
def otel_exporter():
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)
    with patch("app.utils.otel.get_span_processor", return_value=processor):
        with patch("app.utils.otel.get_span_exporter", return_value=exporter):
            yield exporter
