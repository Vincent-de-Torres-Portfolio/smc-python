"""
Vincent de Torres
CS87A-Summer 2024 
Filename: do_i_have_enough.py

This module simulates a scenario where a user wants to determine if they can afford a product. 
It calculates the total cost of the product including an 8% sales tax, prompts the user to input 
the amount of money they have, and checks if they can afford the purchase. It then displays a 
purchase summary including the breakdown of cost, tax, total amount, and whether the purchase is 
affordable based on the user's input.

Constants:
- TAX_RATE (float): The tax rate applied to the product price (8%).
- PRODUCT_PRICE (float): The base price of the product before tax.

Functions:
- print_message(message): Prints a message in a banner-like ASCII art style using box-drawing characters.
- calculate_total_cost(price): Calculates the total cost of the product including tax.
- prompt_for_money(): Prompts the user to input how much money they have.
- check_affordability(money, total_cost): Checks if the user can afford the product based on their money and total cost.
- display_purchase_result(affordable, total_cost, money): Displays the purchase summary including cost breakdown.
- do_i_have_enough(): Main function to simulate the process of determining if the user can afford a product.
- main(): Executes the main function to initiate the simulation.

"""
TAX_RATE = 0.08
PRODUCT_PRICE = 100.0

def print_message(message):
    """
    Prints a message in a banner-like ASCII art style using box-drawing characters.

    Parameters:
    - message (str): The message to be displayed.
    """
    border_top = '┌' + '─' * (90 + 2) + '┐'
    border_bottom = '└' + '─' * (90 + 2) + '┘'
    print(border_top)
    print(f' {message} ')
    print(border_bottom)

def calculate_total_cost(price):
    """
    Calculate the total cost including tax.

    Parameters:
    - price (float): The price of the product.

    Returns:
    - float: The total cost including tax.
    """
    total_cost = price * (1 + TAX_RATE)
    return total_cost

def prompt_for_money():
    """
    Prompt the user to input how much money they have.

    Returns:
    - float: Amount of money user inputs.
    """
    while True:
        try:
            money = float(input("How much money do you have? $"))
            return money
        except ValueError:
            print("Please enter a valid amount (numbers only).")

def check_affordability(money, total_cost):
    """
    Check if the user can afford the product based on their money and total cost.

    Parameters:
    - money (float): Amount of money user has.
    - total_cost (float): Total cost of the product including tax.

    Returns:
    - bool: True if user can afford, False otherwise.
    """
    return money >= total_cost

def display_purchase_result(affordable, total_cost, money):
    """
    Display the result of whether the user can afford the product and breakdown of cost, tax, and total.

    Parameters:
    - affordable (bool): Whether the user can afford the product.
    - total_cost (float): Total cost of the product including tax.
    - money (float): Amount of money user has.
    """
    print_message("Purchase Summary")
    if affordable:
        tax_amount = total_cost - PRODUCT_PRICE
        print(f"\t{('Product Price:'):<20} {f'${PRODUCT_PRICE:.2f}':>10}")
        print(f"\t{('Tax (' + f'{TAX_RATE * 100}' + '%):'): <20} {f'${tax_amount:.2f}':>10}")
        print(f"\t{('Total Cost:'):<20} {f'${total_cost:.2f}':>10}")
        print(f"\t{('Money Left:'):<20} {f'${money - total_cost:.2f}':>10}")
        print_message(f"\n\t Congratulations, you can buy the product.")
    else:
        print(f"{('Total Cost:'):<20} {f'${total_cost:.2f}':>12}")
        if money < total_cost:
            print(f"{'You need an additional':<20} {f'${total_cost - money:.2f}':>10}")
        else:
            print(f"{'Sorry, you cannot afford the product.':^40}")
    print("")

 
def do_i_have_enough():
    """
    Function to determine if the user can afford a product.
    """
    total_cost = calculate_total_cost(PRODUCT_PRICE)
    
    money = prompt_for_money()
    affordable = check_affordability(money, total_cost)
    display_purchase_result(affordable, total_cost, money)

def main():
    """
    Main function to simulate the process of determining if the user can afford a product.
    """
    print_message("\tWelcome to the Product Purchase Simulator")
    do_i_have_enough()

# Execute the main function
if __name__ == "__main__":
    main()
