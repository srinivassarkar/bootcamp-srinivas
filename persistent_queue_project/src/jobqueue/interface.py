# src/jobqueue/interface.py
# Purpose: Defines abstract interface for queue implementations

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class PersistentQInterface(ABC):
    """Abstract base class for persistent job queue implementations."""

    @abstractmethod
    def enqueue(self, job: str) -> None:
        """Enqueues a job with a unique ID."""
        pass

    @abstractmethod
    def dequeue(self) -> Optional[str]:
        """Dequeues a job for processing, locking it atomically."""
        pass

    @abstractmethod
    def complete(self, job_id: str) -> None:
        """Marks a job as completed."""
        pass

    @abstractmethod
    def mark_failed(self, job_id: str) -> None:
        """Marks a job as failed, handling retries."""
        pass

    @abstractmethod
    def get_status(self) -> List[Dict[str, str]]:
        """Returns current status of all jobs."""
        pass

    @abstractmethod
    def resubmit(self, job_id: str) -> None:
        """Resubmits a failed job."""
        pass

    @abstractmethod
    def cancel(self, job_id: str) -> None:
        """Cancels a job."""
        pass

    @abstractmethod
    def heartbeat(self) -> None:
        """Updates consumer heartbeat for active jobs."""
        pass

    @abstractmethod
    def check_stalled_jobs(self) -> None:
        """Requeues stalled jobs."""
        pass