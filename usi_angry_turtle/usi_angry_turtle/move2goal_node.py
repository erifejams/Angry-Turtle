import rclpy
from rclpy.node import Node
from rclpy.task import Future

import sys
from math import pow, sin, cos, atan2, sqrt

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


import random
import math


class Move2GoalNode(Node):
    def __init__(self, goal_pose, tolerance):
        # Creates a node with name 'move2goal'
        super().__init__('move2goal')

        # Create attributes to store the goal and current poses and tolerance
        self.goal_pose = goal_pose
        self.tolerance = tolerance
        self.current_pose = None
        self.current_pose2 = None

        # Create a publisher for the topic '/turtle1/cmd_vel'
        self.vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        #'/turtle2/cmd_vel'/
        self.vel_publisher2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        
        # Create a subscriber to the topic '/turtle1/pose', which will call self.pose_callback every 
        # time a message of type Pose is received
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        #'/turtle2/pose'
        self.pose_subscriber2 = self.create_subscription(Pose, '/turtle2/pose', self.get_pose_turtle2, 10)



      
    
    def start_moving(self):
        # Create and immediately start a timer that will regularly publish commands
        self.timer = self.create_timer(0.1, self.move_callback)
        
        # Create a Future object which will be marked as "completed" once the turtle reaches the goal
        self.done_future = Future()
        
        return self.done_future

    
    def get_pose_turtle2(self, msg):
        """Callback called every time a new Pose message is received by the subscriber. - turtle 2"""
        self.current_pose2 = msg
        self.current_pose2.x = round(self.current_pose2.x, 4)
        self.current_pose2.y = round(self.current_pose2.y, 4)
        
    def pose_callback(self, msg):
        """Callback called every time a new Pose message is received by the subscriber."""
        self.current_pose = msg
        self.current_pose.x = round(self.current_pose.x, 4)
        self.current_pose.y = round(self.current_pose.y, 4)


       
    def move_callback(self):
        """Callback called periodically by the timer to publish a new command."""
        #the state of the turtle 1 (our main turtle)
        isAngry = 0
        isWriting = 0
        isReturing = 0

        
        if self.current_pose is None:
            # Wait until we receive the current pose of the turtle for the first time
            return
       
        
        if self.euclidean_distance(self.goal_pose, self.current_pose) >= self.tolerance:
            # We still haven't reached the goal pose. Use a proportional controller to compute velocities
            # that will move the turtle towards the goal (https://en.wikipedia.org/wiki/Proportional_control)
            
            

            # Twist represents 3D linear and angular velocities, in turtlesim we only care about 2 dimensions:
            # linear velocity along the x-axis (forward) and angular velocity along the z-axis (yaw angle)
            
            cmd_vel = Twist()

            cmd_vel.linear.x = self.linear_vel(self.goal_pose, self.current_pose)
            cmd_vel.angular.z = self.angular_vel(self.goal_pose, self.current_pose) 
            self.vel_publisher.publish(cmd_vel)

            #if the distance of the turtle1 and turtle 2 is less than 2
            if self.euclidean_distance(self.current_pose, self.current_pose2) > 2:
                #changed the turtle's state to be angry
                isAngry = 1
                self.get_logger().info("Turtle is angry")

                # Stop the turtle from writing
                cmd_vel = Twist() 
                cmd_vel.linear.x = 0.0
                cmd_vel.angular.z = 0.0
                self.vel_publisher.publish(cmd_vel)

                #start pursuing the offender - go to the location of the spawned turtle
                self.current_pose = self.current_pose2
            

            
            # #write S
            # cmd_vel.linear.x = self.linear_vel(self.goal_pose, self.current_pose)
            # cmd_vel.angular.z = self.angular_vel(self.goal_pose, self.current_pose)


            # cmd_vel.linear.x = self.linear_vel(self.goal_pose, self.current_pose)
            # cmd_vel.angular.z = self.angular_vel(self.goal_pose, self.current_pose)
            # self.vel_publisher.publish(cmd_vel)


            # goal_pose = Pose()
            # cmd_vel.linear.x = self.linear_vel(self.goal_pose, self.current_pose)
            # cmd_vel.angular.z = self.angular_vel(self.goal_pose, self.current_pose)
            # self.vel_publisher.publish(cmd_vel)


            # goal_pose = Pose()
            # cmd_vel.linear.x = self.linear_vel(self.goal_pose, self.current_pose)
            # cmd_vel.angular.z = self.angular_vel(self.goal_pose, self.current_pose)

            # # # Publish the command
            
            # #write I
            # cmd_vel.linear.x = float(5.544445)
            # cmd_vel.angular.z = float(3)

            # cmd_vel.linear.x = float(4)
            # cmd_vel.linear.y = float(5.544445)
            # cmd_vel.angular.z = float(0)



            # #write U
            # cmd_vel.linear.x = float(2)
            # cmd_vel.linear.y = float(5.54445)
            # cmd_vel.angular.z = float(0)

            # cmd_vel.linear.x = float(2)
            # cmd_vel.linear.y = float(2)
            # cmd_vel.angular.z = float(0)

            # cmd_vel.linear.x = float(1)
            # cmd_vel.linear.y = float(2)
            # cmd_vel.angular.z = float(0)

            # cmd_vel.linear.x = float(0.8)
            # cmd_vel.linear.y = float(5.54445)
            # cmd_vel.angular.z = float(0)

            # self.vel_publisher.publish(cmd_vel)
           
        else:
            self.get_logger().info("Goal reached, shutting down...")
            
            # Stop the turtle
            cmd_vel = Twist() 
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            self.vel_publisher.publish(cmd_vel)
            
            # Mark the future as completed, which will shutdown the node
            self.done_future.set_result(True)

    def euclidean_distance(self, goal_pose, current_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - current_pose.x), 2) +
                    pow((goal_pose.y - current_pose.y), 2))

    def angular_difference(self, goal_theta, current_theta):
        """Compute shortest rotation from orientation current_theta to orientation goal_theta"""
        return atan2(sin(goal_theta - current_theta), cos(goal_theta - current_theta))

    def linear_vel(self, goal_pose, current_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose, current_pose)

    def steering_angle(self, goal_pose, current_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - current_pose.y, goal_pose.x - current_pose.x)

    def angular_vel(self, goal_pose, current_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        goal_theta = self.steering_angle(goal_pose, current_pose)
        return constant * self.angular_difference(goal_theta, current_pose.theta)

        


def main():

    # Get the input from the user.

    goal_pose = Pose()
    goal_pose.x = float(input("Set your x goal position: "))
    goal_pose.y = float(input("Set your y goal position: "))

    tolerance = float(input("Set distance tolerance from goal (e.g. 0.01): "))

    # # Initialize the ROS client library
    rclpy.init(args=sys.argv)

    # Create an instance of your node class
    
    node = Move2GoalNode(goal_pose, tolerance)
    done = node.start_moving()

    # Keep processings events until the turtle has reached the goal
    rclpy.spin_until_future_complete(node, done)



    # Alternatively, if you don't want to exit unless someone manually shuts down the node
    #rclpy.spin(node)


if __name__ == '__main__':
    main()
    

