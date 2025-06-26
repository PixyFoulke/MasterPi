#关掉开机自启
sudo systemctl stop masterpi.service

#重新开启开机自启
sudo systemctl restart masterpi.service

#测试上位机
python3 /home/pi/MasterPi/masterpi_pc_software/Arm.py

# 测试电机和机械臂
python3 /home/pi/MasterPi/board_demo/hardware_test.py
或者按下扩展板的Key1按键

# 软关机
# 长按Key2按键

# 第2章 基础课程/1.麦轮小车运动学基础课程
# 第3课 小车前进
python3 /home/pi/MasterPi/mecanum_control/car_forward_demo.py

# 第4课 小车转向
python3 /home/pi/MasterPi/mecanum_control/car_turn_demo.py

# 第5课 小车前后左右运动
python3 /home/pi/MasterPi/mecanum_control/car_move_demo.py

# 第6课 小车斜向运动
python3 /home/pi/MasterPi/mecanum_control/car_slant_demo.py

# 第7课 小车漂移运动
python3 /home/pi/MasterPi/mecanum_control/car_drifting_demo.py


# 第2章 基础课程/2.机械臂逆运动学基础课程
# 第3课 单次控制多个舵机
python3 /home/pi/MasterPi/board_demo/control_by_servo.py
# 第 4课 机械臂上下左右移动
python3 /home/pi/MasterPi/board_demo/control_by_kinematics.py

# 第3章 进阶课程 1.AI视觉玩法课程
# 第1课 颜色识别
python3 /home/pi/MasterPi/functions/color_detect.py

# 第2课 颜色分拣
python3 /home/pi/MasterPi/functions/color_sorting.py

# 第3课 目标追踪
python3 /home/pi/MasterPi/functions/color_tracking.py
--Wheel 0
--Wheel 1

# 第4课 智能巡线
python3 /home/pi/MasterPi/functions/visual_patrol.py

# 第5课 智能避障
python3 /home/pi/MasterPi/functions/avoidance.py
