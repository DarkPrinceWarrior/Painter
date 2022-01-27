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


if __name__ == '__main__':
    pass
