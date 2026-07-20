a = int(input("A: "))
b = int(input("B: "))

operation = input("Enter operation (add/sub/mul/div): ")

if operation == "add":
    print("A + B =", a + b)

elif operation == "sub":
    print("A - B =", a - b)

elif operation == "mul":
    print("A * B =", a * b)

elif operation == "div":
    if b != 0:
        print("A / B =", a / b)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operation")