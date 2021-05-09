import math

print(
    "A quick and easy solution to finding the Area and Circumference of your Circle by inputting the diameter:"
)

print()
print("Trying to find out the Area of your Circle?")
print()

diameter = float(input("Enter the diameter of the Circle: "))
area = math.pi * ((diameter * diameter) / 4)
print("Area of Circle is:", area)

print()
print("Trying to find out the Circumference of your Circle?")
print()

diameter = float(input("Enter the diameter of the Circle: "))
circumference = 2 * math.pi * (diameter / 2)
print("Circumference of Circle is:", circumference)
