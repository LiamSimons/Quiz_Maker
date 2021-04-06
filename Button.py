import pygame
from fonts import all_fonts


class Button():
    def __init__(self, color, circle, radius, x, y, width, height, text='', name=''):
        self.color = color
        self.circle = circle
        self.radius = radius
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.name = name

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            if not self.circle:
                pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 3)
            else:
                pygame.draw.circle(win, self.color, (self.x+self.width/2, self.y+self.height/2), self.radius+2, 3)
        else:
            if self.circle:
                pygame.draw.circle(win, self.color, (self.x+self.width/2, self.y+self.height/2), self.radius, 3)
            else:
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 3)

        if self.text != '':
            font = pygame.font.SysFont(all_fonts[6], 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def get_name(self):
        return self.name
