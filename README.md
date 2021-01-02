
# Space Commander

In this text-based, resource management game, you will take on the role of a starship commander in the United Earth Federation. During the game you will make decisions regarding the production and expenditure of your ship’s limited resources that will ultimately lead to the success or failure of your mission. Will you lead your crew to victory or annihilation? 

# What you Need to Play

You will need a python environment with access to the random library to play this game. To begin clone this repository and run the main.py file in your python environment. main.py is dependent upon the other files in the repository to run. You will need all of the files in the repository to play.

# The Story so Far...

The year is 202020, and Earth Force Captain, *Chough-Chough* (That’s you!) is returning to base after another successful mission. Star Gazer 1, an Earth outpost, has been the captain’s home away from home for some time now. The Garquackien threat necessitates a round-the-clock vigil, and Earth Force Captain *Chough-Chough* has been tasked with maintaining that vigil throughout the neutral space separating the United Earth Force from the Garquackien Empire. As the ship approached Star Gazer 1, the captain smiled and leaned back, looking forward to some well-deserved R&R when suddenly...

Several Garquackien attack ships appeared out of nowhere. To make matters worse, the ship’s scanners indicated only broken metal and empty space where the Star Gazer outpost should have been. It would have taken an enormous armada to mount this kind of attack, and the approaching vessels left no mystery as to who the culprit was. An attack of this magnitude could mean only one thing. The Garquackiens were launching an all-out attack, and their target would be Earth. If caught unprepared, Earth would likely suffer the same fate as the fallen space station. However, if Earth could be warned before the attack, and muster its defenses the battle would likely turn in Earth’s favor. Though the captain’s crew and resources were already taxed, the new mission was clear: Escape the attacking ships and make it back to Earth in time to raise an alarm about the Garquackien attack!

# Rules

### Winning and Losing

In space commander, your goal is to travel to Earth and warn the United Earth Federation about the impending Garquackien attack. During the game, you will see the distance you still need to travel displayed as YOUR DISTANCE FROM EARTH. If this distance reaches 0, your ship has made it to Earth, and you have won!

You will also see how far the Garquackians are from invading Earth. This will be displayed as GARQUACKIEN DISTANCE FROM EARTH. If this number ever reaches 0, the Garquackiens have made it to Earth before you and you were not able to warn Earth in time. If this happens you have lost the game.

You will need to carefully manage your ship’s resources. If, at any time, your ship's fuel, food, power, hull, crew, or morale ever fall to zero you will lose the game.

### Game Phases

Space Commander takes place over a number of rounds each representing one week of time. Each round has four phases the PRODUCTION, SPEND, EVENT, and TRAVEL. Rounds will continue and phases will repeat in order until the game is either won or lost.

PRODUCTION PHASE: During the production phase you will assign members of your crew to produce resources your ship needs to continue on its mission. Each crew assigned to a resource will have a chance to produce that resource equal to the crew’s morale minus the difficulty of producing that resource. If successful, the amount produced will vary by resource. (See in game information for details during the production phase.) 

SPEND PHASE: The spend phase is when you spend resources on your ship’s weekly needs. First, you will spend food to feed each of your crew. Each of your crew will consume one food reducing the number of food from your supply by the number of crew on your ship. If you do not have enough food to feed all of your crew rioting will break out on your ship and you will lose the game. Second, you will check to see if any of you power crystals have burned out. Each crystal has a 20% chance of burning out each round. If all of your remaining power crystals burn out, your ship will lose power and you will lose the game. Third, you will decide on the amount of fuel you will spend on traveling that week. You must spend a minimum of one fuel to move each round. The more fuel you spend the greater distance you will travel during the travel phase. (See in game information for specific fuel to movement ratios)

EVENT PHASE: The hazards of space travel are many and varied. During the event phase you will encounter two of events that will tax your resources. The resources taxed will depend on the decisions you make during those events.

TRAVEL PHASE: During the travel phase your ship will move closer to Earth. The amount of movement is determined by the amount of fuel spent during the spend phase and will reduce your distance from Eart. During this phase the Garquackiens will also move closer to Earth. The Garquackiens will move between 1 and 4 distance toward Earth reducing Garquackien distance from Earth by an equal amount. If Garquackien distance from Earth reaches zero, the Garquackiens have made it to Earth before you and you were not able to warn Earth in time. If this happens you have lost the game.

### Game Terms

DISTANCE FROM EARTH: How far your ship is from Earth. If this distance ever reaches 0, you have reached Earth ahead of the Garquackiens and have won the game.
   
GARQUACKIEN DISTANCE FROM EARTH: How far the Garquackiens are from Earth. If this distance reaches zero before you make it to Earth, you will arrive too late to sound the alarm, Earth will be destroyed, and you lose the game.

CREW: Members of the ship that are under your command. During the production phase you will assign each of your crew to produce different resources.
    
FOOD: Each week, during the spend phase, you will spend food to feed your crew. Each of your crew will consume 1 food. Because food for the ship is generated through replication technology, if the total food on your ship ever drops to zero you will be unable to replicate more, and you will lose the game.
          
POWER: Your ship is powered my power crystals that supply a large amount of energy but are unstable. Each power crystal in your supply has a 20% chance of burning out each day. If the number of power crystals in your reserve falls to zero your ship will lose all power to your ship and you will lose the game.
    
FUEL: Each week during the spend phase you will spend an amount of fuel on traveling that week. The more fuel you spend the greater distance you will travel during the travel phase and the closer you will be to Earth. The ship's propulsion system is designed to run continuously while not docked at a space station, meaning you must keep at least 1 fuel in your reserve at all times or your ship’s engine will overheat and explode. This will cause you to lose the game.
    
HULL: Represents the physical integrity of the ship. If the ship’s hull ever falls to zero, the ship will be destroyed, and you will lose the game.
    
MORALE: Represents the crew’s resolve and effects how likely they are to produce resources during the production phase. Morale cannot be raised above 100% If morale ever falls to 0 the crew succumbs to despair or mutinies, and you lose the game.

### Other Information:

Resource Caps: Most of the resources for your ship are displayed as current Number / maximum number on your display. current number represents the current number of that resource in your reserve. Maximum number represents the maximum number of that resource your ship can hold. Resources produced in excess of this number are lost. Morale id displayed as a percentage and cannot be raised above 100%.

Event Specifics: There are 21 different events in the game each will either tax one specific resource or tax your choice of two different resources. Each resource or resource paring has an equal likelihood of being encountered and you may encounter the same event in a given round (Though this is unlikely). The amount that each resource will be taxed will very within a given range. The range for each resource is the same across all events.

## Good luck, and thank you for playing!


