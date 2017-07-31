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








class paintLearnbot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        L_eye = Eye()
        L_eye.setEyecolor('#4192D9')
        L_eye.setEyeSize(60, 80, 180, 240)
        R_eye = Eye()
        R_eye.setEyecolor('#4192D9')
        R_eye.setEyeSize(300, 80, 420, 240)
        colourL = L_eye.getEyecolor()
        sizeL = [L_eye.getEyeSize()[0], L_eye.getEyeSize()[1], L_eye.getEyeSize()[2], L_eye.getEyeSize()[3]]
        colourR = R_eye.getEyecolor()
        sizeR = [R_eye.getEyeSize()[0], R_eye.getEyeSize()[1], R_eye.getEyeSize()[2], R_eye.getEyeSize()[3]]

        self.canvas = tk.Canvas(width=480, height=320, background='black')
        self.canvas.pack()
        self.eye = self.canvas.create_oval(sizeL[0], sizeL[1], sizeL[2], sizeL[3], outline=colourL, fill=colourL)
        self.eye = self.canvas.create_oval(sizeR[0], sizeR[1], sizeR[2], sizeR[3], outline=colourR, fill=colourR)






if __name__ == "__main__":
    app = paintLearnbot()
    app.mainloop()
