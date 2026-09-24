"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(title="ReUniteAI")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a basic service health response."""
    return {"status": "ok"}
