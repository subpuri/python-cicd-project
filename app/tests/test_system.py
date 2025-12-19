# app/tests/test_system.py

from app.system.cpu import cpu_usage
from app.system.memory import memory_usage
from app.system.disk import disk_usage
from fastapi.testclient import TestClient
from app.main import app

def test_cpu_usage():
    data = cpu_usage()
    assert "cpu_usage_percent" in data
    assert "cpu_cores" in data

def test_memory_usage():
    data = memory_usage()
    assert "memory_total" in data
    assert "memory_available" in data
    assert "memory_used" in data
    assert "memory_percent" in data

def test_disk_usage():
    data = disk_usage("/")
    assert "disk_total" in data
    assert "disk_used" in data
    assert "disk_free" in data
    assert "disk_percent" in data



client = TestClient(app)
def test_health_api():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}