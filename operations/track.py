# tracking = {
#     "9737731874": {"status": "Shipped", "location": "Surat"},
#     "9737731874": {"status": "Out for Delivery", "location": "Ahmedabad"}
# }

# mobile = input("Enter mobile number: ")

# if mobile in tracking:
#     print("Status:", tracking[mobile]["status"])
#     print("Location:", tracking[mobile]["location"])
# else:
#     print("No tracking found.")



import time
import requests

user_id = "9876543210"
URL = f"http://your-server-ip:5000/location/{user_id}"

while True:
    try:
        data = requests.get(URL).json()
        print("Live →", data)
    except:
        print("Connection issue")
    time.sleep(2)
