'''
travel phase
'''

def travel_phase(distance, distance_traveled):
    '''
    moves ship and gives output to user
    '''

    distance -= distance_traveled

    print("press ENTER to Begin the Travel Phase!")
    input()
    print("")
    print(f"You have traveled a distance of {distance_traveled} galactic standard units!")

    return distance
