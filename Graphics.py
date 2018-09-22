import pygame

pygame.init()
pygame.font.init()
TEXTSIZE = 20
font = pygame.font.Font(None, TEXTSIZE)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (15,15,15)

class Box:
    def __init__(self, x, y, rect, width = 0):
        self.x = x
        self.y = y
        self.rect = rect
        self.width = width

    def adjust(self, newX, newY):
        self.x = newX
        self.y = newY

    def render(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    def getLocation(self):
        return (self.x, self.y)

class Text:
    def __init__(self, text):
        self.text = text
        self.color = BLACK
        self.txt_surface = font.render(text, True, self.color)

    def setText(self, newText):
        self.text = newText
        self.txt_surface = font.render(self.text, True, self.color)


    def getText(self):
        return self.text


class InputBox(Box, Text):
    def __init__ (self, x,y, w, h, text = '0'):
        Box.__init__(self, x, y, pygame.Rect(x, y, w, h))
        Text.__init__(self, text)
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



class OutputBox(Box, Text):
    def __init__ (self, x, y, w, h, text = '0'):
        Box.__init__(self, x, y, pygame.Rect(x, y, w, h), 1)
        Text.__init__(self, text)

    def update(self):
        width = self.txt_surface.get_width()+10
        self.rect.w = width

    def get_rect(self):
        return self.rect

    def render(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect, self.width)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class ScrollButton(Box):
    def __init__(self, x, y, modifying, direction = 1, w = 20, h = 20):
        Box.__init__(self, x, y, pygame.Rect(x, y, w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.direction = direction
        self.modifying = modifying
        if(direction > 0):
            self.triangle = [(self.x + (self.w / 2), self.y + (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + self.h - (self.h / 5)), (self.x + (self.w / 5), self.y + self.h - (self.h / 5))]
        else:
            self.triangle = [(self.x + self.w/2, self.y + self.h - (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + (self.h / 5)), (self.x + (self.w / 5), self.y + (self.h / 5))]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.modifying.setText(str(int(self.modifying.getText()) + self.direction))

    def render(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect, self.width)
        pygame.draw.polygon(screen, WHITE, self.triangle, self.width)

class UnderlineText(Box, Text):
    def __init__(self, x, y, text):
        Box.__init__(self, x,y, pygame.Rect(x, y, 15, TEXTSIZE))
        Text.__init__(self, text)
        self.x = x
        self.y = y
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
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = self.txt_surface.get_width()+10
        self.rect.w = width

    def render(self, screen):
        pygame.draw.line(screen, BLACK, (self.x, self.y + TEXTSIZE), (self.x + self.rect.w, self.y + TEXTSIZE))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class Section:
    def __init__(self, x, y, element):
        self.x = x
        self.y = y
        self.element = element

    def setLocation(self):
        for i in self.element:
            currentX, currentY = i.getLocation()
            i.adjust(currentX + self.x, currentY + self.y)

    def addElement(self, newElement):
        self.element.append(newElement)
        self.setLocation()

    def render(self, screen):
        for i in self.element:
            i.render(screen)