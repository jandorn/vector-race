from re import I
import anki_vector
import time
from anki_vector.motors import *
from anki_vector.util import *
from anki_vector.exceptions import *

MAX_SPEED = 150
BOOST_SPEED = 220
SLOW_SPEED = 100
SLEEP_TIME = 0.05


def DriveStraight(robot):
    try:
        robot.motors.set_wheel_motors(MAX_SPEED, MAX_SPEED)
        time.sleep(SLEEP_TIME)
        print("done")
    except Exception:
        print("Exception thrown")
        pass
    
    
def DriveRight(robot, steering_intensity):
    robot.motors.set_wheel_motors(MAX_SPEED, steering_intensity)
    time.sleep(0.1)
    print("done")
    
    
def DriveLeft(robot, steering_intensity):
    robot.motors.set_wheel_motors(steering_intensity, MAX_SPEED)
    time.sleep(0.1)
    print("done")
    
       
def DriveStop(robot):
    try:       
        robot.motors.stop_all_motors()
        print("done")
    except Exception:
        print("Exception thrown")
        pass

def BananaCollision(robot):
    print("Banana")
    robot.motors.set_wheel_motors(180, -180)
    time.sleep(1)

