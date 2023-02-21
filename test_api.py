import json

import requests

class CustomRequests:
    def request_post(self, input_pet, header):
        return requests.post(url='https://petstore.swagger.io/#/pet/addPet', data=json.dumps(input_pet), headers=header).json()

class TestPet:
    def test_add_pet(self, start_data):
        pet_id, input_pet, header = start_data
        resp = CustomRequests().request_post(input_pet, header)

        assert resp.status_code == 200
        assert resp.json() == input_pet
