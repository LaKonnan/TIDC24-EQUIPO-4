import requests


# test api-obra connection
def test_get_obras():
     response = requests.get("https://xlpxbsnpo3.execute-api.us-east-2.amazonaws.com/dev/obras")
     assert response.status_code == 200


# test api-obra get an obraId response (fails because id:777 doesnt exists in our db)
#def test_get_obra_id():
#     response = requests.get("https://xlpxbsnpo3.execute-api.us-east-2.amazonaws.com/dev/obras/777")
#     assert response.status_code == 200
