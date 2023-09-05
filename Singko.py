def decToBin(decimal):
    binary = []

    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal // 2
    return binary


def binaryToN(binary, typeOfN):
    base = 1
    decimal = 0
    if typeOfN == "D":
        # Binary to Decimal
        while binary > 0:
            remainder = binary % 10
            decimal = decimal + remainder * base
            base = base * 2
            binary = binary // 10
        return decimal

    elif typeOfN == "O":
        # Binary to Decimal
        while binary > 0:
            remainder = binary % 10
            decimal = decimal + remainder * base
            base = base * 2
            binary = binary // 10

        # Binary to Octal
        # octal = ''.join(decToOctal(decimal))
        octal_string = decToOctal(decimal)

        octal_str = ""
        for i in octal_string[::-1]:
            octal_str += str(i)

        return octal_str

    else:
        # binary to decimal
        while binary > 0:
            remainder = binary % 10
            decimal = decimal + remainder * base
            base = base * 2
            binary = binary // 10

        # decimal to binary
        hex_string = ''.join(decToHex(decimal))

        hex_str = ""

        for i in hex_string[::-1]:
            hex_str += i

        return hex_str


def decToOctal(dec):
    octal = []

    while dec > 0:
        octal.append((dec % 8))
        dec = dec // 8

    return octal


def decToHex(dec):
    hexadecimal = []

    while dec != 0:
        remainder = dec % 16
        if remainder < 10:
            hexadecimal.append(remainder)
        else:
            hexadecimal.append(chr(ord('A') + remainder - 10))
        dec = dec // 16

    return hexadecimal


def printList(list_of_number_system):
    for i in list_of_number_system[::-1]:
        print(i, end='')


def main():
    choice = int(input("Please enter number of choice (1-4): "))

    if choice == 1:
        dec = int(input("Please enter a decimal value: "))

        to_bin = decToBin(dec)

        printList(to_bin)

    elif choice == 2:
        binary = int(input("Please enter a binary value: "))
        N = input("Please enter what N of conversion to do (D,O,H): ")

        convert_result = binaryToN(binary, N)

        print(f"{binary} -> {convert_result}")

    elif choice == 3:
        dec = int(input("Please enter a decimal value: "))

        to_octal = decToOctal(dec)

        printList(to_octal)

    elif choice == 4:
        dec = int(input("Please enter a decimal value: "))

        to_hex = decToHex(dec)

        printList(to_hex)

    else:
        print("Invalid option.")


main()
