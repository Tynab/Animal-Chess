import pygame
from enum import Enum, auto
from pygame import image, transform

pygame.init()

_screen = pygame.display.set_mode(Game.SIZE.value)

pygame.display.set_caption(Game.TITLE.value)

_clock = pygame.time.Clock()

_current_player = PlayerLabel.DARK