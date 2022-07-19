import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
import time 

with anki_vector.Robot(enable_custom_object_detection=True) as robot:

        robot.behavior.drive_on_charger()




def turning_angle_vector(env, endposition_x, endposition_y):
    '''Berechnet Winkel, um den sich Vector drehen muss,
    um sich zur Endposition auszurichten.
    '''
    startpositon_y = env.self.position_y
    startpositon_x = env.self.position_x
    countered_leg = endposition_y - startpositon_y  # Gegenkathete
    adjacent_leg = endposition_x - startpositon_x  # Ankathete
    # Winkel zwischen x-Achse und Gerade zwischen Postion 1 und 2 (Bogenmaß):
    angle_rad_pos2 = math.atan2(countered_leg, adjacent_leg)
    angle_deg_pos2 = math.degrees(angle_rad_pos2)  # Winkel in Grad

    # Eventuell Umwandlung in positiven Winkel:
    if angle_deg_pos2 < 0:
        angle_deg_pos2 = 360 + angle_deg_pos2

    angle_deg_vector = env.self.rotation  # aktuelle Rotation des Vectors

    # Umwandlung von negativen in positiven Winkel:
    if angle_deg_vector < 0:
        angle_deg_vector = 360 + angle_deg_vector

    # Berechenen des Winkels um den sich Vector drehen muss:
    turning_angle = 360 - angle_deg_vector + angle_deg_pos2
    # Winkel nicht größer als 360 Grad:
    if turning_angle > 360:
        turning_angle = turning_angle - 360

    # Drehung nicht mehr als 180 Grad:
    if turning_angle > 180:
        turning_angle = turning_angle - 360
    return turning_angle


