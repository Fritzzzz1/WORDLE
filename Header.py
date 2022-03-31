from typing import List
import pygame
import random
import sys
from pygame.locals import *

from Letter_state import LetterState
from Wordle import Wordle

white = (255, 255, 255)
yellow = (255, 255, 102)
green = (50, 255, 50)
grey = (211, 211, 211)
black = (0, 0, 0)
light_green = (140, 255, 102)
red = (255, 0, 0)
blue = (0, 0, 255)

SQUARE_SIZE = 50
BLOCK_SIZE = 80
X_MARGIN = 60
Y_MARGIN = 50
LINE_THICKNESS = 3

height = 600
width = 500
fps = 30

WINDOW_BOTTOM = (0, 500, 500, 200)
WINDOW_BOTTOM_RIGHT = (350, 530)
WINDOW_TYPE_LOCATION = (180, 530)
WINDOW_ENDGAME_PROMPT = (108, 168)
WINDOW_AGAIN_PROMPT = (75, 328)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
