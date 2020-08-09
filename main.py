''' Space Commander '''

# imports
import menu as m
import intro as i
import hud as h
import generate as g
import spend as s
import event as e
import end as ed
import random

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

# Display Menu
running = m.menu()

# begin game loop
while running == True:

    # introduction
    if day == 10:

        fuel, food, power, hull, crew, morale = i.intro(fuel, food, power, hull, crew, morale) 

    # Display Distance
    h.travel(distance, day)

    # Display HUD
    h.hud(fuel, food, power, hull, crew, morale)

    # Phase 1: Production Phase
    fuel, food, power, hull, crew, morale = g.production_phase(fuel, food, power, hull, crew, morale)

    # Display HUD
    h.hud(fuel, food, power, hull, crew, morale)

    # Phase 2: Spend Phase
    fuel, food, power, hull, crew, burn_rate, morale, distance = s.spend(fuel, food, power, hull, crew, burn_rate, morale, distance)

    # Display HUD
    h.hud(fuel, food, power, hull, crew, morale)

    # Check for loss conditions
    running = ed.loss(hull, crew, power, morale)

    # Phase 3: Event Phase
    fuel, food, power, hull, crew, morale, distance = e.event(fuel, food, power, hull, crew, morale, distance)

    # Check for loss conditions
    running = ed.loss(hull, crew, power, morale)

    # Check for win conditions
    running = ed.win(distance, running)

    # Update Day
    day -= 1

print("You have exited the game. Thank you for playing!")
