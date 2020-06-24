import random

# values imported to function
fuel = 30
food = 50
power = 5
hull = 5
crew = 10
morale = 100
distance = 20
day = 1

def event(fuel, food, power, hull, crew, morale, distance):

    event_list = ["one","two","three","four","five"]

    event = random.choice(event_list)

    print(f"{event}")

    if event == "one":

        print("This is event one")

    elif event == "two":

        print("This is event two")

    elif event == "three":

        print("This is event three")

    elif event == "four":
        
        print("This is event four")

    elif event == "five":

        print("This is event five")

    return fuel, food, power, hull, crew, morale, distance


for r in range(9):

    event(fuel, food, power, hull, crew, morale, distance)