import random

import numpy as np
from PIL import ImageDraw, Image

from route_gen import get_route


# Функция возвращающая контуры маски предмета и
# рисует их маски на чистом фоне с заполнением
def get_img(contours, option):
    """ Возвращаем матрицу(растровое изображение)
    элементы которого - это значения 0 либо 255"""

    imgage = Image.new('1', (600, 600), color=0)
    draw = ImageDraw.Draw(imgage)

    if option == 1:
        conts = []
        for i in contours[0]:
            conts.append(i[0])
        draw.polygon([(coords[0], coords[1]) for coords in conts], fill=1)
        return np.array(imgage)

    else:
        for _ in range(random.randint(1, 4)):
            draw.polygon([random.randint(10, imgage.size[0] - 10) for _ in range(8)], fill=1)
        return np.array(imgage)


def image_area_split(img):
    # Матрица изображния, элемент которой - это растр 30 на 30
    # Значение 1 = закрашивем область, 0 - нет соответственно
    box_array = np.array([[0 for _ in range(20)] for _ in range(20)])

    coord_list = []  # интерпретация матрицы выше только в виде списка
    for i in range(len(img) // 30):
        for j in range(len(img) // 30):

            slice1X, slice1Y = 30 * i, 30 * (i + 1)
            slice2X, slice2Y = 30 * j, 30 * (j + 1)

            img1 = img[slice1X:slice1Y, slice2X:slice2Y]
            if 1 in img1:
                box_array[i][j] = 1
                coord_list.append([i, j])

    # Рандомный проход по маске при закрашивании
    Random_coords = random.choice(coord_list)
    route_box = get_route(box_array.copy(), Random_coords[0], Random_coords[1], 0, 0)

    image_detailed_routes = []
    points = []
    for coord_offset in route_box:
        slice1X, slice1Y = 30 * coord_offset["x"], 30 * (coord_offset["x"] + 1)
        slice2X, slice2Y = 30 * coord_offset["y"], 30 * (coord_offset["y"] + 1)

        img1 = img[slice1X:slice1Y, slice2X:slice2Y]
        # check if there is unpainted area in the square of 30x30
        while img1.sum() != 0:
            points.clear()
            for k in range(len(img1)):
                for l in range(len(img1)):
                    if img1[k][l] == 1:
                        points.append({"x": k, "y": l})
            points_length = len(points) - 1
            random_coord = random.randint(0, points_length)
            image_detailed_routes.extend(get_route(img1,
                                                   points[random_coord]["x"],
                                                   points[random_coord]["y"],
                                                   slice1X, slice2X))
        points.clear()


    # print(box_array)
    # print(image_detailed_routes)
    return image_detailed_routes, route_box
