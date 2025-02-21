

# def say_hello(name: str) -> str:
#     return f"Hello, {name}!"





import logging
from .config import load_config

logger = logging.getLogger(__name__)

def say_hello(name: str) -> str:
    config = load_config()
    num_times = config.get("num_times", 1)
    logger.info(f"Saying hello to {name} {num_times} times")
    return "\n".join([f"Hello, {name}!"] * num_times)