'''
travel phase
'''

def travel(distance, distance_traveled):
    '''
    moves ship and gives output to user
    '''

    distance -= distance_traveled

    print("Begin Travel Phase!")
    print("")
    print(f"You have traveled a distance of {distance_traveled} galactic standard units!")

    return distance
