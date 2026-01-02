# This function checks if a number is even or odd
def check_even_odd(number):

    # If the number can be divided by 2 with no remainder
    if number % 2 == 0:
        return "The number is even."

    # If the number has a remainder when divided by 2
    else:
        return "The number is odd."


# This is where the program starts
def main():

    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Send the number to the function
    result = check_even_odd(num)

    # Print the message from the function
    print(result)


# This makes sure the program runs only when started here
if __name__ == "__main__":
    main()
