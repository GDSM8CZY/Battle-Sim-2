# @title Battle Sim 2 code
import os
import random
from time import sleep


# Class for all of the weapons
class Weapon():
    def __init__(self, name, dmgRange, range, critChance, critDmg, accuracy, multiHit):
        '''
        defines variables for weapons
        args
          name {string} - name of the weapon
          dmgRange {list} - has the low and high end for dammage
          range {list} - has the low and high end for the distance where the weapon can hit
          critChance {integer} - percent chance for weapon to critical hit
          critDmg {integer} - percent extra dammage critical hits do
          accuracy {integer} - percent chance the weapon hits the opponent
          multiHit {integer} - the ammount of times the weapon will attempt to attack the enemy
        returns:
          none
        '''
        self.name = name
        self.dmgRange = dmgRange
        self.range = range
        self.critChance = critChance
        self.critDmg = critDmg
        self.accuracy = accuracy
        self.multiHit = multiHit

    def inRange(self, distance):
        '''
        checks if a certain distance is in range
        args:
          distance {integer} - the distance we want to check if its in range
        return:
          weather the distance is in range or not as a bool
        '''
        return distance >= self.range[0] and distance <= self.range[1]

    def testHit(self):
        '''
        Checks if a weapon "miss", "hit", or "crit"
        args:
          none
        return:
          A string either "miss", "hit", or "crit"
        '''
        if random.randint(1, 100) <= self.accuracy:
            if random.randint(1, 100) <= self.critChance:
                return "crit"
            else:
                return "hit"
        else:
            return "miss"


# Class for the player and enemy
class Fighter():
    def __init__(self, sword, bow, name):
        '''
        initializes variables for fighters
        args:
          sword {Weapon} - the sword this fighter will use
          bow {Weapon} - the bow this fighter will use
        return:
          none
        '''
        # used in the game stats
        self.sword = sword
        self.bow = bow
        self.name = name
        self.health = 20
        self.speed = 1
        # account stats
        self.gamesPlayed = 0
        self.lastSword = self.sword
        self.lastBow = self.bow

    def randomWeapons(self):
        '''
        sets random weapons for the fighter
        args:
          none
        return:
          none
        '''
        # select random sword
        _, self.sword = get_random_item(swordsDict)

        # find all bows with no overlapping range with the sword
        possibleBows = []
        for bow in list(bowsDict):
            if bowsDict[bow].range[0] >= self.sword.range[1]:
                possibleBows.append(bow)

        # selects a random bow
        self.bow = bowsDict[random.choice(possibleBows)]

        # gives random bow if there is no bow selected
        if not isinstance(self.bow, Weapon):
            _, self.bow = get_random_item(bowsDict)

    # Taunts made by chatGPT
    # code made by me
    def taunt(self, target):
        # Nice (playful, cheeky) taunts using f-strings
        nice_taunts = [
            f"Is that your best move, {target.name}, or are you just warming up?",
            f"Come on, {target.name}, I know you can hit harder than that!",
            f"You swing like my grandma, {target.name}—and she’s got better footwork!",
            f"That was cute, {target.name}. Do it again so I can laugh harder."
        ]

        # Mean (cutting, aggressive) taunts using f-strings
        mean_taunts = [
            f"You call *that* a punch, {target.name}? My sleep hits harder.",
            f"You're not even worth the energy it takes to dodge, {target.name}.",
            f"This is getting sad, {target.name}. Want me to call your mom?",
            f"You should’ve stayed home, {target.name}. This isn’t your league."
        ]

        # return a random taunt
        for taunt in random.choice([nice_taunts, mean_taunts]):
            if random.randint(1, 100) <= 10:
                return f"{self.name}: {taunt}"

        # if no taunt is selected return this
        return f"{self.name}: ..."

    def write(self):
        # creats stats file if not already created
        try:
            f = open(f"~/BattleSim2-stats{self.name}-stats", "x")
            # opens stats file if created
        except:
            f = open(f"~/BattleSim2-stats{self.name}-stats", "w")

        # writes to stats file
        f.write(f"{self.gamesPlayed}\n{self.lastSword}\n{self.lastBow}")

    def read(self, display):
        # try and read stats from the file
        while True:
            try:
                f = open(f"~/BattleSim2-stats{self.name}-stats", "r")
                self.gamesPlayed = int(f.readline())
                break
            except:
                self.write()

        if display:
            print(f"Games Played: {self.gamesPlayed}")


# funciton from google gemini
def get_random_item(my_dict):
    '''
      Gets a random key-value pair from a dictionary
      args:
        my_dict {dictionary} - The dictionary to select a random item
      return:
        the key as a string and the value in the dict
      '''
    if not my_dict:
        return None

    random_key = random.choice(list(my_dict))
    return random_key, my_dict[random_key]


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

