# BASIC PROGRAMS
#1 Write a python program that prints "Hello, World!" to the console
print("Hello, World!")
#2 to find largest of the three numbers\
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
print("the largest number is:",largest)
#3 accept two numbers from user and print their sum
a = int(input("enter the first number"))
b = int(input("enter the second number"))
sum = a + b
print(sum)
#4 program to determine if the number is even or odd
num = int(input("enter the number"))
if num % 2 == 0:
    print(num,"is an even number.")
else:
    print(num,"ia an odd number.")
#6 python code to check given number is positive,negative or zero
num = int(input("enter the number"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
#7 program to print sum of all the digits of given num
num = input("enter the number:")
sum = 0
for char in num:
    if char.isdigit():
        sum += int(char)
print(f"the sum of the digit is:{sum}")
#8 find the factorial of given number
num = int(input("enter the number:"))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("the factorial is:",factorial)
#11 accept 5 numbers from user and display their cube values
input = input("enter any 5 numbers seperated by spaces:")
numbers = input.split()
for num in numbers:
    number = int(num)
    cube = number ** 3
    print(f"the cube of {number} is {cube}")
#12 program to reverse a given number
num = input("enter the number:")
reversed_num = num[::-1]
print("the reversed number is:",reversed_num)
