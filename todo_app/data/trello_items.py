import requests
import os
import datetime
from flask import session
def get_items():
    boardid = os.getenv('TRELLO_BOARDID')
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    #get nessary items from env
    items = []
    res1 = requests.get('https://api.trello.com/1/boards/'+boardid+'/cards?key='+ key +'&token='+token)
    ##gets cards on board
   
    reponse1 = res1.json()

    for item in reponse1:
        listid = item['idList']

        res2 = requests.get('https://api.trello.com/1/lists/'+listid+'?key='+ key +'&token='+token)
        ##use list id to get name of list
        reponse2 = res2.json()

      
        items.append(Item.from_trello(item,reponse2))
        #makes an item object based on two reposnses
    
    return session.get('items',items)
    #sends to session

def get_item(id):
    items = get_items()
    return next((item for item in items if item.id == int(id)), None)
    #gets all items then compairs to one with same id

def add_item(title,desc,date):
    
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    TODO = os.getenv('TRELLO_TODOID')
    
    url = f"https://api.trello.com/1/cards"
    
    querystring = {"name": title,"desc":desc,"due":date, "idList": TODO, "key": key, "token": token}#make query based on inputs


    requests.request("POST", url, params=querystring) # make post request using querystring as a parameter to the url
   

def save_item(item):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')

    url = f"https://api.trello.com/1/cards"
    querystring = {"cardid":item['cardid'], "key": key, "token": token}
    requests.request("PUT", url, params=querystring)#saves card

def complete(id):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    done = os.getenv('TRELLO_DONEID')

    updateitem = get_item(id)
    
    reqUrl = f"https://api.trello.com/1/cards/{updateitem.cardid}?idList={done}&key={key}&token={token}"#changes list loaction to the done list

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
    }

    payload = ""

    requests.request("PUT", reqUrl, data=payload,  headers=headersList)

def status(item):
    return item.status # used for filter

def uncompleted(item):
    if item.status == "TODO":#method that returns true or false based on status. used for sorting
        return True
    return False

def todeleteitem(id):
    token = os.getenv('TRELLO_TOKEN')
    key = os.getenv('TRELLO_KEY')
    updateitem = get_item(id)
    id = updateitem.cardid
    #gets the card to be deleted id
    reqUrl = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}"
    #make url
    headersList = {
    "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
    }

    payload = ""

    requests.request("DELETE", reqUrl, data=payload,  headers=headersList)#does a delete request

class Item:
    def __init__(self, id, name, card_id, listid,desc,due, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status 
        self.cardid = card_id
        self.listid = listid
        self.desc = desc
        
        if due is None:
            self.due = due#if none pass it as none
        else:#otherwise format the date
            duedate = datetime.datetime.strptime(due,'%Y-%m-%dT%H:%M:%S.%fz')
            self.due = duedate.strftime('due %b %d, %Y')
    @classmethod
    def from_trello(cls,card,list):#converts trello reponse into an item object
        return cls(card['idShort'],card['name'],card['id'],card['idList'],card['desc'],card['due'],list['name'])
