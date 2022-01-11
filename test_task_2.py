
from task_2 import create_dir_in_Yandex, delete_dir_in_Yandex



class Test_:
    def test_create_dir(self):
        _token = "___________"
        assert create_dir_in_Yandex(_token,"test_3").status_code == 201
        delete_dir_in_Yandex(_token, "test_3")


