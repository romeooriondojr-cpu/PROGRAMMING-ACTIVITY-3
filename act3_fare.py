base_fare = float(input("Enter base fare: "))
distance = float(input("Enter distance (km): "))
total = base_fare + distance * 12.5

is_discounted = input("Senior Citizen or PWD? (y/n)") == "y"

if is_discounted:
    total *= 0.80
    print("Total fare is ", total)
else:
    print("Total Fare is: ", total)