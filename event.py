
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

    event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","magnetic_field","ambush","confined","deterioration","astroid_field","mixed","feast","recreation","overworked","relations","syphon","hording","stealing","taking_fire","decenters","boarded"]

    event = random.choice(event_list)

    print(f"{event}")

    if event == "gravitational_force":

        print("")

    elif event == "restock":

        print("")

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

    return fuel, food, power, hull, crew, burn_rate, morale, distance

event(fuel, food, power, hull, crew, burn_rate, morale, distance)