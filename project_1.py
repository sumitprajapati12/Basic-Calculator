# Calculator

print("Simple Calculator")

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

option = float(input("choose an operation: "))

if(option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(option == 1):
        print("Result =", num1 + num2)
    elif(option == 2):
        print("Result =", num1 - num2)
    elif(option == 3):
        print("Result =", num1 * num2)
    elif(option == 4):
        if(num2 == 0):
          print("Error: Cannot divide by zero")
        else:
            print("Result =", num1 / num2)

else:
    print("Invalid operation entered")




    