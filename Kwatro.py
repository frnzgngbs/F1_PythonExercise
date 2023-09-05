def totalSum(number):
    get_sum = 0

    for i in range(1, number + 1):
        get_sum = get_sum + i

    return get_sum


def main():
    print("NUMBER 4")

    given_number = int(input("Enter number: "))

    get_sum = totalSum(given_number)

    print(f"Total sum is = {get_sum}")


main()
