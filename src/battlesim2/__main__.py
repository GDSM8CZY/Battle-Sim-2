import os
import pygame
import random
from time import sleep

from importlib.resources import files

from battlesim2.core import Fighter, swordsDict, bowsDict, armorDict, weaponInfo, armorInfo
from battlesim2.utils import listToMatrix, title, help

# intialize pygame
# not sure if it needs to be done here
pygame.init()

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
    swordsMatrix = listToMatrix(list(swordsDict), 4)
    bowsMatrix = listToMatrix(list(bowsDict), 4)
    armorMatrix = listToMatrix(list(armorDict), 4)

    # clear anything previously in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Selection for sword
    print("Pick your sword!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for sword in swordsMatrix[page]:
            # index for each swords and the swords info
            print(swordsMatrix[page].index(sword)+1)
            printInfo(swordsDict[sword])
        # shows the different pages
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
            # try to use a number
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                swordSelect = int(swordSelect)
                swordSelect = swordsDict[swordsMatrix[page][swordSelect-1]]
                print(f"=-{swordSelect.name} Selected-=\n")
                break
            # if there is a value error
            except ValueError:
                # try to check the key
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    swordSelect = swordsDict[swordSelect]
                    print(f"=-{swordSelect.name} Selected-=\n")
                    break
                # if there is a key error loop again
                except KeyError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("-Something went wrong, try again!-\n")




    # Selection for bow
    print("Pick your bow!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for bow in bowsMatrix[page]:
            print(bowsMatrix[page].index(bow)+1)
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
            # select bow on input
            # try to use a number
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                bowSelect = int(bowSelect)
                bowSelect = bowsDict[bowsMatrix[page][bowSelect-1]]
                print(f"=-{bowSelect.name} Selected-=\n")
                break
            # if there is a value error
            except ValueError:
                # try to check the key
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bowSelect = bowsDict[bowSelect]
                    print(f"=-{bowSelect.name} Selected-=\n")
                    break
                # if there is a key error loop again
                except KeyError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("-Something went wrong, try again!-\n")

    # Selection for armor
    print("Pick your armor!")
    sleep(1)
    page = 0
    while True:
        # print outs the page
        for armor in armorMatrix[page]:
            print(armorMatrix[page].index(armor)+1)
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
            # select armor on input
            # try to use a number
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                armorSelect = int(armorSelect)
                armorSelect = armorDict[armorMatrix[page][armorSelect-1]]
                print(f"=-{armorSelect.name} Selected-=\n")
                break
            # if there is a value error
            except ValueError:
                # try to check the key
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    armorSelect = armorDict[armorSelect]
                    print(f"=-{armorSelect.name} Selected-=\n")
                    break
                # if there is a key error loop again
                except KeyError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("-Something went wrong, try again!-\n")

    # gives player the selected weapons
    global Player, Enemy

    # gets the path to player sprite and creates the player
    playerSprite = files("battlesim2").joinpath("assets", "Player.png")
    Player = Fighter(swordSelect, bowSelect, armorSelect, playerName, str(playerSprite))

    # gives enemies random weapons
    enemySprite = files("battlesim2").joinpath("assets", "Enemy.png")
    Enemy = Fighter("", "", "", enemyName, str(playerSprite))

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
    swordsMatrix = listToMatrix(list(swordsDict), 5)
    bowsMatrix = listToMatrix(list(bowsDict), 5)
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
    # Assign the weapons to the fighters
    assignWeapons("Player", "Enemy")

    # variables needed to start the game
    global distance, playerTurn, playing
    distance = 20
    playerTurn = True
    playing = True


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
            # if they don't attack or can't attack, 10% chance they don't chase you
            elif not inRange and behaviorRandom <= 90:
                print("-They Chase You!-")
                if distance - Enemy.speed < 1:
                    distance = 1
                    print("-Their in Your Face!-")
                else:
                    distance -= Enemy.speed
                playerTurn = True
                # if they don't chase you, 5% chance they don't run
            elif behaviorRandom <= 95:
                print("-They Run From You!-")
                distance += Enemy.speed
                playerTurn = True
                # if they don't do anything, they 'wait' or fail to run
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


# main function
def main():
    '''
        Code for the main menu, also is the main function
    '''

    # true if game is running
    running = True

    # make a pygame screen  and font that are global
    global screen, font
    screen = pygame.display.set_mode((1280, 640))
    font = pygame.font.SysFont(None, 10)

    # get BG and set to 5x scale
    background = files("battlesim2").joinpath("assets", "BG_lonePeak.png")
    background = pygame.image.load(str(background))
    background = pygame.transform.scale(background, (
                                        background.get_width() * 4,
                                        background.get_height() * 4))

    # create buttons
    startBtn = pygame.Rect(640, 110, 150, 50)
    helpBtn = pygame.Rect(640, 180, 150, 50)
    weaponInfoBtn = pygame.Rect(640, 250, 150, 50)
    quitBtn = pygame.Rect(640, 320, 150, 50)

    while running:
        # Put the background on the screen
        screen.blit(background, (0, 0))

        # draw the start button
        pygame.draw.rect(screen, (150, 150, 25), startBtn)
        startText = font.render("Start", True, (255, 255, 255))
        screen.blit(startText, (startBtn.x + 20, startBtn.y + 20))

        # draw the help button
        pygame.draw.rect(screen, (150, 150, 25), helpBtn)
        helpText = font.render("Help", True, (255, 255, 255))
        screen.blit(helpText, (helpBtn.x + 20, helpBtn.y + 20))

        # draw the wepon info button
        pygame.draw.rect(screen, (150, 150, 25), weaponInfoBtn)
        weaponInfoText = font.render("Weapon Info", True, (255, 255, 255))
        screen.blit(weaponInfoText, (weaponInfoBtn.x + 20, weaponInfoBtn.y + 20))

        # draw the quit button
        pygame.draw.rect(screen, (150, 150, 25), quitBtn)
        quitText = font.render("Quit", True, (255, 255, 255))
        screen.blit(quitText, (quitBtn.x + 20, quitBtn.y + 20))

        # flip display
        pygame.display.flip()

        # check events
        for event in pygame.event.get():

            # quit when window is closed
            if event.type == pygame.QUIT:
                running = False

            # detect clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # clicked on start btn?
                if startBtn.collidepoint(event.pos):
                    # clear anything previously in the terminal
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Start the game
                    playGame()

                if quitBtn.collidepoint(event.pos):
                    running = False

#         # do specified action
#         if select == "s" or select == "start game":
#             # clear anything previously in the terminal
#             os.system('cls' if os.name == 'nt' else 'clear')
#             # Start the game
#             playGame()
#         elif select == "h" or select == "help":
#             # clear anything previously in the terminal
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(title + help)
#             input("Press ENTER to close help")
#         elif select == "i" or select == "weapon info":
#             # clear anything previously in the terminal
#             os.system('cls' if os.name == 'nt' else 'clear')
#             # Show all the weapons
#             showAllWeapons()
#         elif select == "q" or select == "quit":
#             break


if __name__ == '__main__':
    main()
