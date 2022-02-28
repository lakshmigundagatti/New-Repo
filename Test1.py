import requests
def test_get_request():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['status'] == True
    print(response.status_code)


