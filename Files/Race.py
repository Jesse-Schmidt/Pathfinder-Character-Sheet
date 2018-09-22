def determineRace(race):
    if race == "human":
        return Human()
    elif race == "elf":
        return Elf()
    elif race == "dwarf":
        return Dwarf()

class Race:
    def __init__(self):
        self.attributes = {"STR" : 10, "DEX": 10, "CON" : 10, "INT" : 10, "WIS" : 10, "CHA" : 10}
        self.speed = 30
        self.languages = ["Common"]
        self.size = 'M'
        self.feats = []
        self.modifiers = {}


    def getAttributes(self):
        return self.attributes

    def getModifiers(self):
        return self.modifiers

    def setAttributes(self):
        self.attributes["STR"] = int(input("What is your strength ability score? \n"))
        self.attributes["DEX"] = int(input("What is your dexterity ability score? \n"))
        self.attributes["CON"] = int(input("What is your constitution ability score? \n"))
        self.attributes["INT"] = int(input("What is your intelligence ability score? \n"))
        self.attributes["WIS"] = int(input("What is your wisdom ability score? \n"))
        self.attributes["CHA"] = int(input("What is your charisma ability score? \n"))
        self.calculateModifiers()

    def calculateModifiers(self):
        for score in self.attributes:
            self.modifiers[score] = int((self.attributes[score] - 10)/2)

    def addFeats(self, newFeat):
        self.feats.append(newFeat)

class Human(Race):
    def __init__(self):
        super().__init__()
        increase = input("What ability score would you like to increase? \n").upper()[0:3]
        self.attributes[increase] = self.attributes[increase] + 2
        self.calculateModifiers()


class Elf(Race):
    def __init__(self):
        super().__init__()
        self.languages.append("Elven")
        self.attributes["DEX"] = self.attributes["DEX"] + 2
        self.attributes["INT"] = self.attributes["INT"] + 2
        self.attributes["CON"] = self.attributes["CON"] - 2
        self.calculateModifiers()


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.attributes["CON"] = self.attributes["CON"] + 2
        self.attributes["WIS"] = self.attributes["WIS"] + 2
        self.attributes["CHA"] = self.attributes["CHA"] - 2
        self.calculateModifiers()
