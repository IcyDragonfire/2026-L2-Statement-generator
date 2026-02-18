# Functions
def int_check(question, low, high):
    """Checks users integer is between 2 values"""

    error = f"You failed. Enter an integer between {low} and {high}\n"


    while True:

        try:
            # change the response to an integer and check it's more than zero
            response = int(input(question))

            response = int(response)

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine

# looping for testing purposes
while True:

    print()

    #ask user for an integer
    my_num = int_check("choose a number: ", 1, 10)
    print(f"You chose {my_num}")