def listToMatrix(list, col):
    '''
    Takes a list and return a matrix
    args:
        list {list} - this will be returned as a matrix
        col {int} - the number of columns in the matrix
    return:
        {list} - a matrix with the specified number of columns
    '''
    rows = (len(list) + col - 1) // col
    matrix = []
    for i in range(rows):
        start = i * col
        end = min(start + col, len(list))
        matrix.append(list[start:end])
    return matrix


# main function
def main():
    # dictionary of all of the swords
    swordsDict = {
        "short sword": Weapon(
            name= "Short Sword",
            dmgRange= (3, 5),
            range= (1, 3),
            critChance= 50,
            critDmg= 2,
            accuracy= 90,
            multiHit= 2
        ),
        "claymore": Weapon(
            name= "Claymore",
            dmgRange= (4, 5),
            range= (1, 5),
            critChance= 20,
            critDmg= 3,
            accuracy= 65,
            multiHit= 1
        ),
        "dagger": Weapon(
            name= "Dagger",
            dmgRange= (4, 5),
            range= (1, 2),
            critChance= 80,
            critDmg= 2,
            accuracy= 90,
            multiHit= 4
        ),
        "knuckles": Weapon(
            name= "Knuckles",
            dmgRange= (6, 7),
            range= (1, 2),
            critChance= 10,
            critDmg= 2,
            accuracy= 90,
            multiHit= 1
        ),
    }

    # dictionary of all of the bows
    bowsDict = {
        "hunting bow": Weapon(
            name= "Hunting Bow",
            dmgRange= (1, 3),
            range= (5, 8),
            critChance= 30,
            critDmg= 2,
            accuracy= 50,
            multiHit= 3
        ),
        "crossbow": Weapon(
            name= "Crossbow",
            dmgRange= (5, 6),
            range= (8, 10),
            critChance= 50,
            critDmg= 2,
            accuracy= 80,
            multiHit= 1
        ),
        "revolver": Weapon(
            name= "Revolver",
            dmgRange= (2, 3),
            range= (5, 10),
            critChance= 25,
            critDmg= 2,
            accuracy= 30,
            multiHit= 6
        ),
        "slingshot": Weapon(
            name= "Slingshot",
            dmgRange= (5, 7),
            range= (3, 6),
            critChance= 75,
            critDmg= 3,
            accuracy= 40,
            multiHit= 1
        ),
        "tomahawk": Weapon(
            name= "Tomahawk",
            dmgRange= (6, 8),
            range= (1, 6),
            critChance= 10,
            critDmg= 3,
            accuracy= 40,
            multiHit= 1
        ),

    }

    # clear anything previously in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII font from https://www.asciiart.eu/
    title = '''
    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
    ██████╔╝███████║   ██║      ██║   ██║     █████╗
    ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝
    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝

    ███████╗██╗███╗   ███╗    ██████╗
    ██╔════╝██║████╗ ████║    ╚════██╗
    ███████╗██║██╔████╔██║     █████╔╝
    ╚════██║██║██║╚██╔╝██║    ██╔═══╝
    ███████║██║██║ ╚═╝ ██║    ███████╗
    ╚══════╝╚═╝╚═╝     ╚═╝    ╚══════╝
    ___________________________________________________
    How to play:
    - Type in the option you want to select
    - When fighting you can type the shortcuts in parentheses '()'
    - Defeat the enemy before they defeat you!
    - You can cycle through pages with "<" or ">"
    ___________________________________________________
    '''

    print(title)

    sleep(1)

    # pick a name for you and the enemy
    print("_" * 20)
    enemyName = input("What is the Enemy called?\n")
    playerName = input("And what are you called?\n")
    if enemyName == "": enemyName = "Enemy"
    if playerName == "": playerName = "Player"
    print("_" * 20, "\n")


    swordsMatrix = listToMatrix(list(swordsDict), 2)
    bowsMatrix = listToMatrix(list(bowsDict), 2)


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
        elif swordSelect == "<" and page > 0:
            page -= 1
        else:
            # select sword on input
            try:
                swordSelect = swordsDict[swordSelect]
                print(f"=-{swordSelect.name} Selected-=\n")
                break
            except:
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
        elif bowSelect == "<" and page > 0:
            page -= 1
        else:
            # select sword on input
            try:
                bowSelect = bowsDict[bowSelect]
                print(f"=-{bowSelect.name} Selected-=\n")
                break
            except:
                print("-Something went wrong, try again!-\n")


    # gives player the selected weapons
    Player = Fighter(swordSelect, bowSelect, playerName)
    Player.read(False)

    # gives enemies random weapons
    Enemy = Fighter(swordsDict["short sword"], bowsDict["hunting bow"], enemyName)
    Enemy.randomWeapons()

    # variables needed to start the game
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
            playerIn = input("Attack (A) | Chase (C) | Run (R) | Weapon Info (I) | Wait (W) | Quit (Q)" + "\n").lower()

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
            # incase the player types something that is not accepted
            else:
                print("-Something went wrong, be careful typing it is case sensitive!-")

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

    Player.write()
    Player.read(True)

    input("press ENTER to end program ")

if __name__ == '__main__':
    main()
