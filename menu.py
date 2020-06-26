
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
        print("1) See Rules. (suggested for first time players)")
        print("2) Play Game!!!")
        print("3) Exit Game")
        print("")

        # store user input
        selection = input()

        # if 1 show rules and continue loop
        if selection == '1': 
            f.rules_text()
        
        # if 3 skip to end
        elif selection == '3':
            menu = False
            running = False

        # if 2 stop menu loop and begin game loop
        elif selection == '2':
            menu = False
            running = Ture
        
        # if other give invalad command prompt and continue loop
        else: 
            print("Command is invalid please enter 1, 2, or 3.")
            print('')

    return running