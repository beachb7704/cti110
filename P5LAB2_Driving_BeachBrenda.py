def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    number_of_gallons = driven_miles / miles_per_gallon;
    total_cost = number_of_gallons * dollars_per_gallon;
    return total_cost;

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print('{:.2f}'.format(driving_cost(10, miles_per_gallon, dollars_per_gallon)))
    print('{:.2f}'.format(driving_cost(50, miles_per_gallon, dollars_per_gallon)))
    print('{:.2f}'.format(driving_cost(400, miles_per_gallon, dollars_per_gallon)))

