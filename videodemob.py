"""
Example commands for Tello:
forward
backward
left
right
up
down
clockwise
counter_clockwise

Created for Tech Garage
"""



from app.Drone import Drone

drone = Drone()



drone.takeoff()
drone.sleep(2)
drone.up(39)
drone.sleep(2)
drone.left(105)
drone.sleep(2)
drone.land()