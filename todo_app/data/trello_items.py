import requests
import os
from flask import session
def get_items():
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    items = []
    res1 = requests.get('https://api.trello.com/1/boards/'+boardid+'/cards?key='+ key +'&token='+token)

   
    reponse1 = res1.json()

    for item in reponse1:
        listid = item['idList']
        res2 = requests.get('https://api.trello.com/1/lists/'+listid+'?key='+ key +'&token='+token)
        reponse2 = res2.json()
        status = reponse2['name']
        id = item['idShort']
        name = item['name']
        cardid = item['id']
        items.append({ 'id': id, 'status': status, 'title': name ,'cardid':cardid})
    return session.get('items',items)

def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def add_item(title):
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    
    res1 = requests.get('https://api.trello.com/1/boards/'+boardid+'/lists?key='+ key +'&token='+token)
    reponse1 = res1.json()

    for item in reponse1:
        if item['name'] == "TODO":
            listid = item['id']
    
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": title, "idList": listid, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def save_item(item):
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')

    url = f"https://api.trello.com/1/cards"
    querystring = {"cardid":item['cardid'], "key": key, "token": token}
    response = requests.request("PUT", url, params=querystring)

def complete(id):
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    done = os.getenv('TRELLO_DONEID')
    updateitem = get_item(id)
    updateitemcardid = updateitem['cardid']
    url = f"https://api.trello.com/1/cards/"+ updateitemcardid
    querystring = {"listid":done, "key": key, "token": token}
    response = requests.request("PUT", url, params=querystring)

def status(item):
    return item["status"]

def uncompleted(item):
    if item["status"] == "TODO":
        return True
    return False