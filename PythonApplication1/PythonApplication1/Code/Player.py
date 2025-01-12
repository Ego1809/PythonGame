import random


class Player:
    def __init__(self, x=0, y=0, life=0, attackPower=0, numberOfpotion=0, healPower=0, emoji="🧙"):
        self.x = x
        self.y = y
        self.life = life
        self.maxLife = life
        self.attackPower = attackPower
        self.luckMultiplier = 1
        self.canTrowDice = True
        self.numberOfpotion = numberOfpotion
        self.healPower = healPower
        self.emoji = emoji
        self.level = 1

    def Attack(self, enemy):
        enemy.life -= self.attackPower * self.luckMultiplier
        self.luckMultiplier = 1
        self.canTrowDice = True
        if enemy.life <= 0 :
            enemy.IsAlive = False
            enemy.emoji = '💀'
            self.LevelUp()

    def Heal(self):
        self.life += self.healPower
        if self.life > self.maxLife:
            self.life = self.maxLife
        self.numberOfpotion -= 1
        self.luckMultiplier = 1
        self.canTrowDice = True
        
    def TrowDice(self):
        self.luckMultiplier = (random.randint(-3, 5) / 10) + 1
        self.canTrowDice = False
            
    def LevelUp(self):
        self.level += 1
        self.attackPower += 5

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        player = Player(
            x = data.get("x", 0),
            y = data.get("y", 0),
            life = data.get("life", 0),
            attackPower = data.get("attackPower", 0),
            numberOfpotion = data.get("numberOfpotion", 0),
            healPower = data.get("healPower", 0),
            emoji = data.get("emoji", "🧙")
        )
        player.maxLife = data.get("maxLife", 100)
        player.luckMultiplier = data.get("luckMultiplier", 1)
        player.canTrowDice = data.get("canTrowDice", True)
        player.level = data.get("level", 1)
        return player
    
        
        