"""
Vincent de Torres
CS87A-Summer 2024 | HW1

Functions:
- prompt_for_base(): Prompt user for the base of the triangle input.
- prompt_for_triangle_input(): Prompt user for triangle dimensions (base and height) with optional units.
- prompt_for_height(base_value, base_unit): Prompt user for the height of the triangle, optionally specifying units.
- parse_input(input_str): Parse user input to extract base and height values with optional units.
- validate_input(base_value, height_value): Validate that both base and height values are positive.
- calculate_triangle_area(base, height): Calculate the area of the triangle given base and height.
- calculate_triangle_perimeter(base, height): Calculate the perimeter of the triangle given base and height.
- calculate_total_surface_area(area, perimeter): Calculate the total surface area of the triangle.
- exit_program(): Exit the program gracefully.
- print_line(): Print a decorative line for visual separation in output.
- main(): Main function to orchestrate the calculation and display of triangle properties.

"""

import math
import os


def prompt_for_base():
    """
    Prompt user for the base of the triangle input.
    
    Returns:
    - base_value (float): The base length of the triangle.
    - base_unit (str or None): The optional unit of measurement for the base.
    """
    while True:
        base_str = input("Enter base of the triangle: ")
        try:
            base_value = float(base_str)
            return base_value, None  # No unit provided initially
        except ValueError:
            print("Oops, something went acute! Enter the base as a number, please.")


def prompt_for_triangle_input():
    """
    Prompt user for triangle dimensions (base and height) with optional units.
    
    Returns:
    - base_value (float): The base length of the triangle.
    - base_unit (str or None): The optional unit of measurement for the base.
    - height_value (float): The height of the triangle.
    - height_unit (str or None): The optional unit of measurement for the height.
    """
    while True:
        input_str = input(
            "Enter base (and optionally height) of the triangle (with optional units, separated by space) or 'q' to quit: ")

        if input_str.lower() == 'q':
            exit_program()

        base_value, base_unit, height_value, height_unit = parse_input(input_str)
        if base_value is None:
            continue

        if base_unit and height_unit and base_unit.strip().lower() != height_unit.strip().lower():
            print(
                'Warning: Inputs do not have the same units of measurement. Please verify your input or perform conversions for accurate results.')

        if height_value is not None:
            if base_unit and height_unit and base_unit.strip().lower() != height_unit.strip().lower():
                confirm = input(
                    f"Units for base ({base_unit}) and height ({height_unit}) are different. Continue? (Y/N): ")
                if confirm.lower() != 'y':
                    continue

            return base_value, base_unit, height_value, height_unit

        confirm = input(f"Is {base_value} {base_unit if base_unit else 'units'} the base? (Y/N): ")
        if confirm.lower() == 'y':
            height_value, height_unit = prompt_for_height(base_value, base_unit)
            return base_value, base_unit, height_value, height_unit
        else:
            continue


def prompt_for_height(base_value, base_unit):
    """
    Prompt user for the height of the triangle, optionally specifying units.
    
    Args:
    - base_value (float): The base length of the triangle.
    - base_unit (str or None): The optional unit of measurement for the base.
    
    Returns:
    - height_value (float): The height of the triangle.
    - height_unit (str or None): The optional unit of measurement for the height.
    """
    while True:
        height_str = input(f"Enter height of the triangle (in {base_unit if base_unit else 'units'}): ")
        try:
            height_value = float(height_str)
            return height_value, None  # No unit provided initially
        except ValueError:
            print("Oops, something went acute! Enter height as a number, please.")


def parse_input(input_str):
    """
    Parse user input to extract base and height values with optional units.
    
    Args:
    - input_str (str): User input string containing base and optionally height with optional units.
    
    Returns:
    - base_value (float or None): The extracted base length of the triangle.
    - base_unit (str or None): The optional unit of measurement for the base.
    - height_value (float or None): The extracted height of the triangle.
    - height_unit (str or None): The optional unit of measurement for the height.
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
    Validate that both base and height values are positive.
    
    Args:
    - base_value (float): The base length of the triangle.
    - height_value (float): The height of the triangle.
    
    Returns:
    - bool: True if both base and height are positive, False otherwise.
    """
    return base_value > 0 and height_value > 0


def calculate_triangle_area(base, height):
    """
    Calculate the area of the triangle given base and height.
    
    Args:
    - base (float): The base length of the triangle.
    - height (float): The height of the triangle.
    
    Returns:
    - float: The calculated area of the triangle.
    """
    return 0.5 * base * height


def calculate_triangle_perimeter(base, height):
    """
    Calculate the perimeter of the triangle given base and height.
    
    Args:
    - base (float): The base length of the triangle.
    - height (float): The height of the triangle.
    
    Returns:
    - float: The calculated perimeter of the triangle.
    """
    return base + 2 * math.sqrt((base / 2) ** 2 + height ** 2)


def calculate_total_surface_area(area, perimeter):
    """
    Calculate the total surface area of the triangle.
    
    Args:
    - area (float): The area of the triangle.
    - perimeter (float): The perimeter of the triangle.
    
    Returns:
    - float: The calculated total surface area of the triangle.
    """
    return area + perimeter


def exit_program():
    """
    Exit the program gracefully.
    """
    print("Leaving so soon? Remember, geometry shapes our world!")
    import sys
    sys.exit()


def print_line():
    """
    Print a decorative line for visual separation in output.
    """
    print('⧦' * 95)


def main():
    """
    Main function to orchestrate the calculation and display of triangle properties.
    """
    os.system('clear')

    while True:
        base, base_unit, height, height_unit = prompt_for_triangle_input()

        if base is None and height is None:
            print("Exiting...")
            break

        if validate_input(base, height):
            area = calculate_triangle_area(base, height)
            perimeter = calculate_triangle_perimeter(base, height)
            tsa = calculate_total_surface_area(area, perimeter)

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
