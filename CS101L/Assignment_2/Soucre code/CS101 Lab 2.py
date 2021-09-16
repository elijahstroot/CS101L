##CS 101 Lab
## Program 2
## Elijah Stroot
## ems3hb@umsystem.edu
## 9/15/21
## We need to calculate the total grade for someone based on weight
##Algorithm:
##  1. We are going to create variables that can be used to get the weighted grades
##  2. Create an if else statement for each of these variables so that they are between 0-100
##  3. Add up each of these grades for the total.
labs = 0
exams = 0
attendance = 0
print("**** Welcome to the LAB grades calculator! ****")
print()
name = input('Who are we calculating grades for? ==>')
labs = int(input('Enter the Labs grade? ==>'))
if 0 < labs <= 100:
    labs = labs
elif labs < 0:
    labs = 0
    print('The lab value should have been zero or greater. It has been changed to zero')
else:
    labs = 100
    print('The lab value should have been 100 or less. It has been changed to 100')
print()
exams = int(input('Enter the EXAMS grade? ==>'))
if 0 < exams <= 100:
    exams = exams
elif exams < 0:
    exams = 0
    print('The EXAMS grade value should have been zero or greater. It has been changed to zero.')
else:
    exams = 100
    print('The EXAMS grade value should have been 100 or less. It has been changed to 100')
print()
attendance = int(input('Enter the Attendance grade? ==>'))
if 0 < attendance <= 100:
    attendance = attendance
elif attendance < 0:
    attendance = 0
    print('The Attendance value should have been zero or greater. It has been changed to zero.')
else:
    attendance = 100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
total_grade = (labs * .7) + (exams * .2) + (attendance * .1)
print()
print('The weighted grade for', name, 'is', total_grade)
if total_grade >= 90:
    letter = 'A'
elif total_grade >= 80:
    letter = 'B'
elif total_grade >= 70:
    letter = 'C'
elif total_grade >= 60:
    letter = 'D'
else:
    letter = 'F'
print(name, 'has a letter grade of', letter)
print()
print('*** Thanks for using the Lab grade calculator ***')
    


    
    
