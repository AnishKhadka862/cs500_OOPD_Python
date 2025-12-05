# Anish Khadka
# 164017
# Lab 03 Question 01
def decimal_to_hex(num):
    hex_chars = "0123456789ABCDEF"
    result = ""

    if num == 0:
        return "0"

    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num //= 16

    return result


def main():
    dec = int(input("Enter a decimal value: "))
    print("The hex value is", decimal_to_hex(dec))


main()