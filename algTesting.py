import pandas as pd

from fill_item import count_n_plot
from find_cont_coords import find_contours
from image_gen import get_img, image_area_split
from route_gen import get_route


def testing(option):

    n_steps = 10

    df = pd.DataFrame(columns=['Steps', 'Area', 'Distance', 'Misses', 'Distance/Area'],
                      index=range(n_steps))

    # Алгоритм прогоняется несколько раз
    # результаты записываются в датафрейм
    coord_contours = list()
    for i in range(n_steps):

        if option == 1:
            coord_contours = find_contours()

        im = get_img(coord_contours, option)

        route, box_route = image_area_split(im.copy())
        sec_arr, distance = count_n_plot(im, route, option, plot=False)
        df.iloc[i]['Steps'] = len(route)
        df.iloc[i]['Area'] = im.sum()
        df.iloc[i]['Distance'] = distance
        df.iloc[i]['Misses'] = (im ^ sec_arr).sum()
        df.iloc[i]['Distance/Area'] = round(distance / im.sum(), 2)

    return df