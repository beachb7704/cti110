#CTI-110
#P4HW2-SalaryCal
#Brenda Beach
#October 16, 2021
#

    
#Enter the employees name or cancel out
employee = input("Enter employee's name or 'None' to terminate: ")

employee_num = 1
overtime_total = 0
reg_total = 0
gross_total = 0

#Begin the while loop that will ask for employee informaton
while employee != 'None':
            
    #Enter the name and hours the employee worked
    hours_worked = float(input("How many hours did {} work? ".format(employee)))

    #Enter what the employee makes per hour
    pay_rate = float(input("What is {} pay rate? ".format(employee)))

    #calculate overtime hours worked
    overtime = hours_worked - 40

    #calculate overtime pay
    overtime_pay = (overtime * pay_rate) + (overtime * pay_rate /2)

    #calculate regular hourly pay
    reg_pay = (hours_worked - overtime) * pay_rate

    #calculate gross pay
    gross_pay = reg_pay + overtime_pay


    #Create If statement to determine if employee had overtime hours or not.
    if hours_worked > 40:
        overtime
    else:
        overtime = 0
    
    #Create if statement to determine overtime pay if overtime was worked, and to add up overtime pay for everyone entered
    if overtime > 0:
        overtime_pay
        overtime_total += overtime_pay
        
    else:
        overtime_pay = 0
        overtime_total = overtime_total
    
    #Create an if statement to determine regular pay worked, and to add up regular pay for everyone entered
    if hours_worked > 40:
        reg_pay
        reg_total += reg_pay
    else:
        reg_pay = pay_rate * hours_worked
        reg_total += reg_pay

    #Create an if statement to determine gross pay, and to add up regular pay for everyone entered
    if hours_worked > 40:
        gross_pay
        gross_total += gross_pay
    else:
        gross_pay = hours_worked * pay_rate
        gross_total += gross_pay
        

    #Print a blank line between questions and output
    print()

    #Print out the name of the employee the user input
    print("Employee Name:  ", employee)

    #Show a blank line
    print(' ')
 
    #Print the line that specifies the colums of information
    print("Hours Worked", "  ", "Pay Rate", "  ", "OverTime", "  ", "OverTime Pay", "  ", "RegHour Pay", "   ", "Gross Pay")

    #draw a line between the column names and answers
    print("---------------------------------------------------------------------------------------")

    #print everything out that was input
    print ('{:<13.2f}'.format(hours_worked), '{:^8.2f}'.format(pay_rate), '{:^14.2f}'.format(overtime), '{:^10.2f}'.format(overtime_pay), '{:^21.2f}'.format(reg_pay), '{:^8.2f}'.format(gross_pay))
    
    print()

    #Enter the employees name orcancel out
    employee = input("Enter employee's name or 'None' to terminate: ")

    #Calculate the total of employees time entered.
    employee_num += 1
    

else:
    #Fix the addition for overtime, reg and gross total.
    print('Total number of employees entered:{}'.format(employee_num - 1))
    print('Total amount payed for overtime: ${:.2f}'.format(overtime_total))
    print('Total amount payed for regular hours: ${:.2f}'.format(reg_total))
    print('Total amount payed in gross: ${:.2f}'.format(gross_total))
