''' Space Commander '''

# imports
import menu as m
import intro as i
import hud as h
import production as p
import spend as s
import event as e
import travel as t
import end as ed
import random

def play_again():

    try_again = True
    while try_again:
    
        print("Would you like to play again? y/n")
        print("")
        again = input()

        if again == "y":

            return True

        elif again == "n":

            return False

        else:

            print("invalid input. Please enter y or n.")
            print('')

def game_loop():

    # Beginning Values
    fuel = 30
    food = 40
    power = 10
    hull = 6
    crew = 10
    morale = 60
    distance = 25
    g_dist = 25

    # begin game loop
    running = True
    while running:

        # introduction
        if g_dist == 25:

            fuel, food, power, hull, crew, morale = i.intro(fuel, food, power, hull, crew, morale) 

        # Display Distance
        h.status(distance, g_dist)

        # Phase 1: Production Phase
        fuel, food, power, hull, crew, morale = p.production_phase(fuel, food, power, hull, crew, morale)

        # Phase 2: Spend Phase
        fuel, food, power, hull, crew, morale, distance_traveled = s.spend_phase(fuel, food, power, hull, crew, morale, g_dist, distance)

        # Check for loss conditions
        if ed.lose(fuel, food, power, hull, crew, morale):
        
            break

        # Phase 3: Event Phase
        fuel, food, power, hull, crew, morale = e.event_phase(fuel, food, power, hull, crew, morale)

        # Check for loss conditions
        if ed.lose(fuel, food, power, hull, crew, morale):
            
            break

        # phase 4: Travel Phase

        distance, g_dist = t.travel_phase(distance, distance_traveled)

        h.status(distance, g_dist)

        # Check for win conditions
        if ed.win(distance):

            break

        

# Display menu, run game loop, ask player if they want to play again
if m.start():

    # begin play again loop
    playing = True
    while playing == True:
    
        game_loop()

        # Prompt user for play again if true continue loop if false break loop
        if play_again() == True:

            pass
        
        else:

            break

# Print exit message
print("You have exited the game. Thank you for playing!")
