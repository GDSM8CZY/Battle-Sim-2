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
          name {string} - custom name for the fighter
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

    def attack(self, target, distance):
        '''
        This is the code for testing for weapon hits and hurting the other fighter
        args:
            target {Fighter} - The other fighter being hit
            distance {int} - The distance between the target and the fighter
        return:
            {bool} - weather the enemy was in range or not
        '''
        # if target is in range of the sword
        if self.sword.inRange(distance):
            # set hitDmg to 0
            hitDmg = 0
            # for the ammount of time the sword hits
            for hit in list(range(self.sword.multiHit)):
                sleep(1)
                hit = self.sword.testHit()
                # if they hit set hitDmg to regular hit dammage
                if hit == "hit":
                    hitDmg = random.randint(self.sword.dmgRange[0], self.sword.dmgRange[1])
                    print(f"-{self.name} hit {target.name} for {hitDmg} Dammage-")
                    # if they crit than use critical multiplyer
                elif hit == "crit":
                    hitDmg = random.randint(self.sword.dmgRange[0], self.sword.dmgRange[1])
                    hitDmg *= self.sword.critDmg
                    print(f"*-{self.name} Critical hit {target.name} for {hitDmg} Dammage!-*")
                    # if they miss do nothing
                elif hit == "miss":
                    print(f"-{self.name} Missed!-")
                if target.health - hitDmg < 0:
                    target.health = 0
                else:
                    target.health -= hitDmg
            # return true because it hit
            return True
                # if target is in bow range and not sword range
        elif self.bow.inRange(distance):
            # set hitDmg to 0
            hitDmg = 0
            # for the ammount of times the bow hits
            for hit in list(range(self.bow.multiHit)):
                sleep(1)
                hit = self.bow.testHit()
                # if the bow hits add to hitDmg
                if hit == "hit":
                    hitDmg = random.randint(self.bow.dmgRange[0], self.bow.dmgRange[1])
                    print(f"-You hit for {hitDmg} Dammage!-")
                    # if they crit than use critical multiplyer
                elif hit == "crit":
                    hitDmg = random.randint(self.bow.dmgRange[0], self.bow.dmgRange[1])
                    hitDmg *= self.bow.critDmg
                    print(f"-You Critical hit for {hitDmg} Dammage-")
                    # if they miss do nothing
                elif hit == "miss":
                    print("-You Missed!-")
                # deal dammage, but don't go below 0
                if target.health - hitDmg < 0:
                    target.health = 0
                else:
                    target.health -= hitDmg
            # return that they hit
            return True
        # return false if their out of range
        else:
            return False

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
            f = open(f"{self.name}-stats", "x")
            # opens stats file if created
        except:
            f = open(f"{self.name}-stats", "w")

        # writes to stats file
        f.write(f"{self.gamesPlayed}\n{self.lastSword}\n{self.lastBow}")

    def read(self, display):
        # try and read stats from the file
        while True:
            try:
                f = open(f"{self.name}-stats", "r")
                self.gamesPlayed = int(f.readline())
                self.lastSword = f.readline()
                self.lastBow = f.readline()
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

# dictionary of all of the swords
swordsDict = {
    "short sword": Weapon(
        name= "Short Sword",
        dmgRange= (3, 5),
        range= (1, 3),
        critChance= 40,
        critDmg= 2,
        accuracy= 99,
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
        multiHit= 1
    ),
    "knuckles": Weapon(
        name= "Knuckles",
        dmgRange= (6, 7),
        range= (1, 2),
        critChance= 10,
        critDmg= 2,
        accuracy= 75,
        multiHit= 4
    ),
    "spear": Weapon(
        name= "Spear",
        dmgRange= (3, 4),
        range= (3, 5),
        critChance= 25,
        critDmg= 3,
        accuracy= 75,
        multiHit= 3
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
        critChance= 80,
        critDmg= 2,
        accuracy= 40,
        multiHit= 1
    ),
    "tomahawk": Weapon(
        name= "Tomahawk",
        dmgRange= (6, 8),
        range= (1, 6),
        critChance= 15,
        critDmg= 2,
        accuracy= 40,
        multiHit= 1
    ),
}
