from lib.reminder import *

def test_reminder_returns_niamh_and_walk():
    result = "walk, niamh!"
    actual = Reminder("niamh","walk").remind()
    assert result == actual 
    print(actual)

def test_raises_error_with_no_task_set():
    reminder = Reminder("niamh")
    result = "No reminder set!"
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_msg = str(e.value)
    assert error_msg == result 
