from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class PersistentQInterface(ABC):
    @abstractmethod
    def enqueue(self, job: str) -> None:
        """Add a job to the queue. Job is a string (max 2000 chars)."""
        pass

    @abstractmethod
    def dequeue(self) -> Optional[str]:
        """Retrieve a job for processing, ensuring no duplicates."""
        pass

    @abstractmethod
    def complete(self, job_id: str) -> None:
        """Mark a job as completed."""
        pass

    @abstractmethod
    def get_status(self) -> List[Dict[str, str]]:
        """Return status of all jobs for monitoring."""
        pass

    @abstractmethod
    def resubmit(self, job_id: str) -> None:
        """Resubmit a failed job."""
        pass

    @abstractmethod
    def cancel(self, job_id: str) -> None:
        """Cancel a job."""
        pass