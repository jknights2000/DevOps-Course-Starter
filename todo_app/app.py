from flask import Flask, redirect,url_for,request
from flask import render_template
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    list_items = sorted(get_items(),key = status)
    list_completed = get_items()
    deletelist = get_items()
    new_list = list(filter(uncompleted,list_completed))
    view_model = ViewModel(list_items,new_list,deletelist)
    return render_template('index.html',view_model = view_model)
@app.route('/add',methods = ['POST'])
def add():
    title = request.form.get('toaddname')
    desc = request.form.get('toadddesc',' ')
    date = request.form.get('toadddate',None)
    add_item(title,desc,date)
    return redirect(url_for('index'))
    
@app.route('/complete',methods = ['POST'])
def done():
    id = request.form['tocomplete']
    complete(id)
    return redirect(url_for('index'))

@app.route('/delete',methods = ['POST'])
def todelete():
    newid = request.form['todelete']
    todeleteitem(newid)
    return redirect(url_for('index'))
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
