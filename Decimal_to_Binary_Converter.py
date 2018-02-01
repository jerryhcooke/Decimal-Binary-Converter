# A converter that takes a denary number and converts it, using comparison rather than recursion, to binary


def generate_comparisons(number): # generates a list of powers of two, the max being the first that is greater than n
    list = [1]
    while max(list) < number:
        x = max(list)
        list.append(x * 2)
    comparisons = reversed(list)
    return comparisons


def convert_to_binary(decimal):  # takes the output of generate_comparisons and uses it to to convert decimal to   binary
    binary = []
    comparison = generate_comparisons(int(decimal))
    for number in comparison:
        if (decimal - number) >= 0:
            binary.append(1)
            decimal -= number
        else:
            binary.append(0)
    return binary


def split_into_fours(output):  # takes an inputted list, reverses it, splits it into four, then reverses it
    new_string = (str(i) for i in output)
    joined = ''.join(new_string)
    joined_flipped = (reversed(joined))
    iterable = ''.join(joined_flipped)
    display = [iterable[i:i+4] for i in range (0, len(joined), 4)]
    display_flipped = (reversed(display))
    return ' '.join(display_flipped)


def binary_to_decimal(user_binary):  # takes an inputted binary number and converts decimal
    output_decimal = 0
    for bit in user_binary:
            output_decimal = output_decimal*2 + int(bit)
    return output_decimal


while True:

    print("To convert Decimal > Binary, enter B, or for Binary > Decimal, enter D, or enter X to quit", "\n")
    choice = input("Please select an option: ")

    if choice == "x":
        break
    elif choice == 'b':
        user_number = input("Your number: ")
        result = split_into_fours(convert_to_binary(int(user_number)))
        print("Your number converted to binary is: ", result, " \n")
    else:
        user_number = input("Your number: ")
        result = binary_to_decimal(user_number)
        print("Your number converted to decimal is: ", result, " \n")



