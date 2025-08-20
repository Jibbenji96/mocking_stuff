# from lib.secret_diary import SecretDiary
# from lib.diary import Diary

# def test_secret_diary_integration():
#     diary = Diary("This is a diary")
#     secret_diary = SecretDiary(diary)
#     assert type(secret_diary) == SecretDiary

# def test_secret_diary_read_returns_message_after_instantiation():
#     diary = Diary("This is a diary")
#     secret_diary = SecretDiary(diary)

#     assert secret_diary.read() == "Go away!"

# def test_secret_diary_read_returns_contents_after_unlock():
#     diary = Diary("This is a diary")
#     secret_diary = SecretDiary(diary)
#     secret_diary.unlock()

#     assert secret_diary.read() == "This is a diary"

# def test_secret_diary_locks_after_unlock():
#     diary = Diary("This is a diary")
#     secret_diary = SecretDiary(diary)
#     secret_diary.unlock()
#     assert secret_diary.read() == "This is a diary"
#     secret_diary.lock()
#     assert secret_diary.read() == "Go away!"