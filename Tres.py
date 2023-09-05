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


def main():
    number = (int(input("Please input a number: ")))
    result = countNumber(number)

    print(f"Number of digits in the given number is: {result[0]}")
    print(f"Smallest Number is: {result[1]}")
    print(f"Largest Number is {result[2]}")


main()
