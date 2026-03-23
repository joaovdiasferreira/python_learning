#basic syntax
"""
try:
    #code that may cause error
except:
    #code that runs if error occurs
"""

'''
try:
    num =  int(input("Enter a number: "))
    print(10/num)
except:
    print("Oops! Something went wrong.")
'''

'''
#cathing specific errors
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Oops! Something went wrong.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
'''

'''
#using else
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Oops! Something went wrong.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
else:
    print("Result: ", 10/num)
    #else runs when no errors happens
'''


'''#using finally
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Oops! Something went wrong.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
finally:
    print("Result: ", 10/num) #this code will divide even if the input is 0 or string'''

#full structure
"""
try:
    #code to be teste / risk code
except errorType:
    #handle error
else:
    #runs if no errors happens
finally:
    #always runs, even when errors happens
"""