import math
import numpy as np
class circle():
    p_size = 3
    def __init__(self, radius, cx, cy, angle, p_speed, width, height):
        self.radius = radius
        self.cx = cx
        self.cy = cy
        self.px = 0
        self.py = 0
        self.angle = angle
        self.p_speed = p_speed
        self.width = width
        self.height = height
        self.draw_point_ids = []
        self.ids = []
        self.x_lines = []
        self.y_lines = []

    def show(self, canvas):
        self.circle_id = canvas.create_oval(self.cx - self.radius,
                                    self.cy - self.radius,
                                    self.cx + self.radius,
                                    self.cy + self.radius,
                                    fill="", outline="white")

        self.px = self.cx + self.radius * math.cos(self.angle)
        self.py = self.cy + self.radius * math.sin(self.angle)

        self.point_id = canvas.create_oval(self.px - self.p_size,
                                    self.py - self.p_size,
                                    self.px + self.p_size,
                                    self.py + self.p_size,
                                    fill="white", outline="")

    def move(self, canvas):
        self.angle += self.p_speed

        self.old_px = self.px
        self.old_py = self.py

        self.px = self.cx + self.radius * math.cos(self.angle)
        self.py = self.cy + self.radius * math.sin(self.angle)

        canvas.move(self.point_id, self.px - self.old_px, self.py - self.old_py)
        self.angle = 0 if (self.angle > math.tau) else self.angle

    def show_line(self, canvas, circle):
        line1_x0 = self.px
        line1_y0 = self.py
        line1_x1 = self.px
        line1_y1 = self.width + self.radius
        
        if(len(circle.y_lines) == 0):
            line2_x0 = circle.px
            line2_y0 = circle.py
            line2_x1 = self.height + self.radius
            line2_y1 = circle.py
            circle.y_lines.append(canvas.create_line(line2_x0, line2_y0, line2_x1, line2_y1, fill="grey"))
        self.x_lines.append(canvas.create_line(line1_x0, line1_y0, line1_x1, line1_y1, fill="grey"))

        self.draw_px = self.px
        self.draw_py = circle.py

        self.draw_point_ids.append(canvas.create_oval(self.draw_px - self.p_size,
                                    self.draw_py - self.p_size,
                                    self.draw_px + self.p_size,
                                    self.draw_py + self.p_size,
                                    fill="white", outline=""))

    def move_line(self, canvas, circles):    
        i = 0
        for circle in circles:
            point = self.draw_point_ids[i]
            p_coords = canvas.coords(point)
            old_draw_px = (p_coords[0] + p_coords[2]) * 0.5
            old_draw_py = (p_coords[1] + p_coords[3]) * 0.5

            self.draw_px = self.px
            self.draw_py = circle.py
            canvas.move(self.x_lines[i], self.px - self.old_px, self.py - self.old_py)            
            canvas.move(point, self.draw_px - old_draw_px, self.draw_py - old_draw_py)
            self.ids.append(canvas.create_line(old_draw_px, old_draw_py, self.draw_px, self.draw_py, fill="grey"))
            i += 1



