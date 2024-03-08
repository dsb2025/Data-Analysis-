# File: MinMax.py
# Student: Danielle Balque
# UT EID: dsb2643
# Course Name: CS303E
# 
# Date: 9/23/22
# Description of Program: This program accepts number inputs and outputs the count of numbers entered and, the maximum and minimum of the entered numbers.
count = 0
val = input("Enter an integer or 'stop' to end: ")
if (val == 'stop'):
    print()
    print("You didn't enter any numbers")
    exit()
num = str(val)
max = num
min = num
while True:
    val = input("Enter an integer or 'stop' to end: ")
    numberRead = str(num)
    if count == 0 or max > numberRead:
            max = numberRead
    if count == 0 or min > numberRead:
            min = numberRead
    count += 1
    if (val == 'stop'):
        print()
        print( "You entered", count, "numbers" )
        print( "The maximum is", max )
        print( "The minimum is", min )
        break
    else:
        num = str(val)
        if num > max:
            max = num
        if num < min:
            min = num
