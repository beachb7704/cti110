def miles_to_laps(user_miles):
    laps = user_miles / .25
    return laps
    
  

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    user_miles = float(input())
    
    print('{:.2f}'.format(miles_to_laps(user_miles)))