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
    
''')


# Main Routine

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
print("program continues...")
