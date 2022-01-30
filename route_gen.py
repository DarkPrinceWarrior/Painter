

def get_route(im, x, y, offsetX, offsetY):
    route = []
    width = len(im)
    height = len(im[0])

    def fill(x, y, start_color, color_to_update):
        # if the square is not the same color as the starting point
        if im[x][y] != start_color:
            return
        # if the square is not the new color
        elif im[x][y] == color_to_update:
            return
        else:
            # update the color of the current square to the replacement color
            im[x][y] = color_to_update
            route.append(
                {
                    'x': x+offsetX,
                    'y': y+offsetY
                }
            )
            neighbors = [(x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1),
                         (x, y - 1), (x, y + 1)]

            for n in neighbors:
                if 0 <= n[0] <= width - 1 and 0 <= n[1] <= height - 1:
                    fill(n[0], n[1], start_color, color_to_update)

    start_x = x
    start_y = y
    start_color = True
    fill(start_x, start_y, start_color, False)

    return route









