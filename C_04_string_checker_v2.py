# Functions
def string_check(question, valid_ans_list, num_letters):
    """Check that the user entera a full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Choose an option from {valid_ans_list}")


# Main Routine
yes_no = ['yes', 'no']
payment_options = ['cash', 'credit']

like_coffee = string_check("You like Coffee",
                           yes_no, 1)

if like_coffee == "no":
    print("I don't care, you have no choice in coffee land")

print(f"You have chosen {like_coffee}")
pay_method = string_check("Payment method: ", payment_options, 2)

print(f"you chose to pay {pay_method}")
