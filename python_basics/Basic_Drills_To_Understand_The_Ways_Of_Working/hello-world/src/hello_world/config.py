

import os
import yaml
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_config():
    config_paths = []
    if "CONFIG_PATH" in os.environ:
        config_paths.extend(os.environ["CONFIG_PATH"].split(":"))
    config_paths.append(Path.cwd() / "_config.yaml")
    config_paths.append(Path(__file__).parent / "_config.yaml")

    for path in config_paths:
        if path.exists():
            logger.info(f"Loading config from {path}")
            with open(path, "r") as f:
                return yaml.safe_load(f)
    logger.info("No config file found, using default config")
    return {"num_times": 1}