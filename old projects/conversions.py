"""
define variables as "num1", "num2", "num3", "str1"
print variable types of each variable
print each variable each variable after type conversion
"""



num1 = 99.23
num2 = 23
num3 = 150
str1 = "100"

print(type(num1))
print(type(num2))
print(type(num3))
print(type(str1))

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
str1 = int(str1)

print("---------")
print(type(num1))
print(type(num2))
print(type(num3))
print(type(str1))

print("-------------")
print("integer of num1 =", num1)
print("num2 as float =", num2)
print("num3 as string=", num3)
print("str1 as integer=", str1)