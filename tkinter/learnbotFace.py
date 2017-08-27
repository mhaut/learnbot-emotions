from __future__ import print_function
import Tkinter as tk
import load_json as paint
import load_configuration as lc
import readchar
#sudo pip install readchar
from termios import tcflush, TCIFLUSH
import time, sys
import queue
import threading

class BaseHead(object):
    def __init__(self):
        self.colour = "black"
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


class Iris(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class Pupil(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)
        self.brightness = [Brightness(), Brightness()]


class Brightness(BaseHead):
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


class Tongue(BaseHead):
    def __init__(self):
        BaseHead.__init__(self)


class Face():
    def __init__(self, name):
        self.eyes = [Eye(), Eye()]
        self.iris = [Iris(), Iris()]
        self.pupil = [Pupil(), Pupil()]
        self.eyebrow = [EyeBrow(), EyeBrow()]
        self.eyelid = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
        self.mouth = Mouth()
        self.tongue = Tongue()
        self.status = None

        self.canvas = tk.Canvas(width=480, height=320, background='black')
        self.canvas.pack()

        self.eyes[0].set_size(paint.checkPaint(name, paint.load_file(name))[0])
        self.eyes[0].set_colour(paint.checkPaint(name, paint.load_file(name))[1])
        self.eyes[1].set_size(paint.checkPaint(name, paint.load_file(name))[2])
        self.eyes[1].set_colour(paint.checkPaint(name, paint.load_file(name))[3])

        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[4])
        self.eyelid[0].set_colour(paint.checkPaint(name, paint.load_file(name))[5])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[6])
        self.eyelid[1].set_colour(paint.checkPaint(name, paint.load_file(name))[7])
        self.eyelid[2].set_size(paint.checkPaint(name, paint.load_file(name))[8])
        self.eyelid[2].set_colour(paint.checkPaint(name, paint.load_file(name))[9])
        self.eyelid[3].set_size(paint.checkPaint(name, paint.load_file(name))[10])
        self.eyelid[3].set_colour(paint.checkPaint(name, paint.load_file(name))[11])

        self.iris[0].set_size(paint.checkPaint(name, paint.load_file(name))[12])
        self.iris[0].set_colour(paint.checkPaint(name, paint.load_file(name))[13])
        self.iris[1].set_size(paint.checkPaint(name, paint.load_file(name))[14])
        self.iris[1].set_colour(paint.checkPaint(name, paint.load_file(name))[15])

        self.pupil[0].set_size(paint.checkPaint(name, paint.load_file(name))[16])
        self.pupil[0].set_colour(paint.checkPaint(name, paint.load_file(name))[17])
        self.pupil[1].set_size(paint.checkPaint(name, paint.load_file(name))[18])
        self.pupil[1].set_colour(paint.checkPaint(name, paint.load_file(name))[19])

        self.pupil[0].brightness[0].set_size(paint.checkPaint(name, paint.load_file(name))[20])
        self.pupil[0].brightness[0].set_colour(paint.checkPaint(name, paint.load_file(name))[21])
        self.pupil[0].brightness[1].set_size(paint.checkPaint(name, paint.load_file(name))[22])
        self.pupil[0].brightness[1].set_colour(paint.checkPaint(name, paint.load_file(name))[23])
        self.pupil[1].brightness[0].set_size(paint.checkPaint(name, paint.load_file(name))[24])
        self.pupil[1].brightness[0].set_colour(paint.checkPaint(name, paint.load_file(name))[25])
        self.pupil[1].brightness[1].set_size(paint.checkPaint(name, paint.load_file(name))[26])
        self.pupil[1].brightness[1].set_colour(paint.checkPaint(name, paint.load_file(name))[27])

        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])

        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[32])
        self.mouth.set_colour(paint.checkPaint(name, paint.load_file(name))[33])

        self.tongue.set_size(paint.checkPaint(name, paint.load_file(name))[34])
        self.tongue.set_colour(paint.checkPaint(name, paint.load_file(name))[35])

        self.eye_l = self.canvas.create_polygon(self.eyes[0].get_size(), fill=self.eyes[0].get_colour())
        self.eye_r = self.canvas.create_polygon(self.eyes[1].get_size(), fill=self.eyes[1].get_colour())
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
        self.eyelid_d_l = self.canvas.create_polygon(self.eyelid[2].get_size(), fill=self.eyelid[2].get_colour())
        self.eyelid_d_r = self.canvas.create_polygon(self.eyelid[3].get_size(), fill=self.eyelid[3].get_colour())
        self.iris_l = self.canvas.create_polygon(self.iris[0].get_size(), fill=self.iris[0].get_colour())
        self.iris_r = self.canvas.create_polygon(self.iris[1].get_size(), fill=self.iris[1].get_colour())
        self.pupil_l = self.canvas.create_polygon(self.pupil[0].get_size(), fill=self.pupil[1].get_colour())
        self.pupil_r = self.canvas.create_polygon(self.pupil[1].get_size(), fill=self.pupil[1].get_colour())
        self.reflex_pupil_l = self.canvas.create_polygon(self.pupil[0].brightness[0].get_size(),
                                                         fill=self.pupil[0].brightness[0].get_colour())
        self.reflex_pupil_r = self.canvas.create_polygon(self.pupil[0].brightness[1].get_size(),
                                                         fill=self.pupil[0].brightness[1].get_colour())
        self.reflex_pupil_2_l = self.canvas.create_polygon(self.pupil[1].brightness[0].get_size(),
                                                           fill=self.pupil[0].brightness[0].get_colour())
        self.reflex_pupil_2_r = self.canvas.create_polygon(self.pupil[1].brightness[1].get_size(),
                                                           fill=self.pupil[0].brightness[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[1].get_colour())
        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        self.tongue_ = self.canvas.create_polygon(self.tongue.get_size(), fill=self.tongue.get_colour())

    def get_angry(self, name):
        self.status = "angry"
        print ("angry")
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[36])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[41])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[96])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[101])
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[0].get_colour())
        x = 0
        y = 1.4
        for i in range(0, 51):
            time.sleep(0.01)
            self.canvas.move(self.eyelid_u_l, x, y)
            self.canvas.move(self.eyelid_u_r, x, y)
            self.canvas.move(self.eyebrow_l, x, y)
            self.canvas.move(self.eyebrow_r, x, y)
            self.canvas.update()
        return self.status


    def clear_angry(self, name):
        print ("clear angry")
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[4])
        self.eyelid[0].set_colour(paint.checkPaint(name, paint.load_file(name))[5])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[6])
        self.eyelid[1].set_colour(paint.checkPaint(name, paint.load_file(name))[7])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])

        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(),
                                                     fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(),
                                                     fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(),
                                                    fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(),
                                                    fill=self.eyebrow[1].get_colour())

    def get_happy(self, name):
        self.status = "happiness"
        print ("happiness")
        self.eyelid[2].set_size(paint.checkPaint(name, paint.load_file(name))[47])
        self.eyelid[3].set_size(paint.checkPaint(name, paint.load_file(name))[52])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[97])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[102])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[107])
        self.canvas.delete(self.eyelid_d_l)
        self.canvas.delete(self.eyelid_d_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.canvas.delete(self.tongue_)
        self.eyelid_d_l = self.canvas.create_polygon(self.eyelid[2].get_size(), fill=self.eyelid[2].get_colour())
        self.eyelid_d_r = self.canvas.create_polygon(self.eyelid[3].get_size(), fill=self.eyelid[3].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[1].get_colour())
        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())

        x = 0
        y = 0.95
        y2 = 0.2
        for i in range(0, 51):
            time.sleep(0.02)
            self.canvas.move(self.eyelid_d_l, x, -y)
            self.canvas.move(self.eyelid_d_r, x, -y)
            self.canvas.move(self.eyebrow_l, x, -y2)
            self.canvas.move(self.eyebrow_r, x, -y2)
            self.canvas.update()
        return self.status


    def clear_happiness(self, name):
        print ("clear happy")
        self.canvas.delete(self.eyelid_d_l)
        self.canvas.delete(self.eyelid_d_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)

        self.eyelid[2].set_size(paint.checkPaint(name, paint.load_file(name))[8])
        self.eyelid[2].set_colour(paint.checkPaint(name, paint.load_file(name))[9])
        self.eyelid[3].set_size(paint.checkPaint(name, paint.load_file(name))[10])
        self.eyelid[3].set_colour(paint.checkPaint(name, paint.load_file(name))[11])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[32])

        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        self.tongue_ = self.canvas.create_polygon(self.tongue.get_size(), fill=self.tongue.get_colour())
        self.eyelid_d_l = self.canvas.create_polygon(self.eyelid[2].get_size(),
                                                     fill=self.eyelid[2].get_colour())
        self.eyelid_d_r = self.canvas.create_polygon(self.eyelid[3].get_size(),
                                                     fill=self.eyelid[3].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(),
                                                    fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(),
                                                    fill=self.eyebrow[1].get_colour())

    def get_sad(self, name):
        self.status = "sadness"
        print ("sadness")
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[38])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[43])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[98])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[103])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[108])
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.canvas.delete(self.tongue_)
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[1].get_colour())
        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        x = 0
        y = 1.4
        y2 = 1
        for i in range(0, 51):
            time.sleep(0.02)
            self.canvas.move(self.eyelid_u_l, x, y)
            self.canvas.move(self.eyelid_u_r, x, y)
            self.canvas.move(self.eyebrow_l, x, y2)
            self.canvas.move(self.eyebrow_r, x, y2)
            self.canvas.update()
        return self.status


    def clear_sadness(self, name):
        print ("clear sadness")
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[4])
        self.eyelid[0].set_colour(paint.checkPaint(name, paint.load_file(name))[5])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[6])
        self.eyelid[1].set_colour(paint.checkPaint(name, paint.load_file(name))[7])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[32])

        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        self.tongue_ = self.canvas.create_polygon(self.tongue.get_size(), fill=self.tongue.get_colour())
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(),
                                                     fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(),
                                                     fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(),
                                                    fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(),
                                                    fill=self.eyebrow[1].get_colour())

    def get_scared(self, name):
        self.status = "scared"
        print ("scared")
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[39])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[44])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[99])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[104])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[109])
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.canvas.delete(self.tongue_)
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[1].get_colour())
        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())

        x = 0
        y = 1.4
        for i in range(0, 51):
            time.sleep(0.01)
            self.canvas.move(self.eye_l, x, -y)
            self.canvas.move(self.eye_r, x, -y)
            self.canvas.update()
        return self.status


    def clear_scared(self, name):
        print ("clear scared")
        self.canvas.delete(self.eyelid_u_l)
        self.canvas.delete(self.eyelid_u_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[4])
        self.eyelid[0].set_colour(paint.checkPaint(name, paint.load_file(name))[5])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[6])
        self.eyelid[1].set_colour(paint.checkPaint(name, paint.load_file(name))[7])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[32])

        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        self.tongue_ = self.canvas.create_polygon(self.tongue.get_size(), fill=self.tongue.get_colour())
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(),
                                                     fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(),
                                                     fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(),
                                                    fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(),
                                                    fill=self.eyebrow[1].get_colour())
        x = 0
        y = 1.4
        for i in range(0, 51):
            self.canvas.move(self.eye_l, x, y)
            self.canvas.move(self.eye_r, x, y)
            self.canvas.update()

    def get_disgust(self, name):
        self.status = "disgust"
        print ("disgust")
        self.eyelid[2].set_size(paint.checkPaint(name, paint.load_file(name))[50])
        self.eyelid[3].set_size(paint.checkPaint(name, paint.load_file(name))[55])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[100])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[105])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[110])
        self.canvas.delete(self.eyelid_d_l)
        self.canvas.delete(self.eyelid_d_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.canvas.delete(self.tongue_)
        self.eyelid_d_l = self.canvas.create_polygon(self.eyelid[2].get_size(), fill=self.eyelid[2].get_colour())
        self.eyelid_d_r = self.canvas.create_polygon(self.eyelid[3].get_size(), fill=self.eyelid[3].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(), fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(), fill=self.eyebrow[1].get_colour())
        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())

        x = 0
        y = 0.95
        for i in range(0, 51):
            time.sleep(0.02)
            self.canvas.move(self.eyelid_d_l, x, -y)
            self.canvas.move(self.eyelid_d_r, x, -y)
            self.canvas.update()
        return self.status

    def clear_disgust(self, name):
        self.status = "disgust"
        print ("clear disgust")
        self.canvas.delete(self.eyelid_d_l)
        self.canvas.delete(self.eyelid_d_r)
        self.canvas.delete(self.eyebrow_l)
        self.canvas.delete(self.eyebrow_r)
        self.canvas.delete(self.mouth_)
        self.eyelid[0].set_size(paint.checkPaint(name, paint.load_file(name))[8])
        self.eyelid[0].set_colour(paint.checkPaint(name, paint.load_file(name))[9])
        self.eyelid[1].set_size(paint.checkPaint(name, paint.load_file(name))[10])
        self.eyelid[1].set_colour(paint.checkPaint(name, paint.load_file(name))[11])
        self.eyebrow[0].set_size(paint.checkPaint(name, paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name, paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name, paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name, paint.load_file(name))[31])
        self.mouth.set_size(paint.checkPaint(name, paint.load_file(name))[32])

        self.mouth_ = self.canvas.create_polygon(self.mouth.get_size(), fill=self.mouth.get_colour())
        self.tongue_ = self.canvas.create_polygon(self.tongue.get_size(), fill=self.tongue.get_colour())
        self.eyelid_u_l = self.canvas.create_polygon(self.eyelid[0].get_size(),
                                                     fill=self.eyelid[0].get_colour())
        self.eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(),
                                                     fill=self.eyelid[1].get_colour())
        self.eyebrow_l = self.canvas.create_polygon(self.eyebrow[0].get_size(),
                                                    fill=self.eyebrow[0].get_colour())
        self.eyebrow_r = self.canvas.create_polygon(self.eyebrow[1].get_size(),
                                                    fill=self.eyebrow[1].get_colour())

    def change_status(self):
        print ("You can change status by pressing")
        print (" n    if you want the state to be neutral")
        print (" a    if you want the state to be angry")
        print (" h    if you want the state to be happiness")
        print (" s    if you want the state to be sadness")
        print (" x    if you want the state to be scared")
        print (" d    if you want the state to be disgust")
        print (" q    if you want exit")
        print (" By default the state is neutral")

        end = False
        while end!=True:
            tcflush(sys.stdin, TCIFLUSH)
            char = readchar.readkey()
            if self.status == "angry":
                self.clear_angry(name)
            if self.status == "happiness":
                self.clear_happiness(name)
            if self.status == "sadness":
                self.clear_sadness(name)
            if self.status == "scared":
                self.clear_scared(name)
            if self.status == "disgust":
                self.clear_disgust(name)

            print ("bucle")
            if char == "a":
                self.get_angry(name)

            if char == "h":
                self.get_happy(name)

            if char == "s":
                self.get_sad(name)

            if char == "x":
                self.get_scared(name)

            if char == "d":
                self.get_disgust(name)

            if char == "q":
                end = True
                print ("end")
                sys.exit(1)


        """
        print "entra change"
        print self.char
        ending= False
        while ending != True:
            print "entra bucle"
            track = 0
            change_state = True
            while change_state:
                x = 0
                y = 1.3
                if track == 0:
                    for i in range(0, 51):
                        time.sleep(0.01)

                        # print (self.eyelids[0].get_size())
                        # self.canvas.move(self.eyelids[0], x,y)
                        self.canvas.move(self.eyelid_u_l, x, y)
                        self.canvas.move(self.eyelid_u_r, x, y)
                        self.canvas.move(self.eyelid_d_l, x, -y)
                        self.canvas.move(self.eyelid_d_r, x, -y)
                        self.canvas.update()
                    track = 1
                    time.sleep(0.1)

                else:
                    for i in range(0, 51):
                        time.sleep(0.01)
                        self.canvas.move(self.eyelid_u_l, x, -y)
                        self.canvas.move(self.eyelid_u_r, x, -y)
                        self.canvas.move(self.eyelid_d_l, x, y)
                        self.canvas.move(self.eyelid_d_r, x, y)
                        self.canvas.update()
                    track = 0
                    time.sleep(3)
                    self.char = getch.getch()
                    if self.char == "a" or self.char == "h" or self.char == "s" or self.char=="x" or self.char == "d" or self.char == "n":
                        change_state = False

"""


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_attributes('-type', 'splash')
    name = lc.loadConfiguration()
    face = Face(name)

    face.change_status()
    # root.attributes('-fullscreen', True)

    root.bind("<Escape>", lambda e: root.quit())
    root.mainloop()
