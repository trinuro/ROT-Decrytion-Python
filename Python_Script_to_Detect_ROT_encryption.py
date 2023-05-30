'''
   .----.
   |C>_ |
 __|____|__
|  ______--|
`-/.::::.\-'a
 `--------'

This is a simple project I did on 26/5/2023. I realised the previous version did not work.
This code shows a ROT encryption algorithm. 
Letters will be shifted to the right by a certain amount, called the 'rotation number'
Uppercase and lowercase letters will remain upper- or lower-case
Numbers are unaffected.

ASCII ART from https://www.asciiart.eu/computers/computers
'''

UPPER_CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CHAR_SET = "abcdefghijklmnopqrstuvwxyz"
DEFAULT_ROT = 13

def rotate(position: int, rotation: int)-> int:
    new_position = position + rotation
    if new_position>25:
        new_position-= 26
    return new_position
# Increases the index of the character. If the index is more than 25, start again from 0.

def encrypt_char(character: str, rotation_number: int) -> str:
    if character.isalpha():
        if character.isupper():
            index = UPPER_CHAR_SET.find(character)
            new_index = rotate(index, rotation_number)
            new_character = UPPER_CHAR_SET[new_index]
        if character.islower():
            index = LOWER_CHAR_SET.find(character)
            new_index = rotate(index, rotation_number)
            new_character = LOWER_CHAR_SET[new_index]

    else:
        new_character = character
        index = "NO INDEX"

    return new_character
# Encrypts a Character. If it is an integer, no encryption is applied

def encrypt(input_string: str, rot_number: int = DEFAULT_ROT)-> str:
    encrypted_text = list()
    for i in input_string:
        encrypted_text.append(encrypt_char(i, rot_number))
    return listToString(encrypted_text)
# Encrypts the whole string

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

#def decrypt_char()


#while True:
#    i = input("Input: ")
#    desired_rot = int(input("ROT: "))
#    print(encrypt(i, desired_rot))
# Just code for debugging
