import pygame
import os
import Screen
import Consts

heart1 = {
    "heart_pic": pygame.image.load(os.path.join("GamePics", "heart.png")),
    "heart_location": (10 * 10, 56 * 10)
}

heart2 = {
    "heart_pic": pygame.image.load(os.path.join("GamePics", "heart.png")),
    "heart_location": (14 * 10, 56 * 10)
}

heart3 = {
    "heart_pic": pygame.image.load(os.path.join("GamePics", "heart.png")),
    "heart_location": (18 * 10, 56 * 10)
}

list_hearts = [heart1, heart2, heart3]


def draw_heart(heart):
    heart_img = heart["heart_pic"]
    heart_final = pygame.transform.scale(heart_img, Consts.HEART_SIZE)
    Screen.screen.blit(heart_final, heart["heart_location"])


def draw_all_hearts():
    for heart in list_hearts:
        draw_heart(heart)


def delete_heart():
    if len(list_hearts) != 0:
        list_hearts.remove(-1)
    else:
        Screen.lost()
