import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_upload_no_file():
    response = client.post("/documents")
    assert response.status_code == 422  # Missing file

def test_upload_invalid_type():
    response = client.post("/documents", files={
        "file": ("test.txt", b"test", "text/plain")
    })
    assert response.status_code == 400

if __name__ == "__main__":
    pytest.main([__file__, "-v"])