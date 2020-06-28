''' Space Commander '''

# imports
import menu as m
import hud as h
import generate as g
import spend as s
import event as e
import end as end
import random

# Beginning Values
fuel = 30
food = 50
power = 5
hull = 5
crew = 10
burn_rate = 10
morale = 70
distance = 20
day = 1
    
# Display Menu
running = m.menu()

# begin game loop
while running == True:

    if day == 1:
        print("opening")
        print('')

    # Display HUD
    h.hud(fuel, food, power, hull, crew, morale, distance, day)

    # Generate Resources
    fuel, food, power, hull, crew, morale = g.gen(fuel, food, power, hull, crew, morale)

    # spend resources
    fuel, food, power, hull, crew, burn_rate, morale, distance = s.spend(fuel, food, power, hull, crew, burn_rate, morale, distance)
    
    # Check for loss conditions
    running = end.loss(hull, crew, power, morale)

    # Event
    fuel, food, power, hull, crew, burn_rate, morale, distance = e.event(fuel, food, power, hull, crew, burn_rate, morale, distance)

    # Check for loss conditions
    running = end.loss(hull, crew, power, morale)

    # Check for win conditions
    running = end.win(distance, running)

    # Update Day
    day += 1


    

print("you have exited the game. Thanks for playing!")


