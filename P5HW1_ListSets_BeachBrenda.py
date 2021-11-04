#Create functions and loops to reduce the redundant code from previous assignment that will collect 10 numbersthen creates a list, then will convert to a set then displays that set.
#11/3/2021
#CTI-110 P5HW1 - Lists and Sets
#Brenda Beach
#
#Create a variable for the loop that will run to ask the user to input numbers.

#Create a variable for the while loop that will run to ask the user to input their numbers and will increase the number in the question each loop.
def gather_nums(num_list):
    number = 1
    while number < 11:
        digit = float(input("Enter your num {}:".format(number)))
        num_list.append(digit)
        number += 1
    menu()



#Create a function that will go through the list and get the lowest, largest, total, and average from the list.
def evaluate_nums(num_list):   
    #declaring variables for the total and length for the list
    total = 0
    length = 0
    #finding the smallest number
    smallest = min(num_list)
    #finding the biggest number
    largest = max(num_list)
    #finding the sum
    total = sum(num_list)
    #finding the length of the list
    length = len(num_list)
    #finding the average
    average = total / length
    return smallest, largest, total, average


#Create a function that will print out the list, and the lowest, largest, total and average from the list, convert the list to a set and then display the set.    
def final_print(smallest, largest, total, average):
    print('\nCreated List \n', (num_list))
    print('Smallest number in list:', smallest)
    print('Largest number in list:', largest)
    print('Sum of numbers in list:', total)
    print('Average of numbers in list:', average)
    print('Created Set\n', set(num_list))
    


#Create a function that will display the main menu when the program first starts up.
def menu():
    print('-----------MENU-----------')
    print()
    print("1) Create List")
    print("2) Display Results")
    print("3) Exit")
    print()
    print('-------------------------')
    choice = int(input("Enter your choice: "))
#Tell the program what to do when they press a selection
    if choice == 1:
        values = gather_nums(num_list)
                   
    elif choice == 2:
        if len(num_list) == 0:
            print("please try again.")
            menu()
        else:
            smallest, largest, total, average = evaluate_nums(num_list)
            evaluate_nums(num_list)
            final_print(smallest, largest, total, average)
            menu()

    elif choice == 3:
        quit

#This will tell the program to inform the user that they pressed the wrong button and to try again.
    else:
        print("please try again")
        menu()



#This starts the program, creates a blank list and brings up the menu.
    
if __name__ == "__main__":
    num_list = []
    menu()

