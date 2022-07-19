import time

import anki_vector
from anki_vector.events import Events
from anki_vector.util import Angle, Pose, Position, degrees, radians, speed_mmps
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
from anki_vector import behavior
import math

def handle_object_appeared(robot, event_type, event):

        speed_mmps
    # This will be called whenever an EvtObjectAppeared is dispatched -
    # whenever an Object comes into view.
    #print(f"--------- Vector started seeing an object --------- \n{event.obj.pose}")

    print({event.obj.pose.position.x}) 
    print({event.obj.pose.position.y}) 
    print({event.obj.pose.position.z}) 
    print({event.obj.pose}) 

    x_coord = event.obj.pose.position.x
    y_coord = event.obj.pose.position.y
    z_coord = 0

    pose2 = Pose(x_coord ,y_coord ,0, angle_z=anki_vector.util.Angle(degrees=0))
    robot.behavior.go_to_pose(pose2)
    robot.motors.stop_all_motors()


    #print(turning_angle_vector(x_coord, y_coord))

    #robot.behavior.turn_in_place(radians(turning_angle_vector(x_coord, y_coord)))
    
    

def turning_angle_vector(endposition_x, endposition_y):

    solution_rad = math.atan2(endposition_x, endposition_y)
    solution_deg = math.degrees(solution_rad)

    return solution_rad


    #robot.audio.stream_wav_file('C:\Vectorsources\\Ludacris - Move Bitch Get Out Da Way (HQ) (online-audio-converter.com).wav', 100)
    #robot.behavior.say_text("Look If you had. One shot. Or one opportunity. To seize everything you ever wanted. In one moment. Would you capture it. Or just let it slip? Yo. ")
    #robot.behavior.say_text("His palms are sweaty, knees weak, arms are heavy, There's vomit on his sweater already, mom's spaghetti, He's nervous, but on the surface he looks calm and ready, To drop bombs, but he keeps on forgettin', What he wrote down, the whole crowd goes so loud, He opens his mouth, but the words won't come out,")
    #robot.behavior.say_text("He's chokin', how, everybody's jokin' now, The clocks run out, times up, over, blaow, Snap back to reality, ope there goes gravity Ope, there goes Rabbit, he choked, He's so mad, but he won't give up that easy? No, He won't have it, he knows his whole back's to these ropes,") 
    #robot.behavior.say_text("It don't matter, he's dope, he knows that, but he's broke, He's so stagnant, he knows, when he goes back to this mobile home, that's when it's Back to the lab again, yo, this whole rhapsody Better go capture this moment and hope it don't pass him, You better lose yourself in the music, the moment, ")
    #robot.behavior.say_text("You own it, you better never let it go You only get one shot, do not miss your chance to blow, This opportunity comes once in a lifetime You better lose yourself in the music, the moment You own it, you better never let it go, You only get one shot, do not miss your chance to blow, This opportunity comes once in a lifetime")

def main():



        with anki_vector.Robot(default_logging=False, show_viewer=True, show_3d_viewer=True, enable_nav_map_feed=True, enable_custom_object_detection=True) as robot:

                
    
                # If necessary, move Vector's Head and Lift down
                
                robot.behavior.set_lift_height(0.0)
                robot.behavior.set_head_angle(degrees(0.0))

                robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType01,
                                                marker=CustomObjectMarkers.Circles3,
                                                size_mm=30.0,
                                                marker_width_mm=30.0, marker_height_mm=30.0)

                robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType02,
                                                marker=CustomObjectMarkers.Circles2,
                                                size_mm=30.0,
                                                marker_width_mm=30.0, marker_height_mm=30.0)

                robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType03,
                                                marker=CustomObjectMarkers.Diamonds2,
                                                size_mm=30.0,
                                                marker_width_mm=30.0, marker_height_mm=30.0)

                robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType04,
                                                marker=CustomObjectMarkers.Diamonds4,
                                                size_mm=30.0,
                                                marker_width_mm=30.0, marker_height_mm=30.0)

                #robot.nav_map.init_nav_map_feed
                robot.events.subscribe(handle_object_appeared, Events.object_appeared)    

                
                
                #pose2 = Pose(0 ,0 ,0, angle_z=anki_vector.util.Angle(degrees=0))
                #robot.behavior.go_to_pose(pose2)       

                time.sleep(100.0)

                                        
                                

if __name__ == '__main__':   
        
        main()
