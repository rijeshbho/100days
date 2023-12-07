# making calculator
# this function adds two numbers
def add(x, y):
    return x + y

# this function subtracts two numbers
def subtracts(x, y):
    return x - y

# this function multiplies two numbers
def multiply(x, y):
    return x * y

# this function divides two numbers
def divides(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# now it begins
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # input from user
    choice = input("Enter choice (1/2/3/4): ")

    # check whether the choice is valid or not
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtracts(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divides(num1, num2))
    else:
        print("Invalid input. Please enter a valid choice.")
