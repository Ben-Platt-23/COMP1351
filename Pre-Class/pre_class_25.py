import dudraw
def draw_grid():
    dudraw.clear(dudraw.WHITE)
    x1 = 0
    y1 = 12
    x2 = 10
    y2 = 12

    x3 = 0
    y3 = 12
    x4 = 0
    y4 = 0

    for i in range(12):
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_pen_width(.025)
        dudraw.line(x1, y1, x2, y2)
        y1 -= 1
        y2 -= 1
        for x in range(10):
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.set_pen_width(.025)
            dudraw.line(x3, y3, x4, y4)
            x3 += 1
            x4 += 1

def main_func():
    # 2D list
    rows, cols = 12, 10
    list = [[0]*cols]*rows
    print(list)

    dudraw.set_canvas_size(500, 600)
    dudraw.set_x_scale(0, 10)
    dudraw.set_y_scale(0, 12)
    draw_grid()
    dudraw.show()

main_func()