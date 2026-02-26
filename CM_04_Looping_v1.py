# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # If name is exit code, break out of the loop
    if name == "xxx":
        break

    tickets_sold +=1

if tickets_sold == MAX_TICKETS:
    print(f"We have sold all {MAX_TICKETS} tickets")
else:
    print(f"We have sold {tickets_sold} out of {MAX_TICKETS} tickets")