import time
from Code.Player import Player
from Code.Enemy import Enemy
from Code.HealPotion import HealPotion

def main():
    fighting = False
    IsWizardTurn = True

    map = [
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
    "~    🌲🌲       🌳🌳       🗻🗻🗻🗻🗻🗻         🌾🌾🌲🌲🌳   🌾🌾🌾🏡  ~",
    "~🌲🌲🌳     🌳           🗻🗻   🗻  🌲🗻    🌲              🌾🌾🌾🏘️🏡 ~",
    "~                                                            🏫  ~",
    "~      🌲🌳🌳    🌳🌳🌲        🗻🗻🗻🗻     🌲🌲🌳         🌾🌾 🌾🌾🏘️ ~",
    "~  🌲🌲🌳🌳     🌲🌲🌳🌳🌳     🗻        🌳🌳       🌳🌳🌳     🌾🏡🌾🏡~",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    ]

    player = Player(name = "Wizard", x = 15, y = 3, life = 100, attaquePower = 20, numberOfpotion = 0, healPower = 30, emoji = "🧙‍♂️")
    enemy = Enemy(name = "Dragon", x = 35, y = 3, life = 100, attaquePower = 25, emoji = "🐉")
    potions = [
        HealPotion(x=3, y=3, emoji='🧪'),
        HealPotion(x=11, y=3, emoji='🧪'),
        HealPotion(x=7, y=3, emoji='🧪')
    ]

    while  True :

        carte_temp = [list(ligne) for ligne in map]
        carte_temp[enemy.y][enemy.x] = enemy.emoji
        for potion in potions:
            carte_temp[potion.y][potion.x] = potion.emoji
        carte_temp[player.y][player.x] = player.emoji

        carte_à_afficher = ["".join(ligne) for ligne in carte_temp]
        DrawMap(carte_à_afficher)

        if player.x >= 60 :
            print("you WIN")
            time.sleep(3)
            break

        for potion in potions[:]: 
            if player.x == potion.x and player.y == potion.y:
                player.numberOfpotion += 1
                potions.remove(potion)

        if fighting == False :

            direction = input("Déplacez le joueur ( s = gauche, d = droite) : ").lower()

            if direction == 's' and player.x > 1:
                player.x -= 2
            elif direction == 'd' and player.x < len(map[0]) - 4:
                player.x += 2

            if player.x == enemy.x - 2 and enemy.IsAlive == True :
                      fighting = True

            time.sleep(0.2)

        elif fighting == True :
            
            print(f"player life :  {player.life} / enemy life :  {enemy.life}")
            print(f"player attaque power : {player.attaquePower} / player heal potions : {player.numberOfpotion}")

            if IsWizardTurn == True :
                if player.numberOfpotion > 0 and player.life != player.maxLife:
                    attaque = input("sorts disponibles ( e : attaque, r : heal) : ").lower()
                else :
                    attaque = input("sorts disponibles ( e : attaque )").lower()
                
                if attaque == 'e' :
                    player.Attaque(enemy)
                    if enemy.IsAlive == False :
                        fighting = False
                    IsWizardTurn = False
                elif attaque == 'r' and player.numberOfpotion > 0 and player.life != player.maxLife:
                    player.Heal()
                    IsWizardTurn = False

            elif IsWizardTurn == False :
                enemy.Attaque(player)
                IsWizardTurn = True
                
                print("enemy attacking...")
                time.sleep(3)


def DrawMap(map):

    print("\033c", end='')
    
    for ligne in map:
        print(ligne)


if __name__ == "__main__":
    main()
