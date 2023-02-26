def decimal_to_binary(decimal):
    binary = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[len(binary)-1-i]) * 2**i
    return decimal


def converter(decimal):
    binary = decimal_to_binary(decimal)
    decimal_from_binary = binary_to_decimal(binary)
    return f'{decimal} в двоичной системе: {binary}, {binary} в десятичной системе: {decimal_from_binary}'

print(converter(1200))