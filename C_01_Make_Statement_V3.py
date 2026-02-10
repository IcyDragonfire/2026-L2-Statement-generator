# Functions go here
def make_statement(statement, decoration, lines=1):
    """Emphasise headings by adding decoration"""

    middle = f"{decoration * 5} {statement} {decoration * 5}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main routine goes here
make_statement("Cloud is in the sky", "=", 3)
print()
make_statement("Cloud is still in the sky", "*", 2)
print()
make_statement("Cloud in action", "☁️",)