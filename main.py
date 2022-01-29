
from algTesting import testing
from fill_item import count_n_plot
from find_cont_coords import find_contours
from image_gen import get_img1, image_area_split1, get_img2, image_area_split2


if __name__ == '__main__':

    # простой консольный ввод, что мы в итоге хотим
    choice = input("Работаем с реальной каринкой - 1\n"
                   "Работаем с нарисованным многоугольником -2\n")


    if choice == "1":
        coord_contours = find_contours()

        image_array = get_img1(coord_contours)
        route = image_area_split1(image_array.copy())
    else:
        image_array = get_img2()
        route = image_area_split2(image_array.copy())


    # Производится проход по маршруту
    sec_arr, distance = count_n_plot(image_array, route,choice)

    print('Сделано шагов:', len(route))
    print('Нужно было закрасить:', image_array.sum())
    print('Пройденная дистанция:', round(distance))
    print('Количество промахов алгоритма:', (image_array ^ sec_arr).sum())
    print('Соотношение пройденной дистанции и закрашиваемой области:', round(distance / image_array.sum(), 2))

    # прогон несколько раз
    df = testing(choice)
    for i in range(len(df)):
        print(df.loc[i, "Steps"],
              df.loc[i, "Area"],
              df.loc[i, "Distance"],
              df.loc[i, "Misses"],
              df.loc[i, "Distance/Area"])

    print(df['Misses'].mean(), df['Distance/Area'].mean())



