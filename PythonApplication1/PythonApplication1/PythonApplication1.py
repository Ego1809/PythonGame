import time
from Code.Player import Player
from Code.Enemy import Enemy
from Code.HealPotion import HealPotion
from Code.WinDestination import WinDestination

def main():
    fighting = False
    IsItPlayerTurn = True

    map = [
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
    "~    🌲🌲       🌳🌳       🗻🗻🗻🗻🗻🗻         🌾🌾🌲🌲🌳   🌾🌾🌾🏡  ~",
    "~🌲🌲🌳     🌳           🗻🗻   🗻  🌲🗻    🌲              🌾🌾🌾🏘️🏡 ~",
    "~                                                              ~",
    "~      🌲🌳🌳    🌳🌳🌲        🗻🗻🗻🗻     🌲🌲🌳         🌾🌾 🌾🌾🏘️ ~",
    "~  🌲🌲🌳🌳     🌲🌲🌳🌳🌳     🗻        🌳🌳       🌳🌳🌳     🌾🏡🌾🏡~",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    ]

    player = Player(x = 15, y = 3, life = 100, attackPower = 20, numberOfpotion = 0, healPower = 30, emoji = "🧙‍♂️")
    enemy = Enemy(x = 35, y = 3, life = 100, attackPower = 25, emoji = "🐍")
    potions = [
        HealPotion(x = 3, y = 3, emoji = '🧪'),
        HealPotion(x = 11, y = 3, emoji = '🧪'),
        HealPotion(x = 7, y = 3, emoji = '🧪')
    ]
    castel = WinDestination(x = 60, y = 3, emoji = '🏫')

    while  True :

        DrawMap(map, potions, enemy, castel, player)

        #win trigger
        if player.x >= castel.x :
            print("you WIN")
            time.sleep(3)
            break
        
        #loose trigger
        if player.life <= 0 :
            print("you LOOSE")
            time.sleep(3)
            break

        #detection of the potions
        for potion in potions[:]: 
            if player.x == potion.x and player.y == potion.y:
                player.numberOfpotion += 1
                potions.remove(potion)

        if fighting == False :

            #deplacement
            player.Move( enemy, map)
            
            #enemy detection
            if player.x == enemy.x - 2 and enemy.IsAlive == True :
                    fighting = True

        elif fighting == True :
            
            #combat
            print(f"player life :  {player.life}                               enemy life :  {enemy.life}")
            print(f"player attaque power : {player.attackPower * player.luckMultiplier}                      enemy attaque power : {enemy.attackPower + enemy.lifeSteal}")
            print(f"player heal power : {player.healPower}")
            print(f"player number of heal potions : {player.numberOfpotion}")

            if IsItPlayerTurn == True :
                #player turn to attack
                if player.numberOfpotion > 0 and player.life != player.maxLife and player.canTrowDice == True:
                    attaque = input("sorts disponibles ( E = attaque, R = heal, T = trow lucky dice) : ").lower()
                elif player.canTrowDice == True :
                    attaque = input("sorts disponibles ( E = attaque , T = trow lucky dice)").lower()
                elif player.numberOfpotion > 0 and player.life != player.maxLife :
                    attaque = input("sorts disponibles ( E = attaque, R = heal )").lower()
                else : 
                    attaque = input("sorts disponibles ( E = attaque )").lower()
                                
                if attaque == 'e' :
                    player.Attack(enemy)
                    if enemy.IsAlive == False :
                        fighting = False
                    IsItPlayerTurn = False
                elif attaque == 'r' and player.numberOfpotion > 0 and player.life != player.maxLife:
                    player.Heal()
                    IsItPlayerTurn = False
                elif attaque == 't' and player.canTrowDice == True:
                    player.TrowDice()

            elif IsItPlayerTurn == False :
                #enemy turn to attack
                enemy.Attack(player)
                IsItPlayerTurn = True
                
                print("enemy attacking...")
                time.sleep(3)


def DrawMap(map, potions, enemy, castel, player):
    #add all objets to the map before drawing
    carte_temp = [list(ligne) for ligne in map]
    carte_temp[castel.y][castel.x] = castel.emoji
    for potion in potions:
        carte_temp[potion.y][potion.x] = potion.emoji
    carte_temp[enemy.y][enemy.x] = enemy.emoji
    carte_temp[player.y][player.x] = player.emoji

    carte_à_afficher = ["".join(ligne) for ligne in carte_temp]
    
    print("\033c", end='')
    
    for ligne in carte_à_afficher:
        print(ligne)


if __name__ == "__main__":
    main()
