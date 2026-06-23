import pytest

from calculator.memory import Memory

@pytest.fixture
def memory():
    return Memory()

def test_create_returns_id(memory):
    assert memory.create(10.0) == 1

def test_create_stores_value(memory):
    memory.create(10.0)
    assert memory.read(1) == 10.0

def test_read_non_existent_id(memory):
    with pytest.raises(ValueError):
        memory.read(999)

def test_update_changes_value(memory):
    memory.create(10.0)
    memory.update(1, 20.0)
    assert memory.read(1) == 20.0

def test_update_non_existent_id(memory):
    with pytest.raises(ValueError):
        memory.update(999, 10.0)

def test_delete_removes_entry(memory):
    memory.create(10.0)
    memory.delete(1)
    with pytest.raises(ValueError):
        memory.read(1)

def test_delete_non_existent_id(memory):
    with pytest.raises(ValueError):
        memory.delete(999)

def test_list_all_returns_values(memory):
    memory.create(10.0)
    memory.create(20.0)
    all_entries = memory.list_all()
    assert all_entries == {1: 10.0, 2: 20.0}