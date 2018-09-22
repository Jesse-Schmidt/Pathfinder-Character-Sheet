class Weapon:
    def __init__(self, name, damageType, damage, size, range = 0, critRange = "20"):
        self.name = name
        self.damageType = damageType
        self.damage = damage
        self.size = size

    def getName(self):
        return self.name

    def getDamage(self):
        return (self.damage, self.damageType)

    def getRange(self):
        return self.range

    def getCritRange(self):
        return self.critRange

    def getSize(self):
        return self.size

class Armor:
    def __init__(self, name, bonus, spellPenalty):
        self.name = name
        self.bonus = bonus
        self.spellPenalty = spellPenalty

    def getName(self):
        return self.name

    def getBonus(self):
        return self.bonus

    def getSpellPenalty(self):
        return self.spellPenalty

shield = Armor("Buckler", 1, 5)