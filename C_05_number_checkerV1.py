# Functions
def num_check(question, num_type, exit_code=None):
    """Checks user enters and integer or is more than zero"""

    if num_type == "integer":
        error = "Enter an integer more than zero\n"
        change_to = int
    else:
        error = "Enter a number more than zero\n"
        change_to = float


    while True:
        response = input(question).lower()

        # exit code
        if response == exit_code:
            return response

        try:
            # change response to an integer and check its more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine
while True:
    print()

    my_float = num_check("Enter a number more than 0: ", "float")
    print()
    print(f"Congratulations, you have chosen {my_float}")
    print()
    my_int = num_check("Enter an integer more than 0: ",
                       "integer", "")

    if my_int == "":
        print("You have chosen infinite mode\n")
    else:
        print(f"You have chosen {my_int}")
