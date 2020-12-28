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
    morale = 80
    distance = 25
    week = 10

    # begin game loop
    running = True
    while running:

        # introduction
        if week == 10:

            fuel, food, power, hull, crew, morale = i.intro(fuel, food, power, hull, crew, morale) 

        # Display Distance
        h.status(distance, week)

        # Phase 1: Production Phase
        fuel, food, power, hull, crew, morale = p.production_phase(fuel, food, power, hull, crew, morale)

        # Phase 2: Spend Phase
        fuel, food, power, hull, crew, morale, distance_traveled = s.spend_phase(fuel, food, power, hull, crew, morale)

        # Check for loss conditions
        if ed.lose(fuel, hull, crew, power, morale):
        
            break

        # Phase 3: Event Phase
        fuel, food, power, hull, crew, morale = e.event_phase(fuel, food, power, hull, crew, morale)

        # Check for loss conditions
        if ed.lose(fuel, hull, crew, power, morale):
            
            break

        # phase 4: Travel Phase
        distance = t.travel_phase(distance, distance_traveled)

        # Check for win conditions
        if ed.win(distance):

            break

        # Update week
        week -= 1

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
