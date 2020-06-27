import random

def event(fuel, food, power, hull, crew, burn_rate, morale, distance):
    '''
    generate a random event for each day
    '''

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

    return fuel, food, power, hull, crew, burn_rate, morale, distance
