import functions as f




''' Space Commander '''



fuel = 30
food = 50
power = 5
hull = 5
crew = 5
morale = 100
distance = 20
# def hud(fuel,food,power,hull,crew,morale):
    

# Display Title
print("Welcome to space commander.")
print("press 'enter' to continue.")

input()


# Main Menu
# options are Play, Rules, Quit
# Rules: display rules Text
# Quit: Exit game
# Play: Begin Game

menu = True

# begin loop for menu
while menu == True:

    # display choices
    print("What would you like to do?")
    print('')
    print("1) See Rules. (suggested for first time players)")
    print("2) Play Game!!!")
    print("3) Exit Game")

    # store user input
    selection = input()

    # if 1 show rules and continue loop
    if selection == '1': 
        f.rules_text()
    
    # if 3 skip to end
    elif selection == '3':
        running = False
        menu = False

    # if 2 stop menu loop and begin game loop
    elif selection == '2':
        running = True
        menu = False
    
    # if other give invalad command prompt and continue loop
    else: 
        print("Command is invalid please enter 1, 2, or 3.")

day = 1
# begin game loop
while running == True:

    if day == 1:
        print("opening")

    # setup
    # repeating tasks
    # ending

    f.hud(fuel, food, power, hull, crew, morale, distance)

    input()

    running = False

print("you have exited the game. Thanks for playing!")


