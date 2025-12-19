from fastapi import FastAPI
from app.system.cpu import cpu_usage
from app.system.memory import memory_usage
from app.system.disk import disk_usage
from app.core.logger import setup_logger


logger = setup_logger(__name__)


app = FastAPI(
    title="InfraOps Automator",
    description = "System and Infrastructure automation APIs",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.get("/system/cpu")
def get_cpu():
    return cpu_usage()

@app.get("/system/memory")
def get_memory():
    return memory_usage()

@app.get("/system/disk")
def get_disk(path: str = "/"):
    return disk_usage(path)
