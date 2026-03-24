import requests
from pprint import pprint
import json

#example
#request = requests.get("https://httpbin.org/get")
#print(request.headers)
#print(request.status_code)


"""
get - get information
post - insert information
put/patch - update information
delete - delete information
"""

"""
#practice using currency quotation 
request = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL")
content = json.loads(request.content)
pprint(content)
"""


#---------------------------------------------------------#
#practice using Firebase

#GET method
def print_content():
    request = requests.get("https://teste-http-74095-default-rtdb.firebaseio.com/.json") #not forget do add ".json" in the end
    content = json.loads(request.content)
    pprint(content)  #it would return None, because the database is empty,
                     #so there is not a valid json


#POST method
user1 = '{"Name": "John", "Age":18, "email":"john@gmail.com"}' #dict in text format
user2 = '{"Name": "Lucas", "Age":21, "email":"lucas@gmail.com"}'
user3 = '{"Name": "Emily", "Age":23, "email":"emily@gmail.com"}'

"""
request = requests.post("https://teste-http-74095-default-rtdb.firebaseio.com/.json", data=user1)
request = requests.post("https://teste-http-74095-default-rtdb.firebaseio.com/.json", data=user2)
request = requests.post("https://teste-http-74095-default-rtdb.firebaseio.com/.json", data=user3)
"""


#PATCH method
#Suposing that I wanna change something in user2, like email
#His id is -OoVpBHECqQRfE021X8K so:
user2_alt = '{"email": "lucas@institucional.com"}'

#request = requests.patch("https://teste-http-74095-default-rtdb.firebaseio.com/-OoVpBHECqQRfE021X8K.json", data=user2_alt)
#PATCH changes partially, in this case, just the email will be changed


#PUT method
#request = requests.put("https://teste-http-74095-default-rtdb.firebaseio.com/-OoVpBHECqQRfE021X8K.json", data=user2_alt)
#just 'email' will be saved in this user, others information will be lost

#user2_alt = '{"Name": "Lucas", "Age":21, "email":"lucas@institucional.com"}'
#request = requests.put("https://teste-http-74095-default-rtdb.firebaseio.com/-OoVpBHECqQRfE021X8K.json", data=user2_alt)
#this resolve that problem, but patch works better here, or we can change the original variable


#DELETE method
user4 = '{"Name": "Pedro", "Age": 25, "email": "pedro@gmail.com"}'
#request = requests.post("https://teste-http-74095-default-rtdb.firebaseio.com/.json", data=user4)
#Suposing that I added a user and I want remove one (user 1, for example) -> id: -OoVlzDoKT2j7qE-bsYT'
#request = requests.delete("https://teste-http-74095-default-rtdb.firebaseio.com/-OoVlzDoKT2j7qE-bsYT.json", )

print_content()

request = requests.get("https://teste-http-74095-default-rtdb.firebaseio.com/.json")
data = request.json()

with open("test.json", "w") as f:
    json.dump(data, f, indent=4)