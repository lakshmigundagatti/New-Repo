import requests


def test_register_user_request():
    payload = {
        "name": "Riyaa Gupta",
        "email": "riya.gupta1@gmail.com",
        "password": "12345678",
        "age": 20
    }

    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/register"    response = requests.post(url=endpoint, json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201
def test_login_user_request():
    payload = {
        "email": "riya.gupta1@gmail.com",
        "password": "12345678"
    }

    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/login"    response = requests.post(url=endpoint, json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
def test_user_logout_request():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTEwNDl9.R4sJr3wnoiG_HwKT3to40u6Z1b_CiClH66sJZRRj9bA"}
    response = requests.post('https://api-nodejs-todolist.herokuapp.com/user/logout',
                             headers=headers)
    print(response.status_code)
    print(response.json())


def test_user_login_request():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRjY2JlYzZiNTVkYTAwMTc1OTcyMmMiLCJpYXQiOjE1NzQ3NTE2ODh9.GPbsl9FLX4VrsGVErodiXypjuz1us4tfD0jwg2_UrzY"}
    response = requests.get('https://api-nodejs-todolist.herokuapp.com/user/me',
                            headers=headers)
    print(response.status_code)
    print(response.json())


def test_user_update_profile_request():
    body = {
        "age": 25
    }
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRjY2JlYzZiNTVkYTAwMTc1OTcyMmMiLCJpYXQiOjE1NzQ3NTE2ODh9.GPbsl9FLX4VrsGVErodiXypjuz1us4tfD0jwg2_UrzY"}
    response = requests.post('https://api-nodejs-todolist.herokuapp.com/user/me',
                             headers=headers, json=body)
    print(response.status_code)
    print(response.json())


def test_delete_user_request():
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/me"
    headers = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTY1NzF9.5v32aulIG6tk91_oOehOexSqDst-YgYHGwD803ZSP_I"}
    response = requests.delete(url=endpoint, headers=headers)
    print(response.status_code)
    print(response.json())

