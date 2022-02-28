import requests
import response
def test_put_request():
    payload = {
        "name": "user104",
        "phone": "+919964222564",
        "email": "user104@hashedin.com",
        "password": "admin",
        "otp": 333333
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())
  #  assert response.status_code == 500