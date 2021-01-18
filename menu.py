'''
Handels the Main menu
'''

def start():
    '''
    Display opening menu and propt user to begin game or exit program
    '''

    # display opening menue
    print("")
    print("Welcome to space commander.")
    print("Press ENTER to continue.")
    input()

    # begin loop for menu
    starting = True
    while starting:

        # display choices
        print("What would you like to do?")
        print('')

        print("a) Play Game")
        print("b) Exit Game")
        print("")

        # store user input
        selection = input()

        # if a show rules and continue loop
        if selection == 'a':
            running = True
            break
        
        # if 2 stop menu loop and begin game loop
        elif selection == 'b':
            running = False
            break

        # if other give invalad command prompt and continue loop
        else: 
            print("Command is invalid please enter a or b.")
            print('')

    return running