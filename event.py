
# Beginning Values
fuel = 30
food = 50
power = 5
hull = 5
crew = 10
burn_rate = 10
morale = 70
distance = 20
day = 1

import random

def event(fuel, food, power, hull, crew, burn_rate, morale, distance):
    '''
    generate a random event for each day
    '''
    # set resolving event to true
    resolving_event = True

    # creare lost variables
    lost_fuel = 0
    lost_food = 0
    lost_power = 0
    lost_hull = 0
    lost_crew = 0
    lost_morale = 0

    # get rndome event
    event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","magnetic_field","ambush","confined","deterioration","astroid_field","mixed","feast","recreation","overworked","relations","syphon","hording","stealing","taking_fire","decenters","boarded"]

    event = random.choice(event_list)

    # print event name
    print(f"{event}")

    # carryout chosen event (display text, give choice if applocable, modify lost variables, display result text)
    if event == "gravitational_force":

        print("Your ship passes by a large star and is nearly caught in its gravity well. ")
        print("Through clever piloting you manage to escape the star’s pull,")
        print("but not without burning through some of your fuel reserves.")
        print("")

        lost_fuel += r.randint(1,10)

        print(f"You have lost {lost_fuel} units of fuel.")
        print("")

    elif event == "restock":

        print("You discover that your food reserves have been stocked to regulation.")
        print("There is a habitable planet not too far from you,")
        print("that you could use to replenish the missing supply.")
        print("However, that would mean spending fuel on the supply run.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Restock supplies and loose 1-10 fuel.")
            print("b) conserve fuel and lose 1-20 food.")
            choice = input()
            print("")

            if choice == "a":

                fuel_loss += r.randint(1,10)
                print(f"You have lost {fuel_loss} units of fuel.")
                print("")
                break

            elif choice == "b":

                food_loss += randint(1,20)
                print(f"You have lost {food_lost} units of food.")
                print("")
                break

            else:

                print("Please enter a of b.")
                print("")
                continue

    elif event == "contamination":
        
        print("")

    elif event == "navigational_malfunction":

        print("")

    elif event == "lifeform":

        print("")

    elif event == "magnetic_field":

        print("")

    elif event == "ambush":

        print("")

    elif event == "confined":

        print("")

    elif event == "deterioration":

        print("")

    elif event == "asteroid_field":

        print("")

    elif event == "mixed":

        print("")

    elif event == "feast":

        print("")

    elif event == "recreation":

        print("")

    elif event == "overworked":

        print("")

    elif event == "relations":

        print("")

    elif event == "syphon":

        print("")

    elif event == "hording":

        print("")

    elif event == "stealing":

        print("")

    elif event == "taking_fire":

        print("")

    elif event == "decenters":

        print("")

    elif event == "boarded":

        print("")

    fuel -= lost_fuel
    food -= lost_food
    power -= lost_power
    hull -= lost_power
    crew -= lost_crew
    morale -= lost_morale  

    return fuel, food, power, hull, crew, burn_rate, morale, distance

event(fuel, food, power, hull, crew, burn_rate, morale, distance)