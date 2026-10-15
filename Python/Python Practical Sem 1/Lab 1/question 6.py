import math
radius = float(input("Radius of Sphere"))
diameter = 2*radius
circumference =  2*math.pi*radius
surfaceArea = 4*math.pi*radius**2
volume = 4/3*math.pi*radius**3

print("diameter: ", diameter, "circumference: ",circumference, "surfaceArea: ", surfaceArea, "volume: ", volume )