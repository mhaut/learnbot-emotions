#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import Tkinter as tk
import time


class BaseHead(object):
    def __init__(self):
        self.colour = "blue"
        self.size = None

    def set_colour(self, colour):
        self.colour = colour

    def set_size(self, points):
        # points = x0, y0, x1, y1
        self.size = points

    def get_colour(self):
        return self.colour

    def get_size(self):
        return self.size


class Eye(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class Pupil(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)
        self.reflex = Pupil_reflex()


class Pupil_reflex(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class EyeLid(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class EyeBrow(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class Mouth(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class Face():
    def __init__(self, window):
        self.window = window
        self.eyes = [Eye(), Eye()]
        self.eyebrows = [EyeBrow(), EyeBrow()]
        self.right_eyebrow = EyeBrow()
        self.eyelids = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
        self.mouth = Mouth()
        self.status = "neutral"

        draw_eyelid = [None, None, None, None]

        for eye, size_eye in zip(self.eyes, [[60, 80, 180, 240], [300, 80, 420, 240]]):
            eye.set_colour('#4192D9')
            eye.set_size(size_eye)

        for eyelid, size_eyelid in zip(self.eyelids, [[40, 0, 200, 80], [40, 240, 200, 320], [280, 0, 440, 80],
                                                      [280, 240, 440, 320]]):
            eyelid.set_colour('black')
            eyelid.set_size(size_eyelid)

        self.canvas = tk.Canvas(width=480, height=320, background='black')
        self.canvas.pack()
        self.canvas.create_oval(self.get_eye("left").get_size(), outline=self.get_eye("left").get_colour(),
                                           fill=self.get_eye("left").get_colour())
        self.canvas.create_oval(self.get_eye("right").get_size(),outline=self.get_eye("right").get_colour(),
                                            fill=self.get_eye("right").get_colour())
        for eyelid in self.eyelids:
            eyelid = self.canvas.create_rectangle(eyelid.get_size(), outline="black", fill="black")



    def set_eye(self, eye, position):
        if position == "left":
            self.eyes[0] = eye
        elif position == "right":
            self.eyes[1] = eye
        else:
            print("ERROR: Position eye set")
            exit()

    def get_eye(self, position):
        if position == "left":
            return self.eyes[0]
        elif position == "right":
            return self.eyes[1]
        else:
            print("ERROR: Position eye get")
            exit()

    def set_eyebrow(self, eyebrow, position):
        if position == "left":
            self.eyebrows[0] = eyebrow
        elif position == "right":
            self.eyebrows[1] = eyebrow
        else:
            print("ERROR: Position eyebrow set")
            exit()

    def get_eyebrow(self, position):
        if position == "left":
            return self.eyebrows[0]
        elif position == "right":
            return self.eyebrows[1]
        else:
            print("ERROR: Position eyebrow get")
            exit()

    def set_eyelids(self, lu_eyeLid, ld_eyeLid, ru_eyeLid, rd_eyeLid):
        self.eyelids = [lu_eyeLid, ld_eyeLid, ru_eyeLid, rd_eyeLid]

    def get_eyelids(self):
        return self.eyelids

    def change_status(self, status):
        print(self.status, "to", status)
        self.status = status
        if self.status == 'happiness':
            circlehappy1 = self.canvas.create_oval(20, 240, 220, 440, fill="black")
            circlehappy2 = self.canvas.create_oval(260, 240, 460, 440, fill="black")
            x = 0
            y = 2.3
            for i in range(0, 51):
                time.sleep(0.01)
                self.canvas.move(circlehappy1, x, -y)
                self.canvas.move(circlehappy2, x, -y)
                self.canvas.update()


            if KeyboardInterrupt:
                status = raw_input("What is the status of Learnbot?")
                self.canvas.delete(circlehappy1)
                self.canvas.delete(circlehappy2)
                self.change_status(status)


        elif self.status == 'angry':
            xy = [(60.2, -94.48), (218.16, -36.08), (188.96, 38.4), (40, -20)]
            angryUle = self.canvas.create_polygon(xy, fill="black")  # Up|Left  eyelid
            xy2 = [(291.04, 38.4), (440, -20), (410.8, -94.48), (261.84, -36.08)]
            angryUre = self.canvas.create_polygon(xy2, fill="black")  # Up|Right  eyelid
            angryDle = self.canvas.create_rectangle(40, 320, 200, 400, fill="black")  # Down|Left  eyelid
            angryDre = self.canvas.create_rectangle(280, 320, 440, 400, fill="black")  # Down|Right eyelid
            x = 0
            y = 2.3
            for i in range(0, 51):
                time.sleep(0.01)
                self.canvas.move(angryUle, x, y)
                self.canvas.move(angryUre, x, y)
                self.canvas.move(angryDle, x, -y)
                self.canvas.move(angryDre, x, -y)
                self.canvas.update()

            if KeyboardInterrupt:
                status = raw_input("What is the status of Learnbot?")
                self.canvas.delete(angryUle)
                self.canvas.delete(angryUre)
                self.canvas.delete(angryDle)
                self.canvas.delete(angryDre)
                self.change_status(status)

        elif self.status == 'sadness':
            x = 0
            y = 2
            xy = [(11.04, 8.4), (160, -50), (189.2, 24.48), (40.24, 82.88)]
            sadUle = self.canvas.create_polygon(xy, fill="black")  # Up|Left  eyelid
            xy2 = [(320, -50), (468.96, 8.4), (439.76, 82.27), (290.8, 24.48)]
            sadUre = self.canvas.create_polygon(xy2, fill="black")  # Up|Right  eyelid
            for i in range(0, 51):
                time.sleep(0.01)
                self.canvas.move(sadUle, x, y)
                self.canvas.move(sadUre, x, y)
                self.canvas.update()

            if KeyboardInterrupt:
                status = raw_input("What is the status of Learnbot?")
                self.canvas.delete(sadUle)
                self.canvas.delete(sadUre)
                self.change_status(status)

        elif self.status == 'scared':
            x = 0
            y = 1
            circlescared1 = self.canvas.create_oval(-10, 240, 190, 440, fill="black")
            circlescared2 = self.canvas.create_oval(290, 240, 490, 440, fill="black")
            for i in range(0, 51):
                time.sleep(0.01)
                self.canvas.move(circlescared1, x, -y)
                self.canvas.move(circlescared2, x, -y)
                self.canvas.update()
            if KeyboardInterrupt:
                status = raw_input("What is the status of Learnbot?")
                self.canvas.delete(circlescared1)
                self.canvas.delete(circlescared2)
                self.change_status(status)
        #self.window.after(1, self.change_status("sadness"))
        else:
            track = 0
            n1=self.canvas.create_rectangle(40, 0, 200, 80, outline="black", fill="black")
            n2=self.canvas.create_rectangle(40, 240, 200, 320, outline="black", fill="black")
            n3=self.canvas.create_rectangle(280, 0, 440, 80, outline="black", fill="black")
            n4=self.canvas.create_rectangle(280, 240, 440, 320, outline="black", fill="black")
            change_state=True
            while change_state:
                x = 0
                y = 1.4
                print ("e")
                if track == 0:
                    for i in range(0, 51):
                        time.sleep(0.01)

                        #print (self.eyelids[0].get_size())
                        #self.canvas.move(self.eyelids[0], x,y)
                        self.canvas.move(n1, x, y)
                        self.canvas.move(n2, x, -y)
                        self.canvas.move(n3, x, y)
                        self.canvas.move(n4, x, -y)
                        self.canvas.update()
                    track = 1
                    time.sleep(0.1)

                else:
                    for i in range(0, 51):
                        time.sleep(0.01)
                        self.canvas.move(n1, x, -y)
                        self.canvas.move(n2, x, y)
                        self.canvas.move(n3, x, -y)
                        self.canvas.move(n4, x, y)
                        self.canvas.update()
                    track = 0
                    time.sleep(4)
                    if KeyboardInterrupt:
                        change_state=False
                        status = raw_input("What is the status of Learnbot?")
                        self.change_status(status)
    def end(self):
        tk.destroy()
        print("end")


if __name__ == "__main__":
    root = tk.Tk()
    face = Face(root)
    status = raw_input("What is the status of Learnbot?")
    face.change_status(status)
    root.mainloop()

"""class App():
	def __init__(self):
		self.root = tk.Tk()
		self.label = tk.Label(text="")
		self.label.pack()
		self.update_clock()
		self.root.mainloop()

	def update_clock(self):
		now = time.strftime("%H:%M:%S")
		self.label.configure(text=now)
		self.root.after(1000, self.update_clock)

app=App()"""
