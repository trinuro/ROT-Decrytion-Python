##########################################################################################
# This script is used to print out all posibble ROT combinations
# Problem: I needed a way to determine whether it was a ROT encryption or not
# Tought process: Initially, I wanted to make it able to detect what ROT number it is
# automatically but it was too difficult. Instead, I just created a script to print
# out all possible ROT combinations. The user will then use logic to choose
# a possible ROT number
##########################################################################################
import string

charSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#standard character set

user_input = ""
ROT = 13 #Default

def determine_position(i):
    output = []
    for i in encryptedData:
        position = charSet.find(i)
        output.append(position)
    return(output)
#map position of all characters in string to charSet

def get_real_pos(i):
    actual_position_array = []
    for element in i:
        if element == -1:
            actual_position_array.append(element)
        else:
            actual_position_array.append((element+ ROT)%26)
    return(actual_position_array)
#add ROT number to each element in position_array

def remap(input_array):
    output =[]
    iteration = 0
    for i in input_array:
        if i != -1:
            output.append(charSet[i])
        else:
            output.append(encryptedData[iteration])
        if user_input[iteration].islower():
            output[iteration] = output[iteration].lower()
        iteration += 1
    return(output)
#map back the elements in array to charSet

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

def decrypt(i):
    main_output = []
    position_array = determine_position(i)
    actual_position_array = get_real_pos(position_array)
    half_ready_output = remap(actual_position_array)
    return(listToString(half_ready_output))
#main decrypt function


#main
while True:
    print("What is your encrypted data?")
    user_input = input()
    encryptedData = user_input.upper()
    print("What is your ROT number?(0-25) \nSpecial number: all")
    x = input()
    
    if x == "all":
        for i in range(26):
            ROT = i
            print('ROT ['+str(ROT)+']'+' '+decrypt(encryptedData))
    elif not isinstance(x, str):
        if int(x) in range(0,26):
            ROT = int(x)
            print('ROT ['+str(ROT)+']'+' '+decrypt(encryptedData))
    else:
        print("Please enter a valid number")

    print("\nContinue?(Y/N)")
    y = input().upper()
    if y == 'Y':
        continue
    else:
        break
