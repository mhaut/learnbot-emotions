import RPi.GPIO as GPIO    
import math
import time                

GPIO.setmode(GPIO.BOARD)   #Raspberry BOARD mode
GPIO.setup(40,GPIO.OUT)    
p = GPIO.PWM(40,50)        #Pin 40 in PWM and frequency 50 pulse/sec

#Minimum degrees allowed  0,472pi(85degrees)
#Maximum degrees allowed pi/1.5 (120 degrees)
class Servo():
    def __init__(self):
        self.angle=4.675# default minimum
        self.acc_angle=0.0
            
    def set_init(self):
        #angle = 4.675 #default 0,472pi rad, 85 degrees (4.675)
        p.start(0.01)           
        p.ChangeDutyCycle(self.angle) 
        time.sleep(1)
        self.acc_angle=self.angle

    def set_move(self,angle):
        angle = math.degrees(angle)
        angle = 0.055*angle
        p.ChangeDutyCycle(angle)
        time.sleep(5)
        self.acc_angle=angle

    def get_angle(self):
        angle = math.radians(self.acc_angle/0.055)
        return angle
            
    def stop_servo(self):
        p.stop()                      
        GPIO.cleanup()


if __name__ =="__main__":
    servo = Servo()
    servo.set_init()
    servo.set_move(math.pi/1.5)
    print servo.get_angle()
    servo.set_init()
    servo.stop_servo()
    
