import os
import random
from time import sleep

from battlesim2.core import Fighter, swordsDict, bowsDict
from battlesim2.utils import listToMatrix, title, help

# prints all the information for a weapon
def weaponInfo(weapon):
    '''
      prints out all the information about a weapon
      args:
        weapon {Weapon} - the weapon that is being inspected
      return:
        none
      '''
    print("_"*20)
    print(f"_-{weapon.name}-_")
    print(f"-{weapon.dmgRange[0]} to {weapon.dmgRange[1]} Dammage-")
    print(f"-{weapon.range[0]}m to {weapon.range[1]}m Range-")
    print(f"-{weapon.accuracy}% Accuracy-")
    print(f"-{weapon.critChance}% Critical Hit Chance")
    print(f"-Critical Hits do {weapon.critDmg}x Dammage")
    print(f"-Hits {weapon.multiHit} Time(s)-")
    print("_"*20)
    sleep(1)


# Prints all the info for the game
def gameInfo():
    '''
      prints out all the information for the current game state
      args:
        none
      return:
        none
    '''
    print("_"*20)
    print(f"{Player.name} HEALTH:")
    print("++ "*Player.health, f"{Player.health}hp")
    print(f"{Enemy.name} HEALTH:")
    print("++ "*Enemy.health, f"{Enemy.health}hp")
    print("")
    print("DISTANCE:")
    print("-- "*distance, f"{distance}m")
    print("_"*20)
    sleep(1)


def checkWin():
    '''
      Checks if the game is over, determines the winner, and prints out the results
      args:
        none
      return:
        {bool} - weather the game is over or not
    '''
    global playing
    if Player.health <= 0:
        print("_"*20)
        # ASCII font from https://www.asciiart.eu/
        print('''
    ▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▄▄▄█████▓
     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
      ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
      ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░
      ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░
       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░
     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░
     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░
     ░ ░         ░ ░     ░            ░  ░    ░ ░        ░
     ░ ░
        ''')
        print("_"*20)
        gameInfo()
        playing = False
        return True
    elif Enemy.health <= 0:
        print("_"*20)
        # ASCII font from https://www.asciiart.eu/
        print('''
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
        ''')
        print("_"*20)
        gameInfo()
        playing = False
        return True
    else:
        return False

