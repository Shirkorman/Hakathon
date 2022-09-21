import pygame
import Consts
import TrashBin

screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))


def init_screen():
    screen.fill((0, 0, 0))
    TrashBin.draw_all_trash_bins()
    pygame.display.update()