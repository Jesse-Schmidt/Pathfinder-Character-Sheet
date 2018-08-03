import pygame, sys
from Sheet import *

pygame.init()
size = (700, 800)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 17)

front = pygame.image.load("Character sheet front.jpg")
back = pygame.image.load("Character sheet back.jpg")
front = pygame.transform.scale(front, size)
back = pygame.transform.scale(back, size)




class InputBox:
    def __init__ (self, x, y, w, h, text = '0'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0,0,0)
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = self.txt_surface.get_width()+10
        self.rect.w = width

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

def main():
    FLIP = InputBox(size[0]-50, 0, 20, 20, "FLIP")
    STR = InputBox(95, 124, 30, 15)
    STR_MOD = InputBox(126, 124, 30, 15)
    DEX = InputBox(95, 142, 30, 15)
    DEX_MOD = InputBox(126, 142, 30, 15)
    CON = InputBox(95, 160, 30, 15)
    CON_MOD = InputBox(126, 160, 30, 15)
    INT = InputBox(95, 178, 30, 15)
    INT_MOD = InputBox(126, 178, 30, 15)
    WIS = InputBox(95, 196, 30, 15)
    WIS_MOD = InputBox(126, 196, 30, 15)
    CHA = InputBox(95, 214, 30, 15)
    CHA_MOD = InputBox(126, 214, 30, 15)
    input_boxes_front = [FLIP, STR, STR_MOD, DEX, DEX_MOD, CON, CON_MOD, INT, INT_MOD, WIS, WIS_MOD, CHA, CHA_MOD]
    input_boxes_back = [FLIP]
    done = False
    sides = [front, back]
    pick = 0
    screen.blit(front, front.get_rect())

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if FLIP.get_rect().collidepoint(event.pos):
                    if pick == 0:
                        pick = 1
                    else:
                        pick = 0

            if pick == 0:
                for box in input_boxes_front:
                    box.handle_event(event)
            else:
                for box in input_boxes_back:
                    box.handle_event(event)

        if pick == 0:
            for box in input_boxes_front:
                box.update()
        else:
            for box in input_boxes_back:
                box.update()

        screen.fill((255,255,255))
        screen.blit(sides[pick], sides[pick].get_rect())
        if pick == 0:
            for box in input_boxes_front:
                box.draw(screen)
        else:
            for box in input_boxes_back:
                box.draw(screen)

        pygame.display.flip()


main()
pygame.quit()