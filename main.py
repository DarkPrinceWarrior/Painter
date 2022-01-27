from PIL import Image, ImageDraw

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import random

# Функция возвращающая маску предмета, рисует
def get_img():
    im = Image.new('1', (400, 400), color=0)
    draw = ImageDraw.Draw(im)
    for _ in range(random.randint(1, 4)):
        draw.polygon([random.randint(10, im.size[0]-10) for x in range(8)], fill=1)
    return np.array(im)



# Очень плохая функция генерирующая маршрут
def get_route(im):
    route = []
    # Точки обходятся сверху вниз, слева направо
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            # Если в точке есть предмет (маска == 1)- красит
            if im[x,y] == 1:
                status = 1
            else:
                status = 0
            # Координаты и статус записываются в маршрут
            route.append(
                {
                    'x': x,
                    'y': y,
                    'status': status
                }
            )
    return route


def count_n_plot(im_arr, route, plot=True):
    # Проверка и визуализация результата
    sec_mask = Image.new('1', (400, 400), color=0)  # Создается второе изображение аналогичного размера
    draw = ImageDraw.Draw(sec_mask)
    distance = 0  # Обнуляется счетчик пройденной дистанции
    prev_coords = (0, 0)  # Координаты руки в момент старта
    for step in route:
        # Для каждого шага по маршруту считается пройденная рукой дистанция
        distance += ((prev_coords[0] - step['x']) ** 2 + (prev_coords[1] - step['y']) ** 2) ** 0.5
        prev_coords = step['x'], step['y']
        # Если в маршруте указан статус 1 точка в текущих координатах закрашивается
        if step['status'] == 1:
            draw.line((prev_coords[1], prev_coords[0], step['y'], step['x']), fill=1)

    sec_arr = np.array(sec_mask)
    if plot:
        fig, axs = plt.subplots(figsize=(12, 9), ncols=3)
        axs[0].imshow(im_arr)
        axs[0].set_title('Изначальная маска')
        axs[1].imshow(sec_arr)
        axs[1].set_title('Закрашенная область')
        axs[2].imshow(im_arr ^ sec_arr)
        axs[2].set_title('Разница между областями')
        plt.show()

    return sec_arr, distance




if __name__ == '__main__':
    pass
