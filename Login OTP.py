import requests
def test_post_request():
    payload = {
    "phone": "+918553510585"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_otp"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())
  #  assert response.status_code == 500