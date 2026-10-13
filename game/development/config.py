import pygame

WIDTH = 1200
HEIGHT = 700
FPS = 60

BACKGROUND = (25, 27, 35)
PANEL = (39, 42, 53)
PANEL_LIGHT = (50, 54, 68)

WHITE = (240, 240, 240)
GRAY = (170, 175, 185)
DARK_GRAY = (85, 90, 100)

GOLD = (220, 180, 80)
GREEN = (80, 170, 100)
RED = (190, 70, 70)
BLUE = (70, 120, 190)
BLUE_HOVER = (95, 150, 225)

WIN_PRESTIGE = 30
LOSE_SMUTA = 10

START_GRAIN = 10
START_MONEY = 10
START_LAND = 5
START_PEOPLE = 10
START_SMUTA = 0

KINGDOM_PANEL = pygame.Rect(30, 110, 300, 440)
PLAYER_PANEL_X = 880
PLAYER_PANEL_Y0 = 110
PLAYER_PANEL_W = 290
PLAYER_PANEL_H = 102
PLAYER_PANEL_STEP = 112

LOG_X = 370
LOG_Y = 160
LOG_LINE_H = 28
LOG_MAX = 10

title_font = None
header_font = None
text_font = None
small_font = None


def init_fonts():
    global title_font, header_font, text_font, small_font
    if not pygame.font.get_init():
        pygame.font.init()
    title_font = pygame.font.Font(None, 48)
    header_font = pygame.font.Font(None, 34)
    text_font = pygame.font.Font(None, 28)
    small_font = pygame.font.Font(None, 24)
