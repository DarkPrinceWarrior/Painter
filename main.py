from PIL import Image, ImageDraw
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random


def find_contours():

    img = cv2.imread('images/horseshoe.jpg')
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # threshold defined manually its up to image
    ret, thresh = cv2.threshold(img_gray, 169,255,0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contList = []
    max1_cont = 0

    # находим длину конутра рамки
    for i in contours:
        if max1_cont < len(i):
            max1_cont = len(i)

    print(max1_cont)
    for i in contours:
        # минимальное число - defined manually (чтобы не взять отдельно лежащие точки)
        # и исключаем рамку из контуров
        if 46 < len(i) < max1_cont:
            contList.append(i)

    cv2.drawContours(img,contList,-1,(255,0,0), thickness=3)

    cv2.imshow("result", img)
    cv2.imshow("result gray", img_gray)
    cv2.waitKey(0)



# Функция возвращающая контуры маски предмета и
# рисует их маски на чистом фоне с заполнением
def get_img():

    """ Возвращаем матрицу(растровое изображение)
    элементы которого - это значения 0 либо 255"""

    img_background = Image.new('1', (400, 400), color=0)
    draw = ImageDraw.Draw(img_background)
    img = plt.imread('images/horseshoe.jpg')
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))


    # for _ in range(random.randint(1, 4)):
    #     draw.polygon([random.randint(10, im.size[0]-10) for _ in range(8)], fill=1)

    plt.imshow(img)
    plt.show()
    return np.array(img)


if __name__ == '__main__':
    find_contours()

