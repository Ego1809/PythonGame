class Player:
    def __init__(self, name, x=0, y=0, life=0, attaquePower=0, numberOfpotion=0, emoji="🧙"):
        self.name = name
        self.x = x
        self.y = y
        self.life = life
        self.attaquePower = attaquePower
        self.numberOfpotion = numberOfpotion
        self.emoji = emoji
        self.level = 1

    def Attaque(self, enemy):
        enemy.life -= self.attaquePower
        if enemy.life <= 0 :
            enemy.IsAlive = False
            enemy.emoji = '💀'
            self.LevelUp()
            
    def LevelUp(self):
        self.level += 1
        self.attaquePower += 5
        
        