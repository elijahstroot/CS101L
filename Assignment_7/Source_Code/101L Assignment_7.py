def open_file(prompt, mode="r"):
    while True:
        try:
            file_name = input(prompt)
            file = open(file_name, mode)
            return file
        except FileNotFoundError:
            print("Could not open file", file_name)
        except IOError:
            print("There is an IO Error", file_name)
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
            print("You must enter a number for the fuel economy")
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
                print("you must enter a number for the fuel econ")
print()
file = open_file("Enter the name of the input vehicle file ==>")
file.readline()
print()
output_file = open_file("Enter the name of the file to output to ==>", "w")
for line in file:
    split_data = line.split(' ')
    for x in split_data:
        if get_min_mpg() < x < get_max_mpg():
            print(line)
            




    