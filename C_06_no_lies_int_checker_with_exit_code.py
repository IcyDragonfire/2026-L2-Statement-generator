# Functions
def int_check(question):
    """Checks user enters an integer """

    error = "Enter an integer"

    exit_code = "xxx"

    while True:

        try:

            response = input(question)

            if response == exit_code:
                return response

            return int(response)

        except ValueError:
            print(error)

# Main routine
while True:
    print()

    # Ask for users name
    name = input("Name: ")

    # Ask for age (has to be between set numbers
    age = int_check("Age: ")

    # output message
    if age == "xxx":
        break
    elif age < 12:
        print(f"{name} is too young")
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
