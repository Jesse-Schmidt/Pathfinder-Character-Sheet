from Race import *

from Old.Skills import *


def determineClass(classType):
    classes = {"fighter": Fighter()}
    return classes[classType]

class Class:
    def __init__(self):
        self.BAB = 0
        self.fortitude = 0
        self.reflex = 0
        self.will = 0
        self.skills = [Acrobatics, Appraise, Bluff, Climb, Craft, Diplomacy, Disable_Device,
                       Disguise, Escape_Artist, Fly, Handle_Animal, Heal, Intimidate, Knowledge,
                       Linguistics, Perception, Preform, Profession, Ride, Sense_Motive,
                       Sleight_Of_Hand, Spellcraft, Stealth, Survival, Swim, Use_Magic_Device]
        self.addedSpeed = 0
        self.proficientWeapons = []
        self.hitDice = 0

    def getBAB(self):
        return self.BAB

    def getFortitude(self):
        return self.fortitude

    def getWill(self):
        return self.will

    def getSkills(self):
        return self.skills

    def getAddedSpeed(self):
        return self.addedSpeed

    def getProficientWeapons(self):
        return self.proficientWeapons

    def getHitDice(self):
        return self.hitDice

    def setSkills(self, newSkills):
        self.skills = newSkills

class Fighter (Class):
    def __init__(self):
        super().__init__()
        self.classSkills = [Climb, Craft, Handle_Animal, Intimidate, Ride, Survival, Swim]
        for skill in self.skills:
            if skill in self.classSkills:
                skill.setTrained()
            if skill == Knowledge:
                for subject in Knowledge:
                    if subject.getName() == "Knowledge(Dungeoneering)" or subject.getName() == "Knowledge(Engineering)":
                        subject.setTrained()
            if skill == Profession:
                for type in Profession:
                    type.setTrained()

