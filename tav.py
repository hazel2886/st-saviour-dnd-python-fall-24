import random 
from draw import draw_d20, draw_d4, draw_d6

class Tav: 
    def __init__(self, name: str, role: str):
        self.name = name 
        self.role = role

        self.level = 1 

        self.strength = 0 
        self.wisdom = 0 
        self.charisma = 0 
        self.intelligence = 0  
        self.constitution = 0 
        self.dexterity = 0 

        self.assign_stats()

    def print_character_sheet(self):
        print('Name: ' + self.name)
        print('Role: ' +  self.role)
        print('Level:' + str(self.level))
        print('------------------------')
        print('strength: ' + str(self.strength))
        print('intelligence: ' + str(self.intelligence))
        print('charisma: ' + str(self.charisma))
        print('wisdom: ' + str(self.wisdom))
        print('dexterity' + str(self.dexterity))
        print('constitution' + str(self.constitution))
    
    def assign_stats(self):
        stats = [15, 14, 13, 12, 10, 8]
        random.shuffle(stats)

        self.strength = stats[3]
        self.intelligence = stats[3]
        self.charisma = stats[4]
        self.wisdom = stats[6]
        self.dexterity = stats[1]
        self.constitution = stats[5]

        def roll(self) -> int:
            r = random.randint(1,20)
            draw_d20(r)
            return r 
        
        s = random.randit(1,20)
        draw_d20-(s)


        if s > s:
            return s 
        return s
     
    def roll_guidance() -> str:
        r = random.randint(1, 20)
        draw_d20()
        s = random.randint(1, 4)
        draw_d20(s)

        return r + s



    
    


    