# CAR_PARKING AUTOMATIC PAYMENT

## EXPLAINATION
The parking code is a software application that automates the process of paying for car parking fees. It works by integrating with an API that provides information about the number plate of the parked car. This information is then used to determine the parking fee that the car owner needs to pay.

Once the fee has been calculated, the code allows Safaricom to display a payment prompt to the car owner. The payment prompt will provide the car owner with an option to pay the parking fee using their Safaricom account. The payment process will be secure and will be carried out in real-time, ensuring that the payment is received by the relevant authorities promptly.

The code is designed to make the process of paying for parking fees more efficient and convenient. By automating the payment process, it eliminates the need for the car owner to search for a parking meter or attend to a parking attendant, saving time and effort. Additionally, the integration with the API allows the code to keep track of the parking fee in real-time, ensuring that the fee remains accurate and up-to-date.

In summary, the parking code uses the number plate information obtained from the API to automate the process of paying for car parking fees. The code integrates with Safaricom to provide a secure and convenient payment solution, making the process of paying for parking more efficient and effortless.

## HOW IT WORKS

This code defines a ```CarGate``` class that represents a gate that opens only when a car has made a payment. The ```CarGate``` class has several methods:

1. ```__init__``` method: This is a constructor method that is called when an instance of the ```CarGate``` class is created. It initializes the ```payment_status``` dictionary that keeps track of the payment status of cars that have entered the gate.

2. ```scan_number_plate``` method: This method scans the car's number plate. It takes no arguments and returns the owner's details obtained from an API call. The API is called using the ```requests``` library and the URL is constructed using the scanned number plate. The response from the API is loaded into a dictionary using the ```json``` library.

3. ```prompt_mpesa_payment``` method: This method prompts the car owner to make a payment. It takes two arguments: ```owner_details``` and ```amount```. It prints a message asking the owner to make a payment and, assuming the payment is successful, updates the ```payment_status``` dictionary to reflect that the car has made a payment.

4. ```open_gate``` method: This method opens the gate if the car has made a payment. It takes one argument: ```number_plate```. It checks if the ```payment_status``` dictionary has an entry for the specified ```number_plate``` and, if it does, whether the entry is ```True``` (i.e., the car has made a payment). If the car has made a payment, the gate is opened, otherwise, a message is printed asking the car to make a payment.

Finally, an instance of the ```CarGate``` class is created and stored in the ```car_gate``` variable. The car's number plate is then scanned and the car owner's details are obtained. If the car has not made a payment, a payment is prompted. Finally, the gate is opened or a message is printed asking the car to make a payment.
