from lib.secret_diary import SecretDiary
from unittest.mock import Mock

def test_secret_diary_integration():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert type(secret_diary) == SecretDiary

def test_secret_diary_read_returns_message_after_instantiation():
    diary = Mock()
    secret_diary = SecretDiary(diary)

    assert secret_diary.read() == "Go away!"

def test_secret_diary_read_returns_contents_after_unlock():
    diary = Mock()
    diary.read.return_value = "This is a diary"
    
    secret_diary = SecretDiary(diary)
    
    assert secret_diary.read() == "Go away!"

    secret_diary.unlock()

    assert secret_diary.read() == "This is a diary"
    

def test_secret_diary_locks_after_unlock():
    diary = Mock()
    diary.read.return_value = "This is a diary"

    secret_diary = SecretDiary(diary)
    
    secret_diary.unlock()

    assert secret_diary.read() == "This is a diary"

    secret_diary.lock()
    
    assert secret_diary.read() == "Go away!" 