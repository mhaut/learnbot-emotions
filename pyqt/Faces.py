import sys

import time

import load_json as load
import load_configuration as settings

from PyQt4 import QtGui, QtCore, Qt

from PyQt4.QtCore import QPoint, QParallelAnimationGroup, QSequentialAnimationGroup
from PyQt4.QtGui import QPolygon, QPolygonF, QBrush, QColor


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

class Face(QtGui.QGraphicsView):
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        self.initUI()
        self.setParts()

    def initUI(self):
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(0,0,480,320)
        self.setStyleSheet("background: black")
        self.setScene(self.scene)

    def setParts(self):
        features = settings.loadConfiguration()
        self.name=features[0]
        self.exist_eyebrows = features[1]
        self.exist_iris = features[2]
        self.exist_pupils = features[3]
        self.exist_brightness = features[4]
        self.exist_more_brightness = features[5]
        self.exist_mouth = features[6]

        self.eyes = [Eye(), Eye()]
        self.iris = [Iris(), Iris()]
        self.pupil = [Pupil(), Pupil()]
        self.eyebrow = [EyeBrow(), EyeBrow()]
        self.eyelid = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
        self.mouth = Mouth()
        self.tongue = Tongue()

        self.eyes = [Eye(), Eye()]
        self.iris = [Iris(), Iris()]
        self.pupil = [Pupil(), Pupil()]
        self.eyebrow = [EyeBrow(), EyeBrow()]
        self.eyelid = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
        self.mouth = Mouth()
        self.tongue = Tongue()

        self.eyes[0].set_size(load.load_file(self.name)[0])
        self.eyes[0].set_colour(load.load_file(self.name)[98])
        self.eyes[1].set_size(load.load_file(self.name)[1])
        self.eyes[1].set_colour(load.load_file(self.name)[98])
        self.eyelid[0].set_size(load.load_file(self.name)[2])
        self.eyelid[0].set_colour(load.load_file(self.name)[99])
        self.eyelid[1].set_size(load.load_file(self.name)[3])
        self.eyelid[1].set_colour(load.load_file(self.name)[99])
        self.eyelid[2].set_size(load.load_file(self.name)[4])
        self.eyelid[2].set_colour(load.load_file(self.name)[99])
        self.eyelid[3].set_size(load.load_file(self.name)[5])
        self.eyelid[3].set_colour(load.load_file(self.name)[99])
        self.iris[0].set_size(load.load_file(self.name)[6])
        self.iris[0].set_colour(load.load_file(self.name)[100])
        self.iris[1].set_size(load.load_file(self.name)[7])
        self.iris[1].set_colour(load.load_file(self.name)[100])
        self.pupil[0].set_size(load.load_file(self.name)[8])
        self.pupil[0].set_colour(load.load_file(self.name)[101])
        self.pupil[1].set_size(load.load_file(self.name)[9])
        self.pupil[1].set_colour(load.load_file(self.name)[101])
        self.pupil[0].brightness[0].set_size(load.load_file(self.name)[10])
        self.pupil[0].brightness[0].set_colour(load.load_file(self.name)[102])
        self.pupil[1].brightness[0].set_size(load.load_file(self.name)[11])
        self.pupil[1].brightness[0].set_colour(load.load_file(self.name)[102])
        self.pupil[0].brightness[1].set_size(load.load_file(self.name)[12])
        self.pupil[0].brightness[1].set_colour(load.load_file(self.name)[102])
        self.pupil[1].brightness[1].set_size(load.load_file(self.name)[13])
        self.pupil[1].brightness[1].set_colour(load.load_file(self.name)[102])
        self.eyebrow[0].set_size(load.load_file(self.name)[14])
        self.eyebrow[0].set_colour(load.load_file(self.name)[103])
        self.eyebrow[1].set_size(load.load_file(self.name)[15])
        self.eyebrow[1].set_colour(load.load_file(self.name)[103])
        self.mouth.set_size(load.load_file(self.name)[16])
        self.mouth.set_colour(load.load_file(self.name)[104])
        self.tongue.set_size(load.load_file(self.name)[17])
        self.tongue.set_colour(load.load_file(self.name)[105])

        lc =self.tongue.get_colour()[0]
        mc= self.mouth.get_colour()[0]

        self.item = QtGui.QGraphicsEllipseItem(-20, -10, 40, 20)
        self.item.setBrush(QBrush(QColor(self.eyes[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #EYES
        points = [self.eyes[0].get_size()[0],self.eyes[0].get_size()[1],self.eyes[0].get_size()[2],self.eyes[0].get_size()[3],self.eyes[0].get_size()[4],self.eyes[0].get_size()[5],self.eyes[0].get_size()[6],self.eyes[0].get_size()[7],self.eyes[0].get_size()[8],self.eyes[0].get_size()[9],self.eyes[0].get_size()[10],self.eyes[0].get_size()[11],self.eyes[0].get_size()[12],self.eyes[0].get_size()[13],self.eyes[0].get_size()[14],self.eyes[0].get_size()[15],self.eyes[0].get_size()[16],self.eyes[0].get_size()[17],self.eyes[0].get_size()[18],self.eyes[0].get_size()[19],self.eyes[0].get_size()[20],self.eyes[0].get_size()[21],self.eyes[0].get_size()[22],self.eyes[0].get_size()[23],self.eyes[0].get_size()[24],self.eyes[0].get_size()[25],self.eyes[0].get_size()[26],self.eyes[0].get_size()[27],self.eyes[0].get_size()[28],self.eyes[0].get_size()[29],self.eyes[0].get_size()[30],self.eyes[0].get_size()[31],self.eyes[0].get_size()[32],self.eyes[0].get_size()[33],self.eyes[0].get_size()[34]]
        eye_left = QPolygonF(points)
        self.eye_left = QtGui.QGraphicsPolygonItem(eye_left)
        self.eye_left.setBrush(QBrush(QColor(self.eyes[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.eyes[1].get_size()[0],self.eyes[1].get_size()[1],self.eyes[1].get_size()[2],self.eyes[1].get_size()[3],self.eyes[1].get_size()[4],self.eyes[1].get_size()[5],self.eyes[1].get_size()[6],self.eyes[1].get_size()[7],self.eyes[1].get_size()[8],self.eyes[1].get_size()[9],self.eyes[1].get_size()[10],self.eyes[1].get_size()[11],self.eyes[1].get_size()[12],self.eyes[1].get_size()[13],self.eyes[1].get_size()[14],self.eyes[1].get_size()[15],self.eyes[1].get_size()[16],self.eyes[1].get_size()[17],self.eyes[1].get_size()[18],self.eyes[1].get_size()[19],self.eyes[1].get_size()[20],self.eyes[1].get_size()[21],self.eyes[1].get_size()[22],self.eyes[1].get_size()[23],self.eyes[1].get_size()[24],self.eyes[1].get_size()[25],self.eyes[1].get_size()[26],self.eyes[1].get_size()[27],self.eyes[1].get_size()[28],self.eyes[1].get_size()[29],self.eyes[1].get_size()[30],self.eyes[1].get_size()[31],self.eyes[1].get_size()[32],self.eyes[1].get_size()[33],self.eyes[1].get_size()[34]]
        eye_right = QPolygonF(points)
        self.eye_right = QtGui.QGraphicsPolygonItem(eye_right)
        self.eye_right.setBrush(QBrush(QColor(self.eyes[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #EYELIDS
        points = [self.eyelid[0].get_size()[0],self.eyelid[0].get_size()[1],self.eyelid[0].get_size()[2], self.eyelid[0].get_size()[3],self.eyelid[0].get_size()[4],self.eyelid[0].get_size()[5],self.eyelid[0].get_size()[6],self.eyelid[0].get_size()[7],self.eyelid[0].get_size()[8],self.eyelid[0].get_size()[9],self.eyelid[0].get_size()[10],self.eyelid[0].get_size()[11],self.eyelid[0].get_size()[12],self.eyelid[0].get_size()[13],self.eyelid[0].get_size()[14],self.eyelid[0].get_size()[15],self.eyelid[0].get_size()[16],self.eyelid[0].get_size()[17],self.eyelid[0].get_size()[18],self.eyelid[0].get_size()[19],self.eyelid[0].get_size()[20],self.eyelid[0].get_size()[21],self.eyelid[0].get_size()[22],self.eyelid[0].get_size()[23],self.eyelid[0].get_size()[24],self.eyelid[0].get_size()[25],self.eyelid[0].get_size()[26],self.eyelid[0].get_size()[27],self.eyelid[0].get_size()[28],self.eyelid[0].get_size()[29],self.eyelid[0].get_size()[30],self.eyelid[0].get_size()[31],self.eyelid[0].get_size()[32],self.eyelid[0].get_size()[33],self.eyelid[0].get_size()[34]]
        eyelid_up_left = QPolygonF(points)
        self.eyelid_up_left = QtGui.QGraphicsPolygonItem(eyelid_up_left)
        self.eyelid_up_left.setBrush(QBrush(QColor(self.eyelid[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.eyelid[1].get_size()[0],self.eyelid[1].get_size()[1],self.eyelid[1].get_size()[2], self.eyelid[1].get_size()[3],self.eyelid[1].get_size()[4],self.eyelid[1].get_size()[5],self.eyelid[1].get_size()[6],self.eyelid[1].get_size()[7],self.eyelid[1].get_size()[8],self.eyelid[1].get_size()[9],self.eyelid[1].get_size()[10],self.eyelid[1].get_size()[11],self.eyelid[1].get_size()[12],self.eyelid[1].get_size()[13],self.eyelid[1].get_size()[14],self.eyelid[1].get_size()[15],self.eyelid[1].get_size()[16],self.eyelid[1].get_size()[17],self.eyelid[1].get_size()[18],self.eyelid[1].get_size()[19],self.eyelid[1].get_size()[20],self.eyelid[1].get_size()[21],self.eyelid[1].get_size()[22],self.eyelid[1].get_size()[23],self.eyelid[1].get_size()[24],self.eyelid[1].get_size()[25],self.eyelid[1].get_size()[26],self.eyelid[1].get_size()[27],self.eyelid[1].get_size()[28],self.eyelid[1].get_size()[29],self.eyelid[1].get_size()[30],self.eyelid[1].get_size()[31],self.eyelid[1].get_size()[32],self.eyelid[1].get_size()[33],self.eyelid[1].get_size()[34]]
        eyelid_up_right = QPolygonF(points)
        self.eyelid_up_right = QtGui.QGraphicsPolygonItem(eyelid_up_right)
        self.eyelid_up_right.setBrush(QBrush(QColor(self.eyelid[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.eyelid[2].get_size()[0],self.eyelid[2].get_size()[1],self.eyelid[2].get_size()[2], self.eyelid[2].get_size()[3],self.eyelid[2].get_size()[4],self.eyelid[2].get_size()[5],self.eyelid[2].get_size()[6],self.eyelid[2].get_size()[7],self.eyelid[2].get_size()[8],self.eyelid[2].get_size()[9],self.eyelid[2].get_size()[10],self.eyelid[2].get_size()[11],self.eyelid[2].get_size()[12],self.eyelid[2].get_size()[13],self.eyelid[2].get_size()[14],self.eyelid[2].get_size()[15],self.eyelid[2].get_size()[16],self.eyelid[2].get_size()[17],self.eyelid[2].get_size()[18],self.eyelid[2].get_size()[19],self.eyelid[2].get_size()[20],self.eyelid[2].get_size()[21],self.eyelid[2].get_size()[22],self.eyelid[2].get_size()[23],self.eyelid[2].get_size()[24],self.eyelid[2].get_size()[25],self.eyelid[2].get_size()[26],self.eyelid[2].get_size()[27],self.eyelid[2].get_size()[28],self.eyelid[2].get_size()[29],self.eyelid[2].get_size()[30],self.eyelid[2].get_size()[31],self.eyelid[2].get_size()[32],self.eyelid[2].get_size()[33],self.eyelid[2].get_size()[34]]
        eyelid_down_left = QPolygonF(points)
        self.eyelid_down_left = QtGui.QGraphicsPolygonItem(eyelid_down_left)
        self.eyelid_down_left.setBrush(QBrush(QColor(self.eyelid[2].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.eyelid[3].get_size()[0],self.eyelid[3].get_size()[1],self.eyelid[3].get_size()[2], self.eyelid[3].get_size()[3],self.eyelid[3].get_size()[4],self.eyelid[3].get_size()[5],self.eyelid[3].get_size()[6],self.eyelid[3].get_size()[7],self.eyelid[3].get_size()[8],self.eyelid[3].get_size()[9],self.eyelid[3].get_size()[10],self.eyelid[3].get_size()[11],self.eyelid[3].get_size()[12],self.eyelid[3].get_size()[13],self.eyelid[3].get_size()[14],self.eyelid[3].get_size()[15],self.eyelid[3].get_size()[16],self.eyelid[3].get_size()[17],self.eyelid[3].get_size()[18],self.eyelid[3].get_size()[19],self.eyelid[3].get_size()[20],self.eyelid[3].get_size()[21],self.eyelid[3].get_size()[22],self.eyelid[3].get_size()[23],self.eyelid[3].get_size()[24],self.eyelid[3].get_size()[25],self.eyelid[3].get_size()[26],self.eyelid[3].get_size()[27],self.eyelid[3].get_size()[28],self.eyelid[3].get_size()[29],self.eyelid[3].get_size()[30],self.eyelid[3].get_size()[31],self.eyelid[3].get_size()[32],self.eyelid[3].get_size()[33],self.eyelid[3].get_size()[34]]
        eyelid_down_right = QPolygonF(points)
        self.eyelid_down_right = QtGui.QGraphicsPolygonItem(eyelid_down_right)
        self.eyelid_down_right.setBrush(QBrush(QColor(self.eyelid[3].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #IRIS
        points = [self.iris[0].get_size()[0], self.iris[0].get_size()[1], self.iris[0].get_size()[2],self.iris[0].get_size()[3], self.iris[0].get_size()[4], self.iris[0].get_size()[5],self.iris[0].get_size()[6], self.iris[0].get_size()[7], self.iris[0].get_size()[8],self.iris[0].get_size()[9], self.iris[0].get_size()[10], self.iris[0].get_size()[11],self.iris[0].get_size()[12], self.iris[0].get_size()[13], self.iris[0].get_size()[14],self.iris[0].get_size()[15], self.iris[0].get_size()[16], self.iris[0].get_size()[17],self.iris[0].get_size()[18], self.iris[0].get_size()[19], self.iris[0].get_size()[20],self.iris[0].get_size()[21], self.iris[0].get_size()[22], self.iris[0].get_size()[23],self.iris[0].get_size()[24], self.iris[0].get_size()[25], self.iris[0].get_size()[26],self.iris[0].get_size()[27], self.iris[0].get_size()[28], self.iris[0].get_size()[29],self.iris[0].get_size()[30], self.iris[0].get_size()[31], self.iris[0].get_size()[32],self.iris[0].get_size()[33], self.iris[0].get_size()[34]]
        iris_left = QPolygonF(points)
        self.iris_left = QtGui.QGraphicsPolygonItem(iris_left)
        self.iris_left.setBrush(QBrush(QColor(self.iris[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.iris[1].get_size()[0], self.iris[1].get_size()[1], self.iris[1].get_size()[2],self.iris[1].get_size()[3], self.iris[1].get_size()[4], self.iris[1].get_size()[5],self.iris[1].get_size()[6], self.iris[1].get_size()[7], self.iris[1].get_size()[8],self.iris[1].get_size()[9], self.iris[1].get_size()[10], self.iris[1].get_size()[11],self.iris[1].get_size()[12], self.iris[1].get_size()[13], self.iris[1].get_size()[14],self.iris[1].get_size()[15], self.iris[1].get_size()[16], self.iris[1].get_size()[17],self.iris[1].get_size()[18], self.iris[1].get_size()[19], self.iris[1].get_size()[20],self.iris[1].get_size()[21], self.iris[1].get_size()[22], self.iris[1].get_size()[23],self.iris[1].get_size()[24], self.iris[1].get_size()[25], self.iris[1].get_size()[26],self.iris[1].get_size()[27], self.iris[1].get_size()[28], self.iris[1].get_size()[29],self.iris[1].get_size()[30], self.iris[1].get_size()[31], self.iris[1].get_size()[32],self.iris[1].get_size()[33], self.iris[1].get_size()[34]]
        iris_right = QPolygonF(points)
        self.iris_right = QtGui.QGraphicsPolygonItem(iris_right)
        self.iris_right.setBrush(QBrush(QColor(self.iris[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #PUPILS
        points = [self.pupil[0].get_size()[0], self.pupil[0].get_size()[1], self.pupil[0].get_size()[2],self.pupil[0].get_size()[3], self.pupil[0].get_size()[4], self.pupil[0].get_size()[5],self.pupil[0].get_size()[6], self.pupil[0].get_size()[7], self.pupil[0].get_size()[8],self.pupil[0].get_size()[9], self.pupil[0].get_size()[10], self.pupil[0].get_size()[11],self.pupil[0].get_size()[12], self.pupil[0].get_size()[13], self.pupil[0].get_size()[14],self.pupil[0].get_size()[15], self.pupil[0].get_size()[16], self.pupil[0].get_size()[17],self.pupil[0].get_size()[18], self.pupil[0].get_size()[19], self.pupil[0].get_size()[20],self.pupil[0].get_size()[21], self.pupil[0].get_size()[22], self.pupil[0].get_size()[23],self.pupil[0].get_size()[24], self.pupil[0].get_size()[25], self.pupil[0].get_size()[26],self.pupil[0].get_size()[27], self.pupil[0].get_size()[28], self.pupil[0].get_size()[29],self.pupil[0].get_size()[30], self.pupil[0].get_size()[31], self.pupil[0].get_size()[32],self.pupil[0].get_size()[33], self.pupil[0].get_size()[34]]
        pupil_left = QPolygonF(points)
        self.pupil_left = QtGui.QGraphicsPolygonItem(pupil_left)
        self.pupil_left.setBrush(QBrush(QColor(self.pupil[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.pupil[1].get_size()[0], self.pupil[1].get_size()[1], self.pupil[1].get_size()[2],self.pupil[1].get_size()[3], self.pupil[1].get_size()[4], self.pupil[1].get_size()[5],self.pupil[1].get_size()[6], self.pupil[1].get_size()[7], self.pupil[1].get_size()[8],self.pupil[1].get_size()[9], self.pupil[1].get_size()[10], self.pupil[1].get_size()[11],self.pupil[1].get_size()[12], self.pupil[1].get_size()[13], self.pupil[1].get_size()[14],self.pupil[1].get_size()[15], self.pupil[1].get_size()[16], self.pupil[1].get_size()[17],self.pupil[1].get_size()[18], self.pupil[1].get_size()[19], self.pupil[1].get_size()[20],self.pupil[1].get_size()[21], self.pupil[1].get_size()[22], self.pupil[1].get_size()[23],self.pupil[1].get_size()[24], self.pupil[1].get_size()[25], self.pupil[1].get_size()[26],self.pupil[1].get_size()[27], self.pupil[1].get_size()[28], self.pupil[1].get_size()[29],self.pupil[1].get_size()[30], self.pupil[1].get_size()[31], self.pupil[1].get_size()[32],self.pupil[1].get_size()[33], self.pupil[1].get_size()[34]]
        pupil_right = QPolygonF(points)
        self.pupil_right = QtGui.QGraphicsPolygonItem(pupil_right)
        self.pupil_right.setBrush(QBrush(QColor(self.pupil[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #BRIGHTNESS
        points = [self.pupil[0].brightness[0].get_size()[0], self.pupil[0].brightness[0].get_size()[1], self.pupil[0].brightness[0].get_size()[2],self.pupil[0].brightness[0].get_size()[3], self.pupil[0].brightness[0].get_size()[4], self.pupil[0].brightness[0].get_size()[5],self.pupil[0].brightness[0].get_size()[6], self.pupil[0].brightness[0].get_size()[7], self.pupil[0].brightness[0].get_size()[8],self.pupil[0].brightness[0].get_size()[9], self.pupil[0].brightness[0].get_size()[10], self.pupil[0].brightness[0].get_size()[11],self.pupil[0].brightness[0].get_size()[12], self.pupil[0].brightness[0].get_size()[13], self.pupil[0].brightness[0].get_size()[14],self.pupil[0].brightness[0].get_size()[15], self.pupil[0].brightness[0].get_size()[16], self.pupil[0].brightness[0].get_size()[17],self.pupil[0].brightness[0].get_size()[18], self.pupil[0].brightness[0].get_size()[19], self.pupil[0].brightness[0].get_size()[20],self.pupil[0].brightness[0].get_size()[21], self.pupil[0].brightness[0].get_size()[22], self.pupil[0].brightness[0].get_size()[23],self.pupil[0].brightness[0].get_size()[24], self.pupil[0].brightness[0].get_size()[25], self.pupil[0].brightness[0].get_size()[26],self.pupil[0].brightness[0].get_size()[27], self.pupil[0].brightness[0].get_size()[28], self.pupil[0].brightness[0].get_size()[29],self.pupil[0].brightness[0].get_size()[30], self.pupil[0].brightness[0].get_size()[31], self.pupil[0].brightness[0].get_size()[32],self.pupil[0].brightness[0].get_size()[33], self.pupil[0].brightness[0].get_size()[34]]
        reflex_pupil_left = QPolygonF(points)
        self.reflex_pupil_left = QtGui.QGraphicsPolygonItem(reflex_pupil_left)
        self.reflex_pupil_left.setBrush(QBrush(QColor(self.pupil[0].brightness[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.pupil[1].brightness[0].get_size()[0], self.pupil[1].brightness[0].get_size()[1], self.pupil[1].brightness[0].get_size()[2],self.pupil[1].brightness[0].get_size()[3], self.pupil[1].brightness[0].get_size()[4], self.pupil[1].brightness[0].get_size()[5],self.pupil[1].brightness[0].get_size()[6], self.pupil[1].brightness[0].get_size()[7], self.pupil[1].brightness[0].get_size()[8],self.pupil[1].brightness[0].get_size()[9], self.pupil[1].brightness[0].get_size()[10], self.pupil[1].brightness[0].get_size()[11],self.pupil[1].brightness[0].get_size()[12], self.pupil[1].brightness[0].get_size()[13], self.pupil[1].brightness[0].get_size()[14],self.pupil[1].brightness[0].get_size()[15], self.pupil[1].brightness[0].get_size()[16], self.pupil[1].brightness[0].get_size()[17],self.pupil[1].brightness[0].get_size()[18], self.pupil[1].brightness[0].get_size()[19], self.pupil[1].brightness[0].get_size()[20],self.pupil[1].brightness[0].get_size()[21], self.pupil[1].brightness[0].get_size()[22], self.pupil[1].brightness[0].get_size()[23],self.pupil[1].brightness[0].get_size()[24], self.pupil[1].brightness[0].get_size()[25], self.pupil[1].brightness[0].get_size()[26],self.pupil[1].brightness[0].get_size()[27], self.pupil[1].brightness[0].get_size()[28], self.pupil[1].brightness[0].get_size()[29],self.pupil[1].brightness[0].get_size()[30], self.pupil[1].brightness[0].get_size()[31], self.pupil[1].brightness[0].get_size()[32],self.pupil[1].brightness[0].get_size()[33], self.pupil[1].brightness[0].get_size()[34]]
        reflex_pupil_right = QPolygonF(points)
        self.reflex_pupil_right = QtGui.QGraphicsPolygonItem(reflex_pupil_right)
        self.reflex_pupil_right.setBrush(QBrush(QColor(self.pupil[1].brightness[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.pupil[0].brightness[1].get_size()[0], self.pupil[0].brightness[1].get_size()[1], self.pupil[0].brightness[1].get_size()[2],self.pupil[0].brightness[1].get_size()[3], self.pupil[0].brightness[1].get_size()[4], self.pupil[0].brightness[1].get_size()[5],self.pupil[0].brightness[1].get_size()[6], self.pupil[0].brightness[1].get_size()[7], self.pupil[0].brightness[1].get_size()[8],self.pupil[0].brightness[1].get_size()[9], self.pupil[0].brightness[1].get_size()[10], self.pupil[0].brightness[1].get_size()[11],self.pupil[0].brightness[1].get_size()[12], self.pupil[0].brightness[1].get_size()[13], self.pupil[0].brightness[1].get_size()[14],self.pupil[0].brightness[1].get_size()[15], self.pupil[0].brightness[1].get_size()[16], self.pupil[0].brightness[1].get_size()[17],self.pupil[0].brightness[1].get_size()[18], self.pupil[0].brightness[1].get_size()[19], self.pupil[0].brightness[1].get_size()[20],self.pupil[0].brightness[1].get_size()[21], self.pupil[0].brightness[1].get_size()[22], self.pupil[0].brightness[1].get_size()[23],self.pupil[0].brightness[1].get_size()[24], self.pupil[0].brightness[1].get_size()[25], self.pupil[0].brightness[1].get_size()[26],self.pupil[0].brightness[1].get_size()[27], self.pupil[0].brightness[1].get_size()[28], self.pupil[0].brightness[1].get_size()[29],self.pupil[0].brightness[1].get_size()[30], self.pupil[0].brightness[1].get_size()[31], self.pupil[0].brightness[1].get_size()[32],self.pupil[0].brightness[1].get_size()[33], self.pupil[0].brightness[1].get_size()[34]]
        reflex_pupil_left_2 = QPolygonF(points)
        self.reflex_pupil_left_2 = QtGui.QGraphicsPolygonItem(reflex_pupil_left_2)
        self.reflex_pupil_left_2.setBrush(QBrush(QColor(self.pupil[0].brightness[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.pupil[1].brightness[1].get_size()[0], self.pupil[1].brightness[1].get_size()[1], self.pupil[1].brightness[1].get_size()[2],self.pupil[1].brightness[1].get_size()[3], self.pupil[1].brightness[1].get_size()[4], self.pupil[1].brightness[1].get_size()[5],self.pupil[1].brightness[1].get_size()[6], self.pupil[1].brightness[1].get_size()[7], self.pupil[1].brightness[1].get_size()[8],self.pupil[1].brightness[1].get_size()[9], self.pupil[1].brightness[1].get_size()[10], self.pupil[1].brightness[1].get_size()[11],self.pupil[1].brightness[1].get_size()[12], self.pupil[1].brightness[1].get_size()[13], self.pupil[1].brightness[1].get_size()[14],self.pupil[1].brightness[1].get_size()[15], self.pupil[1].brightness[1].get_size()[16], self.pupil[1].brightness[1].get_size()[17],self.pupil[1].brightness[1].get_size()[18], self.pupil[1].brightness[1].get_size()[19], self.pupil[1].brightness[1].get_size()[20],self.pupil[1].brightness[1].get_size()[21], self.pupil[1].brightness[1].get_size()[22], self.pupil[1].brightness[1].get_size()[23],self.pupil[1].brightness[1].get_size()[24], self.pupil[1].brightness[1].get_size()[25], self.pupil[1].brightness[1].get_size()[26],self.pupil[1].brightness[1].get_size()[27], self.pupil[1].brightness[1].get_size()[28], self.pupil[1].brightness[1].get_size()[29],self.pupil[1].brightness[1].get_size()[30], self.pupil[1].brightness[1].get_size()[31], self.pupil[1].brightness[1].get_size()[32],self.pupil[1].brightness[1].get_size()[33], self.pupil[1].brightness[1].get_size()[34]]
        reflex_pupil_right_2 = QPolygonF(points)
        self.reflex_pupil_right_2 = QtGui.QGraphicsPolygonItem(reflex_pupil_right_2)
        self.reflex_pupil_right_2.setBrush(QBrush(QColor(self.pupil[1].brightness[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #EYEBROWS
        points = [self.eyebrow[0].get_size()[0], self.eyebrow[0].get_size()[1], self.eyebrow[0].get_size()[2],self.eyebrow[0].get_size()[3], self.eyebrow[0].get_size()[4], self.eyebrow[0].get_size()[5],self.eyebrow[0].get_size()[6], self.eyebrow[0].get_size()[7], self.eyebrow[0].get_size()[8],self.eyebrow[0].get_size()[9], self.eyebrow[0].get_size()[10], self.eyebrow[0].get_size()[11],self.eyebrow[0].get_size()[12], self.eyebrow[0].get_size()[13], self.eyebrow[0].get_size()[14],self.eyebrow[0].get_size()[15], self.eyebrow[0].get_size()[16], self.eyebrow[0].get_size()[17],self.eyebrow[0].get_size()[18], self.eyebrow[0].get_size()[19], self.eyebrow[0].get_size()[20],self.eyebrow[0].get_size()[21], self.eyebrow[0].get_size()[22], self.eyebrow[0].get_size()[23],self.eyebrow[0].get_size()[24], self.eyebrow[0].get_size()[25], self.eyebrow[0].get_size()[26],self.eyebrow[0].get_size()[27], self.eyebrow[0].get_size()[28], self.eyebrow[0].get_size()[29],self.eyebrow[0].get_size()[30], self.eyebrow[0].get_size()[31], self.eyebrow[0].get_size()[32],self.eyebrow[0].get_size()[33], self.eyebrow[0].get_size()[34]]
        eyebrow_left = QPolygonF(points)
        self.eyebrow_left = QtGui.QGraphicsPolygonItem(eyebrow_left)
        self.eyebrow_left.setBrush(QBrush(QColor(self.eyebrow[0].get_colour()[0]), style = QtCore.Qt.SolidPattern))
        points = [self.eyebrow[1].get_size()[0], self.eyebrow[1].get_size()[1], self.eyebrow[1].get_size()[2], self.eyebrow[1].get_size()[3], self.eyebrow[1].get_size()[4], self.eyebrow[1].get_size()[5], self.eyebrow[1].get_size()[6], self.eyebrow[1].get_size()[7], self.eyebrow[1].get_size()[8], self.eyebrow[1].get_size()[9], self.eyebrow[1].get_size()[10], self.eyebrow[1].get_size()[11], self.eyebrow[1].get_size()[12], self.eyebrow[1].get_size()[13], self.eyebrow[1].get_size()[14], self.eyebrow[1].get_size()[15], self.eyebrow[1].get_size()[16], self.eyebrow[1].get_size()[17],self.eyebrow[1].get_size()[18], self.eyebrow[1].get_size()[19], self.eyebrow[1].get_size()[20],self.eyebrow[1].get_size()[21], self.eyebrow[1].get_size()[22], self.eyebrow[1].get_size()[23],self.eyebrow[1].get_size()[24], self.eyebrow[1].get_size()[25], self.eyebrow[1].get_size()[26],self.eyebrow[1].get_size()[27], self.eyebrow[1].get_size()[28], self.eyebrow[1].get_size()[29],self.eyebrow[1].get_size()[30], self.eyebrow[1].get_size()[31], self.eyebrow[1].get_size()[32],self.eyebrow[1].get_size()[33], self.eyebrow[1].get_size()[34]]
        eyebrow_right = QPolygonF(points)
        self.eyebrow_right = QtGui.QGraphicsPolygonItem(eyebrow_right)
        self.eyebrow_right.setBrush(QBrush(QColor(self.eyebrow[1].get_colour()[0]), style = QtCore.Qt.SolidPattern))

        #MOUTH
        points = [self.mouth.get_size()[0], self.mouth.get_size()[1], self.mouth.get_size()[2],self.mouth.get_size()[3], self.mouth.get_size()[4], self.mouth.get_size()[5],self.mouth.get_size()[6], self.mouth.get_size()[7], self.mouth.get_size()[8],self.mouth.get_size()[9], self.mouth.get_size()[10], self.mouth.get_size()[11],self.mouth.get_size()[12], self.mouth.get_size()[13], self.mouth.get_size()[14],self.mouth.get_size()[15], self.mouth.get_size()[16], self.mouth.get_size()[17],self.mouth.get_size()[18], self.mouth.get_size()[19], self.mouth.get_size()[20],self.mouth.get_size()[21], self.mouth.get_size()[22], self.mouth.get_size()[23],self.mouth.get_size()[24], self.mouth.get_size()[25], self.mouth.get_size()[26],self.mouth.get_size()[27], self.mouth.get_size()[28], self.mouth.get_size()[29],self.mouth.get_size()[30], self.mouth.get_size()[31], self.mouth.get_size()[32],self.mouth.get_size()[33], self.mouth.get_size()[34]]
        mouth = QPolygonF(points)
        self.mouth = QtGui.QGraphicsPolygonItem(mouth)
        self.mouth.setBrush(QBrush(QColor(mc), style = QtCore.Qt.SolidPattern))

        #TONGUE
        points = [self.tongue.get_size()[0], self.tongue.get_size()[1], self.tongue.get_size()[2],self.tongue.get_size()[3], self.tongue.get_size()[4], self.tongue.get_size()[5],self.tongue.get_size()[6], self.tongue.get_size()[7], self.tongue.get_size()[8],self.tongue.get_size()[9], self.tongue.get_size()[10], self.tongue.get_size()[11],self.tongue.get_size()[12], self.tongue.get_size()[13], self.tongue.get_size()[14],self.tongue.get_size()[15], self.tongue.get_size()[16], self.tongue.get_size()[17],self.tongue.get_size()[18], self.tongue.get_size()[19], self.tongue.get_size()[20],self.tongue.get_size()[21], self.tongue.get_size()[22], self.tongue.get_size()[23],self.tongue.get_size()[24], self.tongue.get_size()[25], self.tongue.get_size()[26],self.tongue.get_size()[27], self.tongue.get_size()[28], self.tongue.get_size()[29],self.tongue.get_size()[30], self.tongue.get_size()[31], self.tongue.get_size()[32],self.tongue.get_size()[33], self.tongue.get_size()[34]]
        tongue = QPolygonF(points)
        self.tongue = QtGui.QGraphicsPolygonItem(tongue)
        self.tongue.setBrush(QBrush(QColor((lc)), style = QtCore.Qt.SolidPattern))


        self.scene.addItem(self.eye_left)
        self.scene.addItem(self.eye_right)
        self.scene.addItem(self.eyelid_up_left)
        self.scene.addItem(self.eyelid_up_right)
        self.scene.addItem(self.eyelid_down_left)
        self.scene.addItem(self.eyelid_down_right)
        if self.exist_iris == True:
            self.scene.addItem(self.iris_left)
            self.scene.addItem(self.iris_right)
        if self.exist_pupils == True:
            self.scene.addItem(self.pupil_left)
            self.scene.addItem(self.pupil_right)
        if self.exist_brightness == True:
            self.scene.addItem(self.reflex_pupil_left)
            self.scene.addItem(self.reflex_pupil_right)
        if self.exist_more_brightness == True:
            self.scene.addItem(self.reflex_pupil_left_2)
            self.scene.addItem(self.reflex_pupil_right_2)
        if self.exist_eyebrows == True:
            self.scene.addItem(self.eyebrow_left)
            self.scene.addItem(self.eyebrow_right)
        if self.exist_mouth == True:
            self.scene.addItem(self.tongue)
            self.scene.addItem(self.mouth)
        self.scene.addItem(self.item)
"""
    #def getangry(self):

        self.tl = QtCore.QTimeLine(4000)
        self.tl.setFrameRange(0, 100)
        self.a = QtGui.QGraphicsItemAnimation()
        self.a.setItem(self.item)
        self.a.setTimeLine(self.tl)
        self.a.setPosAt(0, QtCore.QPointF(100, 100))
        self.a.setRotationAt(1, 90)
        #elf.tl.start()

        #self.angry_eyebrow = QtGui.QGraphicsItemAnimation()
        #self.angry_eyebrow.setItem(self.eyebrow_left)
        #self.angry_eyebrow.setTimeLine(self.tl)
        #self.angry_eyebrow.setRotationAt(1, 25)
        self.happytl = QtCore.QTimeLine(1500)
        self.happytl.setFrameRange(0, 100)
        self.happy_eyebrow_left = QtGui.QGraphicsItemAnimation()
        self.happy_eyebrow_left.setItem(self.eyebrow_left)
        self.happy_eyebrow_left.setTimeLine(self.happytl)
        self.happy_eyebrow_left.setTranslationAt(1,0,-20)

        self.happy_eyebrow_right = QtGui.QGraphicsItemAnimation()
        self.happy_eyebrow_right.setItem(self.eyebrow_right)
        self.happy_eyebrow_right.setTimeLine(self.happytl)
        self.happy_eyebrow_right.setTranslationAt(1,0,-20)

        self.happy_eyelid_up_left = QtGui.QGraphicsItemAnimation()
        self.happy_eyelid_up_left.setItem(self.eyelid_up_left)
        self.happy_eyelid_up_left.setTimeLine(self.happytl)
        self.happy_eyelid_up_left.setTranslationAt(1,0,-20)

        self.happy_eyelid_up_right = QtGui.QGraphicsItemAnimation()
        self.happy_eyelid_up_right.setItem(self.eyelid_up_right)
        self.happy_eyelid_up_right.setTimeLine(self.happytl)
        self.happy_eyelid_up_right.setTranslationAt(1,0,-20)

        self.happy_eye_left = QtGui.QGraphicsItemAnimation()
        self.happy_eye_left.setItem(self.eye_left)
        self.happy_eye_left.setTimeLine(self.happytl)
        self.happy_eye_left.setTranslationAt(1,0,-20)

        self.happy_eye_right = QtGui.QGraphicsItemAnimation()
        self.happy_eye_right.setItem(self.eye_right)
        self.happy_eye_right.setTimeLine(self.happytl)
        self.happy_eye_right.setTranslationAt(1,0,-20)
        self.happy_eye_right.setTranslationAt(1,-20,0)


        self.happy_eyelid_down_left = QtGui.QGraphicsItemAnimation()
        self.happy_eyelid_down_left.setItem(self.eyelid_down_left)
        self.happy_eyelid_down_left.setTimeLine(self.happytl)
        self.happy_eyelid_down_left.setTranslationAt(1,0,-80)

        self.happy_eyelid_down_right = QtGui.QGraphicsItemAnimation()
        self.happy_eyelid_down_right.setItem(self.eyelid_down_right)
        self.happy_eyelid_down_right.setTimeLine(self.happytl)
        self.happy_eyelid_down_right.setTranslationAt(1,0,-80)

        self.happytl.start()

"""


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    view = Face()
    view.show()
    sys.exit(app.exec_())
