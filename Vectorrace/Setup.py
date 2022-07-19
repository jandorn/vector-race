import anki_vector
from anki_vector.util import *
from anki_vector.motors import *

def startRobot(robot):
    #Connect to Vector
    robot.connect()

    #Setup
    robot.behavior.set_head_angle(degrees(0))


def closeRobot(robot):
    #Get on Charger 
    robot.behavior.drive_on_charger()
    
    #Disconnect Vector
    robot.disconnect()
