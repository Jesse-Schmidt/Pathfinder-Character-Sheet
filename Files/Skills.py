class Skill:
    def __init__(self, name, abilityNeeded, abilityModifier = 0, trained = False, ranks = 0, misc = []): #misc = [(value, reason)]
        self.name = name
        self.abilityNeeded = abilityNeeded
        self.bonus = 0

    def calculate(self):
        self.bonus = self.ranks + self.abilityModifier
        for entry in self.misc:
            self.bonus += entry[0]
        if self.trained:
            self.bonus += 3

    def addRanks(self):
        self.ranks += 1
        self.calculate()

    def setTrained(self):
        self.trained = True

    def getBonus(self):
        return self.bonus

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAbilityNeeded(self):
        return self.abilityNeeded

    def setAbilityModifier(self, modifier):
        self.abilityModifier = modifier
        self.calculate()

    def addMisc(self, newMisc):
        self.misc.append(newMisc)
        self.calculate()

    def getMisc(self):
        return self.misc

    def info(self):
        print(self.name + " " + str(self.bonus) + " "  + self.abilityNeeded + " " + str(self.ranks) + " " + self.addMisc())


Acrobatics = Skill("Acrobatics", "DEX")
Appraise = Skill("Appraise", "INT")
Bluff = Skill("Bluff", "CHA")
Climb = Skill("Climb", "STR")
Craft = [Skill("Craft ___", "INT"), Skill("Craft ___", "INT"), Skill("Craft ___", "INT")]
Diplomacy = Skill("Diplomacy", "CHA")
Disable_Device = Skill("Disable Device", "DEX")
Disguise = Skill("Disguise", "CHA")
Escape_Artist = Skill("Escape Artist", "DEX")
Fly = Skill("Fly", "DEX")
Handle_Animal = Skill("Handle Animal", "CHA")
Heal = Skill("Heal", "WIS")
Intimidate = Skill("Intimidate", "CHA")
Knowledge = [Skill("Knowledge(Arcana)", "INT"), Skill("Knowledge(Dungeoneering)", "INT"),
             Skill("Knowledge(Engineering)", "INT"), Skill("Knowledge(Geography)", "INT"),
             Skill("Knowledge(History)", "INT"), Skill("Knowledge(Local)", "INT"),
             Skill("Knowledge(Nature)", "INT"), Skill("Knowledge(Nobility)", "INT"),
             Skill("Knowledge(Planes)", "INT"), Skill("Knowledge(Religion)", "INT")]
Linguistics = Skill("Linguistics", "INT")
Perception = Skill("Perception", "WIS")
Preform = [Skill("Preform ___", "CHA"), Skill("Preform ___", "CHA")]
Profession = [Skill("Profession ___", "WIS"), Skill("Profession ___", "WIS")]
Ride = Skill("Ride", "DEX")
Sense_Motive = Skill("Sense Motive", "WIS")
Sleight_Of_Hand = Skill("Sleight of Hand", "DEX")
Spellcraft = Skill("Spellcraft", "INT")
Stealth = Skill("Stealth", "DEX")
Survival = Skill("Survival", "WIS")
Swim = Skill("Swim", "STR")
Use_Magic_Device = Skill("Use Magic Device", "CHA")