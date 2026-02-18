# Yes / No function
def yes_no(question):
    """Checking user answers yes or no (y / n)"""


    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Input a yes or no answer.\n")



# Main Routine
while True:
    favorite_color_red = yes_no("Is red your favorite color? ")

    print(f"You chose {favorite_color_red}")

    if favorite_color_red == "yes":
        print("The correct answer \n")
    else:
        print("WRONG! Your favorite color is red \n")

