import Tkinter as tk
import time
import load_json as paint
import getch


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
        self.brightness = [Brightness(),Brightness()]


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
        self.pupil= [Pupil(),Pupil()]
        self.eyebrow = [EyeBrow(), EyeBrow()]
        self.eyelid = [EyeLid(), EyeLid(), EyeLid(), EyeLid()]
        self.mouth = Mouth()
        self.tongue = Tongue()
        self.status = "neutral"

        self.canvas = tk.Canvas(width=480, height=320, background='black')
        self.canvas.pack()

        self.eyes[0].set_size(paint.checkPaint(name,paint.load_file(name))[0])
        self.eyes[0].set_colour(paint.checkPaint(name,paint.load_file(name))[1])
        self.eyes[1].set_size(paint.checkPaint(name,paint.load_file(name))[2])
        self.eyes[1].set_colour(paint.checkPaint(name,paint.load_file(name))[3])

        self.eyelid[0].set_size(paint.checkPaint(name,paint.load_file(name))[4])
        self.eyelid[0].set_colour(paint.checkPaint(name,paint.load_file(name))[5])
        self.eyelid[1].set_size(paint.checkPaint(name,paint.load_file(name))[6])
        self.eyelid[1].set_colour(paint.checkPaint(name,paint.load_file(name))[7])
        self.eyelid[2].set_size(paint.checkPaint(name,paint.load_file(name))[8])
        self.eyelid[2].set_colour(paint.checkPaint(name,paint.load_file(name))[9])
        self.eyelid[3].set_size(paint.checkPaint(name,paint.load_file(name))[10])
        self.eyelid[3].set_colour(paint.checkPaint(name,paint.load_file(name))[11])

        self.iris[0].set_size(paint.checkPaint(name,paint.load_file(name))[12])
        self.iris[0].set_colour(paint.checkPaint(name,paint.load_file(name))[13])
        self.iris[1].set_size(paint.checkPaint(name,paint.load_file(name))[14])
        self.iris[1].set_colour(paint.checkPaint(name,paint.load_file(name))[15])

        self.pupil[0].set_size(paint.checkPaint(name,paint.load_file(name))[16])
        self.pupil[0].set_colour(paint.checkPaint(name,paint.load_file(name))[17])
        self.pupil[1].set_size(paint.checkPaint(name,paint.load_file(name))[18])
        self.pupil[1].set_colour(paint.checkPaint(name,paint.load_file(name))[19])

        self.pupil[0].brightness[0].set_size(paint.checkPaint(name,paint.load_file(name))[20])
        self.pupil[0].brightness[0].set_colour(paint.checkPaint(name,paint.load_file(name))[21])
        self.pupil[0].brightness[1].set_size(paint.checkPaint(name,paint.load_file(name))[22])
        self.pupil[0].brightness[1].set_colour(paint.checkPaint(name,paint.load_file(name))[23])
        self.pupil[1].brightness[0].set_size(paint.checkPaint(name,paint.load_file(name))[24])
        self.pupil[1].brightness[0].set_colour(paint.checkPaint(name,paint.load_file(name))[25])
        self.pupil[1].brightness[1].set_size(paint.checkPaint(name,paint.load_file(name))[26])
        self.pupil[1].brightness[1].set_colour(paint.checkPaint(name,paint.load_file(name))[27])

        self.eyebrow[0].set_size(paint.checkPaint(name,paint.load_file(name))[28])
        self.eyebrow[0].set_colour(paint.checkPaint(name,paint.load_file(name))[29])
        self.eyebrow[1].set_size(paint.checkPaint(name,paint.load_file(name))[30])
        self.eyebrow[1].set_colour(paint.checkPaint(name,paint.load_file(name))[31])

        self.mouth.set_size(paint.checkPaint(name,paint.load_file(name))[32])
        self.mouth.set_colour(paint.checkPaint(name,paint.load_file(name))[33])

        self.tongue.set_size(paint.checkPaint(name,paint.load_file(name))[34])
        self.tongue.set_colour(paint.checkPaint(name,paint.load_file(name))[35])


        eye_l=self.canvas.create_polygon ( self.eyes[0].get_size(), fill=self.eyes[0].get_colour() )
        eye_r=self.canvas.create_polygon ( self.eyes[1].get_size(), fill=self.eyes[1].get_colour() )
        self.eyelid_u_l=self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
        self.eyelid_u_r=self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
        self.eyelid_d_l=self.canvas.create_polygon(self.eyelid[2].get_size(), fill=self.eyelid[2].get_colour())
        self.eyelid_d_r=self.canvas.create_polygon(self.eyelid[3].get_size(), fill=self.eyelid[3].get_colour())
        self.canvas.create_polygon ( self.iris[0].get_size(), fill=self.iris[0].get_colour() )
        self.canvas.create_polygon ( self.iris[1].get_size(), fill=self.iris[1].get_colour() )
        self.canvas.create_polygon ( self.pupil[0].get_size(), fill=self.pupil[1].get_colour() )
        self.canvas.create_polygon ( self.pupil[1].get_size(), fill=self.pupil[1].get_colour() )
        self.canvas.create_polygon ( self.pupil[0].brightness[0].get_size(),fill=self.pupil[0].brightness[0].get_colour() )
        self.canvas.create_polygon ( self.pupil[0].brightness[1].get_size(),fill=self.pupil[0].brightness[1].get_colour() )
        self.canvas.create_polygon ( self.pupil[1].brightness[0].get_size(),fill=self.pupil[0].brightness[0].get_colour())
        self.canvas.create_polygon ( self.pupil[1].brightness[1].get_size(),fill=self.pupil[0].brightness[1].get_colour())
        self.canvas.create_polygon ( self.eyebrow[0].get_size(),fill=self.eyebrow[0].get_colour()  )
        self.canvas.create_polygon ( self.eyebrow[1].get_size(),fill=self.eyebrow[1].get_colour()  )
        self.canvas.create_polygon ( self.mouth.get_size(),fill=self.mouth.get_colour() )
        self.canvas.create_polygon ( self.tongue.get_size(),fill=self.tongue.get_colour() )


    def change_status(self):
        print "You can change status by pressing"
        print " n    if you want the state to be neutral"
        print " a    if you want the state to be angry"
        print " h    if you want the state to be happiness"
        print " s    if you want the state to be sadness"
        print " x    if you want the state to be scared"
        print " d    if you want the state to be disgust"
        print " By default the state is neutral"

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
                time.sleep(4)
                if KeyboardInterrupt:
                        change_state = False# limpiar buffer
        #char = getch.getch()

