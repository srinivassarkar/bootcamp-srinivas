# tests/test_setup.py
def test_import():
    from src.jobqueue import get_queue
    assert get_queue is not None