from fastapi.testclient import TestClient
import pytest
from fastapi.testclient import TestClient
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from unittest.mock import patch
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

@pytest.fixture
def client(otel_exporter):
    from app.main import app
    yield TestClient(app)


@pytest.fixture
def otel_exporter():
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)
    with patch("app.utils.otel.get_span_processor", return_value=processor):
        with patch("app.utils.otel.get_span_exporter", return_value=exporter):
            yield exporter


def test_foobar(client: TestClient, otel_exporter):
    client.get("/foobar")
    assert len(otel_exporter.get_finished_spans()) == 3


def test_home(client: TestClient, otel_exporter):
    client.get("/")
    assert len(otel_exporter.get_finished_spans()) == 3
