from Race import *
from Class import *
from Feats import *
from Skills import *
from Equipment import *

class Character:
    def __init__(self):
        self.characterClass = determineClass(input("what class would you like to be? \n").lower())
        self.characterRace = determineRace(input("what race would you like to be? \n").lower())
        self.armor = [shield]
        self.weapons = []
        self.inventory = []
        self.AC = 10
        self.money = {"Bronze" : 0, "Silver" : 0, "Gold" : 0, "Platinum" : 0}
        self.initiative = self.characterRace.getModifiers()["DEX"]
        self.HP = 0

    def getClass(self):
        return self.characterClass

    def getRace(self):
        return self.characterRace

    def setAC(self):
        self.AC = 10 + self.characterRace.getModifiers()["DEX"]
        for item in self.armor:
            self.AC += item.getBonus()

    def getAC(self):
        return self.AC

    def getMoney(self):
        return self.money

    def addMoney(self, amount, moneyType):
        self.money[moneyType] += amount

    def getIniative(self):
        return self.initiative

    def getHP(self):
        return self.HP

    def setUpSkills(self):
        oldSkills = self.characterClass.getSkills()

