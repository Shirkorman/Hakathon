import Screen
import pygame
import Trash
import Consts
import Heart


def handle_user_events(trash):
    keys = pygame.key.get_pressed()
    if keys[Consts.LEFT_KEY]:
        trash = Trash.go_left(trash)
    elif keys[Consts.RIGHT_KEY]:
        trash = Trash.go_right(trash)
    return trash


def main():
    run = True
    pygame.init()
    i_random = Trash.i_rand(Trash.list_trash)
    Screen.draw_screen_game(i_random)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            Trash.list_trash[i_random] = handle_user_events(Trash.list_trash[i_random])
            if Trash.has_arrived(Trash.list_trash[i_random]):
                flag = Trash.is_touch_right(Trash.list_trash[i_random])
                if flag == False:
                    run = Heart.delete_heart()
                Trash.remove_from_trash(Trash.list_trash, i_random)
                if Trash.is_list_trash_empty():
                    Screen.win()
                    run = False
                i_random = Trash.i_rand(Trash.list_trash)
            Screen.draw_screen_game(i_random)

    pygame.quit()


if __name__ == '__main__':
    main()
