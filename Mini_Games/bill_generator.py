print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M or L: ")
is_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
is_extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")


if size.upper() == "S":
    bill = 15
    if is_pepperoni.upper() == "Y":
        bill += 2
elif size.upper() == "M":
    bill = 20
    if is_pepperoni.upper() == "Y":
        bill += 3
elif size.upper() == "L":
    bill = 25
    if is_pepperoni.upper() == "Y":
        bill += 3

if is_extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

