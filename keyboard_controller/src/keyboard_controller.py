#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from std_msgs.msg import Empty
from pynput import keyboard
from std_srvs.srv import Empty
from alpha_msgs.msg import SteeringAngles
import threading


pub_steer_front = rospy.Publisher('/keyboardcontroller/steering_cmd_front', Float64, queue_size=1)
pub_steer_rear = rospy.Publisher('/lateral_controller/steering_cmd', SteeringAngles, queue_size=1)
pub_steer_dist = rospy.Publisher('/keyboardcontroller/steering_distrution', Float64, queue_size=1)
pub_throttle = rospy.Publisher('/keyboardcontroller/throttle_cmd', Float64, queue_size=1)
pub_Togglelateral_controller = rospy.Publisher('/keyboardcontroller/toggle_lateral_controller', Bool, queue_size=1)
pub_gate = rospy.Publisher('/gate/open_gate', Bool, queue_size=1)
pub_lane_reset = rospy.Publisher('/lane_detection/reset', Bool, queue_size=1)

gate_closed = True
speed_fwd = 1.0
speed_bwd = -0.5
angle_front = 30.0
angle_distrubution = 0.0
use_lateral_controller = True

def close_gate():
    global gate_closed
    if gate_closed:
        return
    else:
        pub_gate.publish(False)
        gate_closed = True  

def on_press(key):
    global speed_fwd, speed_bwd, angle_distrubution, angle_front, gate_closed
    try:
        key.char
    except:
        return
    if key.char == 'e':
        speed_fwd = speed_fwd+0.1
        speed_bwd = speed_bwd-0.1
        print("Speed Forward: {} Speed Backward: {}".format(speed_fwd, speed_bwd))
    if key.char == 'q':
        speed_fwd = speed_fwd-0.1
        speed_bwd = speed_bwd+0.1
        print("Speed Forward: {} Speed Backward: {}".format(speed_fwd, speed_bwd))
    if key.char == 'r':
        try:
            reset_simulation = rospy.ServiceProxy('/gazebo/reset_world', Empty)
            reset_simulation()
            print("Reset simulation!")
        except rospy.ServiceException:
            print("Could not reset simulation!")
        
    if key.char == 'v':
        angle_front = angle_front-1
        print("Angle Front: {} Angle Distribution: {}".format(angle_front, angle_distrubution))
    if key.char == 'b':
        angle_front = angle_front+1
        print("Angle Front: {} Angle Distribution: {}".format(angle_front, angle_distrubution))
    if key.char == 'n':
        angle_distrubution = angle_distrubution-0.1
        pub_steer_dist.publish(angle_distrubution)
        print("Angle Front: {} Angle Distribution: {}".format(angle_front, angle_distrubution))
    if key.char == 'm':
        angle_distrubution = angle_distrubution+0.1
        pub_steer_dist.publish(angle_distrubution)
        print("Angle Front: {} Angle Distribution: {}".format(angle_front, angle_distrubution))
    if key == keyboard.Key.up or key.char == 'w':
        pub_throttle.publish(speed_fwd)
    if key == keyboard.Key.down or key.char == 's':
        pub_throttle.publish(speed_bwd)
    if key == keyboard.Key.left or key.char == 'a':
        pub_steer_dist.publish(angle_distrubution)
        pub_steer_front.publish(angle_front) 
    if key == keyboard.Key.right or key.char == 'd':
        pub_steer_dist.publish(angle_distrubution)
        pub_steer_front.publish(-angle_front)
    if key == keyboard.Key.left or key.char == 'y':
        angles = SteeringAngles(None, 0, 10)
        pub_steer_rear.publish(angles)
    if key == keyboard.Key.right or key.char == 'c':
        angles = SteeringAngles(None, 0, -10)
        pub_steer_rear.publish(angles)
    if key.char == 'o':
        if gate_closed:
            pub_gate.publish(True)
            gate_closed = False
            threading.Timer(30.0, close_gate).start()
        else:
            pub_gate.publish(False)
            gate_closed = True
        
        


def on_release(key):

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        key.char
    except:
        return
    if key == keyboard.Key.up or key.char == 'w':
        pub_throttle.publish(0.0)
    if key == keyboard.Key.down or key.char == 's':
        pub_throttle.publish(0.0)
    if key == keyboard.Key.left or key.char == 'a':
        pub_steer_front.publish(0.0)
    if key == keyboard.Key.right or key.char == 'd':
        pub_steer_front.publish(0.0)
    if key == keyboard.Key.left or key.char == 'y':
        angles = SteeringAngles(None, 0, 0)
        pub_steer_rear.publish(angles)
    if key == keyboard.Key.right or key.char == 'c':
        angles = SteeringAngles(None, 0, 0)
        pub_steer_rear.publish(angles)
    if key.char == 't':
        pub_lane_reset.publish(True)
    if key.char == 'h':
        global use_lateral_controller
        use_lateral_controller = not use_lateral_controller
        pub_Togglelateral_controller.publish(use_lateral_controller)
        if use_lateral_controller:
            print("Enabled Steering of Lateral Controller")
        else:
            print("Disabled Steering of Lateral Controller")


if __name__ == '__main__':
    print("\n\n+++ Press ESCAPE to stop! +++\n")
    print("- w,a,s,d -> Move model")
    print("- y, c -> Steer rear")
    print("- e,q     -> Decrease/Increase speed")
    print("- v,b     -> Decrease/Increase turning radius")
    print("- n,m     -> Decrease/Increase angle distribution front/back")
    print("- r       -> Reset simulation")
    print("- t       -> Reset Lanedetection")
    print("- o       -> Open/Close gate")
    print("- h       -> Toggle LateralController Steering")
    try:
        rospy.init_node('keyboard_controller', anonymous=True)
    except rospy.ROSInterruptException:
        pass

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
