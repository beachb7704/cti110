#CTI-110
#P4HW1-Expenses
#Brenda Beach
#October 16, 2021
#

#Dollar amount of all expenses
expense_amount = int()

#Total of expenses entered
expense_total = int()

#Number to populate for the expense number entered
expense_num = 2

#Enter starting amount in account
start_amount = int(input("Enter starting amount in account $"))

#Print a blank line
print()

#Statement to have user input first expense
enter_exp = int(input("Enter expense 1:"))


#Set the first expense amount to the expense_amount variable
expense_amount += enter_exp

#Set the first expense to the expense_total variable
expense_total += enter_exp


#Ask if user wants to enter a new expense
new_expense = input("Do you want to enter another expense? (y/n)")

#Print a blank line
print()


#create a while loop to have the user input a new expense and add all of them up
#When the user presse N, it will print out the totals.
while new_expense == 'y':
    val = int(input("Enter expense {}:".format(expense_num)))
    expense_num += 1
    expense_total += val
    remain = start_amount - expense_total 
    new_expense = input("Do you want to enter another expense? (y/n)")
    print()
else:
    print("Amount in account before expenses subtracted ${:.1f}".format(start_amount))
    print("Number of expenses entered:", expense_num - 1)
    print("Amount in account After expenses subtracted is ${:.1f}".format(remain))











    
