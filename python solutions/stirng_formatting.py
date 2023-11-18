def print_formatted(number):
    # Calculate the width required for formatting based on the binary representation of the input number.
    width = len(bin(number)[2:])

    # Loop from 1 to the given number.
    for i in range(1, number+1):
        # Convert the number 'i' to decimal and store it as a string.
        deci = str(i)

        # Convert the number 'i' to octal, remove the "0o" prefix, and store it as a string.
        octa = oct(i)[2:]

        # Convert the number 'i' to hexadecimal, remove the "0x" prefix, and convert it to uppercase. Store it as a string.
        hexa = hex(i)[2:].upper()

        # Convert the number 'i' to binary, remove the "0b" prefix, and store it as a string.
        bina = bin(i)[2:]

        # Print the formatted numbers for decimal, octal, hexadecimal, and binary representations.
        # Use rjust(width) to ensure they are right-justified and aligned according to the calculated width.
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))

if __name__ == '__main__':
    # Take user input for the number 'n'.
    n = int(input())

    # Call the 'print_formatted' function to print the formatted numbers.
    print_formatted(n)
