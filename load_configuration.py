import readchar
from termios import tcflush, TCIFLUSH
import sys
import load_json as paint


def loadConfiguration():
    end = False
    while end!=True:
        name = raw_input("How I look today (cozmo,oval,round)")
        if name == "cozmo" or name == "oval" or name == "round":
            end = True
        else:
            print "Can you repeat, please?"
    change= False
    while change != True:
        print "Do you want to change the default setting? ( press y or n )"
        char = readchar.readkey()
        if char == "y":
            end = False
            while end != True:
                print "Have I eyebrows? ( press y or n )"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)
            while end!=True:
                print "Have I iris? ( press y or n and enter)"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)
            while end!=True:
                print "Have I pupils? ( press y or n )"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)
            while end!=True:
                print "Have I brightness in my eyes? ( press y or n )"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)

            while end!=True:
                print "Have I more brightness in my eyes? ( press y or n )"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)
            while end!=True:
                print "Have I mouth? (press y or n)"
                char = readchar.readkey()
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
                    tcflush(sys.stdin, TCIFLUSH)
            end = False
            tcflush(sys.stdin, TCIFLUSH)
            change=True
        elif char == "n":
            change=True
            tcflush(sys.stdin, TCIFLUSH)
        else:
            print "Can you repeat, please?"
            tcflush(sys.stdin, TCIFLUSH)
    return name
loadConfiguration()
