#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

class Movebase_Client:
    def __init__(self):
        rospy.init_node('movebase_client')
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

    def sendGoalToClient(self, x, y, theta):
        self.client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        quat = quaternion_from_euler(0,0,theta)
        goal.target_pose.pose.orientation.x = quat[0]
        goal.target_pose.pose.orientation.y = quat[1]
        goal.target_pose.pose.orientation.z = quat[2]
        goal.target_pose.pose.orientation.w = quat[3]

        self.client.send_goal(goal)

    def getResultFromClient(self):
        wait = self.client.wait_for_result()
        return wait
        # if not wait:
        #     rospy.logerr("Action server not available!")
        #     rospy.signal_shutdown("Action server not available!")
        # else:
        #     return self.client.get_result()   

if __name__ == '__main__':
    # try:
    #    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    #     result = movebase_client()
    #     if result:
    #         rospy.loginfo("Goal execution done!")
    # except rospy.ROSInterruptException:
    #     rospy.loginfo("Navigation test finished.")

    test = Movebase_Client()
    test.sendGoalToClient(0,3,1.57)
    
    result = test.getResultFromClient()
    while result != True:
        print("result:",result)
        status = test.getResultFromClient()
        rospy.sleep(1)