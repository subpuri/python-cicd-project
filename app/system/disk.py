# app/system/disk.py
import psutil
from app.core.logger import setup_logger
logger = setup_logger(__name__)


def disk_usage(path: str = "/") -> dict:
    disk = psutil.disk_usage(path)
    logger.info(f"Collected disk usage data for path: {path}")
    return {
        "disk_total": disk.total,
        "disk_used": disk.used,
        "disk_free": disk.free,
        "disk_percent": disk.percent
    }
