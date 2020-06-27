def loss(hull, crew, power, morale):
    '''
    check for loss conditions
    '''

    # if hull, crew, power, or morale is less than 1
    # display losing message and end game loop
    # if not continue game loop

    if hull < 1:
        print("You have lost due to running out of hull!")
        print('')
        running = False
    
    elif crew < 1:
        print("You have lost due to running out of crew!")
        print('')
        running = False
    
    elif power < 1:
        print("You have lost due to running out of power crystals!")
        print('')
        running = False
    
    elif morale < 1:
        print("You have lost due to running out of morale!")
        print('')
        running = False

    else:
        running = True

        return running

def win(distance, running):
    '''
    check for win conditions
    '''

    # if distance < 1
    if distance <= 0:
        print("You have won the game!!!")
        running = False
        return running

    else:
        running = True
        return running