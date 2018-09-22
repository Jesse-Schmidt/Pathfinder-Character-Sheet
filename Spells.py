class Spell:
    def __init__(self, name, school, level, saving_throw = [], damage = [], effect = "no effect"):
        self.name = name
        self.school = school
        self.level = level

    def getName(self):
        return self.name

    def getSchool(self):
        return self.school

    def getLevel(self):
        return self.level

    def getDamage(self):
        return self.damage

    def getEffect(self):
        return self.effect

    def getSave(self):
        return self.saving_throw

