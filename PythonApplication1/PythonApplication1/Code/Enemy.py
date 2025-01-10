class Enemy:
    def __init__(self, x=0, y=0, life=0, attackPower=0, emoji="🐍"):
        self.x = x
        self.y = y
        self.life = life
        self.maxLife = life
        self.attackPower = attackPower
        self.lifeSteal = 0
        self.emoji = emoji
        self.IsAlive = True
        self.hasEvelved = False

    def Attack(self, player):
        if self.life < self.maxLife / 2 and self.hasEvelved == False:
            self.Evolve()
        
        player.life -= self.attackPower + self.lifeSteal
        self.life += self.lifeSteal

    def Evolve(self):
        self.emoji = '🐉'
        self.lifeSteal += 2
        self.hasEvelved = True