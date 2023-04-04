# Robotics
# To run the main python file:
•	Ros2 run usi_angry_turtle move2goal – this is the command to get the python script to run.

# Another terminal(EVERYTIME CHANGES ARE MADE TO THE PACKAGE CD TO THE ~/dev_ws/ folder):
•	Colcon build
•	source ~/dev_ws/install/setup.bash

# Open another terminal:
•	sudo apt update
•	sudo apt install ~nros-humble-rqt*
•	rqt
•	then in the service string name the turtle turtle2
•	change the x and y to 1.0
•	then press call near the service area. This will spawn the other turtle make sure your running the turtlesim window (ros2 run turtlesim turtlesim_node) in another terminal.

# Another terminal(TO SPAWN A NEW TURTLE):
•	ros2 service call /spawn turtlesim/srv/Spawn '{x: 2.0, y: 2.0, theta: 0.0, name: turtle2}' 'turtle2' can be changed to any name you want
•	you can press any arrow to control the spawned turtle to go in any direction.

# Open another terminal: to get the spawned turtle to move by itself
•	ros2 topic pub --rate 1 /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
