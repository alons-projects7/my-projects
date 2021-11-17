alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(type, word, num):
    new_word = ''
    for letter in word:
        if letter not in alphabet:
            new_word += letter
        else:
            ind = alphabet.index(letter)
            if type == "encode":
                new_index = ind + num
                test = new_index // 25
                new_index -= test * 26

            elif type == "decode":
                new_index = ind - num
                test = new_index // 25
                new_index += -1 * test * 26

            new_word += alphabet[new_index]
    print(new_word)


caesar(direction, text, shift)
bol = True
while bol:
    ans = input("Would you like to continue?")
    if ans == "yes":
        direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text1 = input("Type your message:\n").lower()
        shift1 = int(input("Type the shift number:\n"))
        caesar(direction1, text1, shift1)
    elif ans == "no":
        print("Goodbye")
        bol = False
    else:
        print("please type yes or no")


