# src/jobqueue/interface.py
"""Abstract interface for persistent job queue implementations."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class PersistentQInterface(ABC):
    """Abstract base class defining queue operations for job processing."""

    @abstractmethod
    def enqueue(self, job_id: str) -> None:
        """Enqueues a job with a unique identifier (file path, max 2000 chars)."""
        pass

    @abstractmethod
    def dequeue(self) -> Optional[str]:
        """Dequeues a job atomically, locking it for processing; returns None if empty."""
        pass

    @abstractmethod
    def complete(self, job_id: str) -> None:
        """Marks a job as completed, releasing its lock."""
        pass

    @abstractmethod
    def mark_failed(self, job_id: str) -> None:
        """Marks a job as failed; retryable up to 3 times, then unprocessable."""
        pass

    @abstractmethod
    def get_status(self) -> List[Dict[str, str]]:
        """Returns current status of all jobs in the queue."""
        pass

    @abstractmethod
    def resubmit(self, job_id: str) -> None:
        """Resubmits a failed job to PENDING state for reprocessing."""
        pass

    @abstractmethod
    def cancel(self, job_id: str) -> None:
        """Cancels a job, marking it as CANCELED."""
        pass

    @abstractmethod
    def heartbeat(self) -> None:
        """Updates heartbeat timestamp for jobs in PROCESSING state."""
        pass

    @abstractmethod
    def check_stalled_jobs(self) -> None:
        """Requeues PROCESSING jobs stalled beyond 5 minutes due to consumer crash."""
        pass
