class Enemy:
    def __init__(self, x=0, y=0, life=0, attackPower=0, emoji="🐍"):
        self.x = x
        self.y = y
        self.life = life
        self.maxLife = life
        self.attackPower = attackPower
        self.lifeSteal = 0
        self.emoji = emoji
        self.isAlive = True
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
        
    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        enemy = Enemy(
            x = data.get("x", 0),
            y = data.get("y", 0),
            life = data.get("life", 0),
            attackPower = data.get("attackPower", 0),
            emoji = data.get("emoji", "🐉")
        )
        enemy.maxLife = data.get("maxLife", 100)
        enemy.lifeSteal = data.get("lifeSteal", 0)
        enemy.isAlive = data.get("IsAlive", True)
        enemy.hasEvolved = data.get("hasEvolved", False)
        return enemy