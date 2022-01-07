import pytest
from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem,Item
from todo_app.data.ViewModel import ViewModel
def viewmodel_test():
    list_new = [Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'TODO')
    ,Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'Doing')
    ,Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'Done')]
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
def test_GetItems(monkeypatch):
    test_model = viewmodel_test()
    test_list = get_items()
    monkeypatch.setattr(get_items, 'get', stub)
    assert test_list[0] == test_model.items[0]
def stub():
    return StubResponse
class StubResponse(): 
 def Itemlist(self): 
    return {Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'TODO')
    ,Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'Doing')
    ,Item("1", "bob", "card_id", "listid","desc","2000-12-02T12:50:30.07z", status = 'Done')}