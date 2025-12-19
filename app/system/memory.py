# app/system/memory.py
import psutil
from app.core.logger import setup_logger

logger = setup_logger(__name__)


def memory_usage() -> dict:
    memory = psutil.virtual_memory()
    logger.info("Collected memory usage data")
    return {
        "memory_total": memory.total,
        "memory_available": memory.available,
        "memory_used": memory.used,
        "memory_percent": memory.percent
    }