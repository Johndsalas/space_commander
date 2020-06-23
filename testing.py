import random

# Variables passed to function
crew = 10
morale = 50
fuel = 10

# number of crew assigned to each resource
fuel_crew = 0
food_crew = 0
power_crew = 0
hull_crew = 0
morale_crew = 0

# pelalty to production chance for each reasorce
fuel_pen = 0
food_pen = 0
power_pen = 0
hull_pen = 0
morale_pen = 0

# chance to produce each reasorce 
fuel_chance = (morale-fuel_pen)
food_chance = (morale-fuel_pen)
power_chance = (morale-fuel_pen)
hull_chance = (morale-fuel_pen)
morale_chance = 1

# number of resorces produced on success
fuel_prod = 10
food_prod = 10
power_prod = 10
hull_prod = 10
morale_prod = 10 

print("This is the generation phase. In this phase you will assign crew members to generate resorces (fuel, food, power, hull, crew, morale).")
print('')
print(f"Your total crew is {crew}.")
print('')

gathering = True

while gathering == True:

    print("How many crew members will you assign to fuel.")
    fuel_crew = input()

    print("How many crew members will you assign to food.")
    food_crew = input()

    print("How many crew members will you assign to power.")
    power_crew = input()

    print("How many crew members will you assign to hull.")
    hull_crew = input()

    print("How many crew members will you assign to morale.")
    morale_crew = input()

    if fuel_crew.isdigit() == True and food_crew.isdigit() == True and power_crew.isdigit() == True and hull_crew.isdigit() == True and morale_crew.isdigit() == True:

        assigned = int(fuel_crew) + int(food_crew) + int(power_crew) + int(hull_crew) + int(morale_crew)

        if assigned <= crew:

            crew_check = True
            
            while crew_check:
           
                print(f"You have assigned {fuel_crew} crew to fuel.") 
                print(f"You have assigned {food_crew} crew to food.")
                print(f"You have assigned {power_crew} crew to power.")
                print(f"You have assigned {hull_crew} crew to hull.")
                print(f"You have assigned {morale_crew} crew to fuel.")
                print('')

                if assigned < crew:

                    print("You have not assigned all of your crew members!!!")


                print("Proceed with the current assignment? (y/n)")
                acknowledge = input()

                if acknowledge in ('y','n'):
                    break

                else:
                    
                    print('')
                    print("Invalid command please type 'y' or 'n")
                    print('')
              
            if acknowledge == 'y':

                print("calculating resorces")

                fuel_gen = 0
                food_gen = 0
                power_gen = 0
                hull_gen = 0
                morale_gen = 0
                
                for r in range(0, int(fuel_crew)):

                    if int(random.randrange(1,101)) <= fuel_chance:

                        fuel_gen += fuel_prod
                        
                        print("Fueling successful!!!")
                        print('')

                    else:

                        print("Fueling Unsuccessfull!!!")
                        print('')

                fuel += fuel_gen

                break

            elif acknowledge == 'n':

                print("Reasign your crew.")

        elif assigned > crew:

            print(f"Number of crew member's assigned exceeds total number of crew. you may only assign a total of {crew} crew")

    else:

        print("Invalid Command please input only numbers during this phase.")

print(f"Fuel: {fuel} ")
print("End Demo")