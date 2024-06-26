def up_it(number):
    double_up = number * 2
    quadruple_up = number * 4
    return f"\\~Double up is {double_up}~\\-----/~Quadruple up is {quadruple_up}~/"

def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program : \n")
            break

        try:
            number = int(user_input)
            result = up_it(number)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Challenge: Loop for numbers 1 through 10
    for number in range(1, 11):

        result = up_it(number)
        print(result)


if __name__ == "__main__":
    main()
