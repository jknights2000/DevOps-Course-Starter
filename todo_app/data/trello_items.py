import requests
import os
import datetime
import pymongo
from flask import session
from pymongo import MongoClient
from bson.objectid import ObjectId
def get_items():
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    db = client.project
    collection = db.Items
    #get nessary items from env
    return session.get('items',collection.find())
    #sends to session

def get_item(id):
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    document = client.db.collection.find_one({'_id': ObjectId(id)})
    return document  
    #gets all items then compairs to one with same id

def add_item(title,desc,date):
    
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    db = client.project
    collection = db.Items
    item = {"name": title,
        "desc": desc,
        "due": date,
        "satus": "TODO"}
    collection.insert_one(item)
   

def save_item(item):
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    db = client.project
    collection = db.Items
    newvalues = { "$set": {"name": item.title,
        "desc": item.desc,
        "due": item.date,
        "satus": item.status} }
    collection.update_one({'_id': ObjectId(item.id)}, newvalues)

def complete(id):
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    db = client.project
    collection = db.Items
    newvalues = { "$set": {
        "satus": "Done"} }
    collection.update_one({'_id': ObjectId(id)}, newvalues)

def status(item):
    return item.status # used for filter

def uncompleted(item):
    if item.status == "TODO":#method that returns true or false based on status. used for sorting
        return True
    return False

def todeleteitem(id):
    client = MongoClient(os.getenv('CONNECTION_STRING'))
    db = client.project
    collection = db.Items
    collection.delete_one({'_id': ObjectId(id)})

class Item:
    def __init__(self, id, name,desc,due, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status 
        self.desc = desc
        if due is None:
            self.due = due#if none pass it as none
        else:#otherwise format the date
            duedate = datetime.datetime.strptime(due,'%Y-%m-%dT%H:%M:%S.%fz')
            self.due = duedate.strftime('due %b %d, %Y')
