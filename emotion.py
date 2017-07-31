import Tkinter as tk
import time, math

class Eye():
    def __init__(self):
        self.color = ""
        self.size = [0.0, 0.0, 0.0, 0.0]
        #self.eye = self.canvas.create_oval(60, 80, 180, 240, outline='#4192D9', fill="#4192D9")

    def setEyecolor(self,color):
        self.color=color

    def setEyeSize(self,x1,y1,x2,y2):
        self.size[0] = x1
        self.size[1] = y1
        self.size[2] = x2
        self.size[3] = y2


    def getEyecolor(self):
        return self.color

    def getEyeSize(self):
        return self.size[0],self.size[1],self.size[2],self.size[3]






def defineLearnbot(colour,size):
    L_eye = Eye()
    colour = L_eye.setEyecolor('#4192D9')
    L_eye.setEyeSize(60, 80, 180, 240)
    size = [ L_eye.getEyeSize()[0],L_eye.getEyeSize()[1],L_eye.getEyeSize()[2],L_eye.getEyeSize()[3]]
    print colour
    print size[2]

class paintLearnbot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #defineLearnbot(colour,size)

        self.canvas = tk.Canvas(width=480, height=320, background='black')
        self.canvas.pack()

        #lEye.getEyeSize(x1, y1, x2, y2)
        #self.eye = self.canvas.create_oval(x1, y1, x2, y2, outline='#4192D9', fill="#4192D9")






if __name__ == "__main__":
    app = paintLearnbot()
    app.mainloop()
