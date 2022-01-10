import pytest
from dotenv import load_dotenv, find_dotenv
import requests
import os
from todo_app import app
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

class StubResponse():
 def __init__(self, fake_response_data):
    self.fake_response_data = fake_response_data

def json(self):
    return self.fake_response_data

def get_lists_stub(url, params):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
        'id': '123abc',
        'name': 'To Do',
        'cards': [{'id': '456', 'name': 'Test card'}]
        }]
    return StubResponse(fake_response_data)