"""
Vincent de Torres
CS87A-Summer 2024 
Filename:did_i_fail.py

This script calculates and displays the grade and remarks based on a provided score.
It includes constants for grade thresholds and remarks, functions for input handling,
grade determination using both if and switch-like approaches, and display functions.

Constants:
- GRADE_THRESHOLDS: Dictionary defining grade thresholds and associated remarks.
- LABEL_INPUT_SCORE: Label for input score display.
- LABEL_LETTER_GRADE: Label for letter grade display.
- LABEL_REMARKS: Label for remarks display.
- WIDTH_SCORE: Width for input score alignment.

Functions:
- print_message(text, max_width=None): Formats text into a box with optional maximum width.
- preprocess_input(user_input): Sanitizes and converts user input to an integer.
- determine_grade_switch(score): Determines grade and remarks using a switch-like approach based on score.
- determine_grade(score): Determines grade and remarks using if-elif conditions based on score.
- display_grade(input_score, letter_grade, remarks): Displays formatted input score, letter grade, and remarks.
- get_score(): Prompts user to enter a score between 1 and 100.
"""

# Constants defining grade thresholds and remarks
GRADE_THRESHOLDS = {
    "A": (90, 100, "No, you got an A!"),
    "B": (80, 89, "No, you got a B!"),
    "C": (70, 79, "It's a C!"),
    "D": (60, 69, "It's a D!"),
    "F": (0, 59, "Yeah, you did fail, I'm sorry!"),
}

# Constants for display labels and widths
LABEL_INPUT_SCORE = "Input Score"
LABEL_LETTER_GRADE = "Letter Grade"
LABEL_REMARKS = "Remarks"
WIDTH_SCORE = 3  # Width for input score alignment


def print_message(text, max_width=None):
    """
    Formats text into a box with optional maximum width.

    Args:
    - text (str or list): Text to be formatted into a box. Can be a single string or a list of strings.
    - max_width (int, optional): Maximum width for the box. Defaults to None.

    Returns:
    - str: Formatted text enclosed in a box.

    Raises:
    - ValueError: If input is not a string or a list of strings.
    """
    if isinstance(text, str):
        lines = [text]
    elif isinstance(text, list):
        lines = text
    else:
        raise ValueError("Input must be a string or a list of strings.")

    if max_width:
        lines = [line[:max_width] for line in lines]

    min_width = max(len(line) for line in lines)  # Determine minimum width based on longest line
    box_width = min_width + 4  # Border and padding width based on minimum width

    result = []
    result.append(f"╭{'─' * box_width}╮")
    for line in lines:
        padding = ' ' * (min_width - len(line) + 2)
        result.append(f"| {line}{padding} |")
    result.append(f"╰{'─' * box_width}╯")

    return '\n'.join(result)


def preprocess_input(user_input):
    """Sanitize and convert user input to an integer."""
    try:
        processed_input = int(user_input.strip())  # Remove any leading/trailing whitespace and convert to int
        return processed_input
    except ValueError:
        return None  # Return None if input cannot be converted to an integer


def determine_grade_switch(score):
    """Determine grade and remarks based on the provided score using a floor division approach."""
    switch_value = score // 10
    
    # Using match-case (available from Python 3.10+)
    match switch_value:
        case 10:
            return "A", "No, you got an A!"
        case 9:
            return "A", "No, you got an A!"
        case 8:
            return "B", "No, you got a B!"
        case 7:
            return "C", "It's a C!"
        case 6:
            return "D", "It's a D!"
        case _:
            return "F", "Yeah, you did fail, I'm sorry!"


def determine_grade(score):
    """Determine grade and remarks based on the provided score."""
    for grade, (lower, upper, remarks) in GRADE_THRESHOLDS.items():
        if lower <= score <= upper:
            return grade, remarks
    return None, "Invalid score entered."


def display_grade(input_score, letter_grade, remarks):
    """Display the input score, letter grade, and remarks with aligned key-value pairs."""
    output = []
    output.append(f"{LABEL_INPUT_SCORE:<15} : {input_score}")  # Left-aligned label, right-aligned score
    output.append(f"{LABEL_LETTER_GRADE:<15} : {letter_grade}")  # Left-aligned label, left-aligned grade
    output.append(f"{LABEL_REMARKS:<15} : {remarks}")  # Left-aligned label, left-aligned remarks

    print(print_message(output))


def get_score():
    """Prompt user to enter a score between 1 and 100."""
    while True:
        score_input = input("Enter your score (1-100), or 'q' to quit: ").strip().lower()
        if score_input == 'q':
            return 'q'  # Signal to quit
        score = preprocess_input(score_input)
        if score is not None and 1 <= score <= 100:
            return score
        else:
            print("Invalid input. Please enter a number between 1 and 100.")


def main():
    """Main function to run the grade calculator."""
    while True:
        score = get_score()
        if score == 'q':
            break  # Exit loop if user enters 'q'
        
        score = int(score)  # Convert score to integer after confirming it's not 'q'
        
        # Using the if approach
        grade, remarks = determine_grade(score)
        if grade:
            print("Using if approach:")
            display_grade(score, grade, remarks)
        else:
            print(remarks)
        
        # Using the switch-like approach
        grade_switch, remarks_switch = determine_grade_switch(score)
        if grade_switch:
            print("\nUsing switch-like approach:")
            display_grade(score, grade_switch, remarks_switch)
        else:
            print(remarks_switch)


if __name__ == "__main__":
    main()
