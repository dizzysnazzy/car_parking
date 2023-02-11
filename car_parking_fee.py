import requests
import json

class CarGate:


    def __init__(self):
        self.payment_status = {}


    def scan_number_plate(self, number_plate):
        # Call the car number plate API to get owner's details
        response = request.get(f"https://api.example.com/number_plate/{number_plate}")
        owner_details = json.loads(response.text)

        return owner_details
