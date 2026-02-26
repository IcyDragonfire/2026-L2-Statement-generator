# Functions
def make_statement(statement, decoration):
    pass

def string_check(question, valid_answers=('yes', 'no'), num_letters=1):

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

def instructions():
    make_statement("Instructions", "🛃")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticker holder who wins the draw (their ticket is free).
    
''')

def not_blank(question):
    """Checks that the users response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You can not make this answer blank. Try again. \n")

def int_check(question):
    """Checks user enters an integer """

    error = "Enter an integer"

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# Initialise variables
payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want Instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    # ask user for name
    name = not_blank("Name: ")
    # If name is exit code, break out of the loop
    if name == "xxx":
        break

    # Ask user for age
    age = int_check("Age: ")

    # output error / success message
    if age < 12:
        print(f"{name} is too young for this movie")
        print()
        continue
    elif age > 120:
        print(f"{name} is too old for this movie")
        continue
        print()
    else:
        pass


    # ask user for payment method
    pay_method = string_check("Payment method: ", payment_ans, 2 )
    print(f"{name} has bought a ticket ({pay_method})")
    print()


    tickets_sold +=1

if tickets_sold == MAX_TICKETS:
    print(f"We have sold all {MAX_TICKETS} tickets")
else:
    print(f"We have sold {tickets_sold} out of {MAX_TICKETS} tickets")
