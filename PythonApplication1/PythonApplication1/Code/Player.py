class Player:
    def __init__(self, name, x=0, y=0, life=0, attaquePower=0, healPower=0, emoji="🧙"):
        self.name = name
        self.x = x
        self.y = y
        self.life = life
        self.attaquePower = attaquePower
        self.healPower = healPower
        self.emoji = emoji

    def Attaque(self, enemy):
        enemy.life -= self.attaquePower

    def Heal(self):
        self.life += self.healPower
        if self.healPower != 0 :
            self.healPower -= 5