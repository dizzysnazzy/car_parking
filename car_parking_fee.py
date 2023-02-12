import requests
import json


class CarGate:


    def __init__(self):
        self.payment_status = {}


    def scan_number_plate(self):
        # Scan the car's number plate
        number_plate = input("Scanning car number plate...")

        # Call the car number plate API to get owner's details
        response = requests.get(f"https://api.example.com/number_plate/{number_plate}")
        owner_details = json.loads(response.text)

        return owner_details


    def prompt_mpesa_payment(self, owner_details, amount):
        # Prompt for MPesa payment
        print(f"Payment of KES {amount} requested for car with number plate {owner_details['number_plate']}")
        print(f"Owned by {owner_details['owner_name']} ({owner_details['owner_phone']})")

        # Assuming payment is successful
        self.payment_status[owner_details['number_plate']] = True
        print("Payment successful!")


    def open_gate(self, number_plate):
        # Check if payment has been made for the car with the specified number plate
        if number_plate in self.payment_status and self.payment_status[number_plate]:
            print("Gate opened. Enjoy your drive!")
        else:
            print("Payment required. Please make payment and try again.")

#Initialize the CarGate object
car_gate = CarGate()

# Scan the car's number plate
owner_details = car_gate.scan_number_plate()

if owner_details['number_plate'] not in car_gate.payment_status:
    # Car has not made payment before
    car_gate.prompt_mpesa_payment(owner_details, 100)

car_gate.open_gate(owner_details['number_plate'])
