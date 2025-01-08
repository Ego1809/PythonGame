class ForcePotion:
    def __init__(self, x=0, y=0, puissance=0, emoji='🧪'):
        self.x = x
        self.y = y
        self.puissance = puissance
        self.emoji = emoji

    def ApplyEffects(self, player):
        player.attaquePower += self.puissance
        player.healPower += self.puissance