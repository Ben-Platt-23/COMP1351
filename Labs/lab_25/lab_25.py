import dudraw


dudraw.set_canvas_size(500, 600)
dudraw.set_x_scale(0, 10)
dudraw.set_y_scale(0, 12)
grid = []


for row in range(12):
    temp = []
    for col in range(10):
        temp.append(0)
    grid.append(temp)


while True:
    for row in range(12):
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_pen_width(.025)
        dudraw.line(0, row, 10, row)
    for col in range(10):
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_pen_width(.025)
        dudraw.line(col, 0, col, 12)
    
    for row in range(12):
        for col in range(10):
            dudraw.text(col + .5, row + .5, f'{grid[row][col]}')

    if dudraw.mouse_pressed():
        x = 0
        y = 0
        
        if dudraw.mouse_x() <= 1:
            x = 0
        elif dudraw.mouse_x() <= 2 and dudraw.mouse_x() > 1:
            x = 1
        elif dudraw.mouse_x() <= 3 and dudraw.mouse_x() > 2:
            x = 2
        elif dudraw.mouse_x() <= 4 and dudraw.mouse_x() > 3:
            x = 3
        elif dudraw.mouse_x() <= 5 and dudraw.mouse_x() > 4:
            x = 4
        elif dudraw.mouse_x() <= 6 and dudraw.mouse_x() > 5:
            x = 5
        elif dudraw.mouse_x() <= 7 and dudraw.mouse_x() > 6:
            x = 6
        elif dudraw.mouse_x() <= 8 and dudraw.mouse_x() > 7:
            x = 7
        elif dudraw.mouse_x() <= 9 and dudraw.mouse_x() > 8:
            x = 8
        elif dudraw.mouse_x() <= 10 and dudraw.mouse_x() > 9:
            x = 9
        
        if dudraw.mouse_y() <= 1:
            y = 0
        elif dudraw.mouse_y() <= 2 and dudraw.mouse_y() > 1:
            y = 1
        elif dudraw.mouse_y() <= 3 and dudraw.mouse_y() > 2:
            y = 2
        elif dudraw.mouse_y() <= 4 and dudraw.mouse_y() > 3:
            y = 3
        elif dudraw.mouse_y() <= 5 and dudraw.mouse_y() > 4:
            y = 4
        elif dudraw.mouse_y() <= 6 and dudraw.mouse_y() > 5:
            y = 5
        elif dudraw.mouse_y() <= 7 and dudraw.mouse_y() > 6:
            y = 6
        elif dudraw.mouse_y() <= 8 and dudraw.mouse_y() > 7:
            y = 7
        elif dudraw.mouse_y() <= 9 and dudraw.mouse_y() > 8:
            y = 8
        elif dudraw.mouse_y() <= 10 and dudraw.mouse_y() > 9:
            y = 9
        elif dudraw.mouse_y() <= 11 and dudraw.mouse_y() > 10:
            y = 10
        elif dudraw.mouse_y() <= 12 and dudraw.mouse_y() > 11:
            y = 11
        
        grid[x][y] += 1

        dudraw.clear(dudraw.WHITE)
    dudraw.show()