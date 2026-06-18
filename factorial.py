num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "is", factorial)
number1 = int(input("Enter another number: "))
number2 = int(input("Enter another number: "))
result = number1 + number2
print("The sum of", number1, "and", number2, "is", result)