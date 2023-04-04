# Robotics



# To run repositary
## Another terminal:
### (EVERYTIME CHANGES ARE MADE TO THE PACKAGE CD TO THE ~/dev_ws/ folder): <br>
•	Colcon build <br>
•	source ~/dev_ws/install/setup.bash <br>

### To run the main python file:
•	ros2 run usi_angry_turtle move2goal – this is the command to get the python script to run.

## Open another terminal:
•	sudo apt update <br>
•	sudo apt install ~nros-humble-rqt* <br>
•	rqt <br>
•	then in the service string name the turtle turtle2 <br>
•	change the x and y to 1.0 <br>
•	then press call near the service area. This will spawn the other turtle make sure your running the turtlesim window (ros2 run turtlesim turtlesim_node) in another terminal. <br>

## Another terminal
### (TO SPAWN A NEW TURTLE)
•	ros2 service call /spawn turtlesim/srv/Spawn '{x: 2.0, y: 2.0, theta: 0.0, name: turtle2}' 'turtle2' can be changed to any name you want <br>
•	you can press any arrow to control the spawned turtle to go in any direction.

## Open another terminal: 
### to get the spawned turtle to move by itself
•	ros2 topic pub --rate 1 /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" <br>

### To write usi with main turtle:
•	in thE terminal where this line is running 'ros2 run usi_angry_turtle move2goal', enter the points as follows : <br>
<br>
*NB - THE FIRST POINT IS THE X, THE SECOND IS THE Y AND THE TOLERANCE IS 0.2 IN ALL CASE. <br>
*NB - BEFORE INPUTTING EACH POINT, THE LINE 'ros2 run usi_angry_turtle move2goal' MUST BE RAN IN THE TERMINAL [MANUAL] <br>
<br>
**points writes I** <br>
(5.54445, 3)<br>
()<br>

**points writes S** <br>
(4, 5.544445)<br>
(4, 3.5)<br>
(5.5, 3.5)<br>
(5, 2)<br>
(4, 2)<br>

**points writes U** <br>
(2, 5.544445)<br>
(2, 2)<br>
(1, 2)<br>
(0.8, 5.54445)<br>
