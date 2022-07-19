from importlib.machinery import PathFinder
import anki_vector
import time
from anki_vector.exceptions import VectorException
from anki_vector.motors import *
from anki_vector.util import *
import cv2
from sqlalchemy import true
import torch
from PIL import Image
import Driving
import keyboard
import math

#middle is 320 and the lines are offset by 10 in either direction
left_line_coordinates = 310
right_line_coordinates = 330

object_last_frame_empty = True

max_delta_d = 320 #größtmöglicher abstand zw targetbox und mitte

right = True

def main():

    with anki_vector.Robot() as robot:
        #load the model 
        model = torch.hub.load('C:\\vector-race-gruppe-2\\yolov5', 'custom', path='C:\\vector-race-gruppe-2\yolov5\\best.pt', source='local', force_reload=True)  # local repo
        robot.behavior.set_head_angle(degrees(30))
        robot.behavior.set_lift_height(0.0)
        robot.behavior.set_eye_color(0,1)
        
        robot.camera.init_camera_feed()
        print("press S")
        
        while True:
            
            if keyboard.is_pressed('s'):                
                while True: 

                    #get latest image and save at source destination
                    robot.camera.latest_image.raw_image.save('C:\\vector-race-gruppe-2\\yolov5\\Source\\latest_img.jpeg')       
                    
                    #open image 
                    imgs = Image.open('C:\\vector-race-gruppe-2\\yolov5\\Source\\latest_img.jpeg') 

                    #inference picture 
                    results = model(imgs, size=640) 

                    #save result
                    results.save('C:\\vector-race-gruppe-2\\yolov5\\Results\\image') 

                    # Pandas DataFrame
                    #print(results.pandas().xyxy[0])  

                    #save frame in variables
                    pandas_frame = results.pandas().xyxy[0] 

                    #see if dataframe is empty 
                    print("Dataframe is empty? " + str(pandas_frame.empty))

                    #create and openCV picture stream of all inferenced pictures 
                    createCVStream()
                    
                    if(pandas_frame.empty == False):
                        confidence = pandas_frame["confidence"].values[0].astype(float)
                        #print(confidence)

                    #if the frame doesnt contain a checkpoint the robot doesnt attempt to drive and stops and takes another picture to inference    
                    if((pandas_frame.empty == False) and (confidence > 0.50)): 
                            
                        #get the x and y coordiantes of the inference box
                        x_min, y_min, x_max, y_max,_,_= results.xyxy[0][0].cpu().data.numpy().astype(int)  

                        #print(getCenter(x_max, x_min, y_max, y_min))

                        #get the center of the inference box to determine if one should drive left or right
                        x_center = getCenter(x_max, x_min, y_max, y_min)[0]
                        #y_center = getCenter(x_max, x_min, y_max, y_min)[1]

                        #print Steering intensity 
                        print(x_center)
                        print(calcSteeringIntensity(x_center))

                        #determines direction for the robot to drive in 
                        driveInDirection(x_center, robot)
                        object_last_frame_empty = False
                        print("-------------------------")         
                    elif (object_last_frame_empty == True) and (pandas_frame.empty == True):

                        print("elif block")   

                        if(right):
                            robot.motors.set_wheel_motors(80,40)
                            time.sleep(0.05)
                        else:
                            robot.motors.set_wheel_motors(40,80)
                            time.sleep(0.05)

                        print("-------------------------")
                    else: 
                        print("else block")
                        Driving.DriveStop(robot)
                        object_last_frame_empty = True
                        print("-------------------------")
            
def getCenter(x_max, x_min, y_max, y_min):

    x_center = x_min + ((x_max - x_min)/2).astype(int)  
    y_center = y_min + ((y_max - y_min)/2).astype(int)  

    return [x_center, y_center]

def driveInDirection(x_center, robot):

    steering_intensity = calcSteeringIntensity(x_center)

    if x_center <= left_line_coordinates:
        print("drive left")
        Driving.DriveLeft(robot, steering_intensity)
    
    elif x_center >= right_line_coordinates:
        print("drive right")
        Driving.DriveRight(robot, steering_intensity)
    else:
        print("straight")
        Driving.DriveStraight(robot)
        
def calcSteeringIntensity(x_center):

    delta_right = x_center - right_line_coordinates
    delta_left = left_line_coordinates - x_center

  
    if x_center >= right_line_coordinates:

        wurzel_koeffizient = ((Driving.MAX_SPEED**2)/max_delta_d)
        #Wurzel:
        y = (wurzel_koeffizient*delta_right)**(1/2)
        y = y/3
        return (Driving.MAX_SPEED-y)

    elif x_center <= left_line_coordinates:

        wurzel_koeffizient = ((Driving.MAX_SPEED**2)/max_delta_d)
        #Wurzel:
        y = (wurzel_koeffizient*delta_left)**(1/2)
        y = y/3
        return (Driving.MAX_SPEED-y)
            
    else:
        return 1

def createCVStream():
    img_color = cv2.imread('C:/vector-race-gruppe-2/yolov5/Results/image/latest_img.jpg',cv2.IMREAD_COLOR)
    img_color = cv2.line(img_color, (left_line_coordinates, 0), (left_line_coordinates, 640), (0, 255, 0), thickness=2)
    img_color = cv2.line(img_color, (right_line_coordinates, 0), (right_line_coordinates, 640), (0, 255, 0), thickness=2)
    cv2.imshow("Vector Race POV", img_color)
    cv2.waitKey(1)
  
if __name__ == '__main__':                          
        
        main()
        

