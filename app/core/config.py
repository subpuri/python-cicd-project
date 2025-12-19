#app/core/config.py
import os
from dataclasses import dataclass

@dataclass
class Settings:
    app_name: str = "InfraOps Automator"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
settings = Settings()
