# Functions
def string_check(question, valid_ans_list):
    """Check that the user entera a full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Choose an option from {valid_ans_list}")


# Main Routine
levels = ['epic sauce', 'medium', 'hard']

question_red = string_check("Yes or no, why is "
                            "red your favorite color?", ['yes', 'no'])
choose_level = string_check("choose a level: ", levels)
