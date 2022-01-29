from PIL import Image, ImageDraw

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def count_n_plot(im_arr, route,choice, plot=True):
    # Проверка и визуализация результата
    sec_mask = Image.new('1', (600, 600), color=0)
    # Создается второе изображение аналогичного размера
    draw = ImageDraw.Draw(sec_mask)
    distance = 0  # Обнуляется счетчик пройденной дистанции
    prev_coords = (0, 0)  # Координаты руки в момент старта
    for step in route:
        # Для каждого шага по маршруту считается пройденная рукой дистанция
        distance += ((prev_coords[0] - step['x']) ** 2 + (prev_coords[1] - step['y']) ** 2) ** 0.5
        prev_coords = step['x'], step['y']
        # Если в маршруте указан статус 1 точка в текущих координатах закрашивается
        if choice == "2":
            draw.line((prev_coords[1], prev_coords[0], step['y'], step['x']), fill=1)
        else:
            draw.point(xy=(step['y'], step['x']), fill=1)




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