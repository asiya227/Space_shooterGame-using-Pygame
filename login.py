import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Login System")

class TextInput:
    def __init__(self, x, y, width, height, font, font_color, active_color, inactive_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.font_color = font_color
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.text = ""
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
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        def draw(self, screen):
            color = self.active_color if self.active else self.inactive_color
            pygame.draw.rect(screen, color, self.rect, 2)
            text_surface = self.font.render(self.text, True, self.font_color)
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

username_input = TextInput(300, 200, 200, 30, pygame.font.Font(None, 30), (255, 255, 255), (255, 255, 255), (200, 200, 200))
password_input = TextInput(300, 300, 200, 30, pygame.font.Font(None, 30), (255, 255, 255), (255, 255, 255), (200, 200, 200))


def render_login_page():
    login_page = pygame.image.load("login_page.png")  # Replace "login_page.png" with your own image file
    login_page = pygame.transform.scale(login_page, (800, 600))
    screen.blit(login_page, (0, 0))
    pygame.display.flip()

render_login_page()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pygame.display.update()

pygame.quit()
