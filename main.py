import Screen
import pygame


def main():
    run = True
    pygame.init()
    Screen.draw_screen_game()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == '__main__':
    main()
