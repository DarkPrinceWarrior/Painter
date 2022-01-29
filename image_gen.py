import random

import numpy as np
from PIL import ImageDraw, Image

from route_gen import get_route



# Функция возвращающая контуры маски предмета и
# рисует их маски на чистом фоне с заполнением
def get_img1(contours):
    """ Возвращаем матрицу(растровое изображение)
    элементы которого - это значения 0 либо 255"""

    img_background2 = Image.new('1', (600, 600), color=0)
    draw = ImageDraw.Draw(img_background2)

    conts = []
    for i in contours[0]:
        conts.append(i[0])
    draw.polygon([(coords[0], coords[1]) for coords in conts], fill=1)

    # plt.imshow(img_background2)
    # plt.show()

    return np.array(img_background2)


# Функция возвращающая маску предмета, рисует
def get_img2():
    im = Image.new('1', (600, 600), color=0)
    draw = ImageDraw.Draw(im)
    for _ in range(random.randint(1, 4)):
        draw.polygon([random.randint(10,im.size[0]-10) for x in range(8)], fill=1)
    return np.array(im)


def image_area_split1(img):

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

    return routes


def image_area_split2(img):

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

    return routes