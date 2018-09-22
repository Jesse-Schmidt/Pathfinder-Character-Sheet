from Graphics import *

size = width, height = 800, 700


CharacterInfo = Section(10, 10)
Name = UnderlineText(0, 0, "Your Name")
Alignment = UnderlineText(10, 0, "Alignment")
Player = UnderlineText(150, 0, "Player")
CharacterInfo.addElement(Name)
CharacterInfo.addElement(Alignment)
CharacterInfo.addElement(Player)