import anki_vector
from anki_vector import camera_viewer
import cv2
import numpy as np 
from pyzbar.pyzbar import decode
import tkinter as tk
import Setup
import time
from PIL import Image
from threading import Thread

with anki_vector.Robot() as robot:

    

    #for x in range(10): 
    #    robot.audio.stream_wav_file("C:\Vectorsources\yoshi-tongue (online-audio-converter.com) (1).wav", 75)

    #robot.behavior.drive_on_charger()

    

    def sound():
         for x in range(10): 
            robot.audio.stream_wav_file("C:\Vectorsources\yoshi-tongue (online-audio-converter.com) (1).wav", 100)
            time.sleep(1)


    def drive():
        robot.motors.set_wheel_motors(-220, 220)

        #time.sleep(2)
        #robot.motors.stop_all_motors()
        #robot.motors.set_wheel_motors(220, 150)
        #time.sleep(2)

    Thread(target = drive()).run()
    Thread(target = sound()).run()
    
    
    
