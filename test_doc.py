import pytest
from unittest.mock import patch
from unittest import mock
from doc_netology import add_new_doc, check_document_existance, get_doc_owner_name, delete_doc, add_new_shelf, get_doc_shelf, remove_doc_from_shelf







class Test_check_doc:

    def test_check_doc(self):
        assert check_document_existance("10006") == True
        assert check_document_existance('220222') == False



    def test_get_doc_owner_name(self):
        assert get_doc_owner_name("10006") == 'Аристарх Павлов'
        assert get_doc_owner_name("220222") is None

    def test_delete_doc(self):
        assert delete_doc('10006') == ("10006", True)

    def test_add_new_shelf(self):
        assert add_new_shelf("10") == ("10", True)
        assert add_new_shelf("1") == ('1', False)

    def test_get_doc_shelf(self):
        assert get_doc_shelf("10006") == '2'
        assert get_doc_shelf("220222") is None

    def test_remove_doc_from_shelf(self):
        assert remove_doc_from_shelf("11-2") is True
        assert remove_doc_from_shelf("11-222") is False

@patch("builtins.input",side_effect=["454545","ПАСТОРТ","КУЗЬМА ПРУТКОВ","3"])
def test_add_new_doc(mock):
    assert add_new_doc() == '3'



