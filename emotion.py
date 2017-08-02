#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import Tkinter as tk
import time, math

import headrobot





class Status(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.state = None
		self.paint = headrobot.DefiningLearnbot()

	def setStatus(self, status):
		self.status = status

	def getStatus(self):
		return self.status

	def display_status(self):
		if self.status == 'happiness':
			circlehappy1 = self.paint.canvas.create_oval(20, 240, 220, 440, fill="black")
			circlehappy2 = self.paint.canvas.create_oval(260, 240, 460, 440, fill="black")
			x = 0
			y = 2.3
			for i in range(0, 51):
				time.sleep(0.01)
				self.paint.canvas.move(circlehappy1, x, -y)
				self.paint.canvas.move(circlehappy2, x, -y)
				self.paint.canvas.update()
			time.sleep(0.1)
		elif self.status == 'angry':
			xy = [(60.2, -94.48), (218.16, -36.08), (188.96, 38.4), (40, -20)]
			angryUle = self.paint.canvas.create_polygon(xy, fill="black")  # Up|Left  eyelid
			xy2 = [(291.04, 38.4), (440, -20), (410.8, -94.48), (261.84, -36.08)]
			angryUre = self.paint.canvas.create_polygon(xy2, fill="black")  # Up|Right  eyelid
			angryDle = self.paint.canvas.create_rectangle(40, 320, 200, 400, fill="black")  # Down|Left  eyelid
			angryDre = self.paint.canvas.create_rectangle(280, 320, 440, 400, fill="black")  # Down|Right eyelid
			x = 0
			y = 2.3
			for i in range(0, 51):
				time.sleep(0.01)
				self.paint.canvas.move(angryUle, x, y)
				self.paint.canvas.move(angryUre, x, y)
				self.paint.canvas.move(angryDle, x, -y)
				self.paint.canvas.move(angryDre, x, -y)
				self.paint.canvas.update()

			time.sleep(0.1)
		elif self.status == 'sadness':
			x = 0
			y = 2
			xy = [(11.04, 8.4), (160, -50), (189.2, 24.48), (40.24, 82.88)]
			sadUle = self.paint.canvas.create_polygon(xy, fill="black")  # Up|Left  eyelid
			xy2 = [(320, -50), (468.96, 8.4), (439.76, 82.27), (290.8, 24.48)]
			sadUre = self.paint.canvas.create_polygon(xy2, fill="black")  # Up|Right  eyelid
			for i in range(0, 51):
				time.sleep(0.01)
				self.paint.canvas.move(sadUle, x, y)
				self.paint.canvas.move(sadUre, x, y)
				self.paint.canvas.update()
			time.sleep(0.1)
		elif self.status =='scared':
			x = 0
			y = 1
			circlescared1 = self.paint.canvas.create_oval(-10, 240, 190, 440, fill="black")
			circlescared2 = self.paint.canvas.create_oval(290, 240, 490, 440, fill="black")
			for i in range(0, 51):
				time.sleep(0.01)
				self.paint.canvas.move(circlescared1, x, -y)
				self.paint.canvas.move(circlescared2, x, -y)
				self.paint.canvas.update()
			time.sleep(0.1)
		else:
			track = 0
			while True:
				x = 0
				y = 1.4

				if track == 0:
					for i in range(0, 51):
						time.sleep(0.01)
						self.paint.canvas.move(self.paint.draw_eyelid[0], x, y)
						self.paint.canvas.move(self.paint.draw_eyelid[1], x, -y)
						self.paint.canvas.move(self.paint.draw_eyelid[2], x, y)
						self.paint.canvas.move(self.paint.draw_eyelid[3], x, -y)
						self.paint.canvas.update()
					track = 1
					time.sleep(0.1)

				else:
					for i in range(0, 51):
						time.sleep(0.01)
						self.paint.canvas.move(self.paint.draw_eyelid[0], x, -y)
						self.paint.canvas.move(self.paint.draw_eyelid[1], x, y)
						self.paint.canvas.move(self.paint.draw_eyelid[2], x, -y)
						self.paint.canvas.move(self.paint.draw_eyelid[3], x, y)
						self.paint.canvas.update()
					track = 0
					time.sleep(4)


if __name__ == "__main__":
	app = Status()
	app.setStatus('scared')
	app.display_status()
	app.mainloop()
