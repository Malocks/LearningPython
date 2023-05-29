"""
test
"""
from api_requests import requests

def get_user_input():
    """
    This function prompts the user to enter a number between 1 and 30 and returns the input value.
    """

    question = "Please insert a number between 1 and 30: "
    result_product_id = input(question)
    return result_product_id


def main():
    """
    Call the get_user_input() function and store the return value
    """

    user_input = get_user_input()
    requests.PRODUCT_ID(user_input)

    # Concatenation strings using the format method
    show_product = f"Here is your product, {user_input}!"

    # Print the Dialog in the console
    print(show_product)


if __name__ == "__main__":
    main()
