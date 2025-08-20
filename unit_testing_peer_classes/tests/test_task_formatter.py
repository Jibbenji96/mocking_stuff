from lib.TaskFormatter import TaskFormatter
from unittest.mock import Mock

def test_task_formatter_integration():
    task = Mock()
    formatted_task = TaskFormatter(task)
    assert type(formatted_task) == TaskFormatter

def test_task_formatter_returns_correct_incomplete_format():
    task = Mock()
    task.name = "task"
    task.complete = False
    formatted_task = TaskFormatter(task)
    assert formatted_task.format() == "- [ ] task"

def test_task_formatter_returns_correct_complete_format():
    task = Mock()
    task.name = "task"
    task.complete = True
    formatted_task = TaskFormatter(task)
    assert formatted_task.format() == "- [x] task"