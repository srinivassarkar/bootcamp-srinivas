# src/jobqueue/__init__.py
"""Queue abstraction layer for persistent job processing.

Provides a factory function `get_queue()` to instantiate a queue backend,
ensuring implementation details (e.g., SQLite) are hidden from other modules.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .interface import PersistentQInterface

from .sqlite_backend import PersistentQSQLite


def get_queue() -> "PersistentQInterface":
    """Returns a queue implementation adhering to PersistentQInterface.

    Currently uses SQLite backend (PersistentQSQLite). Swap here for Redis or
    other backends without altering dependent modules.
    """
    return PersistentQSQLite()
