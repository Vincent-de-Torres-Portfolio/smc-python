"""
Vincent de Torres
CS87A-Summer 2024 
Filename: voltage.py

Problem:
Ask a user to enter a number representing voltage and classify it into different categories:
- <= 30: Low voltage
- 31-59: Medium voltage
- >= 60 and < 240: High voltage
- >= 240: Electrocution

Example:
- Input: 50
- Output: Medium voltage

Functions:
- validate_input(input_str): Validates user input to ensure it's a valid integer.
- classify_voltage(voltage): Determines the voltage category based on the input value using a dictionary-based approach.

Reference:
- Python input validation: https://docs.python.org/3/library/functions.html#input
"""

# Constants for voltage thresholds and messages
LOW_VOLTAGE_THRESHOLD = 30
MEDIUM_VOLTAGE_THRESHOLD = 59
HIGH_VOLTAGE_THRESHOLD = 239

# Messages corresponding to voltage categories
LOW_VOLTAGE_MESSAGE = "Low voltage"
MEDIUM_VOLTAGE_MESSAGE = "Medium voltage"
HIGH_VOLTAGE_MESSAGE = "High voltage"
ELECTROCUTION_MESSAGE = "Electrocution"

def validate_input(input_str):
    """
    Validates user input to ensure it's a valid integer.
    
    Args:
    - input_str (str): String input from the user.
    
    Returns:
    - int: Validated integer value.
    
    Raises:
    - ValueError: If input is not a valid integer.
    """
    while True:
        try:
            value = int(input(input_str))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def classify_voltage(voltage):
    """
    Determines the voltage category based on the input value using predefined constants.
    
    Args:
    - voltage (int): Voltage value entered by the user.
    
    Returns:
    - str: Classification message based on voltage range.
    """
    if voltage < 0:
        return "Negative voltage"
    elif voltage <= LOW_VOLTAGE_THRESHOLD:
        return LOW_VOLTAGE_MESSAGE
    elif voltage <= MEDIUM_VOLTAGE_THRESHOLD:
        return MEDIUM_VOLTAGE_MESSAGE
    elif voltage <= HIGH_VOLTAGE_THRESHOLD:
        return HIGH_VOLTAGE_MESSAGE
    else:
        return ELECTROCUTION_MESSAGE

def main():
    """
    Main function to ask user for voltage input, validate it, and classify it.
    """
    print("Voltage Classification")
    
    # Validate input and normalize if needed (not implemented in this simple case)
    voltage = validate_input("Enter a number representing voltage: ")
    
    # Classify voltage and print the result
    classification = classify_voltage(voltage)
    print(f"The voltage {voltage} is classified as: {classification}")

if __name__ == "__main__":
    main()

