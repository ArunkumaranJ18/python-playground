calc_art = """
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_| 

 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


print(calc_art)

def calculator():

    game_type = 'n'
    result = 0.0
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    while game_type != 'q':

        if game_type == 'y':
            first_number = result
        else:
            first_number = float(input("What's the first number?"))

        for key in operations:
            print(key)

        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?"))

        if operations.get(operation):
            result = operations[operation](first_number,second_number)
        else:
            print("Please enter a valid operation!")
            game_type = 'q'
            continue

        print(f"{first_number} {operation} {second_number} = {result}")

        game_type = input(f"Type 'y' to continue with {result}, or type to start a new calculation or type 'q' to quit.")

calculator()