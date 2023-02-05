#Variables and Datatypes and Typecasting


a = 34 # Variable storing an integer
b = 23.2 # Variable storing real number


# Variable in Python:
abc = "It's a string variable"
_abcnum = 40 # It is an example of int variable
abc123 = 55.854 # It is an example of float variable
print(_abcnum + abc123) # This will give sum of 40 + 55.854


# type() Function in Python:
harry = "40"
demo = 55.5
demo = 40
print (type(harry)) #It will give output as string type
demo3 = type(demo) #It will return data type as float
print(demo3) #It will print that data type
print(type(demo2)) #It will give output as int type


var1 = "It's a String"
var2 = 5
print(var1+var2) ''' It will give an error as we can't add string to any number. '''


var1 = "My Name is "
var2 = "Harry"
var3 = var1+var2+" & I am a Good Boy."
print(var1+var2) # It will give output 'My Name is Harry'
print(var3)


# Typecasting in Python :
abc = 5
abc2 = '45'
abc3 = 55.95
xyz = 5.0
abc4=int(abc2)
print(abc+abc4) # Output : 50
print(abc+int(abc2)) # Output : 50
print(float(abc)+xyz) # It will add 5.0 + 5.0 and will return 10.0
print(str(abc)+45) # It will give an error as abc has been changed into string.


# Input Function in Python:
print("Enter your name : ")
name = input() #It will take input from user
print("Your Name is",name) # It will show the name
xyz = input("Enter your age : ")
print("Your age is ",xyz)


# Quiz :
print("Enter First Number : ")
num1= input()
print("Enter Second Number : ")
num2=input()
print("The Sum is",num2) #It will give output as sum of two numbers.


var1 = "54"
var4 = "32"
var2 = 4
var3 = 36.7
# print(100 * str(int(var1) + int(var4)) )
# print(100 * "Hello world\n")
# print("Enter your number")
# inpnum = input()


# print("You entered", int(inpnum)+10)
"""
str()
int()
float()
"""
"""
Quiz - Solved in the video
Exercise - Next video
Project - Some awesome python utility
"""
# print(type(var1))
print("Enter first number")
n1 = input()
print("Enter second number")
n2 = input()
print("Sum of these two numbers is", int(n1) + int(n2))

