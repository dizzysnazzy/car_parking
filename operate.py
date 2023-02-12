class CarGate:

    def __init__(self):
        self.payment_status = {}
        self.number_plates = {
            "KCC 123A": {
                "owner_name": "John Doe",
                "owner_phone": "0712345678",
                "number_plate": "KCC 123A"
            },
            "KCC 456B": {
                "owner_name": "Jane Doe",
                "owner_phone": "0723456789",
                "number_plate": "KCC 456B"
            }   
        }


    def scan_number_plate(self):
        number_plate = input("Scanning car number plate...")
        if number_plate in self.number_plates:
            return self.number_plates[number_plate]
        else:
            return None


    def prompt_mpesa_payment(self, owner_details, amount):
        print(f"Payment of KES {amount} requested for car with number plate {owner_details['number_plate']}")
        print(f"Owned by {owner_details['owner_name']} ({owner_details['owner_phone']})")
        self.payment_status[owner_details['number_plate']] = True
        print("Payment successful!")

    def open_gate(self, number_plate):
        if number_plate in self.payment_status and self.payment_status[number_plate]:
            print("Gate opened. Enjoy your drive!")
        else:
            print("Payment required. Please make payment and try again.")

car_gate = CarGate()
owner_details = car_gate.scan_number_plate()
if owner_details is not None:
    if owner_details['number_plate'] not in car_gate.payment_status:
        car_gate.prompt_mpesa_payment(owner_details, 100)
        car_gate.open_gate(owner_details['number_plate'])
else:
    print("This car is not in the system. Please contact the administrator.")
