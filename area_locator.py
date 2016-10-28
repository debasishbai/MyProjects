import json
from time import sleep
import requests

# This function will take an Indian pincode as input and displays all the areas associated with it.
 
def locate(x):
    
    # This is the url to which we're going to send the request
    template = "http://postalpincode.in/api/pincode/"

    # Encoding the user entered pincode with the url
    url = template + x

    # Making the request
    data = requests.get(url)

    # Using the buit-in json decoder from the requests module 
    js = data.json()

    print("Retrieving Data",end=' ')
    for _ in range(3):
        print(".",end=" ")
        sleep(1)
    print()
    print()

    # Display the response
    if js["Status"] == "Success":
        print(js['Message'])
        print()
        for i in range(len(js["PostOffice"])):
            print('Name:',js["PostOffice"][i]['Name'])
            print("BranchType:",js["PostOffice"][i]["BranchType"])
            print("DeliveryStatus:",js["PostOffice"][i]["DeliveryStatus"])
            print("Circle:",js["PostOffice"][i]["Circle"])
            print("Division:",js["PostOffice"][i]["Division"])
            print("District:",js["PostOffice"][i]["District"])
            print("State:",js["PostOffice"][i]["State"])
            print()

    elif js['Status'] == "Error":
        print(js['Message'])
        print()
    return None


while True:
    pin = input("Enter Pincode: ")
    if pin.isdigit():
        if len(pin)==6:
            locate(pin)
        else:print("Pin Code should be 6 digits!")

    # Enter 'q' to exit the loop
    elif pin.strip() == 'q':break
    
    else:print("Invalid Input")

print()
print("Thank you")
