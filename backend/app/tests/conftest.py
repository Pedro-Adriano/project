import pytest
from fastapi.testclient import TestClient

from app.core.settings.fast_api import create_app  # ← ajuste para o nome REAL


@pytest.fixture
def client():
    app = create_app()
    with TestClient(app, raise_server_exceptions=False) as client:
        yield client
