# src/jobqueue/__init__.py
# Purpose: Provides queue abstraction for extensibility

from .interface import PersistentQInterface  
from .sqlite_backend import PersistentQSQLite

def get_queue() -> PersistentQInterface:
    """Returns queue implementation; swap here for future backends (e.g., Redis)."""
    return PersistentQSQLite()
