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