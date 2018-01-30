# A converter that takes a denary number and converts it, using comparison rather than recursion, to binary
import sys

def generate_comparisons(n):  # generates a list of powers of two, the max being the first that is greater than n
    list = [1]
    while max(list) < n:
        x = max(list)
        list.append(x * 2)
    comparisons = reversed(list)
    return comparisons


def convert_to_binary(d):  # takes the output of generate_comparisons and uses it to to convert d to binary
    binary = []
    c = generate_comparisons(int(d))
    for n in c:
        if (d - n) >= 0:
            binary.append(1)
            d -= n
        else:
            binary.append(0)
    return binary


def split_into_fours(x):  # takes an inputted list, reverses it, splits it into four, then reverses it
    new_string = (str(i) for i in x)
    joined = ''.join(new_string)
    joined_flipped = (reversed(joined))
    iterable = ''.join(joined_flipped)
    display = [iterable[i:i+4] for i in range (0, len(joined), 4)]  # rejig so that last block is always four digits
    display_flipped = (reversed(display))
    return ' '.join(display_flipped)


while True:

    print("Enter a decimal number to convert or x to exit", "\n")
    user_number = input("Your number: ")
    if user_number != 'x':
        result = split_into_fours(convert_to_binary(int(user_number)))
        print("Your number converted to binary is: ", result, " \n")
    else:
        sys.exit()


