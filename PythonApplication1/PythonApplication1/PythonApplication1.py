import json
import time
import os
from Code.Player import Player
from Code.Enemy import Enemy
from Code.HealPotion import HealPotion
from Code.WinDestination import WinDestination

def main():
    if os.path.exists("save_game.json"):
        choice = input("A backup exists. Do you want to delete it and start a new game? ? (y/n) : ").lower()
        if choice == 'y':
            os.remove("save_game.json")
            print("Save deleted. A new game begins.")
            time.sleep(3)
        else:
            print("Loading the save...")
            time.sleep(3)
    
    loaded_game = load_game() if os.path.exists("save_game.json") else None
    if loaded_game:
        #load old game
        player, enemy, potions, gameMap, fighting, IsItPlayerTurn = loaded_game
    else:
        #creat new game
        fighting = False
        IsItPlayerTurn = True
        gameMap = [
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

        DrawMap(gameMap, potions, enemy, castel, player)

        #win trigger
        if player.x >= castel.x :
            print("you WIN")
            if os.path.exists("save_game.json"):
                os.remove("save_game.json")
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

            #deplacement and save
            direction = input("Déplacez le joueur ( S = gauche, D = droite, save = save this game) : ").lower()
            if direction == 'save':
                save_game(player, enemy, potions, gameMap, fighting, IsWizardTurn)
            elif direction == 's' and player.x > 1:
                player.x -= 2
            elif direction == 'd' and player.x < len(gameMap[0]) - 4:
                player.x += 2
            
            #enemy detection
            if player.x == enemy.x - 2 and enemy.isAlive == True :
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
                    if enemy.isAlive == False :
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


def save_game(player, enemy, potions, gameMap, fighting, IsItPlayerTurn):
    game_state = {
        "player": player.to_dict(),
        "enemy": enemy.to_dict(),
        "potions": [potion.to_dict() for potion in potions],
        "gameMap": gameMap,
        "fighting": fighting,
        "IsItPlayerTurn": IsItPlayerTurn,
    }
    with open("save_game.json", "w") as file:
        json.dump(game_state, file, indent=4)
    print("Jeu sauvegardé avec succès !")


def load_game():
    try:
        with open("save_game.json", "r") as file:
            game_state = json.load(file)
        player = Player.from_dict(game_state["player"])
        enemy = Enemy.from_dict(game_state["enemy"])
        potions = [HealPotion.from_dict(p) for p in game_state["potions"]]
        gameMap = game_state["gameMap"]
        fighting = game_state["fighting"]
        IsItPlayerTurn = game_state["IsItPlayerTurn"]
        print("Jeu chargé avec succès !")
        return player, enemy, potions, gameMap, fighting, IsItPlayerTurn
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée. Une nouvelle partie commence.")
        return None


def DrawMap(gameMap, potions, enemy, castel, player):
    #add all objets to the map before drawing
    carte_temp = [list(ligne) for ligne in gameMap]
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
