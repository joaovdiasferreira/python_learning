#it isn't necessary declare a type explicitly
from encodings import normalize_encoding

name = "John"
age = 18
height = 1.76 #(m)

print("type of name: ", type(name))
print("type of age: ", type(age))
print("type of height", type(height))

#conversion
height = 176 #(cm) -> dynamic typing
print("type of height (converted): ", type(height))

age = "20" #age becomes str -> dynamic typing
age = int(age) #now it is converted to int

#---------------------------------------#
#data types
#string (str)
message = "Hello World"
print("type of message: ", type(message))

#integer (int)
num = 10
print("type of num: ", type(num))

#float (float)
price = 19.99
print("type of price: ", type(price))

#boolean (bool)
is_admin = True
print("type of is_admin: ", type(is_admin))

#list (list)
numbers = [1,2,3,4,5]
print("type of numbers: ", type(numbers))

#dictonary (dict)
user = {
    "name": "John",
    "age": 18,
    "height": 1.76
}
print("type of user: ", type(user))

#tuple (tuple)
coord = (110, 250)
print("type of coord: ", type(coord))

#NoneType (none)
result = None
print("type of result: ", type(result))