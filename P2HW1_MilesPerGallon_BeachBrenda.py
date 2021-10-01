#Program to determine what the miles per gallon of gasoline will be.
#10/01/2021
#CTI-110 P2HW1 - Miles Per Gallon
#Brenda Beach
#
#Start

#input section

#input amount of miles driven
miles = int(input('Enter miles driven:' ' ')) #int converts string to integer
#input amount of gallons of gas used
gas = int(input('Enter gallons used:' ' ')) #int converts string to integer
#input cost of gas per gallon
cost = float(input('Enter cost per gallon:' ' ')) #float converts string to a decimal number

#processing section
gallons_used = miles / gas
cost_gas = cost * gas
average = gallons_used / cost_gas

#Display section
#Put a space between the input and print section
print()
#Print miles driven per gallon of gas
print('Miles Per Gallon:   ${:.2f}'.format(gallons_used))
#print total cost of gas
print('Total Gas Cost:     ${:.2f}'.format(cost_gas))
#print the cost of gas per mile.
print('Cost Per Mile:      ${:.1f}'.format(average))

#end




