import pytest
from dotenv import load_dotenv, find_dotenv
import requests
import os
from todo_app import app
from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem

@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
 # Create the new app.
 test_app = app.create_app()
 # Use the app to create a test_client that can be used in our tests.
 with test_app.test_client()as client:
    yield client

def test_index_page(monkeypatch, client):
 # Replace call to requests.get(url) with our own function
 monkeypatch.setattr(requests, 'get', get_lists_stub)
 response = client.get('/')
 assert response.status_code == 200
 
    
class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
        self.status_code = 200
    def json(self):
        return self.fake_response_data

def get_lists_stub(url, params = None):
        test_board_id = os.getenv('TRELLO_BOARDID')
        token = os.getenv('TRELLO_TOKEN')
        key = os.getenv('TRELLO_KEY')
        
        fake_response_data = None
        if url == f'https://api.trello.com/1/boards/'+test_board_id+'/cards?key='+ key +'&token='+token:
            fake_response_data = {
            "id": "abc123",
            "desc": "",
            "idList": "123abc",
            "idShort": 21,
            "name": "lego movie",
            "due": "2021-12-29T00:00:00.000Z"
            }
        if url == 'https://api.trello.com/1/lists/123abc?key='+ key +'&token='+token:
            fake_response_data = {
                "name":"TODO"
            }
        return StubResponse(fake_response_data)