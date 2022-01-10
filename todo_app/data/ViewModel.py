from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem
class ViewModel:
    def __init__(self, items,uncompleted,deletelist):
        self._items = items
        self._uncompleted = uncompleted
        self._deletelist = deletelist
    @property
    def items(self):
        return self._items
    @property
    def uncompleted(self):
        return self._uncompleted
    @property
    def deletelist(self):
        return self._deletelist
    
    def getTodo(self):
        todolist =[]
        for item in self._items:
            if item.status == "TODO":
                todolist.append(item)
        return todolist
    def getDoing(self):
        Doinglist =[]
        for item in self._items:
            if item.status == "Doing":
                Doinglist.append(item)
        return Doinglist 
    def getDone(self):
        Donelist =[]
        for item in self._items:
            if item.status == "Done":
                Donelist.append(item)
        return Donelist