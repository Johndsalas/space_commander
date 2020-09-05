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

    play_again = True
    while play_again:
    
        print("Would you like to play again? y/n")
        print("")
        again = input()

        if again == "y":

            return True

        elif again == "n":

            return False

        else:

            print("invalid input. Please enter y or n.")

def game_loop():

    # Beginning Values
    fuel = 30
    food = 50
    power = 10
    hull = 5
    crew = 10
    burn_rate = 10
    morale = 100
    distance = 20
    day = 10

    # begin game loop
    running = True
    while running:

        # introduction
        if day == 10:

            fuel, food, power, hull, crew, morale = i.intro(fuel, food, power, hull, crew, morale) 

        # Display Distance
        h.status(distance, day)

        # Phase 1: Production Phase
        fuel, food, power, hull, crew, morale = p.production_phase(fuel, food, power, hull, crew, morale)

        # Phase 2: Spend Phase
        fuel, food, power, hull, crew, morale, distance_traveled = s.spend(fuel, food, power, hull, crew, morale)

        # Check for loss conditions
        if ed.lose(hull, crew, power, morale):
        
            if play_again():

                game_loop()

            else:

                break

        # Phase 3: Event Phase
        fuel, food, power, hull, crew, morale, distance = e.event(fuel, food, power, hull, crew, morale, distance)

        # Check for loss conditions
        if ed.lose(hull, crew, power, morale):
            
            if play_again():

                game_loop()

            else:

                break

        # phase 4: Travel Phase
        distance = t.travel(distance, distance_traveled)

        # Check for win conditions
        if ed.win(distance, running):
            
            if play_again():

                game_loop()

            else:

                break

        # Update Day
        day -= 1



# Display menu and run game loop
if m.start():
    
    game_loop()

# Print exit message
print("You have exited the game. Thank you for playing!")
