"""
Write a Python program to calculate the area and 
circumference of a circle with a given radius from
 terminal.
"""
# SOLUTION--->
import math

try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")
    exit()


area = math.pi * radius**2


circumference = 2 * math.pi * radius


print(f"\nFor a circle with radius {radius}:")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
