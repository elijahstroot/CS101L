#Elijah Stroot
#CS101L
#Assignment 9
#11/6/21
'''
Algorithm:
1. We are going to define all of our functions to create dictionaries and lists from the CSV file that is given
2. the user is going to input a file name to input, and if it isn't there we are going to print an error. 
3. Once they input the file, we are going to print different things using the defined functions. 
4. We are goint to show the top offenses and the month with the most offenses. 
5. The user gets to pick a given offense and see how many times it has been committed and where it has been committed and when. 

'''

import csv
def month_from_number(x):
    try:
        month = {
            1: "January",
            2: "Febuary",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        month_string = month[x]
        return month_string
    except:
        print("There must be a number for the month")
def read_in_file(myfile: str) -> list:
    file = open(myfile, encoding='utf-8')
    new_file = csv.reader(file)
    lst = list(new_file)
    file.close()
    return lst
def create_reported_date_dict(file_lst: list) -> dict:
  endgame = {}
  for line in file_lst[1:]:
    date = line[1].stript()
    endgame[date] = endgame.get(date, 0) + 1
  return endgame
def create_reported_month_dict(file_lst: list) -> dict:
  endgame = {}
  for line in file_lst[1:]:
    month = int(line[1].split("/")[0].strip())
    endgame[month] = endgame.get(month, 0) + 1
  return  endgame
def create_offense_dict(file_lst: list) -> dict:
  endgame = {}
  for line in file_lst[7:]:
    offense = (line[7].split("/")[0].strip())
    endgame[offense] = endgame.get(offense, 0) + 1
  return endgame 
def create_offense_by_zip(file_lst: list) -> dict:
  endgame = {}
  for line in file_lst[7:]:
    offense = (line[7].split("/")[0].strip())
    endgame[offense] = endgame.get(offense, 0) + 1
  return endgame 
def get_top_ten_key_values(x):
  x = 'none'
  return x
if __name__ == "__main__":
  invalid_file = True
  while invalid_file:
    try:
      file_name = input("Enter the name of the crime data file ==> ")
      lst = read_in_file(file_name)
      invalid_file = False
    except FileNotFoundError:
      print("Could not find the file specified. {} not found".format(file_name))
  print()
  month_number = create_reported_month_dict(lst)
  top_10_month_number = get_top_ten_key_values(month_number)
  print("The month with the highest # of crimes is {} with {} offenses".format(month_from_number(top_10_month_number[0][0]), top_10_month_number[0][1]))
  offenses = create_offense_dict(lst)
  top_10_offenses = get_top_ten_key_values(offenses)
  print("The offense with the higest # of crimes is {} with {} offenses".format(top_ten_offenses[0][0], top_10_offenses[0][1]))
  offense_by_zip = create_offense_by_zip(lst)
  print()
  invalid_key = True
  while invalid_key:
    offense_key = input("Enter an offense")
    if offense_key in offense_by_zip:
      invalid_key = False
    else:
      print("Not a valid offense found, please try again")
  print()
  print("{} offenses by Zip Code".format(offense_key))
  print("{:20}{:10}".format("Zip Code", "# Offenses"))
  print("=" * 30)
  for key, value in offense_by_zip[offense_key].items():
    print("{:<20}{:>10}".format(key, value))

  
    
