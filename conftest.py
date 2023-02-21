import random

import pytest
from faker import Faker


@pytest.fixture(scope='class')
def start_data():
    faker = Faker()
    pet_id = random.randint(1, 9999)
    input_pet = {
      "id": pet_id,
      "category": {
        "id": random.randint(1, 9999),
        "name": faker.name()
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": random.randint(1, 9999),
          "name": faker.name()
        }
      ],
      "status": "available"
    }
    header = {'accept': 'application/json','Content-Type': 'application/json'}
    return pet_id, input_pet, header
