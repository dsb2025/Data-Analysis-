# File: DecisionTree.py
# Student: Danielle Balque
# UT EID: dsb2643
# Course Name: CS303E
# 
# Date: 9/18/22
# Description of Program: This program implements a decision tree to determine whether a specific individual buys a computer.
print()
age = int( input("Please enter person's age: ") )
income = input("Person's income (High, Medium, Low): ")
student = input("Is this person a student (Yes or No)? ")
credit = input("Does this person have good credit (Yes or No)? ")
print()
if income == "Low" and ( age >= 31 ) and ( age <= 40 ) and student == "Yes" and credit == "Yes":
  print("This person will purchase a computer.")
  print()
elif income == "Medium" and ( age >= 31 ) and ( age <= 40 ) and student == "No" and credit == "Yes":
  print("This person will purchase a computer.")
  print()
elif income == "Medium" and ( age <= 30 ) and student == "Yes" and credit == "Yes":
  print("This person will purchase a computer.")
  print()
elif income == "Medium" and ( age <= 30 ) and student == "No" and credit == "No":
  print("This person will not purchase a computer.")
  print()
elif income == "Medium" and "( age > 40 )" and student == "No" and credit == "Yes":
  print("This person will not purchase a computer.")
  print()
elif income == "Low" and "( age > 40 )" and student == "Yes" and credit == "Yes":
  print("This person will not purchase a computer.")
  print()
elif income == "High" and ( age <= 30 ) and student == "No" and credit == "No" or credit == "Yes":
  print("This person will not purchase a computer.")
  print()
elif income == "Low" and ( age <= 30 ) and student == "Yes" and credit == "No":
  print("This person will purchase a computer.")
  print()
elif income == "Medium" and ( age > 40 ) and student == "Yes" and credit == "No":
  print("This person will purchase a computer.")
  print()
elif income == "Medium" or income == "High" and ( age >= 31 ) and ( age <= 40 ) and student == "Yes" or student == "No" and credit == "Yes" or credit == "No":
  print("This person will purchase a computer.")
  print()


