'''
travel phase
'''

import random

def travel_phase(distance, distance_traveled, g_dist, g_traveled):
    '''
    moves ship and gives output to user
    '''

    g_traveled = random.randint(0,4)

    print("press ENTER to Begin the Travel Phase!")
    input()
    print("")
    print(f"You have traveled a distance of {distance_traveled} galactic standard units!")
    print('')
    print(f"The Garquackiens have traveled a distance of {g_traveled} galactic standard units!")

    distance -= distance_traveled
    g_dist -= g_traveled 

    return distance, g_dist
