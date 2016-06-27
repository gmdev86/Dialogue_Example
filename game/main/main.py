import pygame
import sys
from pygame.locals import *
from Dialogue import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
font_size = 20
font_name = "comicsansms"
dialogue_rect = pygame.Rect(20, 384, 600, 240)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

DISPLAYSURF.fill(BLACK)
o_dialogue = Dialogue(font_name, font_size, WHITE, DISPLAYSURF)
o_rect = o_dialogue.display_dialogue(dialogue_rect, None, None, None, None)
lines = o_dialogue.wrapline("Now is the time for all good men to come to the aid of their country",
                            dialogue_rect.width - 10, None)
counter = 0
for line in lines:
    o_dialogue.display_text_animation(o_rect, line, counter, None, None, None, None)
    counter += font_size

pygame.display.update()
main()
