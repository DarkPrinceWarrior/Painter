import pandas as pd

from fill_item import count_n_plot
from find_cont_coords import find_contours
from image_gen import get_img1, image_area_split1, get_img2
from route_gen import get_route


def testing(choice):

    n_steps = 10

    df = pd.DataFrame(columns=['Steps', 'Area', 'Distance', 'Misses', 'Distance/Area'],
                      index=range(n_steps))

    # Алгоритм прогоняется несколько раз
    # результаты записываются в датафрейм
    for i in range(n_steps):

        if choice == "2":
            im = get_img2()
        else:
            coord_contours = find_contours()
            im = get_img1(coord_contours)

        route = image_area_split1(im.copy())
        sec_arr, distance = count_n_plot(im, route,1, plot=False)
        df.iloc[i]['Steps'] = len(route)
        df.iloc[i]['Area'] = im.sum()
        df.iloc[i]['Distance'] = distance
        df.iloc[i]['Misses'] = (im ^ sec_arr).sum()
        df.iloc[i]['Distance/Area'] = round(distance / im.sum(), 2)

    return df