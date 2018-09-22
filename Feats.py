class Feat:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def getName(self):
        return self.name

    def getEffect(self):
        return self.getEffect()

Low_Light_Vision = Feat("Low-Light Vision", "can see twice as far in dim light")
Elven_Immunities = Feat("Elven Immunities", ["immune to magic sleep effects", "+2 saving throw bonus against enchantment spells and effects"])
