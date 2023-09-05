

def maxNumber(num1, num2, num3):
    maximum = num1
    if num1 >= num2 and num1 >= num3:
        maximum = num1
    elif num2 >= num1 and num2 >= num3:
        maximum = num2
    else:
        maximum = num3
    return maximum


def countNumber(number):
    count = 1
    minimum = number % 10
    maximum = number % 10
    number = number // 10

    while number > 0:
        count = count + 1
        store = number % 10
        if minimum > store:
            minimum = store
        if maximum < store:
            maximum = store
        number = number // 10

    return [count, minimum, maximum]


def totalSum(number):
    sum = 0

    for i in range(1, number + 1):
        sum = sum + i

    return sum


def main():
    print("NUMBER 1")

    print("NUMBER 2")

    num1 = int(input("Enter value: "))
    num2 = int(input("Enter value: "))
    num3 = int(input("Enter value: "))

    get_max = maxNumber(num1, num2, num3)

    print(f"{get_max} is the maximum among the three integers.")

    print("NUMBER 3")

    number = (int(input("Please input a number: ")))
    result = countNumber(number)

    print(f"Number of digits in the given number is: {result[0]}")
    print(f"Smallest Number is: {result[1]}")
    print(f"Largest Number is {result[2]}")

    print("NUMBER 4")

    given_number = int(input("Enter number: "))

    get_sum = totalSum(given_number)

    print(f"Total sum is = {get_sum}")


main()
