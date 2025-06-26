#!/usr/bin/python3
# coding=utf8
import sys
import time
from common.ros_robot_controller_sdk import Board

board = Board()

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
**********************************************************
********************PWM舵机和电机测试************************
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * 按下Ctrl+C可关闭此次程序运行，若失败请多次尝试！
----------------------------------------------------------
''')
board.pwm_servo_set_position(0.3, [[1, 1800]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[1, 1500]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[1, 1200]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[1, 1500]]) 
time.sleep(1.5)

board.pwm_servo_set_position(0.3, [[3, 900]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[3, 695]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[3, 500]])
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[3, 695]]) 
time.sleep(1.5)

board.pwm_servo_set_position(0.3, [[4, 2215]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[4, 2415]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[4, 2215]])
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[4, 2415]]) 
time.sleep(1.5)

board.pwm_servo_set_position(0.3, [[5, 580]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[5, 780]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[5, 980]])
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[5, 780]]) 
time.sleep(1.5)

board.pwm_servo_set_position(0.3, [[6, 1800]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[6, 1500]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[6, 1200]]) 
time.sleep(0.3)
board.pwm_servo_set_position(0.3, [[6, 1500]]) 
time.sleep(1.5)


board.set_motor_duty([[1, 45]])
time.sleep(0.5)
board.set_motor_duty([[1, 0]])
time.sleep(1)
        
board.set_motor_duty([[2, 45]])
time.sleep(0.5)
board.set_motor_duty([[2, 0]])
time.sleep(1)

board.set_motor_duty([[3, 45]])
time.sleep(0.5)
board.set_motor_duty([[3, 0]])
time.sleep(1)

board.set_motor_duty([[4, 45]])
time.sleep(0.5)
board.set_motor_duty([[4, 0]])
time.sleep(1)

