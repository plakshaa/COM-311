a)	Python Program for type checking of various functions.
# DataType Output: str 
x = "Welcome to CSE Department" 
print("DataType Output:", type(x)) 

# DataType Output: int 
x = 50 
print("DataType Output:", type(x)) 

# DataType Output: float 
x = 60.5 
print("DataType Output:", type(x)) 

# DataType Output: complex 
x = 3j 
print("DataType Output:", type(x)) 

# DataType Output: list 
x = ["Python", "Programming", "Language"] 
print("DataType Output:", type(x)) 

# DataType Output: tuple 
x = ("MIET", "CSE", "Students") 
print("DataType Output:", type(x)) 

# DataType Output: range 
x = range(10) 
print("DataType Output:", type(x)) 

# DataType Output: dict 
x = {"name": "Kartik", "age": 21} 
print("DataType Output:", type(x)) 

# DataType Output: set 
x = {"Data", "Types", "Python"} 
print("DataType Output:", type(x)) 


b)	Write a program to demonstrate type checking of various data types and demonstrate the use of following built in functions in python: abs(), len(), min(), round(), isalnum(), type().

'''Demonstrate the use of following built-in-functions in python:
abs(), len(), min(), round(), isalnum(), type()'''

# The abs() function returns the absolute value of a number.
print(abs(-10))

#the len() function returns the length of a string or a sequence.
print(len("Welcome to MIET!"))

#The min() function returns the minimum value of a function.
print(min([10,20,30]))

#The round() function rounds a number to a specified number of decimal places.
print(round(3.15422,2))

#The isanum() returns True if a string contains only alphanumeric characters, False otherwise.
print("CSE, 3rd sem ".isalnum())
print("123abc".isalnum())

#The type() function returns the type of an object.
print(type(10))
print(type("AI and, ML!"))




