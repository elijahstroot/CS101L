'''
CS 101 Lab
Program 6. (Assignment_6)
Elijah Stroot
ems3hb@umsystem.edu

Problem:
We are defining functions and ultimately creating a program that can cipher an encoded text, or encode a text. 

Algorithm:
1. creating a loop that continues to run until the user quits
2. we are going to print a menu for them to view and then present three options for them to choose from
3. If their option is 1, then we will take a string and encode it
4. We will encode this within a created function by taking the string, making it into a list, going through the list using a loop, and changing the characters.  
5. Once the characters are changed, we will add this to a new list, and then change that list back into a string. 
6. If the user's option is 2, then we will take a string and decode it using the same process given above. 
7. If the user's option is 3 or Q, then we will ultimately stop the program and tell them to have a great day. 


'''

import string 
string.ascii_uppercase


def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    old_string = list(string_text)
    new_string = []
    for i in old_string:
        character = i.find(i) + int_key
        new_character = chr(character)
        new_string.append(new_character)
    string = ''.join(str(x) for x in new_string)
    return string

def Decrypt(string_text, int_key):
    ''' Decrypts Caesar-encrypted string with specified key. '''
    old_string = list(string_text)
    new_string = []
    for i in old_string:
        character = i.find(i) + int_key
        new_character = chr(character)
        new_string.append(new_character)
    string = ''.join(str(x) for x in new_string)
    return string



def Get_input():
    Again = True
    while Again:
        Print_menu()
        inp = input('Enter your selection ==> ').strip()
        if not inp in ('1', '2', '3', '4'):
            print('not a valid choice, please enter again.')
        else:
            Again = False
    return inp 

def Print_menu():
  '''Prints menu. No user interaction. '''
  print('Main Menu')
  print('1) Encode a String')
  print('2) Decode a String')
  print('Q) Quit')

'''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
  
def main(): 
  Again = True 
  while Again: 
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper()
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 


# our entire program: 
print('Welcome to the Caesar Cipher')
begin_playing = 'Y'
main()
