def maxNumber(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        maximum = num1
    elif num2 >= num1 and num2 >= num3:
        maximum = num2
    else:
        maximum = num3
    return maximum


def main():
    num1 = int(input("Enter value: "))
    num2 = int(input("Enter value: "))
    num3 = int(input("Enter value: "))

    get_max = maxNumber(num1, num2, num3)

    print(f"{get_max} is the maximum among the three integers.")


main()
