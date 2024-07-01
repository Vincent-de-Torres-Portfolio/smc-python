"""
Vincent de Torres
CS87A-Summer 2024 

Functions:
- parse_input(input_str): Parses the input string to extract the value and unit ('mi' or 'km').
- miles_to_kilometers(value): Converts miles to kilometers.
- kilometers_to_miles(value): Converts kilometers to miles.
- print_line(): Prints a line separator.
- main(): Main function to prompt user input for a distance value and unit, 
          perform conversion using the appropriate function, and display the results.
"""

def parse_input(input_str):
    """
    Parses the input string to extract the value and unit, assuming 'mi' if no unit is specified.

    Args:
    - input_str (str): Input string containing value with optional unit ('mi' or 'km').

    Returns:
    - tuple: A tuple containing (value, unit).
             If parsing fails, returns (None, None).
    """
    try:
        # Check if the input string ends with 'mi' or 'km'
        if input_str.lower().endswith('mi' or ' mi') or input_str.lower().endswith('km' or ' km'):
            unit = input_str[-2:].lower()
            value_str = input_str[:-2].strip()
        else:
            # Assume 'mi' as the default unit if no unit is specified explicitly
            value_str = input_str.strip()
            unit = 'mi'  # Default unit is miles if not specified

        value = float(value_str)

        if unit not in ['mi', 'km']:
            raise ValueError(f"Invalid unit: {unit}")

        return value, unit

    except (ValueError, IndexError) as ve:
        print(f"Error parsing input: {ve}")
        return None, None


def miles_to_kilometers(value):
    """
    Converts miles to kilometers.

    Args:
    - value (float): Value in miles to convert to kilometers.

    Returns:
    - float: Value converted to kilometers.
    """
    return value * 1.60934


def kilometers_to_miles(value):
    """
    Converts kilometers to miles.

    Args:
    - value (float): Value in kilometers to convert to miles.

    Returns:
    - float: Value converted to miles.
    """
    return value / 1.60934

def print_line():
    """
    Prints a line separator.
    """
    print('░' * 95)

def main():
    """
    Main function to prompt user input for a distance value and unit, 
    perform conversion using the appropriate function, and display the results.
    """
    from_val = 'miles (mi)'
    to_val = 'kilometers (km)'
    while True:
        print_line()

        input_str = input("Enter a value with optional unit ('mi' or 'km') [miles]: ")
        value, unit = parse_input(input_str)

        if value is None or unit is None:
            print("Exiting...")
            break

        if unit == 'mi':
            print(f"\n   {from_val} ➦ {to_val} ")
            kilometers = miles_to_kilometers(value)
            print(f"{value} miles is equal to {kilometers:.2f} kilometers")
        elif unit == 'km':
            from_val = 'kilometers (km)'
            to_val = 'miles (mi)'
            print(f"\n   {from_val} ➦ {to_val} ")
            miles = kilometers_to_miles(value)
            print(f"{value} kilometers is equal to {miles:.2f} miles")

if __name__ == "__main__":
    main()
