
# Space Commander

In this text-based, resource management game, you will take on the role of a starship commander in the United Earth Federation. During the game you will make decisions regarding the production and expenditure of your ship’s limited resources that will ultimately lead to the success or failure of your mission. Will you lead your crew to victory or annihilation? 

# What you Need to Play

You will need a python environment with access to the random library to play this game.
To begin clone this repository and run the main.py file in your python environment.

(Don’t do this just yet. This game is still actively being worked on and may not run in its current state.)

# The Story so Far...

The year is 202020, and Space Force Captain, *Chough-Chough* (That’s you!) is returning to base after another successful mission. Star Gazer 1, an Earth outpost, has been the captain’s home away from home for some time now. The Garquackien threat necessitated a round-the-clock vigil, and Space Force Captain *Chough-Chough* had been tasked with maintaining that vigil throughout the neutral space separating the United Earth Force from the Garquackien Empire and its quest for galactic domination. As the captain’s ship approached Star gazer 1, the captain was looking forward to some well-deserved R&R when suddenly...Several Garquackien attack ships appeared out of nowhere. To make matters worse, the ship’s scanners indicated only broken metal and empty space where the Star Gazer outpost should have been. 

It would have taken an enormous armada to mount this kind of attack, and the approaching vessels left no mystery as to who had gathered such a force. A attack of this magnitude could mean only one thing. The Garquackiens were launching an all-out attack, and thier final target would be Earth. If caught unprepared, Earth would likely suffer the same fate as the fallen space station. However, if Earth could be warned before the attack, and muster its defenses the battle would likely turn in Earth’s favor. Though the captain’s crew and resources are already taxed, their new mission was clear: Escape the attacking ships and make it back to Earth in time to raise the alarm about the Garquackien attack!

# Rules

### Winning and Losing

In space commander, your goal is to travel to Earth and warn the United Earth Federation about the impending Garquackien attack. During the game, you will see the distance you still need to travel displayed as distance from Earth. If this distance reaches 0, your ship had made it to Earth and you have won!

You will also see how far the Garquackians are from Earth (WEEKS UNTILL THE GARQUACKIEN INVASION). If the Garquackiens reach Earth before you do, they will begin their attack before the United Earth Federation has a chance to ready its defenses. If this is allowed to happen Earth will be destroyed and you will lose the game.

During play, you will need to carefully manage your ship’s resources. If your ship's crew, power, hull, fuel, or morale ever fall to zero you will lose the game.

### Game Phases

Space Commander takes place over four phases which repeat in order until the game is either won or lost. Each repitition represents one week of time.

PRODUCTION PHASE: During the production phase you will assign members of your crew to produce resources your ship needs to continue its mission. Each of your assigned crew will have a chance to produce the resource its assigned to. That chance is equal to the crew’s morale minus the difficulty of producing that resource. If successful, the amount produced will vary by resource. (See in game information for details during the production phase.) 

SPEND PHASE: The spend phase is when you spend reasoeces on your ships weekly needs. This takes place over three steps. First you will spend food to feed each of your crew. Each of your crew will consume one food reducing the number of food from your supply by the number of crew on your ship. If you do not have enough food to feed all of your crew, the ones that are not fed will starve and die, reducing the number of crew in your ship by the number of unfed crew. Second you will check to see if any of you power crystals burned out during the previous week. Each crystal has a small chance of burning out each week. If all of your power crystals burn out at once your ship will be left without power and you will lose the game. Third you will decide on the amount of fuel you will spend on traveling that week. The more fuel you spend the greater distance you will travel during the travel phase. This reduces your distance from Earth and bring you closer to winning the game.

EVENT PHASE: The hazards of space travel are many and varied. During the event phase you will encounter a number of events that will tax your resources. The resources taxed will depend on the decisions you make during those events.

TRAVEL PHASE: During the travel phase your ship will move closer to Earth and a you will be closer to winning the game. The amount you move is determined by the amount of fuel you spent during the spend phase for movement. If your distance from Earth reaches zero you have arrived at Earth and have won the game.

### Game Terms

DISTANCE FROM EARTH: How far your ship is from Earth in galactic standard units. If distance ever reaches 0, you have reached Earth and have won the game.
   
WEEKS UNTILL THE GARQUACKIEN INVASION: The number of weeks until the Garquackien invasion reaches 
Earth. This number will count down by one each game round. If it reaches zero before you make it to Earth, you are too late. The Earth will be destroyed, and you will lose the game.

CREW: Members of the ship that are under your command. During the production phase you will assign each of your crew to produce different resources.
    
FOOD: Each week, during the spend phase, you will spend food to feed your crew. Each of your crew will consume 1 food. Crew that cannot be feed will starve.
          
POWER: Your ship is powered my power crystals that supply a large amount of energy but are unstable. Each power crystal in your supply has a small chance of burning out each day. If the number of power crystals in your reserve falls to 0 your ship will lose all power and you will lose the game.
    
FUEL: Each week during the spend phase you will decide on the amount of fuel you will spend on traveling that week. The more fuel you spend the greater distance you will travel during the travel phase and the closer you will be to Earth. Be warned the faster the ship moves the worse its fuel efficiency is. Also, the ship's propulsion system is designed to run continuously while not docked at a space station, meaning you must keep at least 1 fuel in your reserve at all times or your ship’s engine will overheat and explode. This will cause you to lose the game.
    
HULL: Represents the physical integrity of the ship. Hull cannot be raised above it's starting value. If the ship’s hull ever falls to zero, the ship will be destroyed, and you will lose the game.
    
MORALE: Represents the crew’s resolve and effects how likely they are to produce resources during the production phase. Morale cannot be raised above 100% If morale ever falls to 0 the crew succumbs to despair or mutinies, and you lose the game.

DISTANCE: Shows the total remaining distance your ship must traveled in order to reach Earth.
If distance reaches 0 you arrive on Earth and win the game.

