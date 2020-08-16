
fuel = 30
food = 50
power = 10
hull = 5
crew = 10
burn_rate = 10
morale = 100
distance = 20
day = 10



def lose(hull, crew, power, morale):
    '''
    check for loss conditions
    '''

    # if hull, crew, power, or morale is less than 1
    # display losing message and end game loop
    # if not continue game loop

    lose = False

    if hull < 1:
        print("You have lost due to running out of hull!")
        print('')
        lose = True
    
    elif crew < 1:
        print("You have lost due to running out of crew!")
        print('')
        lose = True
    
    elif power < 1:
        print("You have lost due to running out of power crystals!")
        print('')
        lose = True
    
    elif morale < 1:
        print("You have lost due to running out of morale!")
        print('')
        lose = True

    return lose

def win(distance, running):
    '''
    check for win conditions
    '''

    win = False

    # if distance < 1
    if distance <= 0:
        print("You have won the game!!!")
        win = True 
        

    else:
        running = True
        return running