#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

def greet(name):
    print(f"Hello, {name}!")
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    

def add(num1, num2):
    return num1 + num2
sum_result = add(1, 2)
print(sum_result)
    

def halve(number):
    if not isinstance(number,(int, float)):
        return None
    return number / 2
# Call the halve function and store results in variables
result1 = halve(10)
result2 = halve("string")  # This will return None since it's not a number
print(result1)
print(result2)
    
