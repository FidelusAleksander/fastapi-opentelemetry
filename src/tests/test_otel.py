from fastapi.testclient import TestClient


def test_foobar(client: TestClient, otel_exporter):
    client.get("/foobar")
    assert len(otel_exporter.get_finished_spans()) == 3


def test_home(client: TestClient, otel_exporter):
    client.get("/")
    assert len(otel_exporter.get_finished_spans()) == 3
