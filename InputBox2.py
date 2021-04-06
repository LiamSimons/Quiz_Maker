import pygame
from fonts import all_fonts
# import time

pygame.init()
pygame.key.set_repeat(500, 50)

FONT = pygame.font.SysFont(all_fonts[6], 30)

COLOR_INACTIVE = (0, 0, 0)
COLOR_ACTIVE = (176, 217, 235)


class InputBox:

    def __init__(self, x, y, w, h, head, text='', head_text=''):
        self.color = COLOR_INACTIVE
        self.x = x
        self.y = y
        self.w = w
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        txt_surface_h = self.txt_surface.get_height()
        self.h = h + txt_surface_h
        self.rect = pygame.Rect(x, y, w, self.h)
        self.active = False
        self.head = head
        self.head_text = head_text
        self.head_surface = FONT.render(head_text, True, self.color)
        # self.time = 0
        # self.timer = False
        # self.line_active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                # self.time = time.time()  # x is the time when you press enter
                # self.timer = True
            else:
                self.active = False
            # self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                # if event.key == pygame.K_RETURN:
                # print(self.text)
                # self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_SPACE:
                    pass
                else:
                    if len(self.text) < 50:
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, COLOR_INACTIVE)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # if self.timer:
        #    if self.active and (time.time() - self.time) % 1 == 0:
        #        self.line_active = not self.line_active
        if self.active:
            line = '|'
            line_surface = FONT.render(line, True, COLOR_INACTIVE)
            screen.blit(line_surface, (self.rect.x + self.txt_surface.get_width() + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        if self.head:
            screen.blit(self.head_surface, (self.rect.x-self.head_surface.get_width()+5, self.rect.y+5))

    def get_text(self):
        return self.text

    def toggle_active(self):
        self.active = not self.active

    def get_active(self):
        return self.active
