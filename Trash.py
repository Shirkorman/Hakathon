import Consts
import random

dict_trash = {
    "type": "",
    "place": random.randrange(Consts.NUM_COL),
    "pic": ""
}


def go_down(trash, screen):
    row = trash[0]
    col = trash[1]
    if col + 1 < 21:
        trash = screen[row][col + 1]
    elif row + 4 == 48:
        trash = (row, col)
    return trash


def go_left(trash, screen):
    row = trash[0]
    col = trash[1]
    if row - 1 >= 0:
        trash = screen[row - 1][col]
    trash = go_down(trash, screen)
    return trash


def go_right(trash, screen):
    row = trash[0]
    col = trash[1]
    if row + 1 < 48:
        trash = screen[row + 1][col]
    elif col + 4 == 24:
        trash = (row, col)
    trash = go_down(trash, screen)
    return trash


def pic_rand(type):
    if type == Consts.PLASTIC:
        list_pic = ["plastic_bag.png", "plastic_bottle1.png", "plastic_bottle2.png", "plastic_cup.png"]
        pic = list_pic[random.randrange(len(list_pic))]
    elif type == Consts.PAPER:
        list_pic = ["paper_cups.png", "paper_envelope.png", "paper_newspaper.png", "paper_bag.png"]
        pic = list_pic[random.randrange(len(list_pic))]
    elif type == Consts.GLASS:
        list_pic = ["glass_bottle1.png", "glass_bottle2.png", "glass_cup.png", "glass_jar.png"]
        pic = list_pic[random.randrange(len(list_pic))]
    return pic


def set_pic(type):
    dict_trash["pic"] = pic_rand(type)
    return dict_trash["pic"]


def set_type(type):
    dict_trash["type"] = type


def five_type(type):
    list = []
    for i in range(5):
        dict_trash = {
            "type": type,
            "place": random.randrange(Consts.NUM_COL),
            "pic": ""
        }
        dict_trash["pic"] = set_pic(dict_trash["type"])
        list.append(dict_trash)
    return list


def i_rand(list_trash):
    return random.randrange(len(list_trash))


def remove_from_trash(list_trash, i):
    list_trash.pop(i)


list_plastic = five_type(Consts.PLASTIC)
list_paper = five_type(Consts.PAPER)
list_glass = five_type(Consts.GLASS)
list_trash = list_plastic + list_paper +list_glass
