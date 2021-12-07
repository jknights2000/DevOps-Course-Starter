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

        # status = reponse2['name']
        # id = item['idShort']
        # name = item['name']
        # cardid = item['id']
        # listid = item['idList']
        items.append(Item.from_trello(item,reponse2))
    return session.get('items',items)

def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def add_item(title):
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    TODO = os.getenv('TRELLO_TODOID')
    
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": title, "idList": TODO, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def save_item(item):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')

    url = f"https://api.trello.com/1/cards"
    querystring = {"cardid":item['cardid'], "key": key, "token": token}
    response = requests.request("PUT", url, params=querystring)

def complete(id):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    done = os.getenv('TRELLO_DONEID')

    updateitem = get_item(id)
    
    reqUrl = f"https://api.trello.com/1/cards/{updateitem['cardid']}?idList={done}&key={key}&token={token}"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
    }

    payload = ""

    response = requests.request("PUT", reqUrl, data=payload,  headers=headersList)

def status(item):
    return item.status

def uncompleted(item):
    if item.status == "TODO":
        return True
    return False
def todeleteitem(id):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    updateitem = get_item(id)
    id = updateitem['cardid']
    reqUrl = f"https://api.trello.com/1/cards/{updateitem['cardid']}?key={key}&token={token}"

    headersList = {
    "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
    }

    payload = ""

    response = requests.request("DELETE", reqUrl, data=payload,  headers=headersList)

class Item:
    def __init__(self, id, name, card_id, listid,desc, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status 
        self.cardid = card_id
        self.listid = listid
        self.desc = desc
    @classmethod
    def from_trello(cls,card,list):
        return cls(card['idShort'],card['name'],card['id'],card['idList'],card['desc'],list['name'])
