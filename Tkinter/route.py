import random
from tkinter import *

from algTesting import testing
from fill_item import count_n_plot
from find_cont_coords import find_contours
from image_gen import image_area_split, get_img
from route_gen import get_route

Windows_width = 700
Windows_height = 700
Space_size = 30
Color_body = "#0f1ab2"
Color_head = "#241ffc4"
BACKGROUND_COLOR = 'black'
Box_color = "#ff42d0"
# для юзера установить 150/160

Speed = 80

def move(canvas,window,coord_list,index):

    if index > len(coord_list)-1:
        return
    else:
        x = coord_list[index]["y"] * Space_size
        y = coord_list[index]["x"] * Space_size
        canvas.create_rectangle(x, y, x + Space_size, y + Space_size, fill=Box_color)

    window.after(Speed, move,canvas,window,coord_list,index+1)


def application(option):
    window = Tk()
    window.title('Маршрутизация')
    window.resizable(False, False)
    label = Label(window, text="Маршрутизация руки по покраске фигуры", font=('Arial', '20'))
    label.pack()
    canvas = Canvas(window, height=Windows_height, width=Windows_width, bg=BACKGROUND_COLOR)
    canvas.pack()
    button = Button(window, text="Показать детали маршрута", font=('Arial', '15'))
    button.pack()
    window.geometry('700x800')  # Размер окна

    coord_contours = list()
    if option == 1:
        coord_contours = find_contours()

    image_array = get_img(coord_contours, option)
    image_detailed_routes, route_box = image_area_split(image_array.copy())

    index = 0
    move(canvas, window,route_box,index)

    window.mainloop()

    # Производится проход по маршруту
    sec_arr, distance = count_n_plot(image_array, image_detailed_routes, option)
    print('Сделано шагов:', len(image_detailed_routes))
    print('Нужно было закрасить:', image_array.sum())
    print('Пройденная дистанция:', round(distance))
    print('Количество промахов алгоритма:', (image_array ^ sec_arr).sum())
    print('Соотношение пройденной дистанции и закрашиваемой области:', round(distance / image_array.sum(), 2))


    # прогон несколько раз
    df = testing(option)
    for i in range(len(df)):
        print(df.loc[i, "Steps"],
              df.loc[i, "Area"],
              df.loc[i, "Distance"],
              df.loc[i, "Misses"],
              df.loc[i, "Distance/Area"])

    print(df['Misses'].mean(), df['Distance/Area'].mean())
