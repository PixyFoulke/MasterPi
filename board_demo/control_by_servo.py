#!/usr/bin/python3
# coding=utf8

# 第2章 课程基础/2.机械臂逆运动学基础课程/第3课 单次控制多个舵机 

import time
from common.ros_robot_controller_sdk import Board

board = Board()
board.pwm_servo_set_position(0.5, [[1, 1300]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1500]])
time.sleep(1)

board.pwm_servo_set_position(0.5, [[1, 1300], [3, 700]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1500], [3, 500]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1300], [3, 700]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1500], [3, 500]])
time.sleep(1)


board.pwm_servo_set_position(0.5, [[4, 2200]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[4, 2400]])
time.sleep(1)

board.pwm_servo_set_position(0.5, [[5, 580]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[5, 780]])
time.sleep(1)

board.pwm_servo_set_position(0.5, [[1, 1300], [6, 1300]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1500], [6, 1500]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1300], [6, 1700]])
time.sleep(1)
board.pwm_servo_set_position(0.5, [[1, 1500], [6, 1500]])