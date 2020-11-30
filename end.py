
def lose(fuel,hull, crew, power, morale, distance_traveled):
    '''
    check for loss conditions
    '''

    # if hull, crew, power, or morale is less than 1
    # display losing message and return True
    # if not return false

    loss = False

    if fuel < 1:
        print("You have zero fuel")
        print("Your ship’s engines overheat and explode!")
        print('')

    if hull < 1:
        print("You have 0 hull.")
        print("Your ship has been destroyed!")
        print('')
    
    if crew < 1:
        print("You have 0 remaining crew.")
        print("All of your crew has died!")
        print('')
    
    if power < 1:
        print("You have 0 power crystals.")
        print("Your ship has lost power, including life support!")
        print('')
    
    if morale < 1:
        print("You have 0 morale.")
        print("Your crew has mutinied and taken over the ship!")
        print('')
       
    if (fuel < 1) or (hull < 1) or (crew < 1) or (power < 1) or (morale < 1):

        print("You are unable to continue your mission and Earth will surely be destroyed!")
        print("You have lost the game.")
        print('')

        loss = True

    return loss

def win(distance):
    '''
    check for win conditions
    '''

    won = False

    # if distance < 1 display winning message and return True
    # if not return False
    if distance <= 0:
        print("You arrive at Earth in time to warn Earth Force about the impending attack. Thanks to your ")
        print("efforts Earth Force will be prepared to defend against the Garquackien attack.")
        won = True

    return won