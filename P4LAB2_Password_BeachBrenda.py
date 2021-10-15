word = input()
password = ''

for character in word:
    if character == 'i':
        password += '1'
    elif character == 'a':
        password += '@'
    elif 'm' == character:
        password += 'M'
    elif 'B' == character:
        password += '8'
    elif 's' == character:
        password += '$'
    else:
        password += character
print('{}!'.format(password))