from flask import Flask, redirect,url_for,request
from flask import render_template
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    list_items = get_items()
    return render_template('index.html',Items = list_items)
@app.route('/add',methods = ['POST'])
def add():
    title = request.form['toadd']
    add_item(title)
    return redirect(url_for('index'))
