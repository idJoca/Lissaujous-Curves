from circle import circle
from frame_rate import *
from tkinter import *
import numpy as np
import random
class main_loop():

    #===Consts===
    circ_radius = 30
    speed = 0.1
    speed_off = random.uniform(0.01, 0.05)
    x_off = 4
    y_off = 4
    x_circs = np.empty(5, circle)
    y_circs = np.empty(5, circle)

    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.fr_control = frame_rate_control(30)

        self.root = Tk()
        self.root.title("Lissaujous Curves")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.configure(background="black")
        self.canvas.pack()


    def start(self):
        random.seed()
        self.x_off = 4
        self.y_off = 4
        self.speed = 0.01    
        self.speed_off = random.uniform(0.01, 0.05)
        for i in range(0, len(self.x_circs)):
            self.x_circs[i] = circle(self.circ_radius, self.circ_radius * 2 * (i + self.x_off), 50, 0, self.speed + self.speed_off, self.width, self.height)
            self.x_circs[i].show(self.canvas)
            self.x_off += 0.2
            self.speed += self.speed_off


            self.y_circs[i] = circle(self.circ_radius, 50, self.circ_radius * 2 * (i + self.y_off), 0, self.speed + self.speed_off, self.width, self.height)
            self.y_circs[i].show(self.canvas)
            self.speed += self.speed_off
            self.y_off += 0.2

        for i in range(0, len(self.x_circs)):
            for j in range(0, len(self.y_circs)):
                self.x_circs[i].show_line(self.canvas, self.y_circs[j])
    
    def main(self):
        while(True):            
            self.fr_control.start()
            list(map(lambda x: x.move(self.canvas), self.x_circs))
            list(map(lambda y: y.move(self.canvas), self.y_circs))
            list(map(lambda x: x.move_line(self.canvas, self.y_circs), self.x_circs))
            for circle in self.y_circs:
                self.canvas.move(circle.y_lines[0],  circle.px - circle.old_px, circle.py - circle.old_py)
            self.root.update()
            self.fr_control.delay()
            if (len(self.x_circs[0].ids) > 1000):
                for x_circ in self.x_circs:
                    x_circ.ids = []

                self.canvas.delete(ALL)                
                self.start()
            #self.start()
            
loop = main_loop(600, 600)
loop.start()
loop.main()
