from Graphics import *
import pygame, sys

pygame.init()
size = width, height = 800, 700
screen = pygame.display.set_mode((size))

inputs = []
inputs.append(InputBox(20,20,50,25, "yes"))
outputs = []
outputs.append(OutputBox(40,40,50,25, "5"))
clickers = []
clickers.append(ScrollButton(80, 80, outputs[0], -1))
clickers.append(ScrollButton(60,60, outputs[0]))
underlines = []
underlines.append(UnderlineText(100,100, "this is a sentence"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for x in inputs:
            x.handle_event(event)
        for y in underlines:
            y.handle_event(event)
        for z in clickers:
            z.handle_event(event)

    screen.fill((255, 255, 255))
    for w in underlines:
        w.update()
        w.render(screen)
    for x in inputs:
        x.update()
        x.render(screen)
    for y in outputs:
        y.update()
        y.render(screen)
    for z in clickers:
        z.render(screen)
    pygame.display.flip()