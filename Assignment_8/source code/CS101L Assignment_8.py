""""
#Elijah Stroot
#CS101Lab Assignment_8
#ems3hb@umsystem.edu
#due October 30, 2021

Problem:
We are creating a program to store, and calculate grades. Ultimately it will take grades from the user, store them, and print a final grade when the user wants it too. 

Algorithm:
1. We are going to create two empty lists, one for the tests and one for the assignments
2. Create a loop that continues to run until the user no longer wants it too. 
3. We are going to call a function called menu() that prints the menu every time the loop iterates. 
4. Once the user inputs their choice from the menu, we are going to do a number of things from that. 
5. If their choice is 1, we are going to add their input test score to the list of tests
6. If their choice is 2, we are going to remove their test score from the list of tests
7. If their choice is 3, we are going to clear the test scores from the list
8. If their choice is 4, we are going to add an assignment score to the list of assignments
9. If their choice is 5 we are going to remove an assignment score from the list of assignments. 
10. If their choice is D we are going to display the scores. 
11. If their choice is Q we are going to quit the loop
12. We will tell the user to have a nice day. 
"""
import math


tests = []
assignments = []


def adding_test(x, tests):
  tests.append(x)
  return tests

def adding_assignment(x, assignments):
  assignments.append(x)
  return assignments

def remove_test(x, tests):
  tests.remove(x)
  return tests
  
def remove_assignment(x, assignments):
  assignments.remove(x)
  return assignments

def clear_list(y):
  y.clear()
  return y

def menu():
  print("1 - Add Test")
  print("2 -Remove Test")
  print("3 -Clear Tests")
  print("4 -Add Assignment")
  print("5 -Remove Assignment")
  print("6 -Clear Assignments")
  print("D -Display Scores")
  print("Q -Quit")

def adding_test_input():
  print("Enter the new Test score 0-100 ==>")
  while True:
    try:
      x = float(input())
      while (x < 0) or (x > 100):
        print("You must input a valid test score")
        x = float(input())
      return x
    except:
      print("You need to input a floating point number for the grade")
      continue

def adding_assignment_input():
  print("Enter the new assignment score 0-100 ==>")
  while True:
    try:
      x = float(input())
      while (x < 0) or (x > 100):
        print("You must input a valid test score")
        x = float(input())
      return x
    except:
      print("You need to input a floating point number for the grade")
      continue

def remove_test_input():
  print("Enter the Test to remove 0-100 ==> ")
  while True:
    try:
      x = float(input())
      while (x < 0) or (x > 100):
        print("You must input a valid test score to remove")
        x = float(input())
      return x
    except:
      print("You must input a floating point number for the grade")
      continue

def remove_assignment_input():
  print("Enter the Assignment to remove 0-100 ==> ")
  while True:
    try:
      x = float(input())
      while (x < 0) or (x > 100):
        print("You must input a valid test score to remove")
        x = float(input())
      return x
    except:
      print("You must input a floating point number for the grade")
      continue

user_input = 'y'
while user_input != 'Q':
  menu()
  user_input = input("==> ")
  try:
    if user_input == '1':
      x = adding_test_input()
      adding_test(x, tests)
      print("You have just added a test score")
    elif user_input == '2':
      while True:
        try:
          x = remove_test_input()
          remove_test(x, tests)
          print("You have just removed a test score")
          break
        except:
          print("Could not find that test to remove")
          continue
    elif user_input == '3':
      print("Are you sure you want to clear the tests?")
      input_thought = input("Type yes or no ")
      if input_thought == 'yes':
        clear_list(tests)
        print("You have cleared the tests")
      else:
        print("You chose not to clear the tests")
    elif user_input == '4':
      x = adding_assignment_input()
      adding_assignment(x, assignments)
      print("You have just added an assignment")
    elif user_input == '5':
      try:
        y = remove_assignment_input()
        remove_assignment(y, assignments)
        print("You have removed", y, "from assignments")
      except:
        print("Could not find assignment to remove")
    elif user_input == '6':
      print("Are you sure you want to clear the assignments?")
      input_thought = input("Type yes or no ")
      if input_thought == 'yes':
        clear_list(assignments)
        print("You have cleared the assignments")
      else:
        print("You chose not to clear the assignments")
    elif user_input == 'D':
      average_test = (sum(tests))/(len(tests))
      average_assignment = (sum(assignments))/(len(assignments))
      weighted_score = (average_test * .6) + (average_assignment * .4)
      random_x = 0
      random_x2 = 0
      test_amount = len(tests)
      assignment_amount = len(assignments)
      for i in tests:
        random_y = i - average_test
        random_y_squared = (random_y)^2
        random_x = random_y_squared + random_x
      random_x_division = random_x / test_amount
      std_test = math.sqrt(random_x_division)
      for i in assignments:
        random_y = i - average_assignment
        random_y_squared = (random_y)^2
        random_x2 = random_y_squared + random_x2
      random_x2_division = random_x2 / assignment_amount
      std_assignment = math.sqrt(random_x2_division)
      print("{:10s} {:3} {:6} {:6} {:6} {:4}".format("Type", "#", "min", "max", "avg", "std"))
      print("{:10s} {:3} {:6} {:6} {:6} {:4}".format("Tests", test_amount, min(tests), max(tests), average_test, std_test)) 
      print("{:10s} {:3} {:6} {:6} {:6} {:4}".format("Assignments", assignment_amount, min(assignments), max(assignments), average_assignment, std_assignment))
    elif user_input == 'Q':
      print("Are you sure you want to stop?")
      new_user = input("Type yes or no")
      if new_user == 'yes':
        break
      else:
        new_user == 'no'
        print("You have chosen to continue to program")
        continue
    else:
      print("You must choose a valid option from the menu")
  except:
    print("You must input a valid option from the menu")

print("Have an amazing day!")