def assignWeapons(playerName, enemyName):
    '''
        Assigns weapons and creats the Player and Enemy
        args:
            {string} playerName - name of the player
            {string} enemyName - name of the enemy
        return:
            none
    '''
    # convert swordsDict and bowsDict to marticies
    swordsMatrix = listToMatrix(list(swordsDict), 2)
    bowsMatrix = listToMatrix(list(bowsDict), 2)

    # clear anything previously in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Selection for sword
    print("Pick your sword!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for sword in swordsMatrix[page]:
            weaponInfo(swordsDict[sword])
        print(f"<Pg{page + 1}/{len(swordsMatrix)}>")
        swordSelect = input().lower()
        # logic for changeing pages
        if swordSelect == ">" and page < len(swordsMatrix) - 1:
            page += 1
            os.system('cls' if os.name == 'nt' else 'clear')
        elif swordSelect == "<" and page > 0:
            page -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            # select sword on input
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                swordSelect = swordsDict[swordSelect]
                print(f"=-{swordSelect.name} Selected-=\n")
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-Something went wrong, try again!-\n")

    # Selection for bow
    print("Pick your bow!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for bow in bowsMatrix[page]:
            weaponInfo(bowsDict[bow])
        print(f"<Pg{page + 1}/{len(bowsMatrix)}>")
        bowSelect = input().lower()
        # logic for changeing pages
        if bowSelect == ">" and page < len(bowsMatrix) - 1:
            page += 1
            os.system('cls' if os.name == 'nt' else 'clear')
        elif bowSelect == "<" and page > 0:
            page -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            # select sword on input
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                bowSelect = bowsDict[bowSelect]
                print(f"=-{bowSelect.name} Selected-=\n")
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-Something went wrong, try again!-\n")

    # gives player the selected weapons
    global Player, Enemy
    Player = Fighter(swordSelect, bowSelect, playerName)
    Player.read(False)

    # gives enemies random weapons
    Enemy = Fighter(swordsDict["short sword"], bowsDict["hunting bow"], enemyName)
    Enemy.randomWeapons()


def playGame():
    '''
        The game loop along with some setup
        args:
            none
        return:
            none
    '''
    # pick a name for you and the enemy
    print("_" * 20)
    enemyName = input("What is the Enemy called?\n")
    playerName = input("And what are you called?\n")
    if enemyName == "": enemyName = "Enemy"
    if playerName == "": playerName = "Player"
    print("_" * 20, "\n")

    # Assign the weapons to the fighters
    assignWeapons(playerName, enemyName)

    # variables needed to start the game
    global distance, playerTurn, playing
    distance = 10
    playerTurn = True
    playing = True

    # Code inspired by my Python 1 project 'Battle Sim'
    # This is the game loop
    while playing:
        # Player turn actions
        while playerTurn:
            gameInfo()
            # running total of dammage done this turn
            hitDmg = 0
            # get player input
            print("What do you want to do?")
            playerIn = input("Attack (A) | Chase (C) | Run (R) | Weapon Info (I) | Wait (W) | Clear (CLS) | Quit (Q)" + "\n").lower()

            # When the player wants to attack
            if playerIn == "attack" or playerIn == "a":
                # if enemy is in range of the sword
                if Player.sword.inRange(distance):
                    # for the ammount of time the sword hits
                    for hit in list(range(Player.sword.multiHit)):
                        sleep(1)
                        hit = Player.sword.testHit()
                        # if they hit set hitDmg to regular hit dammage
                        if hit == "hit":
                            hitDmg = random.randint(Player.sword.dmgRange[0], Player.sword.dmgRange[1])
                            print(f"-You hit for {hitDmg} Dammage-")
                            # if they crit than use critical multiplyer
                        elif hit == "crit":
                            hitDmg = random.randint(Player.sword.dmgRange[0], Player.sword.dmgRange[1])
                            hitDmg *= Player.sword.critDmg
                            print(f"*-You Critical hit for {hitDmg} Dammage!-*")
                            # if they miss do nothing
                        elif hit == "miss":
                            print("-You Missed!-")
                        if Enemy.health - hitDmg < 0:
                            Enemy.health = 0
                        else:
                            Enemy.health -= hitDmg
                            # reset dammage for next hit
                            hitDmg = 0
                        # end player turn
                        playerTurn = False
                        # if enemy is in bow range and not sword range
                elif Player.bow.inRange(distance):
                    # for the ammount of times the bow hits
                    for hit in list(range(Player.bow.multiHit)):
                        sleep(1)
                        hit = Player.bow.testHit()
                        # if the bow hits add to hitDmg
                        if hit == "hit":
                            hitDmg = random.randint(Player.bow.dmgRange[0], Player.bow.dmgRange[1])
                            print(f"-You hit for {hitDmg} Dammage!-")
                            # if they crit than use critical multiplyer
                        elif hit == "crit":
                            hitDmg = random.randint(Player.bow.dmgRange[0], Player.bow.dmgRange[1])
                            hitDmg *= Player.bow.critDmg
                            print(f"-You Critical hit for {hitDmg} Dammage-")
                            # if they miss do nothing
                        elif hit == "miss":
                            print("-You Missed!-")
                        # deal dammage, but don't go below 0
                        if Enemy.health - hitDmg < 0:
                            Enemy.health = 0
                        else:
                            Enemy.health -= hitDmg
                        # reset dammage for next hit
                        hitDmg = 0
                    # end player turn
                    playerTurn = False
                    # say if enemy is not in range, let them pick again
                else:
                    print("-Enemy not in range!-")
            elif playerIn == "chase" or playerIn == "c":
                # reduce distance when you chase unless your too close
                if distance - Player.speed * 2 <= 1:
                    print("-Your can't get closer!-")
                    distance = 1
                else:
                    print("-You chase the enemy!-")
                    distance -= Player.speed * 2
                playerTurn = False
            elif playerIn == "run" or playerIn == "r":
                # Increase distance when you run
                print("-You run from the enemy!-")
                distance += Player.speed
                playerTurn = False
            elif playerIn == "weapon Info" or playerIn == "i":
                # Give information on your weapons and enemies weapons
                print("_"*20)
                print("Your Weapons:")
                sleep(1)
                weaponInfo(Player.sword)
                weaponInfo(Player.bow)
                print("_"*20)
                print("Enemy Weapons:")
                sleep(1)
                weaponInfo(Enemy.sword)
                weaponInfo(Enemy.bow)
            elif playerIn == "quit" or playerIn == "q":
                # Ends the game loop, quitting the game
                playing = False
                break
            elif playerIn == "wait" or playerIn == "w":
                # Skips your turn
                print("-You wait for the opponent-")
                print(Player.taunt(Enemy))
                playerTurn = False
            elif playerIn == "clear" or playerIn == "cls":
                # clear all text from terminal
                os.system('cls' if os.name == 'nt' else 'clear')
            # incase the player types something that is not accepted
            else:
                print("-Something went wrong-")

        # check if the game is over
        if checkWin():
            Player.gamesPlayed += 1
            break

        # Enemy turn logic
        while not playerTurn:
            gameInfo()
            # Add some random behavior to the enemy
            behaviorRandom = random.randint(1, 100)
            sleep(int(behaviorRandom/10))
            # 80% chance to not attack
            if Enemy.sword.inRange(distance) and behaviorRandom > 20:
                print("-The Enemy Attacks!-")
                sleep(1)
                # for the ammount of time the sword hits
                for hit in list(range(Enemy.sword.multiHit)):
                    sleep(1)
                    hit = Enemy.sword.testHit()
                    # if they hit set hitDmg to regular hit dammage
                    if hit == "hit":
                        hitDmg = random.randint(Enemy.sword.dmgRange[0], Enemy.sword.dmgRange[1])
                        print(f"-They hit for {hitDmg} Dammage-")
                    # if they crit than use critical multiplyer
                    elif hit == "crit":
                        hitDmg = random.randint(Enemy.sword.dmgRange[0], Enemy.sword.dmgRange[1])
                        hitDmg *= Enemy.sword.critDmg
                        print(f"*-They Critical hit for {hitDmg} Dammage!-*")
                # if they miss do nothing
                    elif hit == "miss":
                        print("-They Missed!-")
                # deal the dammage and reset dammage to zero for next turn
                if Player.health - hitDmg < 0:
                    Player.health = 0
                else:
                    Player.health -= hitDmg
                # reset dammage for next hit
                hitDmg = 0
                # end enemy turn
                playerTurn = True
            # 80% chance to not attack
            elif Enemy.bow.inRange(distance) and behaviorRandom > 20:
                print("-The Enemy Attacks!-")
                sleep(1)
                # for the ammount of times the bow hits
                for hit in list(range(Enemy.bow.multiHit)):
                    sleep(1)
                    hit = Enemy.bow.testHit()
                    # if the bow hits add to hitDmg
                    if hit == "hit":
                        hitDmg = random.randint(Enemy.bow.dmgRange[0], Enemy.bow.dmgRange[1])
                        print(f"-They hit for {hitDmg} Dammage!-")
                    # if they crit than use critical multiplyer
                    elif hit == "crit":
                        hitDmg = random.randint(Enemy.bow.dmgRange[0], Enemy.bow.dmgRange[1])
                        hitDmg *= Enemy.bow.critDmg
                        print(f"-They Critical hit for {hitDmg} Dammage-")
                    # if they miss do nothing
                    elif hit == "miss":
                        print("-They Missed!-")
                    # deal dammage and reset
                    if Player.health - hitDmg < 0:
                        Player.health = 0
                    else:
                        Player.health -= hitDmg
                    # reset dammage for next hit
                    hitDmg = 0
                # end enemy turn
                playerTurn = True
                # if they don't attack or can't attack, 10% chance they don't chase you
            elif distance > Enemy.bow.range[1] or (distance < Enemy.bow.range[0] and distance > Enemy.sword.range[1]) and behaviorRandom <= 90:
                print("-They Chase You!-")
                if distance - Enemy.speed * 2 < 1:
                    distance = 1
                    print("-Their in Your Face!-")
                else:
                    distance -= Enemy.speed * 2
                playerTurn = True
                # if they don't chase you, 5% chance they don't run
            elif behaviorRandom <= 95:
                print("-They Run From You!-")
                distance += Enemy.speed
                playerTurn = True
                # if they don't do anything, they 'wait'
            else:
                print("-They wait for you-")
                print(Enemy.taunt(Player))
                playerTurn = True

        # check if the game is over
        if checkWin():
            Player.gamesPlayed += 1
            break

    input("Press ENTER to end")

    Player.write()
    Player.read(True)

# main function
def main():
    '''
        Code for the main menu, also is the main function
    '''
    while True:
        # clear anything previously in the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # prints title in utils
        print(title)

        # get input
        select = input("(S) Start Game\n(H) Help\n(Q) Quit\n").lower()

        # do specified action
        if select == "s" or select == "start game":
            # clear anything previously in the terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            # Start the game
            playGame()
        elif select == "h" or select == "help":
            # clear anything previously in the terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print(title + help)
            input("ENTER to close help")
        elif select == "q" or select == "quit":
            break


if __name__ == '__main__':
    main()
