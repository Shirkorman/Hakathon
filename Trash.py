import Consts
import random
import TrashBin

dict_trash = {
    "type_trash": "",
    "place": (0, random.randrange(Consts.NUM_COL) * 10),
    "pic": ""
}


def go_down(trash, screen):
    row = trash["place"][0]
    col = trash["place"][1]
    if col + 1 < 21:
        trash = screen[row][col + 1]
    elif row + 4 == 48:
        trash = (row, col)
    return trash


def go_left(trash, screen):
    row = trash["place"][0]
    col = trash["place"][1]
    if row - 1 >= 0:
        trash = screen[row - 1][col]
    trash = go_down(trash, screen)
    return trash


def go_right(trash, screen):
    row = trash["place"][0]
    col = trash["place"][1]
    if row + 1 < 48:
        trash = screen[row + 1][col]
    elif col + 4 == 24:
        trash = (row, col)
    trash = go_down(trash, screen)
    return trash


def pic_rand(type_trash):
    if type_trash == Consts.PLASTIC:
        pic = list_pic[random.randrange(len(list_pic_plastic))]
        list_pic_plastic.pop(pic)
    elif type_trash == Consts.PAPER:
        pic = list_pic[random.randrange(len(list_pic_paper))]
        list_pic_paper.pop(pic)
    elif type_trash == Consts.GLASS:
        pic = list_pic[random.randrange(len(list_pic_glass))]
        list_pic_glass.pop(pic)
    return pic


def set_pic(type_trash):
    dict_trash["pic"] = pic_rand(type_trash)
    return dict_trash["pic"]


def five_type(type):
    list = []
    for i in range(5):
        dict_trash = {
            "type_trash": type,
            "place": (0, random.randrange(Consts.NUM_COL)),
            "pic": ""
        }
        dict_trash["pic"] = set_pic(dict_trash["type"])
        list.append(dict_trash)
    return list


def i_rand(list_trash):
    return random.randrange(len(list_trash))


def remove_from_trash(list_trash, i):
    list_trash.pop(i)


def is_touch_right(trash):
    row = trash["place"][0]
    col = trash["place"][1]
    if row + 3 == 470:
        if col >=0 and col <= 80:
            if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[0]):
                return True
        elif col >= 81 and col <= 160:
            if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[1]):
                return True
        elif col >= 161 and col <= 239:
            if TrashBin.is_trash_fit(trash, TrashBin.list_trash_bins[2]):
                return True
        return False
    return 0




list_pic_plastic = ["plastic_bag.png", "plastic_bottle1.png", "plastic_bottle2.png", "plastic_cup.png"]
list_pic_paper = ["paper_cups.png", "paper_envelope.png", "paper_newspaper.png", "paper_bag.png"]
list_pic_glass = ["glass_bottle1.png", "glass_bottle2.png", "glass_cup.png", "glass_jar.png"]

list_plastic = five_type(Consts.PLASTIC)
list_paper = five_type(Consts.PAPER)
list_glass = five_type(Consts.GLASS)
list_trash = list_plastic + list_paper +list_glass
