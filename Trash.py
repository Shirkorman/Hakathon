import Consts
import random
import TrashBin
import pygame
import os
import Screen


def create_screen():
    screen = []
    tuple_coordinates = []
    for row in range(Consts.SCREEN_WIDTH):
        for col in range(Consts.SCREEN_HEIGHT):
            tuple_coordinates.append((row, col))
        screen.append(tuple_coordinates)
        tuple_coordinates = []
    return screen


def go_down(trash):
    screen = create_screen()
    row = trash["trash_place"][0]
    col = trash["trash_place"][1]
    if col + 3 < 52:
        trash["trash_place"] = screen[row][col + 1]
    elif row + 3 == 27:
        trash["trash_place"] = (row, col)
    return trash


def go_left(trash):
    screen = create_screen()
    row = trash["trash_place"][0]
    col = trash["trash_place"][1]
    if row - 1 >= 0:
        trash["trash_place"] = screen[row - 1][col]
    trash = go_down(trash)
    return trash


def go_right(trash):
    screen = create_screen()
    row = trash["trash_place"][0]
    col = trash["trash_place"][1]
    if row + 3 < 27:
        trash["trash_place"] = screen[row + 1][col]
    elif col + 3 == 50:
        trash = (row, col)
    trash = go_down(trash)
    return trash



def set_pic(dict_trash):
    dict_trash["trash_pic"] = pic_rand(dict_trash["type_trash"])
    return dict_trash["trash_pic"]


def five_type(type, list_pic):
    list = []
    for i in range(5):
        dict_trash = {"type_trash": type,
                      "trash_place": (random.randrange(Consts.NUM_COL), 0),
                      "trash_pic":pygame.image.load(os.path.join("GamePics", list_pic[i]))}
        list.append(dict_trash)
    return list


def i_rand(list_trash):
    return random.randrange(len(list_trash))


def remove_from_trash(list_trash, i):
    list_trash.pop(i)


def is_list_trash_empty():
    if len(list_trash) > 0:
        return False
    return True

def has_arrived(trash):
    if trash["trash_place"][1] + 3 >= 47:
        return True
    return False

def is_touch_right(trash):
    print(trash["trash_place"])
    row = trash["trash_place"][0]
    col = trash["trash_place"][1]
    if row >=0 and row <= 8:
        if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[0]):
            return True
    elif row >= 9 and row <= 20:
         if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[1]):
              return True
    elif row >= 21 and row <= 26:
        if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[2]):
            return True
    return False


def draw_trash(trash):
    trash_img = trash["trash_pic"]
    trash_final = pygame.transform.scale(trash_img, Consts.TRASH_SIZE)
    Screen.screen.blit(trash_final, (trash["trash_place"][0] * 10, trash["trash_place"][1] * 10))


list_pic_plastic = ["plastic_bag.png", "plastic_bottle1.png", "plastic_bottle2.png", "plastic_cup.png",
                    "trash_plastic_bag.png"]
list_pic_paper = ["paper_cups.png", "paper_envelope.png", "paper_newspaper.png", "paper_paperbag.png", "paper_sheets.png"]
list_pic_glass = ["glass_bottle1.png", "glass_bottle2.png", "glass_cup.png", "glass_jar.png", "broken_glass.png"]

list_plastic = five_type(Consts.PLASTIC, list_pic_plastic)
list_paper = five_type(Consts.PAPER, list_pic_paper)
list_glass = five_type(Consts.GLASS, list_pic_glass)
list_trash = list_plastic + list_paper + list_glass
