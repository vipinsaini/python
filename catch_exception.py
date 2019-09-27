
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print("Invalid number!")
    print(err)
except ZeroDivisionError:
    print("Divided by zero!!")
