# File: RA_01.py         
# Author:  Ryan_McWeeny
# Section: 001
# E-mail:  rrm5585@psu.edu

# Temperature Converter

fahrenheit = float(input("Enter temperature in F:"))
Celsius = (fahrenheit - 32) * (5/9)
print(fahrenheit, "F is equivalent to", Celsius, "C")

# Weekly Commute

miles = float(input("Number of miles for one-way trip:"))
days = int(input("Worked days:"))
SPEED = 55

weekly_miles = miles*days*2
hours = weekly_miles / SPEED

print("The number of miles driven in a week is", weekly_miles)
print("The number of hours spent in the car is", hours)
