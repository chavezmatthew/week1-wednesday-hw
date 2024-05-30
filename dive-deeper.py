# Task 1: Code Correction You are provided with a Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.



number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")



# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

num1 = float (input ("Enter the first number: "))
num2 = float (input ("Enter the second number: "))
num3 = float (input ("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

message = f"the largest number is {largest}"
print (message)