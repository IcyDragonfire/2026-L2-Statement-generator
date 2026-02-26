# Functions
def int_check(question):
    """Checks user enters an integer """

    error = "Enter an integer"

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)

def not_blank(question):
    """Checks that the users response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You can not make this answer blank. Try again. \n")

def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's in the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Choose an item from {valid_answers}\n")


# Main Routine

# Initialise variables
payment_ans = ('cash', 'credit')

# loop for testing purposes
while True:
    print()

    # ask user for name
    name = not_blank("Name: ")

    # Ask user for age
    age = int_check("Age: ")

    # output error / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method
    pay_method = string_check("Payment method: ", payment_ans, 2 )
    print(f"{name} has bought a ticket ({pay_method})")
