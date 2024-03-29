**Gazebo simulation of the Turtlebot tracing a circle and a sqaure**

Below is the file structure of this workspace:

    .
    ├── ...
    ├── a2b_ws                     
    │   ├── build                                     # build files generated by catkin_make
    │   ├── devel                                     # devel files generated by catkin_make
    │   ├── src
    │   │   ├── assign2b                              # This is the ROS package responsible for executing the circle and square tracing
    │   │   │   ├── launch
    │   │   │   │   ├── circle.launch                 #Use this launch file to run only the circle trajectory
    │   │   │   │   ├── move.launch                   #Use this launch file to select either circle or square by passing an extra argument
    │   │   │   │   ├── square.launch                 #Use this launch file to run only the square trajectory
    │   │   │   ├── src
    │   │   │   │   ├── circle.py                     #Edit this script to modify the target linear and angular velocity of the turtlebot
    │   │   │   │   ├── square.py                     #Edit  this script to change the side of the square and the turtlebot velocities
    │   │   │   ├── CMakeLists.txt
    │   │   │   ├── package.xml                       #Contains package dependencies
    │   │   └── ...
    │   └── videos        # Screen recordings of the execution in .gif format
    └── ...

**TLDR:**
The videos are useful in quickly visualizing the results of the multiple angular and linear velocity inputs given to the turtlebot. In summary, under 0.5 m/s and 0.5 rad/s linear and angular velocities respectively, the turtlebot reliably traces a circle.
However, the square is out of shape even at 0.3 m/s and 0.3 rad/s velocities.

**How to reproduce the results?**
In order to run the simulation on your own, download and copy the assign2b directory into the src directory under your catkin workspace and execute catkin_make.

Run the following commands to launch:

``` roslaunch assign2b circle.launch ``` - launches the circle trajectory program

``` roslaunch assign2b square.launch ``` - launches the square trajectory program

Alternatively, you can use the move.launch to select either trajectory as follows:

``` roslaunch assign2b move.launch code:=circle```

``` roslaunch assign2b move.launch code:=square ```

You can play around with the velocities by modifying the ``` vel_msg.linear.x ``` and ``` vel_msg.angular.z ``` in the circle.py and square.py script files.  
