import time
from Code.Player import Player
from Code.Enemy import Enemy
from Code.ForcePotion import ForcePotion

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

    player = Player(name = "Wizard", x = 15, y = 3, life = 100, attaquePower = 20, healPower = 20, emoji = "🧙‍♂️")
    enemy = Enemy(name = "Dragon", x = 35, y = 3, life = 100, attaquePower = 20, emoji = "🐉")
    potion = ForcePotion(x = 3, y = 3, puissance = 5, emoji='🧪')

    while  True :

        carte_temp = [list(ligne) for ligne in map]
        carte_temp[enemy.y][enemy.x] = enemy.emoji
        carte_temp[potion.y][potion.x] = potion.emoji
        carte_temp[player.y][player.x] = player.emoji

        carte_à_afficher = ["".join(ligne) for ligne in carte_temp]
        DrawMap(carte_à_afficher)

        if player.x >= 65 :
            break
            print("you WIN")

        #if player.x == potion.x :
        #    potion.ApplyEffects(player)
        #    player.emoji = '🧙‍♀️'
        #faire en sorte que sans la potion on puisse pas ce heal

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
            
            print(player.life, enemy.life)

            if IsWizardTurn == True :
                attaque = input("attaquer l'enemie ( e = attaque, r = heal) : ").lower()
                
                if attaque == 'e' :
                    player.Attaque(enemy)
                    if enemy.life <= 0 :
                        enemy.IsAlive = False
                        enemy.emoji = '💀'
                        fighting = False
                    IsWizardTurn = False
                elif attaque == 'r' :
                    player.Heal()
                    IsWizardTurn = False

            elif IsWizardTurn == False :
                enemy.Attaque(player)
                if player.life <= 0 :
                    player.emoji = '💀'
                    break
                IsWizardTurn = True
                
                print("enemy attacking...")
                time.sleep(3)


def DrawMap(map):

    print("\033c", end='')
    
    for ligne in map:
        print(ligne)


if __name__ == "__main__":
    main()
