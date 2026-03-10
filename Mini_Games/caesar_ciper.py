logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
game_over = 'yes'
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(message, alphabets, shift_number):
    result = ""
    for letter in message:
        if letter in alphabets:
            index = (alphabets.index(letter) + shift_number) % len(alphabets)
            result += alphabets[index]
        else:
            result += letter
    print(f"Here's the encoded result: {result}")

def decode(message, alphabets, shift_number):
    result = ""
    for letter in message:
        if (letter in alphabets):
            index = (alphabets.index(letter) - shift_number)
            result += alphabets[index]
        else:
            result += letter
    print(f"Here's the decrypted message: {result}")

while game_over == 'yes':
    type_of_crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    if type_of_crypt == "encode":
        encode(message, alphabets, shift_number)

    elif type_of_crypt == "decode":
        decode(message, alphabets, shift_number)

    else:
        print("The provided input is not valid. Please try again.")

    game_over = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
