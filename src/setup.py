from setuptools import setup, find_packages

setup(
    name="test-fastapi",
    version="0.1.0",
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'fastapi',
        'opentelemetry-distro',
        'opentelemetry-instrumentation-fastapi',
        'opentelemetry-instrumentation-httpx',
        'opentelemetry-exporter-otlp-proto-grpc',
        'uvicorn',
        'httpx',
        'pytest'
    ]
)
