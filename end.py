'''
contains functions that check for willing and losing conditions
'''

def lose(fuel, food, power, hull, crew, morale, g_dist):
    '''
    check for loss conditions
    '''

    loss = False

    # if hull, crew, power, or morale is less than 1 display part one of losing message
    if fuel < 1:
        print("You have zero fuel")
        print("Your ship’s engines overheat and explode!")
        print('')

    if food < 1:
        print("You have insufficient food to feed your crew.")
        print("Rioting breaks out over what little food remains!")
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
       
    # if hull, crew, power, or morale is less than 1 display part two of losing message
    # and set loss to True
    if (fuel < 1) or (food < 1) or (hull < 1) or (crew < 1) or (power < 1) or (morale < 1):

        print("You are unable to continue your mission and Earth will surely be destroyed!")
        print("You have lost the game.")
        print('')

        loss = True

    # if garquackiens reach Earth first (g_dist is less than 0) display losing message
    # and set loss to True
    if g_dist < 1:

        print("The Garquackian Armada arrived before you could give warning and Earth")
        print("will surely be destroyed. You have lost the game.")
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
        print("You arrive at Earth in time to warn Earth Force about the impending attack.")
        print("Thanks to your efforts Earth Force will be prepared to defend against the Garquackien attack.")
        print('')
        print("You have won the game.")
        print('')
        won = True

    return won