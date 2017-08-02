#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import Tkinter as tk

class BaseHead(object):
	def __init__(self):
		self.colour = "blue"
		self.size = None

	def set_colour(self, colour):
		self.colour = colour

	def set_size(self, points):
		#points = x0, y0, x1, y1
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
	def __init__(self):
		self.eyes = [Eye(), Eye()]
		self.eyebrows = [EyeBrow(), EyeBrow()]
		self.right_eyebrow = EyeBrow()
		self.eyelids = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
		self.mouth = Mouth()

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




if __name__ == "__main__":
	tk.Tk.__init__()
	face = Face()
	draw_eyelid = [None, None, None, None]

	for eye, size_eye in zip(face.eyes, [[60, 80, 180, 240], [300, 80, 420, 240]]):
		eye.set_colour('#4192D9')
		eye.set_size(size_eye)

	for eyelid, size_eyelid in zip(face.eyelids, [[40, 0, 200, 80], [40, 240, 200, 320], [280, 0, 440, 80], [280, 240, 440, 320]]):
		eyelid.set_colour('black')
		eyelid.set_size(size_eyelid)

	# Drawing
	canvas = tk.Canvas(width=480, height=320, background='black')
	canvas.pack()
	eye_left = canvas.create_oval(face.get_eye("left").get_size(), outline=face.get_eye("left").get_colour(), fill=face.get_eye("left").get_colour())
	eye_right = canvas.create_oval(face.get_eye("right").get_size(), outline=face.get_eye("right").get_colour(), fill=face.get_eye("right").get_colour())

	colour_lue = face.get_eyelids()[0].get_colour()
	colour_lde = face.get_eyelids()[1].get_colour()
	colour_rue = face.get_eyelids()[2].get_colour()
	colour_rde = face.get_eyelids()[3].get_colour()
	size_lue = face.get_eyelids()[0].get_size()
	size_lde = face.get_eyelids()[1].get_size()
	size_rue = face.get_eyelids()[2].get_size()
	size_rde = face.get_eyelids()[3].get_size()

	draw_eyelid[0] = canvas.create_rectangle(size_lue[0], size_lue[1], size_lue[2], size_lue[3],
													outline=colour_lue,
													fill=colour_lue)
	draw_eyelid[1] = canvas.create_rectangle(size_lde[0], size_lde[1], size_lde[2], size_lde[3],
													outline=colour_lde,
													fill=colour_lde)
	draw_eyelid[2] = canvas.create_rectangle(size_rue[0], size_rue[1], size_rue[2], size_rue[3],
													outline=colour_rue,
													fill=colour_rue)
	draw_eyelid[3] = canvas.create_rectangle(size_rde[0], size_rde[1], size_rde[2], size_rde[3],
													outline=colour_rde,
													fill=colour_rde)
	print("fin")
