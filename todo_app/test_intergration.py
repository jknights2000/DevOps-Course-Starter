import pytest
from dotenv import load_dotenv, find_dotenv
import requests
import os
from todo_app import app
from todo_app.data.trello_items import get_items,add_item,complete,status,uncompleted,todeleteitem
import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client
