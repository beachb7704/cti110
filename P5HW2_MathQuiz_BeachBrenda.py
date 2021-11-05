#Create a program that will give random numbers in a math problem with the
#operator chosen by the user. If the user gets it wrong, allow them another
#chance, and when they get it right, bring up the menu again until they
#decide to exit out of the program.
#11/3/2021
#CTI-110 P5HW2 - Math Quiz
#Brenda Beach
#

#Must import the random module in order to have Python print random numbers
import random



#Create an addition function that will print 2 random numbers to be added
#together. randint(1, 99) is the number sequence I want my random numbers
#to populate with. If the number is above or below double digits, create an
#if statement to populate the appropriate amount of spaces to have the numbers
#line up appropriately. Also kep track of how many guesses the user makes. 
def math_add():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = '{} + {}'.format(number1, number2)
    if int(number1) < 10:
        print("  ", number1)
    else:
        print(" ", number1)
    if int(number2) < 10:
        print('+','', number2)
    else:
        print('+', number2)
    answer = int(input("Enter answer.\n"))
    guesses = 1
    
#Create a while loop that will look at the variable, and it will compare it to
#the actual answer, and make the appropriate selection. If it's not correct, it
#will look as the input, and determine if it is too high or too low, let the
#user know and then ask them to retype their answer. If it is correct, let the
#user know and go back to the main menu.
    while answer != number1 + number2:
        if answer > number1 + number2:
            guesses += 1
            print('Sorry guess is too high.')
            answer = int(input("try again:"))
        else:
            guesses += 1
            print('Sorry, guess is too low.')
            answer = int(input("try again:"))
        
    else:
        print("Congradulations!!! Your answer is correct...")
        print("Number of guesses: {}".format(guesses))
        menu()






        
    
#Create subract function. It works the same way as the addition function, but
#to keep the answer from always populating a negative number, set the end point
# for number 2 to not go above variable number 1.
def math_subtract():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, number1)
    question = '{} - {}'.format(number1, number2)
    if int(number1) < 10:
        print("  ", number1)
    else:
        print(" ", number1)
    if int(number2) < 10:
        print('-','', number2)
    else:
        print('-', number2)
    answer = int(input("Enter answer.\n"))
    guesses = 1
    

    while answer != number1 - number2:
        if answer > number1 - number2:
            guesses += 1
            print('Sorry, guess is too high.')
            answer = int(input("try again:"))
        else:
            guesses += 1
            print('Sorry, guess is too low.')
            answer = int(input("try again:"))
        
    else:
        print("Congradulations!!! Your answer is correct...")
        print("Number of guesses: {}".format(guesses))
        menu()  

            
            
        
#Create a function that will display the main menu when the program first starts up.
def menu():
    print('Welcome to Math Quiz')
    print()
    print()
    print('MAIN MENU')
    print('--------------------------')
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("Exit")
    print()
    choice = int(input("Please Choose one of the menu options: "))
#Tell the program what to do when they press a selection
    if choice == 1:
        values = math_add()
                   
    elif choice == 2:
        values = math_subtract()

    elif choice == 3:
        print('Thank youfor playing...')
        print('Bye!!')
        quit
#This will tell the program to inform the user that they pressed the wrong button and to try again.
    else:
        print("please try again")
        menu()




menu()
