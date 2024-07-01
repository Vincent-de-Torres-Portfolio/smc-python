"""
Vincent de Torres
CS87A-Summer 2024 

This module provides functions to perform calculations related to circles:

- calculate_area(radius): Calculate the area of a circle given its radius.
- validate_input(value): Validate that the input value is a positive number.
- calculate_radius_from_diameter(diameter): Calculate the radius of a circle given its diameter.
- calculate_radius_from_circumference(circumference): Calculate the radius of a circle given its circumference.

Constants:
- PI: Mathematical constant π.

The module includes a main function demonstrating the usage of these functions with examples.
"""

import math

# Constants
PI = math.pi

# Function to calculate the area of a circle given its radius
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    """
    area = PI * (radius ** 2)
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
    return radius

# Function to calculate the radius from the circumference
def calculate_radius_from_circumference(circumference):
    """
    Calculate the radius of a circle given its circumference.
    """
    radius = circumference / (2 * PI)
    return radius

def main():
    # Step 1: Define radius and calculate area
    print("Step 1: Calculate and output the area of a circle with a radius of 2.5")
    radius = 2.5
    area = calculate_area(radius)
    print(f"   Radius: {radius}")
    print(f"   Calculated Area: {area:.2f}")

    # Step 2: Handle bogus input for radius
    print("\nStep 2: Challenge - Guarding for bogus input")
    invalid_radius = -1
    if validate_input(invalid_radius):
        area = calculate_area(invalid_radius)
        print(f"   Radius: {invalid_radius}")
        print(f"   Calculated Area: {area:.2f}")
    else:
        print(f"   Invalid radius: {invalid_radius}. Please enter a positive number.")

    # Step 3: Calculate and output radius from diameter
    print("\nStep 3: Challenge - Find the radius given the diameter")
    diameter = 5.0
    radius_from_diameter = calculate_radius_from_diameter(diameter)
    print(f"   Diameter: {diameter}")
    print(f"   Calculated Radius from Diameter: {radius_from_diameter:.2f}")

    # Step 4: Calculate and output radius from circumference
    print("\nStep 4: Challenge - Find the radius given the circumference")
    circumference = 40.0
    radius_from_circumference = calculate_radius_from_circumference(circumference)
    print(f"   Circumference: {circumference}")
    print(f"   Calculated Radius from Circumference: {radius_from_circumference:.2f}")

if __name__ == "__main__":
    main()
