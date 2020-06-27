
def rules_text():
    '''
    Displays rules text
    '''
    print("These are the rules!")
    print('')
    print("Press 'enter' to continue.")
    print('')
    input()

def menu():

    print("Welcome to space commander.")
    print("press 'enter' to continue.")

    input()

    menu = True

    # begin loop for menu
    while menu == True:

        # display choices
        print("What would you like to do?")
        print('')
        print("a) See Rules. (suggested for first time players)")
        print("b) Play Game!!!")
        print("c) Exit Game")
        print("")

        # store user input
        selection = input()

        # if a show rules and continue loop
        if selection == 'a': 
            rules_text()
        
        # if 2 stop menu loop and begin game loop
        elif selection == 'b':
            running = True
            menu = False
            

        # if 3 turn off menu loop and game loop to get to exit
        elif selection == 'c':
            running = False
            menu = False

        # if other give invalad command prompt and continue loop
        else: 
            print("Command is invalid please enter a, b, or c.")
            print('')

    return running