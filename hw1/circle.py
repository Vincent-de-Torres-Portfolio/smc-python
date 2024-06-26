"""
HW1: CircleArea
filename: circle.py
gist:

This script calculates the area of a circle, the radius from a given diameter, and the radius from a given circumference.
It also displays the step-by-step calculations for each process.

Vincent de Torres
CS87A-Summer 2024 | HW1
"""

import math

# Function to calculate the area of a circle given its radius
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    """
    area = math.pi * (radius ** 2)
    return area

# Function to validate the input
def validate_input(value):
    """
    Validate that the input is a positive number.
    """
    return value > 0

# Function to calculate the radius from the diameter
def calculate_radius_from_diameter(diameter):
    """
    Calculate the radius of a circle given its diameter
    """
    radius = diameter / 2
    print("\nRADIUS FROM DIAMETER")
    print("Formula used: radius = diameter / 2")
    return radius

# Function to calculate the radius from the circumference
def calculate_radius_from_circumference(circumference):
    """
    Calculate the radius of a circle given its circumference.
    """
    radius = circumference / (2 * math.pi)
    print("\nRADIUS FROM CIRCUMFERENCE")
    print("Formula used: radius = circumference / (2 * π)")
    return radius



def main():
    # Calculate and display the area for a given radius
    radius = 2.5
    if validate_input(radius):
        area = calculate_area(radius)
        print(f"\nCIRCLE AREA\nRadius: {radius}\nArea: {area:.2f}")
    else:
        print("Invalid radius")

    # Calculate and display the radius from the diameter
    diameter = 5.0  # Example diameter
    if validate_input(diameter):
        radius_from_diameter = calculate_radius_from_diameter(diameter)
        print(radius_from_diameter)
    else:
        print("Invalid diameter")

    # Calculate and display the radius from the circumference
    circumference = 15.70796
    if validate_input(circumference):
        radius_from_circumference = calculate_radius_from_circumference(circumference)
        print(radius_from_circumference)
    else:
        print("Invalid circumference")

if __name__ == "__main__":
    main()
