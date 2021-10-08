#CTI-110
#P3HW2-Salary
#Brenda Beach
#October 7, 2021
#

#Enter the employees name
employee = input("Enter employee's name:")

#Enter the hours the employee worked
hours_worked = float(input("Enter number of hours worked:"))

#Enter what the employee makes per hour
pay_rate = float(input("Enter employee's pay rate:"))

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
    
#Create if statement to determine overtime pay if overtime was worked.
if overtime > 0:
    overtime_pay       
else:
    overtime_pay = 0
    
#Create an if statement to determine regular pay worked.
if hours_worked > 40:
    reg_pay
else:
    reg_pay = pay_rate * hours_worked

#Create an if statement to determine gross pay.
if hours_worked > 40:
    gross_pay
else:
    gross_pay = hours_worked * pay_rate
    

    

#draw a line between the questions and the output
print("-----------------------------------------")

#Print out the name of the employee the user input
print("Employee Name:  ", employee)

#Show a blank line
print(' ')
 
#Print the line that specifies the colums of information
print("Hours Worked", "  ", "Pay Rate", "  ", "OverTime", "  ", "OverTime Pay", "  ", "RegHour Pay", "   ", "Gross Pay")

#draw a line between the column names and answers
print("---------------------------------------------------------------------------------------")

print ('{:<13.1f}'.format(hours_worked), '{:^8.1f}'.format(pay_rate), '{:^14.1f}'.format(overtime), '{:^10.1f}'.format(overtime_pay), '{:^21.1f}'.format(reg_pay), '{:^8.1f}'.format(gross_pay))
