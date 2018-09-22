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

    def getRect(self):
        return self.rect

    def update(self, x, y):
        self.x = x
        self.y = y
        width = self.txt_surface.get_width()+10
        self.rect.w = width
        self.rect.x = self.x
        self.rect.y = self.y

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
    def __init__ (self, x, y, text = '0'):
        Box.__init__(self, x, y, pygame.Rect(x, y, 15, TEXTSIZE))
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

    def get_rect(self):
        return self.rect

    def render(self, screen):
        self.update(self.x, self.y)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class OutputBox(Box, Text):
    def __init__ (self, x, y, text = '0'):
        Box.__init__(self, x, y, pygame.Rect(x, y, 15, TEXTSIZE), 1)
        Text.__init__(self, text)

    def get_rect(self):
        return self.rect

    def render(self, screen):
        self.update(self.x, self.y)
        pygame.draw.rect(screen, BLACK, self.rect, self.width)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class ScrollButton(Box):
    def __init__(self, x, y, modifying, direction = 1, w = 10, h = 10):
        Box.__init__(self, x, y, pygame.Rect(x, y, w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.direction = direction
        self.modifying = modifying
        if direction > 0:
            self.triangle = [(self.x + (self.w / 2), self.y + (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + self.h - (self.h / 5)), (self.x + (self.w / 5), self.y + self.h - (self.h / 5))]
        else:
            self.triangle = [(self.x + self.w/2, self.y + self.h - (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + (self.h / 5)), (self.x + (self.w / 5), self.y + (self.h / 5))]

    def update(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        if self.direction > 0:
            self.triangle = [(self.x + (self.w / 2), self.y + (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + self.h - (self.h / 5)), (self.x + (self.w / 5), self.y + self.h - (self.h / 5))]
        else:
            self.triangle = [(self.x + self.w/2, self.y + self.h - (self.h / 5)), (self.x + self.w - (self.w / 5), self.y + (self.h / 5)), (self.x + (self.w / 5), self.y + (self.h / 5))]


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.modifying.setText(str(int(self.modifying.getText()) + self.direction))

    def render(self, screen):
        self.update(self.x, self.y)
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

    def render(self, screen):
        self.update(self.x, self.y)
        pygame.draw.line(screen, BLACK, (self.x, self.y + TEXTSIZE), (self.x + self.rect.w, self.y + TEXTSIZE))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class Section:
    def __init__(self, x, y, elements = []):
        self.x = x
        self.y = y
        self.elements = elements

    def render(self, screen):
        for i in self.elements:
            i.render(screen)

    def settle(self):
        for first in range(len(self.elements)):
            count = first
            first = self.elements[first]
            for second in range(count, len(self.elements)):
                second = self.elements[second]
                firstX, firstY = first.getLocation()
                firstW = first.getRect().w
                secondX, secondY = second.getLocation()
                secondW = second.getRect().w
                if firstY != secondY and abs(firstY - secondY) < TEXTSIZE:
                    secondY = firstY
                elif firstY != secondY and abs(firstY - secondY) > TEXTSIZE and firstY < secondY:
                    secondY = firstY + round(((secondY - firstY) / TEXTSIZE)) * TEXTSIZE
                elif firstY != secondY and abs(firstY - secondY) > TEXTSIZE and firstY > secondY:
                    firstY = secondY + round(((firstY - secondY) / TEXTSIZE)) * TEXTSIZE

                if firstY == secondY:
                    if firstX < secondX and (firstX + firstW + 25) > secondX:
                        secondX = firstX + firstW + 25
                    elif secondX < firstX and (secondX + secondW + 25) > firstX:
                        firstX = secondX + secondW + 25
                first.update(firstX, firstY)
                second.update(secondX, secondY)

    def addElement(self, newElement):
        currentX, currentY = newElement.getLocation()
        newElement.update(currentX + self.x, currentY + self.y)
        self.elements.append(newElement)
        self.settle()

    def handle_event(self, event):
        for first in range(len(self.elements)):
            count = first
            first = self.elements[first]
            if type(first) is not OutputBox:
                first.handle_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    for second in range(count, len(self.elements)):
                        second = self.elements[second]
                        firstX, firstY = first.getLocation()
                        secondX, secondY = second.getLocation()
                        if first != second and secondY == firstY:
                            secondX = secondX - 10
                            second.update(secondX, secondY)
                self.settle()