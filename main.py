from PIL import Image, ImageDraw
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
from find_cont_coords import find_contours
import sys
from route_gen import get_route


# Функция возвращающая контуры маски предмета и
# рисует их маски на чистом фоне с заполнением
def get_img(contours):
    """ Возвращаем матрицу(растровое изображение)
    элементы которого - это значения 0 либо 255"""

    img_background2 = Image.new('1', (600, 600), color=0)
    draw = ImageDraw.Draw(img_background2)

    conts = []
    for i in contours[0]:
        conts.append(i[0])
    draw.polygon([(coords[0], coords[1]) for coords in conts], fill=1)

    plt.imshow(img_background2)
    plt.show()

    return np.array(img_background2)


def image_area_split(img):

    box_array = np.array([[0 for _ in range(20)] for _ in range(20)])

    routes = []
    for i in range(len(img) // 30):
        for j in range(len(img) // 30):

            x1, y1 = 30 * i, 30 * (i + 1)
            x2, y2 = 30 * j, 30 * (j + 1)

            img1 = img[x1:y1, x2:y2]
            if 1 in img1:
                points =[]
                for k in range(len(img1)):
                    for l in range(len(img1)):
                        if img1[k][l] == 1:
                            points.append({"x":k,"y":l})
                random_num = random.randint(0,len(points)-1)            
                routes.extend(get_route(img1,
                                        points[random_num]["x"],
                                        points[random_num]["y"],
                                        x1, x2))
                box_array[i][j] = 1

    img_background2 = Image.new('1', (600, 600), color=0)
    draw = ImageDraw.Draw(img_background2)

    # вторая координата - x, а первая y
    for xy in routes:
        draw.point(xy=(
        (xy['y'], xy['x'])
    ), fill='white')

    plt.imshow(img_background2)
    plt.show()


if __name__ == '__main__':
    coord_contours = find_contours()

    image_array = get_img(coord_contours)

    image_area_split(image_array)
