
print(2**3)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


base = int(input("Enter the base number:"))
power = int(input("Enter the power number:"))

print(raise_to_power(base, power))
