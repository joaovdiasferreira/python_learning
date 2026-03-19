"""BEST PRACTICES
- Clear names (example_func, exampleFunc etc)
- One function, one responsibility
- Prefer return over print
"""

#basic example
def multiply(a,b):
    return a*b

a = multiply(3,4)
print("Result from multiply: ",a)

#---------------------------------------#

#multiples parameters
def person(name,age, email):
    return {
        'name':name,
        'age':age,
        'email':email
    } # return a dictionary -> person['parameter']

user = person('John',23,'jhon@gmail')
print("accessing email from user: ", user['email'])
#---------------------------------------#

#scope
x = 10
def testScope():
    x = 5
    print(f"inside function (local scope): {x}")

testScope()
print(f"outside func (global scope): {x}")

#---------------------------------------#

#returning multiples values
def calc(num1,num2): #add, mult, div
    return num1+num2, num1*num2, num1/num2 #Returns a tuple

print("Result from calc: ", calc(2,5))

#---------------------------------------#

#functions as objects
#functions can be passed as arguments
def executeFunc(func):
    func()

def func():
    print(("Hello from func!"))

executeFunc(func)

#---------------------------------------#

#lambda functions
#shortcuts functions
add = lambda a,b: a+b

print("result from lambda add: ", add(3,4))

#---------------------------------------#
#*args and **kwargs
#*args collects multiples arguments into a tuple

def sumAll(*args):
    return sum(args)

print("Result from sumAll: ", sumAll(1,2,3,4,5,6))

#**kwargs allows a function to receive multiple named arguments
#collec everything into a dictionary
def show_user(**kwargs):
    return kwargs

user_2 = show_user(first_name="John", last_name="Doe")
user_3 = show_user(first_name="John", last_name="Doe", age="21")
print("User using first name and last name: ", user_2)
print("User using first name, last name and age: ", user_3)

#usem them together
#order matters: function(arg, *args, **kwargs)
#that is -> normal parameters, *args and **kwargs
def args(y, *args, **kwargs):
    print("From args:")
    print("Printing y: ", y)
    print("Printing args: ", args)
    print("Printing kwargs: ", kwargs)

args(10, 1,2,3, name="John", age="21")