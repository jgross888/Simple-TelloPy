
# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain 

from __future__ import division
import pygame
from time import sleep
import os
from app.TEST import Drone



drone = Drone()

pygame.init()

drone.video()

joystick_count = pygame.joystick.get_count()
speed = 50
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')

while True:
    pygame.event.get()

    if joystick_count != 0:
        rightsticky = gamepad.get_axis(1)
        leftsticky = gamepad.get_axis(4)
        """
        drone.pitch()
        drone.throttle()
        drone.yaw()
        drone.roll()
        """
        rightstickx = gamepad.get_axis(0)
        leftstickx = gamepad.get_axis(3)
        Start = gamepad.get_button(7)
        Back = gamepad.get_button(6)
        x, y = gamepad.get_hat(0)
        LT = gamepad.get_axis(2)
        RT = gamepad.get_axis(5)
        LB = gamepad.get_button(4)
        RB = gamepad.get_button(5)
        X = gamepad.get_button(2)
        Y = gamepad.get_button(3)
        A = gamepad.get_button(0)
        B = gamepad.get_button(1)


    if Start == 1:
        print('Start pressed')
        drone.takeoff1()

    if Back == 1:
        print('Back pressed')
        drone.land()

    if A == 1:
        print('A pressed')
        drone.throttle(1)

    if Y == 1:
        print('Y pressed')
        drone.throttle(-1)

    if X == 1:
        print('X pressed')
        drone.roll(-1)

    if B == 1:
        print('B pressed')
        drone.roll(1)

    if LB == 1 and RB == 1:
        drone.pitch(-1)

    if leftsticky == 1 and rightsticky == -1:
        drone.yaw(1)

    if leftsticky == -1 and rightsticky == 1:
        drone.yaw(-1)

    if RT == 1 and LT == 1:
        drone.pitch(1)

    sleep(.02)










