##Elijah Stroot
#CS101 lab
#Assignment_10
#11/13/21
'''
Algorithm:
1. Ask user to input a file name to read
2. We need to output the ten words used most (Exclude words that are three characters or less)
3. Output the number words that appear only once
4. Output how many unique words there are. 
'''
from collections import Counter

def open_file(prompt, mode="r"):
  while True:
    try:
      filename = input(prompt)
      file = open(filename, mode)
      return file
    except FileNotFoundError:
      print("Could not open", filename)
      print("please try again")
    except IOError:
      print("There is an IO Error", filename)
      print("please try again")
    except:
      print("Could not open the file {}, please try again".format(filename))

def words_dict(x):
  file = x.read()
  my_file = file.split()
  try:
    for i in my_file:
      if ',' in i:
        i.remove(',')
      if '.' in i:
        i.remove('.')
  except:
    print("Could not remove punctuation")
  collection = list(my_file)
  collection_dict = {}
  for i in my_file:
    z = my_file.count(i)
    collection.append(i)
    collection_dict[z] = i
  return collection_dict

def highest_values(z_dict):
  c = Counter(z_dict)
  highest = c.most_common(10)
  for i in highest:
    return (i[0], " :", i[1], " ")

def more_occurence(z_dict):
  x = []
  for k,v in z_dict():
    if (k == 1) and (len(v) > 3):
      x.append(v)
  return len(x)

def unique_words(z_dict):
  x = []
  for k,v in z_dict():
    if len(v) > 3:
      x.append(v)
  return len(x)


#main

print("Enter the name of the file to open:")
x = open_file("file name ==> ")
my_dict = words_dict(x)
try:
  highest = highest_values(my_dict)
  print("{:7} {:7} {:10}".format("frequency", "Word"))
  print("="*10)
  for k,v in highest:
    print("{:7} {:7} {:10}".format(k, v))
except:
  print("There was an error trying to print chart with the greatest words")

print("There are", more_occurence(my_dict), "that occur only once.")
print("There are", unique_words(my_dict), "unique words in the document")



