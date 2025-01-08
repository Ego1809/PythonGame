class Enemy:
    def __init__(self, name, x=0, y=0, life=0, attaquePower=0, emoji="🐉"):
        self.name = name
        self.x = x
        self.y = y
        self.life = life
        self.attaquePower = attaquePower
        self.emoji = emoji
        self.IsAlive = True

    def Attaque(self, player):
        player.life -= self.attaquePower