"""
    def change_status(self, status):

        if self.status == 'angry':
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
        self.status = "neutral"
        for j in xrange(0,5):
            xul=[]
            yul=[]
            xur=[]
            yur=[]
            xdl=[]
            ydl=[]
            xdr=[]
            ydr=[]

            for i in xrange(0,18):
                xul.append(self.eyelid[0].get_size()[i][0])
                yul.append(self.eyelid[0].get_size()[i][1]+((140-self.eyelid[0].get_size()[i][1])/2.5))
                xur.append(self.eyelid[1].get_size()[i][0])
                yur.append(self.eyelid[1].get_size()[i][1]+((140-self.eyelid[1].get_size()[i][1])/2.5))
                xdl.append(self.eyelid[2].get_size()[i][0])
                ydl.append(self.eyelid[2].get_size()[i][1]+((140-self.eyelid[2].get_size()[i][1])/2.5))
                xdr.append(self.eyelid[3].get_size()[i][0])
                ydr.append(self.eyelid[3].get_size()[i][1]+((140-self.eyelid[3].get_size()[i][1])/2.5))
            for i in xrange(18,35):
                xul.append(self.eyelid[0].get_size()[i][0])
                yul.append(self.eyelid[0].get_size()[i][1])
                xur.append(self.eyelid[1].get_size()[i][0])
                yur.append(self.eyelid[1].get_size()[i][1])
                xdl.append(self.eyelid[2].get_size()[i][0])
                ydl.append(self.eyelid[2].get_size()[i][1])
                xdr.append(self.eyelid[3].get_size()[i][0])
                ydr.append(self.eyelid[3].get_size()[i][1])

            res=zip(xul,yul)
            res2 = zip(xur, yur)
            res3=zip(xdl,ydl)
            res4 = zip(xdr, ydr)

            self.eyelid[0].set_size(res)
            self.eyelid[1].set_size(res2)
            self.eyelid[2].set_size(res3)
            self.eyelid[3].set_size(res4)

            time.sleep(1)

            eyelid_u_l=self.canvas.create_polygon(self.eyelid[0].get_size(), fill=self.eyelid[0].get_colour())
            eyelid_u_r = self.canvas.create_polygon(self.eyelid[1].get_size(), fill=self.eyelid[1].get_colour())
            eyelid_d_l = self.canvas.create_polygon(self.eyelid[2].get_size(), fill=self.eyelid[2].get_colour())
            eyelid_d_r = self.canvas.create_polygon(self.eyelid[3].get_size(), fill=self.eyelid[3].get_colour())

            self.canvas.update()

        time.sleep(3)

"""

