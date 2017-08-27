#import readchar
from termios import tcflush, TCIFLUSH
import sys
import json
import load_json as load

def loadConfiguration():
    end = False
    while end!=True:
        name = raw_input("How I look today (cozmo,oval,round, base_head, base_emotions)")
        if name == "cozmo" or name == "oval" or name == "round" or name == "base_head" or name == "base_emotions":
            end = True
        else:
            print "Can you repeat, please?"
    change= False
    with open(name + '.json', 'r+') as data_file:
        file = json.load(data_file)
        if file["eyebrow_left"]["exist"]== "yes":
            eyebrow=True
        else:
            eyebrow=False
        if file["iris_left"]["exist"] == "yes":
            iris=True
        else:
            iris=False
        if file["pupil_left"]["exist"] =="yes":
            pupils = True
        else:
            pupils=False
        if file["reflex_pupil_left"]["exist"] == "yes":
            brightness = True
        else:
            brightness = False
        if file["reflex_pupil_left_2"]["exist"] == "yes":
            more_brightness = True
        else:
            more_brightness = False
        if file["mouth"]["exist"]== "yes":
            mouth=True
        else:
            mouth=False
        while change != True:
            print "Do you want to change the default setting? ( press y or n )"
            char = raw_input("")
            if char == "y":
                end = False
                while end != True:
                    print "Have I eyebrows? ( press y or n )"
                    char = raw_input("")
                    if char == "y":
                        eyebrow=True
                        load.create_part(name,"eyebrow_left")
                        load.create_part(name,"eyebrow_right")
                        end = True
                    elif char == "n":
                        eyebrow=False
                        load.delete_part(name,"eyebrow_left")
                        load.delete_part(name,"eyebrow_right")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False
                while end!=True:
                    print "Have I iris? ( press y or n and enter)"
                    char = raw_input("")
                    if char == "y":
                        iris=True
                        load.create_part(name,"iris_left")
                        load.create_part(name,"iris_right")
                        end = True
                    elif char == "n":
                        iris=False
                        load.delete_part(name,"iris_left")
                        load.delete_part(name,"iris_right")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False
                while end!=True:
                    print "Have I pupils? ( press y or n )"
                    char = raw_input("")
                    if char == "y":
                        pupils=True
                        load.create_part(name,"pupil_left")
                        load.create_part(name,"pupil_right")
                        end = True
                    elif char == "n":
                        pupils=False
                        load.delete_part(name,"pupil_left")
                        load.delete_part(name,"pupil_right")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False
                while end!=True:
                    print "Have I brightness in my eyes? ( press y or n )"
                    char = raw_input("")
                    if char == "y":
                        brightness=True
                        pupils=True
                        load.create_part(name,"reflex_pupil_left")
                        load.create_part(name,"reflex_pupil_right")
                        end = True
                    elif char == "n":
                        brightness=False
                        load.delete_part(name,"reflex_pupil_left")
                        load.delete_part(name,"reflex_pupil_right")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False

                while end!=True:
                    print "Have I more brightness in my eyes? ( press y or n )"
                    char = raw_input("")
                    if char == "y":
                        more_brightness=True
                        load.create_part(name,"reflex_pupil_left_2")
                        load.create_part(name,"reflex_pupil_right_2")
                        end = True
                    elif char == "n":
                        more_brightness=False
                        load.delete_part(name,"reflex_pupil_left_2")
                        load.delete_part(name,"reflex_pupil_right_2")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False
                while end!=True:
                    print "Have I mouth? (press y or n)"
                    char = raw_input("")
                    if char == "y":
                        mouth=True
                        load.create_part(name,"mouth")
                        load.create_part(name,"tongue")
                        end = True
                    elif char == "n":
                        mouth=False
                        load.delete_part(name,"mouth")
                        load.delete_part(name,"tongue")
                        end = True
                    else:
                        print "Can you repeat, please?"
                        tcflush(sys.stdin, TCIFLUSH)
                end = False
                change=True
            elif char == "n":
                change=True
                #tcflush(sys.stdin, TCIFLUSH)
            else:
                print "Can you repeat, please?"
                tcflush(sys.stdin, TCIFLUSH)
            res =[name,eyebrow,iris,pupils,brightness,more_brightness,mouth]
    return res

