import json
import requests

BASE_URL="https://reqres.in/api"

def get_users():
  response = requests.get(f"{BASE_URL}/users")
  return response.json()
def get_user(id):
  response = requests.get(f"{BASE_URL}/users/{id}")
  return response
def create_user(name,job):
  json_data={"name":name,"job":job}
  response=requests.post(f'{BASE_URL}/users',json=json_data)
  return response
def delete_user(id):
  response=requests.delete(f'{BASE_URL}/users/{id}')
  return response