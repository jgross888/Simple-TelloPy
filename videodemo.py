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
drone.up(40)
drone.sleep(2)
drone.right(122)
drone.sleep(2)
drone.land()