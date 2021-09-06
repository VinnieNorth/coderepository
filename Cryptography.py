#Create a program that accepts two numbers from the keyboard.
#The user is then asked to input if they would like to add, subtract,
#divide or multiply the numbers. That sum is then done with the answer shown on the screen.

num1 = int(input("Please input your first number"))
num2 = int(input("Please input your second number"))
total=num1*num2
print(total)
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")


if choice == "1":
   print('Add')
   total=num1+num2
   print(total)

elif choice == "2":
   print(num1-num2)

elif choice == "3":
   print(num1*num2)

else:
   print(num1/num2)