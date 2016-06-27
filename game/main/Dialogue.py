import pygame
import sys
from pygame.locals import *
from pygame import gfxdraw
from itertools import chain


class Dialogue(object):

    def __init__(self, font_name, font_size, font_color, display_surface):
        self.__font = pygame.font.SysFont(font_name, font_size)
        self.__font_color = font_color
        self.__surface = display_surface
        self.__BLACK = (0, 0, 0)
        self.__WHITE = (255, 255, 255)
        self.__dia_background_color = (0, 0, 100, 127)
        self.__boarder_width = 3
        self.__text_offset = 10
        self.__text_speed = 100

    def get_background_color(self):
        return self.__dia_background_color

    def get_surface(self):
        return self.__surface

    def get_color_white(self):
        return self.__WHITE

    def get_boarder_width(self):
        return self.__boarder_width

    def get_font(self):
        return self.__font

    def get_text_offset(self):
        return self.__text_offset

    def get_text_delay(self):
        return self.__text_speed

    def display_dialogue(self, dia_rect, display_surface=None, bg_color=None,
                         boarder_color=None, boarder_width=None):
        if display_surface is None:
            display_surface = self.get_surface()
        if bg_color is None:
            bg_color = self.get_background_color()
        if boarder_color is None:
            boarder_color = self.get_color_white()
        if boarder_width is None:
            boarder_width = self.get_boarder_width()

        pygame.gfxdraw.box(display_surface, dia_rect, bg_color)
        pygame.draw.rect(display_surface, boarder_color, dia_rect, boarder_width)
        pygame.display.update()
        return dia_rect

    def display_text_animation(self, v_rect, string, v_counter, display_surface=None,
                               font_color=None, offset=None,
                               text_speed=None):
        if display_surface is None:
            display_surface = self.get_surface()
        if font_color is None:
            font_color = self.get_color_white()
        if offset is None:
            offset = self.get_text_offset()
        if text_speed is None:
            text_speed = self.get_text_delay()

        text = ''
        for i in range(len(string)):
            text += string[i]
            text_surface = self.get_font().render(text, True, font_color)
            text_rect = text_surface.get_rect()
            text_rect.x = v_rect.x
            text_rect.y = v_rect.y
            text_rect.width = v_rect.width
            text_rect.height = v_rect.height
            text_rect.center = (v_rect.centerx + offset, v_rect.centery + v_counter)
            display_surface.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(text_speed)

    def truncline(self, text, maxwidth, font=None):
        if font is None:
            font = self.get_font()

        real = len(text)
        stext = text
        l = font.size(text)[0]
        cut = 0
        a = 0
        done = 1
        old = None
        while l > maxwidth:
            a = a + 1
            n = text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext = n[:-cut]
            else:
                stext = n
            l = font.size(stext)[0]
            real = len(stext)
            done = 0
        return real, done, stext

    def wrapline(self, text, maxwidth, font=None):
        if font is None:
            font = self.get_font()

        done = 0
        wrapped = []

        while not done:
            nl, done, stext = self.truncline(text, maxwidth, font)
            wrapped.append(stext.strip())
            text = text[nl:]
        return wrapped

    def wrap_multi_line(self, text, maxwidth, font=None):
        """ returns text taking new lines into account.
        """
        if font is None:
            font = self.get_font()

        lines = chain(*(self.wrapline(line, maxwidth, font) for line in text.splitlines()))
        return list(lines)
