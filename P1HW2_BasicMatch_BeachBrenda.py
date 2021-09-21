#This project is to help someone try to figure their taxes on their expenses for a month as well as taxes and total bill for a year.
#Septemer 21, 2021
#CTI-110 P1HW2-Basic Math
#Brenda Beach
#
'''
m = get user input for bill name
n = get user input for bill amount
p = take user input for bill amount and multiply it by 6%
r = take user input for bill amount and add it to the tax amount
s = take the user input for the total amount of the bill and tax and multiply it by 12
print the name of the bill as well as the cost of the bill and use currency formatting to keep
      the decimal points only at 2 places, and remove the space after the $ symbol, and place
      , symbol to seperate the thousands.
print the monthly tax of the bill and use currency formatting to keep
      the decimal points only at 2 places, and remove the space after the $ symbol, and place
      , symbol to seperate the thousands.
print the total amount of the monthly bill added to the tax of the bill and use currency formatting to keep
      the decimal points only at 2 places, and remove the space after the $ symbol, and place
      , symbol to seperate the thousands.
print the total amount of the bill added to the tax and then multiplied by 12 to get the annual cost
      of the bill and use currency formatting to keep
      the decimal points only at 2 places, and remove the space after the $ symbol, and place
      , symbol to seperate the thousands.
'''


bill = input('Enter the name of your expense:')
cost = float(input('Enter amount of expense for the month:'))
month_tax = cost * 0.06
full_month = month_tax + cost
full_year = full_month * 12


print('Bill:', bill, '--------- Before Tax: ${:,.2f}'.format(cost))
print('Monthly Tax:       ${:,.2f}'.format(month_tax))
print('Monthly Charge:    ${:,.2f}'.format(full_month))
print('Annual Charge:     ${:,.2f}'.format(full_year))
