def convertCelsius(celsius):
    return (9 / 5 * celsius) + 32


def main():
    celsius = float(input("Enter celsius: "))
    fahrenheit = convertCelsius(celsius)

    print(f"The {celsius} celsius is equivalent to {fahrenheit:.2f} fahrenheit")


main()