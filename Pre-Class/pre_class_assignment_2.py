import dudraw

dudraw.set_canvas_size(400, 400)
dudraw.clear(dudraw.DARK_BLUE)

dudraw.set_pen_color(dudraw.RED)
dudraw.filled_rectangle(0.5, 0.2, 0.4, 0.2)

dudraw.set_pen_color(dudraw.DARK_GREEN)
dudraw.filled_quadrilateral(0, 0.4, 0.1, 0.6, 0.9, 0.6, 1, 0.4)

dudraw.set_pen_color(dudraw.WHITE)
dudraw.filled_circle(0.8, 0.8, 0.05)



dudraw.show(5000)