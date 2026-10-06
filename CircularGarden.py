# CIRCUMFERENCE CALCULATOR
# DELMAS & MUSCARA
import math

radius = float(input("Enter radius of garden: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
area2 =  math.sqrt(area)
floor = math.floor(area2)
ceil = math.ceil(area2)

print(f"Area of Garden: {area:.2f} square meters")
print(f"Circumference of Garden: {circumference:.2f} meters")
print(f"Square root of the area: {area2:.2f}")
print(f"Area rounded down: {floor:.2f} square meters")
print(f"Circumference rounded up: {ceil:.2f} square meters")
