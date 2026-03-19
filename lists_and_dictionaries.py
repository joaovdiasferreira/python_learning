#list, like arrays (collection of values)
numbers = [10,20,30,40,50]
names = ["John", "Poe", "Lisa", "Marie"]

#accessing elements -> list[index]
print("numbers in index 0: ", numbers[0]) #first position (start at 0)
print("names in index 1: ", names[1])
#or print all list
print("all list of names: ", names)

"""or printing element by element
for name in names:
    print(name)
"""
#add and delete elements
names.append("Lucas")
names.remove("John")
print(names)
print("length of names: ", len(names))

#---------------------------------------#

#dictionaries, key-values pairs
user = {
    "name": "John",
    "age": 20,
    "email": "john@gmail.com"
}
#accessing elements -> user["key"]
print("User name: ", user["name"])

#adding / updating
user["age"] = 18
user["city"] = "London"
print(f"User: {user["name"]}, age: {user["age"]}, city: {user['city']}")

#removing
del user["email"]
print(user)

#printing one by one
for key, value in user.items():
    print(f"key: {key}, value: {value}")