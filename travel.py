'''
Handels Travel phase
'''

import random

def travel_phase(distance, distance_traveled, g_dist):
    '''
    move player and garquackiens closer to earth
    '''

    # display beginning of phase message
    print("press ENTER to Begin the Travel Phase!")
    input()
    print("")

    # display distance the player has traveled this turn
    print(f"You have traveled a distance of {distance_traveled}!")
    print('')

    # remove distance traveled from total distance
    distance -= distance_traveled

    # if the player has not won the game move the garquackien ship
    if distance > 0:

        # move garquackiens 1-4 distance
        g_traveled = random.randint(0,4)

        # print distance garquackiens moved this round
        print(f"The Garquackiens have traveled a distance of {g_traveled}!")
        print("")

        # remove the distance the garquackians traveled from thier total distance from Earth
        g_dist -= g_traveled

    return distance, g_dist
