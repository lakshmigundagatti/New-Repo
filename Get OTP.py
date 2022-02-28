import requests
def test_post_request():
    payload = {
         "phone": "+919964222564"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())
  #  assert response.status_code == 201