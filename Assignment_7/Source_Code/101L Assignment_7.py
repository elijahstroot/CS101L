#Elijah Stroot
#CS101 Lab
#Assignment_7
#10/22/21
"""
Algorithm
1. We need to define a function to open a file that the user wants to open. 
2. The user will input a file name, and then it will be opened. 
3. If they input something other then the right file, it will print that there is no file with that name
4. If there is an input error, it will print that there is one. 
5. we need to define another function that will get the minimum miles per gallon. 
6. In this function we are going to ask the user what they want the minimum to be. 
7. If their input is less then 0, we will tell them it must be greater then 0. 
8. If their input is greater then 100, we will tell them it must be less then 100. 
9. And if their input is not a number, we will tell them that they must input a number. 
10. we will create basically the same function for a maximum mpg
11. We will now call the function that opens the file, and we will use user input to open the file they want. 
12. We will now ask the user what file they want to output to, and we will make output for that file. 
13. We need to iterate through the file they are trying to read to get the information we want. 
14.
"""




def open_file(prompt, mode="r"):
    while True:
        try:
            file_name = input(prompt)
            file = open(file_name, mode)
            return file
        except FileNotFoundError:
            print("could not open file", file_name)
        except IOError:
            print("There is an IO error", file_name)
def get_min_mpg():
    while True:
        try:
            mpg = float(input("Enter the minimum mpg "))
            if mpg <= 0:
                print("MPG given must be greater then 0")
            elif mpg > 100:
                print("MPG must be less then 100")
            else:
                return mpg
        except ValueError:
            print("You must enter a number for the miles per gallon")
def get_max_mpg():
    while True:
        try:
            mpg = float(input("Enter the maximimum miles per gallon"))
            if mpg <= 0:
                print("MPG must be greater then 50 ")
            elif mpg > 100:
                print("mpg must be less then 100")
            else:
                return mpg
        except ValueError:
                print("you must enter a number for the miles per gallon")
print()
file = open_file("Enter the name of file you want to open ")
file.readline()
print()
output_file = open_file("Enter the name of the file you want to output to ", "w")
for line in file:
    split_data = line.split(' ')
    for x in split_data:
        if get_min_mpg() < x < get_max_mpg():
            print(line)
            




    