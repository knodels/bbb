from requests import Response
import pytest
from main import *
def test_get_users():
  response=get_users()
  assert response.status_code==200
  assert "data" in response.json()

def test_get_user():
  response=get_user(1)
  assert response.status_code==200
  assert response.json()['data']['id']==2
def test_create_user():
  response=create_user('Jack','teacher')
  assert response.status_code==201
  assert response.json()['name']=='Jack'
  assert response.json()['job']=='teacher'
def test_update_user():
  response=update_user(2,'Lisa','singer')
  assert response.status_code==200
  assert response.json()['name']=='Lisa'
  assert response.json()['job']=='singer'
def test_delete_user():
  response=delete_user(2)
  response=delete_user(2)
  assert response.status_code==204
def test_get_user_not():
  response=get_user(13)
  assert response.status_code==404
  