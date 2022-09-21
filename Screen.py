import pygame
import Consts
import TrashBin
import Heart
import Trash

screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))


def draw_screen_game(i):
    screen.fill((97, 224, 135))
    TrashBin.draw_all_trash_bins()
    Heart.draw_all_hearts()
    Trash.draw_trash(Trash.list_trash[i])
    pygame.display.update()


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.update()
    pygame.time.delay(1000)


def lost():
    draw_message(Consts.LOSE_MESSAGE, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION)


def win():
    draw_message(Consts.WIN_MESSAGE, Consts.WIN_FONT_SIZE,
                 Consts.WIN_COLOR, Consts.WIN_LOCATION)