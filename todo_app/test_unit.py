import pytest
from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem,Item
from todo_app.data.ViewModel import ViewModel
def viewmodel_test():
    list_new = [Item("1", "name1", "card_id1", "listid1","desc","2000-12-02T12:50:30.07z", status = 'TODO')
    ,Item("2", "name2", "card_id2", "listid2","desc",None, status = 'Doing')
    ,Item("3", "name3", "card_id3", "listid3","desc",None, status = 'Done')]
    return ViewModel(list_new,list_new,list_new)
def test_Todo():
    test_model = viewmodel_test()
    test_todolist = test_model.getTodo()
    assert len(test_todolist) == 1
def test_Doing():
    test_model = viewmodel_test()
    test_todolist = test_model.getDoing()
    assert len(test_todolist) == 1
def test_Done():
    test_model = viewmodel_test()
    test_todolist = test_model.getDone()
    assert len(test_todolist) == 1