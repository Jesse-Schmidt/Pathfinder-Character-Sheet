from Graphics import *
from Layout import *
import pygame, sys

pygame.init()
size = width, height = 800, 700
screen = pygame.display.set_mode((size))

frontSections = [CharacterInfo]
backSections = []
flip = False

flipButton = OutputBox(750,0, "FLIP")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flipButton.getRect().collidepoint(event.pos):
                flip = not flip

        if not flip:
            for section in frontSections:
                section.handle_event(event)
        else:
            for section in backSections:
                section.handle_event(event)

    screen.fill((255, 255, 255))
    flipButton.render(screen)
    if not flip:
        for section in frontSections:
            section.render(screen)
    else:
        for section in backSections:
            section.render(screen)

    pygame.display.flip()