def loadConfiguration(name):
    change= False
    while change != True:
        print "Do you want to change the default setting? (press y or n and enter)"
        char = getch.getch()
        if char == "y":
            end = False
            while end != True:
                print "Have I eyebrows? (press y or n and enter)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name,"eyebrow_left")
                    paint.create_part(name, "eyebrow_right")
                    end = True
                elif char == "n":
                    paint.delete_part(name,"eyebrow_left")
                    paint.delete_part(name, "eyebrow_right")
                    end = True
                else:
                    print "Can you repeat, please?"
                    char = getch.getch()
            end = False
            while end!=True:
                print "Have I iris? (press y or n and enter)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name,"iris_left")
                    paint.create_part(name, "iris_right")
                    end = True
                elif char == "n":
                    paint.delete_part(name,"iris_left")
                    paint.delete_part(name, "iris_right")
                    end = True
                else:
                    print "Can you repeat, please?"
            end = False
            while end!=True:
                print "Have I pupils? (press y or n and enter)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name,"pupil_left")
                    paint.create_part(name, "pupil_right")
                    end = True
                elif char == "n":
                    paint.delete_part(name,"pupil_left")
                    paint.delete_part(name, "pupil_right")
                    end = True
                else:
                    print "Can you repeat, please?"

            end = False
            while end!=True:
                print "Have I brightness in my eyes? (press y or n and enter)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name,"reflex_pupil_left")
                    paint.create_part(name, "reflex_pupil_right")
                    end = True
                elif char == "n":
                    paint.delete_part(name,"reflex_pupil_left")
                    paint.delete_part(name, "reflex_pupil_right")
                    end = True
                else:
                    print "Can you repeat, please?"

            end = False
            while end!=True:
                print "Have I more brightness in my eyes? (press y or n and enter)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name, "reflex_pupil_left_2")
                    paint.create_part(name, "reflex_pupil_right_2")
                    end = True
                elif char == "n":
                    paint.delete_part(name, "reflex_pupil_left_2")
                    paint.delete_part(name, "reflex_pupil_right_2")
                    end = True
                else:
                    print "Can you repeat, please?"

            end = False
            while end!=True:
                print "Have I mouth? (press y or n)"
                char = getch.getch()
                char = getch.getch()
                if char == "y":
                    paint.create_part(name, "mouth")
                    paint.create_part(name, "tongue")
                    end = True
                elif char == "n":
                    paint.delete_part(name, "mouth")
                    paint.delete_part(name, "tongue")
                    end = True
                else:
                    print "Can you repeat, please?"
            change=True
        elif char == "n":
            change=True
        else:
            print "Can you repeat, please?"
            char = getch.getch()



if __name__ == "__main__":
    root = tk.Tk()
    end = False
    while end!=True:
        name = raw_input("How I look today (cozmo,oval,round)")
        if name == "cozmo" or name == "oval" or name == "round":
            end = True
        else:
            print "Can you repeat, please?"
    loadConfiguration(name)
    face = Face(name)
    face.change_status()
    #root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.quit())
    root.mainloop()
