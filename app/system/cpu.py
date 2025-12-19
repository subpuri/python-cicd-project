# app/systems/cpu.py
import psutil
from app.core.logger import setup_logger

logger = setup_logger(__name__)


def cpu_usage() -> dict:
    usage = psutil.cpu_percent(interval=1)
    cores = psutil.cpu_count()
    logger.info("Collected CPU usage data")
    return {"cpu_usage_percent": usage, "cpu_cores": cores} 