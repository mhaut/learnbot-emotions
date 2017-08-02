import Tkinter as tk
import time, math


class BaseHead(object):
	def __init__(self):
		self.colour = "blue"
		self.size = None

	def set_colour(self, colour):
		self.colour = colour

	def set_size(self, x0, y0, x1, y1):
		self.size = [x0, y0, x1, y1]

	def get_colour(self):
		return self.colour

	def get_size(self):
		return self.size


class Eye(BaseHead):
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
		self.left_eye = Eye()
		self.right_eye = Eye()
		self.left_eyebrow = EyeBrow()
		self.right_eyebrow = EyeBrow()
		self.eyelids = None
		self.mouth = Mouth()

	def set_eye(self, eye, position):
		if position == "left":
			self.left_eye = eye
		elif position == "right":
			self.right_eye = eye
		else:
			print("ERROR: Position eye set")
			exit()

	def get_eye(self, position):
		if position == "left":
			return self.left_eye
		elif position == "right":
			return self.right_eye
		else:
			print("ERROR: Position eye get")
			exit()

	def set_eyebrow(self, eyebrow, position):
		if position == "left":
			self.left_eyebrow = eyebrow
		elif position == "right":
			self.right_eyebrow = eyebrow
		else:
			print("ERROR: Position eyebrow set")
			exit()

	def get_eyebrow(self, position):
		if position == "left":
			return self.left_eyebrow
		elif position == "right":
			return self.right_eyebrow
		else:
			print("ERROR: Position eyebrow get")
			exit()

	def set_eyelids(self, lu_eyeLid, ld_eyeLid, ru_eyeLid, rd_eyeLid):
		self.eyelids = [lu_eyeLid, ld_eyeLid, ru_eyeLid, rd_eyeLid]

	def get_eyelids(self):
		return self.eyelids



class DefiningLearnbot(tk.Tk):
	def __init__(self):
		self.face = Face()
		self.draw_eyelid = [None, None, None, None]

		# Defining Eyes
		L_eye = Eye()
		L_eye.set_colour('#4192D9')
		L_eye.set_size(60, 80, 180, 240)
		self.face.set_l_eye(L_eye)

		R_eye = Eye()
		R_eye.set_colour('#4192D9')
		R_eye.set_size(300, 80, 420, 240)
		self.face.set_r_eye(R_eye)

		# Defining Eyelid
		Lu_eyeLid = EyeLid()
		Lu_eyeLid.set_colour('black')
		Lu_eyeLid.set_size(40, 0, 200, 80)

		Ld_eyeLid = EyeLid()
		Ld_eyeLid.set_colour('black')
		Ld_eyeLid.set_size(40, 240, 200, 320)

		Ru_eyeLid = EyeLid()
		Ru_eyeLid.set_colour('black')
		Ru_eyeLid.set_size(280, 0, 440, 80)

		Rd_eyeLid = EyeLid()
		Rd_eyeLid.set_colour('black')
		Rd_eyeLid.set_size(280, 240, 440, 320)

		self.face.set_eyelids(Lu_eyeLid, Ld_eyeLid, Ru_eyeLid, Rd_eyeLid)

		# Simplifying
		colourL = self.face.get_l_eye().get_colour()
		sizeL = self.face.get_l_eye().get_size()
		colourR = self.face.get_r_eye().get_colour()
		sizeR = self.face.get_r_eye().get_size()

		colour_lue = self.face.get_eyelids()[0].get_colour()
		colour_lde = self.face.get_eyelids()[1].get_colour()
		colour_rue = self.face.get_eyelids()[2].get_colour()
		colour_rde = self.face.get_eyelids()[3].get_colour()
		size_lue = self.face.get_eyelids()[0].get_size()
		size_lde = self.face.get_eyelids()[1].get_size()
		size_rue = self.face.get_eyelids()[2].get_size()
		size_rde = self.face.get_eyelids()[3].get_size()

		# Drawing
		self.canvas = tk.Canvas(width=480, height=320, background='black')
		self.canvas.pack()
		eye = self.canvas.create_oval(sizeL[0], sizeL[1], sizeL[2], sizeL[3], outline=colourL, fill=colourL)
		eye = self.canvas.create_oval(sizeR[0], sizeR[1], sizeR[2], sizeR[3], outline=colourR, fill=colourR)

		self.draw_eyelid[0] = self.canvas.create_rectangle(size_lue[0], size_lue[1], size_lue[2], size_lue[3],
														outline=colour_lue,
														fill=colour_lue)
		self.draw_eyelid[1] = self.canvas.create_rectangle(size_lde[0], size_lde[1], size_lde[2], size_lde[3],
														outline=colour_lde,
														fill=colour_lde)
		self.draw_eyelid[2] = self.canvas.create_rectangle(size_rue[0], size_rue[1], size_rue[2], size_rue[3],
														outline=colour_rue,
														fill=colour_rue)
		self.draw_eyelid[3] = self.canvas.create_rectangle(size_rde[0], size_rde[1], size_rde[2], size_rde[3],
														outline=colour_rde,
														fill=colour_rde)


class Status(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.state = None
		self.paint = DefiningLearnbot()

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
