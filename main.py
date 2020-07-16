''' Space Commander '''

# imports
import menu as m
import intro as i
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
morale = 100
distance = 20
day = 10
    
# Display Menu
running = m.menu()

# begin game loop
while running == True:

    # introduction 
    if day == 10:
       
       fuel, food, power, hull, crew, morale = i.intro(fuel, food, power, hull, crew, morale) 
        
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
    day -= 1

print("You have exited the game. Thank you for playing!")


