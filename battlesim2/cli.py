import os
import random
from time import sleep

from battlesim2.core import Fighter, swordsDict, bowsDict, armorDict, weaponInfo, armorInfo
from battlesim2.utils import listToMatrix, title, help




# Prints all the info for the game
def gameInfo():
    '''
      prints out all the information for the current game state
      args:
        none
      return:
        none
    '''
    print(f"{Player.name} gear")
    Player.fighterInfo()
    print(f"{Enemy.name} gear")
    Enemy.fighterInfo()
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

# print weapon info
def printInfo(obj):
    '''
    Take a weapon or armor object and prints it's info
    args
        obj {Weapon} or {Armor} - object that is being inspected
    return:
        none
    '''
    if type(obj) == type(swordsDict['short sword']):
        print("\n".join(weaponInfo(obj)))
    else:
        print("\n".join(armorInfo(obj)))


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
        # clear anything previously in the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
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
        # clear anything previously in the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
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
    swordsMatrix = listToMatrix(list(swordsDict), 3)
    bowsMatrix = listToMatrix(list(bowsDict), 3)
    armorMatrix = listToMatrix(list(armorDict), 3)

    # clear anything previously in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Selection for sword
    print("Pick your sword!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for sword in swordsMatrix[page]:
            printInfo(swordsDict[sword])
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
            printInfo(bowsDict[bow])
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

    # Selection for armor
    print("Pick your armor!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for armor in armorMatrix[page]:
            printInfo(armorDict[armor])
        print(f"<Pg{page + 1}/{len(armorMatrix)}>")
        armorSelect = input().lower()
        # logic for changeing pages
        if armorSelect == ">" and page < len(armorMatrix) - 1:
            page += 1
            os.system('cls' if os.name == 'nt' else 'clear')
        elif armorSelect == "<" and page > 0:
            page -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            # select sword on input
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                armorSelect = armorDict[armorSelect]
                print(f"=-{armorSelect.name} Selected-=\n")
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-Something went wrong, try again!-\n")

    # gives player the selected weapons
    global Player, Enemy
    Player = Fighter(swordSelect, bowSelect, armorSelect, playerName)
    Player.read(False)

    # gives enemies random weapons
    Enemy = Fighter("", "", "", enemyName)

# shows all the weapons
def showAllWeapons():
    '''
    Shows all of the current weapons in pages, first swords then bows
    args:
        none
    return:
        none
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    # convert swordsDict and bowsDict to marticies
    swordsMatrix = listToMatrix(list(swordsDict), 4)
    bowsMatrix = listToMatrix(list(bowsDict), 4)
    armorMatrix = listToMatrix(list(armorDict), 5)
    page = 0

    # print all swords
    while True:
        print("-SWORDS-")
        for sword in swordsMatrix[page]:
            printInfo(swordsDict[sword])

        playerIn = input(f"<{page+1}/{len(swordsMatrix)}>\n(N) Next\n").lower()

        if playerIn == "n" or playerIn == "next":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif playerIn == "<" and page > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            page -= 1
        elif playerIn == ">" and page < len(swordsMatrix) - 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            page += 1

    page = 0
    while True:
        print("-BOWS-")
        for bow in bowsMatrix[page]:
            printInfo(bowsDict[bow])

        playerIn = input(f"<{page+1}/{len(bowsMatrix)}>\n(N) Next\n").lower()

        if playerIn == "n" or playerIn == "next":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif playerIn == "<" and page > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            page -= 1
        elif playerIn == ">" and page < len(bowsMatrix) - 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            page += 1

    page = 0
    while True:
        print("-ARMOR-")
        for armor in armorMatrix[page]:
            printInfo(armorDict[armor])

        playerIn = input(f"<{page+1}/{len(armorMatrix)}>\n(N) Next\n").lower()

        if playerIn == "n" or playerIn == "next":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif playerIn == "<" and page > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            page -= 1
        elif playerIn == ">" and page < len(armorMatrix) - 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            page += 1


    

def playGame():
    '''
        The game loop along with some setup
        args:
            none
        return:
            none
    '''
    # TEMPORARYLY REMOVED
    # pick a name for you and the enemy
    # print("_" * 20)
    # enemyname = input("what is the enemy called?\n")
    # playername = input("and what are you called?\n")
    # if enemyname == "": enemyname = "enemy"
    # if playername == "": playername = "player"
    # print("_" * 20, "\n")

    # Assign the weapons to the fighters
    assignWeapons("Player", "Enemy")

    # variables needed to start the game
    global distance, playerTurn, playing
    distance = 20
    playerTurn = True
    playing = True

    # Code inspired by my Python 1 project 'Battle Sim'
    # This is the game loop
    while playing:
        # Player turn actions
        while playerTurn:
            gameInfo()
            # get player input
            print("What do you want to do?")
            playerIn = input("Attack (A) | Chase (C) | Run (R) | Wait (W) | Quit (Q)" + "\n").lower()

            # When the player wants to attack
            if playerIn == "attack" or playerIn == "a":
                # attack the enemy
                inRange = Player.attack(Enemy, distance)
                # it was in range end turn
                if inRange:
                    playerTurn = False
                    break
                # else tell the player
                else:
                    print("-Enemy not in range!-")
            elif playerIn == "chase" or playerIn == "c":
                # reduce distance when you chase unless your too close
                if distance - Player.speed <= 1:
                    print("-Your can't get closer!-")
                    distance = 1
                else:
                    print("-You chase the enemy!-")
                    distance -= Player.speed
                playerTurn = False
            elif playerIn == "run" or playerIn == "r":
                # Increase distance when you run
                if random.randint(1, 2) == 1:
                    print("-You run from the enemy!-")
                    distance += Player.speed
                else:
                    print("-You tried to run away!-")
                playerTurn = False
            elif playerIn == "quit" or playerIn == "q":
                # Ends the game loop, quitting the game
                playing = False
                break
            elif playerIn == "wait" or playerIn == "w":
                # Skips your turn
                print("-You wait for the opponent-")
                print(Player.taunt(Enemy))
                playerTurn = False
            # incase the player types something that is not accepted
            else:
                print("-Something went wrong-")

        # check if the game is over
        if checkWin():
            Player.gamesPlayed += 1
            break

        if playing:
            input("Press ENTER to continue")
        # Clear the sceren after the turn
        os.system('cls' if os.name == 'nt' else 'clear')

        # Enemy turn logic
        while not playerTurn:
            gameInfo()
            # Add some random behavior to the enemy
            behaviorRandom = random.randint(1, 100)
            sleep(int(behaviorRandom/10))
            # attack the player
            inRange = Enemy.attack(Player, distance)
            # if in range, end turn
            if inRange:
                playerTurn = True
                break
            # if they don't attack or can't attack, 20% chance they don't chase you
            elif not inRange and behaviorRandom <= 80:
                print("-They Chase You!-")
                if distance - Enemy.speed < 1:
                    distance = 1
                    print("-Their in Your Face!-")
                else:
                    distance -= Enemy.speed
                playerTurn = True
                # if they don't chase you, 10% chance they don't run
            elif behaviorRandom <= 90:
                print("-They Run From You!-")
                distance += Enemy.speed
                playerTurn = True
                # if they don't do anything, they 'wait'
            else:
                if random.randint(1, 2) == 1:
                    print("-They wait for you-")
                    print(Enemy.taunt(Player))
                    playerTurn = True
                else:
                    print("-They tried to run away!-")
                    playerTurn = True

        # check if the game is over
        if checkWin():
            Player.gamesPlayed += 1
            break

        if playing:
            input("Press ENTER to continue")
        # Clear the sceren after the turn
        os.system('cls' if os.name == 'nt' else 'clear')

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
        select = input("(S) Start Game\n(H) Help\n(I) Weapon Info\n(Q) Quit\n").lower()

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
            input("Press ENTER to close help")
        elif select == "i" or select == "weapon info":
            # clear anything previously in the terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            # print title
            print(title)
            # Show all the weapons
            showAllWeapons()
        elif select == "q" or select == "quit":
            break


if __name__ == '__main__':
    main()
