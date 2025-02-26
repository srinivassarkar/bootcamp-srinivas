# tests/test_producer.py
# Purpose: Unit tests for producer functionality

import os
from unittest.mock import Mock

import pytest

from src.producer.producer import Producer


@pytest.fixture
def producer(tmp_path):
    """Setup producer with mock queue and temp dir."""
    queue = Mock()
    output_dir = str(tmp_path / "files")
    p = Producer(queue, output_dir)
    yield p

def test_generate_file(producer: Producer):
    """Test file generation."""
    filepath = producer.generate_file()
    assert filepath is not None
    assert os.path.exists(filepath)
    with open(filepath, "r") as f:
        assert f.read() == "Sample content\n"

def test_run(producer: Producer, monkeypatch):
    """Test producer run loop."""
    monkeypatch.setattr("time.sleep", lambda x: None)
    producer.running = False
    producer.run()
    producer.queue.enqueue.assert_called_once()
