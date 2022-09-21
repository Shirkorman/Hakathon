import pygame
import os
import Screen
import Consts

purple_trash_bin = {
    "trash_bin_pic": pygame.image.load(os.path.join("GamePics", "purple_trashbin.png")),
    "trash_bin_location": (0, 41 * 10),
    "trash_bin_type": Consts.GLASS

}

blue_trash_bin = {
    "trash_bin_pic": pygame.image.load(os.path.join("GamePics", "blue_trashbin.png")),
    "trash_bin_location": ((8 + 4) * 10, 41 * 10),
    "trash_bin_type": Consts.PEPER
}

orange_trash_bin = {
    "trash_bin_pic": pygame.image.load(os.path.join("GamePics", "orange_trashbin.png")),
    "trash_bin_location": ((16 + 8) * 10, 41 * 10),
    "trash_bin_type": Consts.PLASTIC
}

list_trash_bins = [purple_trash_bin, blue_trash_bin, orange_trash_bin]


def draw_trash_bin(trash_bin):
    trash_bin_img = trash_bin["trash_bin_pic"]
    trash_bin_final = pygame.transform.scale(trash_bin_img, Consts.TRASH_BIN_SIZE)
    Screen.screen.blit(trash_bin_final, trash_bin["trash_bin_location"])


def draw_all_trash_bins():
    for trash_bin in list_trash_bins:
        draw_trash_bin(trash_bin)


def is_trash_fit(trash, trash_bin):
    if trash_bin["trash_bin_type"] == trash["trash_type"]:
        return True
    else:
        return False

