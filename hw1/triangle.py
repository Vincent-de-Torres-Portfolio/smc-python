"""
HW1: Triangle Calculator
filename: triangle.py
gist: This script calculates the area, perimeter, and total surface area of a triangle.
      It prompts users for triangle dimensions, handles units, and displays step-by-step calculations.

Vincent de Torres
CS87A-Summer 2024 | HW1
"""

import math
import os


def prompt_for_base():
    """
    Prompts the user to enter the base of the triangle.

    Returns:
    - tuple: A tuple containing (base_value, base_unit).
    """
    triangle_puns = [
        "Looks like you're triangulating the wrong input! Please enter a number for the base.",
        "Oops, something went acute! Enter the base as a number, please.",
        "Don't be a square! Enter a positive number for the base."
    ]

    while True:
        base_str = input("Enter base of the triangle: ")
        try:
            base_value = float(base_str)
            return base_value, None  # No unit provided initially
        except ValueError:
            print(triangle_puns[1])


def prompt_for_triangle_input():
    """
    Prompts the user to enter base and optionally height of the triangle.

    Returns:
    - tuple: A tuple containing (base_value, base_unit, height_value, height_unit).
             If parsing fails or values are invalid, returns (None, None, None, None).
    """
    while True:
        input_str = input(
            "Enter base (and optionally height) of the triangle (with optional units, separated by space) or 'q' to quit: ")

        if input_str.lower() == 'q':
            exit_program()

        # Parse input
        base_value, base_unit, height_value, height_unit = parse_input(input_str)
        if base_value is None:
            continue

        if base_unit and height_unit and base_unit.strip().lower() != height_unit.strip().lower():
            print(
                'Warning: Inputs do not have the same units of measurement. Please verify your input or perform conversions for accurate results.')

        # If both base and height are provided, return immediately
        if height_value is not None:
            # Check if units are different
            if base_unit and height_unit and base_unit.strip().lower() != height_unit.strip().lower():
                confirm = input(
                    f"Units for base ({base_unit}) and height ({height_unit}) are different. Continue? (Y/N): ")
                if confirm.lower() != 'y':
                    continue

            return base_value, base_unit, height_value, height_unit

        # If only base is provided, prompt to confirm it's the base, then for height
        confirm = input(f"Is {base_value} {base_unit if base_unit else 'units'} the base? (Y/N): ")
        if confirm.lower() == 'y':
            height_value, height_unit = prompt_for_height(base_value, base_unit)
            return base_value, base_unit, height_value, height_unit
        else:
            continue


def prompt_for_height(base_value, base_unit):
    """
    Prompts the user to enter the height of the triangle.

    Args:
    - base_value (float): Base value of the triangle.
    - base_unit (str): Unit of measurement for the base.

    Returns:
    - tuple: A tuple containing (height_value, height_unit).
    """
    triangle_puns = [
        "Oops, something went acute! Enter height as a number, please."
    ]

    while True:
        height_str = input(f"Enter height of the triangle (in {base_unit if base_unit else 'units'}): ")
        try:
            height_value = float(height_str)
            return height_value, None  # No unit provided initially
        except ValueError:
            print(triangle_puns[0])


def parse_input(input_str):
    """
    Parses the input string to extract base, base unit, height, and height unit.

    Args:
    - input_str (str): Input string containing base and height values (with optional units).

    Returns:
    - tuple: A tuple containing (base_value, base_unit, height_value, height_unit).
             If parsing fails, returns (None, None, None, None).
    """
    try:
        parts = input_str.split()

        if len(parts) < 2:
            raise ValueError("Not enough values provided")

        base_value_str = parts[0]
        base_unit = ''.join(filter(lambda x: not x.isdigit() and x != '.', base_value_str))
        base_value = float(''.join(filter(lambda x: x.isdigit() or x == '.', base_value_str)))

        height_value_str = parts[1]
        height_unit = ''.join(filter(lambda x: not x.isdigit() and x != '.', height_value_str))
        height_value = float(''.join(filter(lambda x: x.isdigit() or x == '.', height_value_str)))

        return base_value, base_unit, height_value, height_unit

    except ValueError as ve:
        print(f"Error parsing input: {ve}")
        return None, None, None, None

    except IndexError:
        print("Index error: Not enough values provided")
        return None, None, None, None


def validate_input(base_value, height_value):
    """
    Validates the input values for base and height of a triangle.
    Checks if both values are positive numbers.

    Args:
    - base_value (float): Base value of the triangle.
    - height_value (float): Height value of the triangle.

    Returns:
    - bool: True if both values are positive numbers, False otherwise.
    """
    if base_value > 0 and height_value > 0:
        return True
    else:
        return False


def calculate_triangle_area(base, height):
    """
    Calculates the area of a triangle given its base and height.

    Args:
    - base (float): Base of the triangle.
    - height (float): Height of the triangle.

    Returns:
    - float: Area of the triangle.
    """
    area = 0.5 * base * height
    return area


def calculate_triangle_perimeter(base, height):
    """
    Calculates the perimeter of a triangle given its base and height.
    Uses the Pythagorean theorem to find the hypotenuse as the perimeter.

    Args:
    - base (float): Base of the triangle.
    - height (float): Height of the triangle.

    Returns:
    - float: Perimeter of the triangle.
    """
    perimeter = base + 2 * math.sqrt((base / 2) ** 2 + height ** 2)
    return perimeter


def calculate_total_surface_area(area, perimeter):
    """
    Calculates the Total Surface Area (TSA) of a triangle,
    which is the sum of its area and perimeter.

    Args:
    - area (float): Area of the triangle.
    - perimeter (float): Perimeter of the triangle.

    Returns:
    - float: Total Surface Area (TSA) of the triangle.
    """
    tsa = area + perimeter
    return tsa


def exit_program():
    print("Leaving so soon? Remember, geometry shapes our world!")
    import sys
    sys.exit()


def print_line():
    print('⧦' * 95)


def main():
    os.system('clear')

    while True:
        base, base_unit, height, height_unit = prompt_for_triangle_input()

        if base is None and height is None:
            print("Exiting...")
            break

        # Calculate area and perimeter
        if validate_input(base, height):
            area = calculate_triangle_area(base, height)
            perimeter = calculate_triangle_perimeter(base, height)
            tsa = calculate_total_surface_area(area, perimeter)

            # Print triangle details
            print_line()
            print("◺ TRIANGLE")
            print_line()
            print(f" ⟘   Base       {base} {base_unit if base_unit else 'units'}")
            print(f" ⟊   Height     {height} {height_unit if height_unit else 'units'}")
            print_line()
            print(f" ⟶   Area       {area:.2f} {base_unit if base_unit else 'units'}²")
            print(f" ⟶   Perimeter  {perimeter:.2f}  {base_unit if base_unit else 'units'}")
            print(f" ⟶   Total Surface Area (TSA)   {tsa:.2f}")
            print_line()

        else:
            print("Invalid triangle dimensions provided. Please ensure both base and height are positive numbers.")


if __name__ == "__main__":
    main()
