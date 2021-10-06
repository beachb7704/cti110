highway_number = int(input())

if highway_number >= 1 and highway_number <= 99:
    if (highway_number % 2) == 0:
        print('I-' + str(highway_number), 'is primary, going east/west.')
    else:
        print('I-' + str(highway_number), 'is primary, going north/south.')

elif highway_number >= 100 and highway_number <= 999:
    if (highway_number % 100) == 0:
      print(str(highway_number), 'is not a valid interstate highway number.')
    elif (highway_number % 2) == 0:
        print('I-' + str(highway_number), 'is auxiliary, serving I-%d, going east/west.' % (highway_number % 100))
    else:
        print('I-' + str(highway_number), 'is auxiliary, serving I-%d, going north/south.' % (highway_number % 100))
else:
    print(highway_number, 'is not a valid interstate highway number.')