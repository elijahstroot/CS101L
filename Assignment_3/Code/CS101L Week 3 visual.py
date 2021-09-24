#Python
#CS 101 Lab
## Program 3 / Assignment 3
## Elijah Stroot
## ems3hb@umsystem.edu
##
##Problem: We are trying to determine what the original number of the user was, based on remainders that they give from dividing the number.
## Algorithm: 
# 1. We need to establish variables for the remainders and the user input. 
# 2. We need to make a loop that continues to run until the user does not want to play anymore. 
# 3. We need to create conditions that say the remainders must be within a certain range. 
# 4. As long as those conditions are met, then the remainders will be used to determine "i", which will be the original number.
# 5. Tell them the original number that they had in their head.  
# 6. We need to create another condition that if the original number is not between 0 - 100, then they need to try a different number. 
# 7. Ask if the user wants to play again. 
# 8. If not, then have a parting phrase. 

print('Welcome to the Flarsheim Guesser!')
print()
print('Please think of a number between and including 1 and 100.')
print()
remainder3 = 0
remainder5 = 0
remainder7 = 0
user_input = input()
counter = 0 
original_number = 0
while user_input != ('N'):
    if user_input == ('Y'):

        print('What is the remainder when your number is divided by 3 ?')
        remainder_input = int(input())
        while (remainder_input > 3) or (remainder_input < 0):
            if remainder_input > 3:
                    print('The value entered must be less than 3')
                    remainder_input = int(input())
            elif remainder_input < 0:
                    print('the value entered must be 0 or greater')
                    remainder_input = int(input())
            else:
                    remainder_input = remainder_input
        remainder_input2 = int(input('What is the remainder when your number is divided by 5 ?'))
        while (remainder_input2 >5) or (remainder_input2 < 0):
            if remainder_input2 > 5:
                print('The value you entered must be less than 5')
                remainder_input2 = int(input())
            elif remainder_input2 < 0:
                print('The remainder entered must be 0 or greater')
                remainder_input2 = int(input())
            else:
                remainder_input2 = remainder_input2
        remainder_input3 = int(input('What is the remainder when your number is divided by 7 ?'))
        while (remainder_input3 > 7) or (remainder_input3 < 0):
            if remainder_input3 > 7:
                print('The remainder you entered must be less then 7')
                remainder_input = int(input())
            elif remainder_input3 < 0:
                print('The remainder you entered must be greater then 0')
                remainder_input3 = int(input())
            else:
                remainder_input3 = remainder_input3
        for i in range(1, 101):
            if (i % 3 == remainder_input) and (i%5 == remainder_input2) and (i%7 == remainder_input3):
                print("Your number was {} \nHow amazing was that?".format(i))
        else: 
            print('Please think of a number between 1 and 100.') 
    print('Do you want to play again? Y to continue, N to quit  ==>')
        #else:
    user_input = input()
print('Have a great day!')
