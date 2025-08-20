# from unittest.mock import Mock

# def test_creates_a_sophisticated_mock():
#     # Uncomment and set up your mocks here

#     task = Mock()
#     task2 = Mock()
#     task_list = Mock()
#     task_list.tasks = [] 

#     def add_task(task):
#         task_list.tasks.append(task)
    
#     def clear_tasks():
#         task_list.tasks.clear()
#         return "success"

    
#     task_list.add = add_task
#     task_list.list = lambda: task_list.tasks
#     task_list.count = lambda: len(task_list.tasks)
#     task_list.clear = clear_tasks

# def test_creates_a_sophisticated_mock():
#     # Uncomment and set up your mocks here
#     task = Mock()
#     task_list = Mock() 

#     task_list.list.return_value = [task]
#     task_list.count.return_value = 1
#     task_list.clear.return_value = "success"
    
#     # Don't edit below
#     task_list.add(task)
#     assert task_list.list() == [task]
#     assert task_list.count() == 1
#     assert task_list.clear() == "success"
    
