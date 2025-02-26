# tests/test_consumer.py
# Purpose: Unit tests for consumer functionality

#import os
from unittest.mock import Mock

import pytest

from src.consumer.consumer import Consumer


@pytest.fixture
def consumer(tmp_path):
    """Setup consumer with mock queue."""
    queue = Mock()
    c = Consumer()
    c.queue = queue
    c.queue.consumer_id = "test-consumer"
    yield c

def test_process_job(consumer: Consumer, tmp_path):
    """Test job processing."""
    job_file = tmp_path / "test.txt"
    job_file.write_text("Test line\n")
    consumer.process_job(str(job_file))
    consumer.queue.complete.assert_called_once_with(str(job_file))
