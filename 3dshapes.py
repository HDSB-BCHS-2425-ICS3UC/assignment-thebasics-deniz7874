# Author: Deniz
# program that calculates the volume of different 3D shapes
# user can choose from a cube, sphere, cone, or cylinder

import math  # importing math module for calculations

# Function to calculate the volume of a cube
def cube_volume(length):
    return length ** 3  # Formula: A^3 (A is the edge length)

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3  # formula: (4/3) * π * r^3

# function to calculate the volume of a cone
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height  # formula: (1/3) * π * r^2 * h

# function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height  # formula: π * r^2 * h

# Asking the user to choose a shape
shape = input("Choose a shape (cube, sphere, cone, cylinder): ").lower()  # converts input to lowercase

# if the user chooses a cube
if shape == "cube":
    l = float(input("Enter the edge length of the cube: "))  # gets length from user
    print(f"The volume of the cube is: {cube_volume(l)}")  # Prints cube volume

# If the user chooses a sphere
elif shape == "sphere":
    r = float(input("Enter the radius of the sphere: "))  # Gets radius from user
    print(f"The volume of the sphere is: {sphere_volume(r)}")  # Prints sphere volume

# If the user chooses a cone
elif shape == "cone":
    r = float(input("Enter the radius of the cone's base: "))  # Gets radius from user
    h = float(input("Enter the height of the cone: "))  # Gets height from user
    print(f"The volume of the cone is: {cone_volume(r, h)}")  # Prints cone volume

# If the user chooses a cylinder
elif shape == "cylinder":
    r = float(input("Enter the radius of the cylinder's base: "))  # Gets radius from user
    h = float(input("Enter the height of the cylinder: "))  # Gets height from user
    print(f"The volume of the cylinder is: {cylinder_volume(r, h)}")  # Prints cylinder volume

# if the user enters something invalid
else:
    print("Invalid shape entered. Please choose either cube, sphere, cone, or cylinder.")  # error message