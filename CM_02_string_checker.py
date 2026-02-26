# Functions
def string_checker(question, valid_ans_list=['yes', 'no'],
                   num_letters=1):

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's in the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Choose an item from {valid_ans_list}\n")

# Main routine
# payment_list = ['cash', 'credit']

while True:
    want_instructions = string_checker("Do you want to see the instructions")
    print(f"You chose {want_instructions}")
    print()

# pay_method = string_checker("payment method: ", payment_ans, 2)
# print(f"you chose {payment_method}")