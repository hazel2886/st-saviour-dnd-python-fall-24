import random
import time
from tav import Tav
from draw import draw_d4, draw_d6, draw_d20

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__': 
    print( 'Dungeons and Flagons')

    # player = Tav('Hazel', 'Human')
    # player.print_character_sheet()
    # print()
    
locations = ['cave', 'bedroom', 'dungeon']
r = random.randint(0, len(locations) -1)
jobs = ['dragon, human, troll']
j = random.randint(0, len(jobs)-1)

# collecting use input 
name = input ('Name: ')
role = jobs[j]
print('Role: ' + jobs[j])
player = role(name, role)
player.print_character_sheet()

if player.role == 'Human':
     print('You are a Human!')
if player.role == 'Dragon!':
     print('You are a Dragon!')
if player.role == 'Troll':
     print('You are a Troll')

# print(name)
print_dramatic_text('Our story begins in a castle ... Welcome ' + name + ' to the cave...')
print_dramatic_text('You begin in the ' + locations[r])
print('Floor -1: Cave')
print('Floor 1: Dungeon')
print('Floor 2: Bedroom')
print_dramatic_text('Which room would you like to explore?')
room = input('Floor -1')
if (room == 'cave'):
     print_dramatic_text('You are in the cave!')
roll = random.randint(1,20)
draw_d20(roll)
if roll == 6:
     print_dramatic_text('You might have won this time but not next time')
else:
     print_dramatic_text('You can try again but... you may loose!')
if (room == 'floor -1'):
     print_dramatic_text('A gremlin escaped from the cage! Escape!')
if (room == 'floor 1'):
     print_dramatic_text('You have entered the bedroom...')
roll = random.randint(1,20)
draw_d20(roll)
if roll == 4: 
    room = input('Floor 2: ')
if (room == 'Bedroom' ):
    print_dramatic_text('You are in the castle bedroom!')
    roll = random.randint(1,20)
    draw_d4(roll)
if roll == 4: 
        room = input('Floor')
        if (room == 'Floor 1'):
            print_dramatic_text('You may have have won this time but Ill be back...')
else:
        if roll > 2: 
            print_dramatic_text('You go down to the dungeon and ask the witch for a gold gem and roll a 6 you win!')
            print_dramatic_text('Did you roll a 4? ')
            if player.role == 'Human':
                print_dramatic_text('HINT: H')
            else: 
                print_dramatic_text('Would you like buffs?')
                print_dramatic_text('No or yes')
                choice = input('Choice: ')
            if choice == "no" or "yes":
                player.strength += 1 
                player.print_character_sheet()
                print_dramatic_text('You have beaten me...')
            else:
                print_dramatic_text('Youll never beat me!')
            answer =input ('Answer: ')
            if answer == 'yes' or 'yes':
                room = input('bedroom: ')
                if (room == 'bedroom '): 
                    print_dramatic_text('You are in the bedroom')
                    roll = random.randint(1,20)
                    draw_d6(roll)
            print_dramatic_text('You beat me...')
        if (room == 'dungeon '):
            print_dramatic_text(' A troll came out from the dungeon!')
        else:
            skelly = '\U0001F480'
            print_dramatic_text('I have once again won against you!')
        if room == ('dungeon'): 
            print_dramatic_text('enter the cave...')
            roll = random.randint(1,4)
            draw_d4(roll)
            if roll <= 2:
                room = input('cave: ')
            if roll > 2: 
                print_dramatic_text('Explore the cave!')
                print_dramatic_text('skelly scares you!')
                if player.role == 'troll':
                    print_dramatic_text('to win, you have to talk to the troll.')
                else:
                    print_dramatic_text('Buffs?')
                    print_dramatic_text('No or yes?')
                    player.strength += 1 
                    player.print_character_sheet()
            else:
                print_dramatic_text('I have won against you again!')
        else:
            print_dramatic_text('You did not talk to the troll?')
        Skully = '\UU0001F480'
        print_dramatic_text(Skully + ' You traitor!')
        skully = '\U0001F480'
        print_dramatic_text(skully + 'You traitor!')

    
            





         


        



   
