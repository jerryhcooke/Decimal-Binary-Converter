# A converter that takes a denary number and converts it, using comparison rather than recursion, to binary

print("Please enter a decimal number to convert")

while True:
    def generate_comparisons(n):
        list = [1]
        while max(list) < n:
            x = max(list)
            list.append(x * 2)
        comparisons = reversed(list)
        return(comparisons)

    def convert_to_binary(decimal):
        binary = []
        c = generate_comparisons(int(original))
        for n in c:
            if (decimal - n) >= 0:
                binary.append(1)
                decimal -= n
            else:
                binary.append(0)
        converted = (str(i) for i in binary)  # I need to turn this section of code into a function to tidy things up
        joined= ''.join(converted)
        n = 4
        display = [joined[i:i+n] for i in range (0, len(joined), n)]  # rejig so that last block is always four digits
        print("")
        print(display)
        print("")
        print("Input another number or x to exit")


    original = input("Your number: ")
    if original != 'x':
        convert_to_binary(int(original))
    else:
        print("Thanks for using the converter!")
