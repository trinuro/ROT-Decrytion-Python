'''
This project is finished on 28/5/2023
This script can be used to decrypt a string based on suspected ROT encryption.
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

def decrypt_char(character: str, suspected_rot_number: int) -> str:
    if character.isalpha():
        if character.isupper():
            index = UPPER_CHAR_SET.find(character)
            new_index = rotate(index, 26 - suspected_rot_number)
            new_character = UPPER_CHAR_SET[new_index]
        if character.islower():
            index = LOWER_CHAR_SET.find(character)
            new_index = rotate(index, 26 - suspected_rot_number)
            new_character = LOWER_CHAR_SET[new_index]
    else:
        new_character = character

    return new_character
# decrypt a character

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

def decrypt(word: str, suspected_rot: int = DEFAULT_ROT) -> str:
    decrypted_text = list()
    for i in word:
        decrypted_text.append(decrypt_char(i, suspected_rot))
    return listToString(decrypted_text)
# decrypt a string

#while True:
#    i = input("Input: ")
#    sus_rot = int(input("Suspected ROT: "))
#    print(decrypt(i, sus_rot))
# Just code for debugging
