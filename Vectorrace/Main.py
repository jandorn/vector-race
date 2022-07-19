import anki_vector
from anki_vector.util import *
import Setup
from  anki_vector import camera_viewer
import time

NAME = "Vector-H2T1"
IP = "192.168.0.246"
SERIAL = "0050149a"

#create Robot Instance
robot = anki_vector.Robot()

def main():

    #Setup Robot
    Setup.startRobot(robot)

    robot.viewer.show()
    time.sleep(5)

    #Close down Robot
    Setup.closeRobot(robot)
        

if __name__ == "__main__":
    main()
