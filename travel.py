'''
travel phase 
'''

def travel(distance, distance_traveled):
    '''
    moves ship and gives output to user
    '''

    print("Begin Travel Phase!")
    print("")
    print(f"You have traveled a distance of {distance_traveled} galactic standard units!")

    distance -= distance_traveled

    return distance



