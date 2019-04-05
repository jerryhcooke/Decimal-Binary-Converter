# A converter that takes a denary number and converts it, using comparison
# rather than recursion, to binary

import sys

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty())

cprint(figlet_format('Binary / Decimal Converter', font='doom'), 'white',
       attrs=['bold'])


def generate_comparisons(number):   # generates a list of powers of two, the
    # max being the first that is greater than n
    list = [1]
    while max(list) < number:
        x = max(list)
        list.append(x * 2)
    comparisons = reversed(list)
    return comparisons


def convert_to_binary(decimal):
    # takes the output of generate_comparisons and uses it to to convert
    binary = []
    comparison = generate_comparisons(int(decimal))
    for number in comparison:
        if (decimal - number) >= 0:
            binary.append(1)
            decimal -= number
        else:
            binary.append(0)
    new_string = "".join(str(i) for i in binary)
    return new_string


def binary_to_decimal(user_binary):
    # takes an inputted binary number and converts decimal
    output_decimal = 0
    for bit in user_binary:
        output_decimal = output_decimal*2 + int(bit)
    return output_decimal


while True:
    print("Please select from the following options:", "\n")
    print("1 - Convert Decimal -> Binary")
    print("2 - Convert Binary -> Decimal")
    print("X - Exit the program", "\n")
    choice = input("Please make your selection: ")
    if choice == "x":
        break
    elif choice == '1':
        try:
            user_number = input("Your number: ")
            result = convert_to_binary(int(user_number))
            print("\n", "Your number converted to binary is: ", "0b", result,
                        " \n")
        except ValueError:
            print("\n", "Please enter an integer" " \n")
    elif choice == '2':
        try:
            user_number = input("Your number: ")
            result = binary_to_decimal(user_number)
            print("\n", "Your number converted to decimal is: ", result, " \n")
        except ValueError:
            print("\n""Please enter a decimal number." " \n")
    else:
        print("\n", "!! Please select from one of the three options !!", " \n")
