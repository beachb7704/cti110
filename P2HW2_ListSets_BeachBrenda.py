#CTI-110
#P2HW2 - List and Sets
#Brenda Beach
#10/01/2021
#
#Start

#input section

#Input number 1
num1 = float(input('Enter num 1:' ' '))
#Input number 2
num2 = float(input('Enter num 2:' ' '))
#Input number 3
num3 = float(input('Enter num 3:' ' '))
#Input number 4
num4 = float(input('Enter num 4:' ' '))
#Input number 5
num5 = float(input('Enter num 5:' ' '))
#Input number 6
num6 = float(input('Enter num 6:' ' '))

#processing section

#Create a blank list with name num_list
num_list = []
#Append the blank list with num1 variable
num_list.append(num1)
#Append the blank list with num2 variable
num_list.append(num2)
#Append the blank list with num3 variable
num_list.append(num3)
#Append the blank list with num4 variable
num_list.append(num4)
#Append the blank list with num5 variable
num_list.append(num5)
#Append the blank list with num6 variable
num_list.append(num6)
#Find the lowest number in the list
lowest = min(num_list)
#Find the largest number in the list
highest = max(num_list)
#Add all of the numbers in list together
total = sum(num_list)
#Find the average of all numbers in list
average = total / 6
#Turn list num_list into a set
num_set = set(num_list)

#Display section

#Print a blank line
print('')
#Print the created list of all 6 numbers
print('Created list \n', (num_list))
#Print the smallest number in the list
print('Smallest number in list:', lowest)
#print the largest number in the list
print('Largest number in list:', highest)
#Print the sum of all of the numbers
print('Sum of numbers in list:', total)
#Print the average of all the numbers
print('Average of numbers in list:', average) 
#print a blank line
print('')
#print the created set from the list
print('Created set\n', num_set)


#end

