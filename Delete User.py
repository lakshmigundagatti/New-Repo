import requests
def test_delete_request():
    payload = {
             "phone": "+919964222564",
             "otp": 333333
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())
  #  assert response.status_code == 500