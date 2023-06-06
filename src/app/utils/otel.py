from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter


def get_span_exporter() -> OTLPSpanExporter:
    return OTLPSpanExporter(endpoint="http://localhost:4317/")


def get_span_processor(span_exporter: SpanExporter) -> BatchSpanProcessor:
    return BatchSpanProcessor(span_exporter)


def instrument_opentelemetry(app: FastAPI) -> None:
    resource = Resource(attributes={"service.name": "test-service"})
    tracer_provider = TracerProvider(resource=resource)

    otlp_exporter = get_span_exporter()
    trace.set_tracer_provider(tracer_provider)

    span_processor = get_span_processor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app=app)

    HTTPXClientInstrumentor().instrument()
