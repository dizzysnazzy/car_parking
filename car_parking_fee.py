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


    def prompt_mpesa_payment(self, owner_details, amount):
        # Prompt for MPesa payment
        print(f"Payment of KES {amount} requested for car with number plate {owner_details['number_plate']}")
        print(f"Owned by {owner_details['owner_name']} ({owner_details['owner_phone']})")

        # Assuming payment is successful
        self.payment_status[owner_details['number_plate']] = True
        print("Payment successful!")
