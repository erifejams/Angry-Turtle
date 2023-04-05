# Robotics



# To run 
## Terminal #1:
### (EVERYTIME CHANGES ARE MADE TO THE PACKAGE CD TO THE ~/dev_ws/ folder): <br>
•	Colcon build <br>
•	source ~/dev_ws/install/setup.bash <br>

## Terminal #2:
### to get the turtlesim simulator running
ros2 run turtlesim turtlesim_node <br>

## Terminal #3:
### To run the main python file:
•	ros2 run usi_angry_turtle move2goal – this is the command to get the python script to run. <br>

## Terminal #4:
•	sudo apt update <br>
•	sudo apt install ~nros-humble-rqt* <br>
•	rqt <br>
•	then in the service string name the turtle turtle2 <br>
•	change the x and y to 1.0 <br>
•	then press call near the service area. This will spawn the other turtle make sure your running the turtlesim window (ros2 run turtlesim turtlesim_node) in another terminal. <br>

## Terminal #5:
### (TO SPAWN A NEW TURTLE) - this can be done using the previous command so can skip
•	ros2 service call /spawn turtlesim/srv/Spawn '{x: 2.0, y: 2.0, theta: 0.0, name: turtle2}' 'turtle2' can be changed to any name you want <br>
•	you can press any arrow to control the spawned turtle to go in any direction. <br>

## Terminal #6: 
### to get the spawned turtle to move by itself
•	ros2 topic pub --rate 1 /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" <br>
• rosrun turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel <br>


### To write usi with main turtle from #3 terminal:
•	in thE terminal where this line is running 'ros2 run usi_angry_turtle move2goal', enter the points as follows : <br>
<br>
*NB - Make sure to spawn the turle first in the rqt before continuing <br>
*NB - THE FIRST POINT IS THE X, THE SECOND IS THE Y AND THE TOLERANCE IS 0.2 IN ALL CASE. <br>
*NB - BEFORE INPUTTING EACH POINT, THE LINE 'ros2 run usi_angry_turtle move2goal' MUST BE RAN IN THE TERMINAL [MANUAL] <br>
<br>
**points writes I** <br>

(5.544445, 2)<br>
(5.544445, 4.9)<br>

**points writes S** <br>
(4, 5.544445)<br>
(4, 3.5)<br>
(4.6, 3.5)<br>
(4.6, 2)<br>
(4, 2)<br>

**points writes U** <br>
(3.5, 5.544445)<br>
(2, 2)<br>
(1, 2)<br>
(0.8, 5.544445)<br>

1.The result of running the code to write USI with how to write it<br>
![](http://url/to/img.png)<img width="1375" alt="Screenshot 2023-04-05 at 06 30 26" src="https://user-images.githubusercontent.com/44726422/229989626-d98684e8-a97c-4df9-8888-946d19a35487.png">


2.When the turtle is less than 1 meter of the other turtle, the turtle becomes angry, stops writing and starts pursuing the other turtle
<img width="1465" alt="Screenshot 2023-04-05 at 06 44 05" src="https://user-images.githubusercontent.com/44726422/229991544-cd7990f1-dbf2-4bbd-85d2-130e258a2b65.png">


3. Spawn more than 1 turtle (make a separate terminal to run the other turtle with this command ' rosrun turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel'
(change the turtle name) <br>
<img width="1476" alt="Screenshot 2023-04-05 at 06 50 42" src="https://user-images.githubusercontent.com/44726422/229992994-849b671b-808c-4df6-8d5c-487eea3c70b4.png">
tle1/cmd_vel:=turtle2/cmd_vel
')

