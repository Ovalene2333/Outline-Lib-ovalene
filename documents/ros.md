# ROS

## 基本操作

```shell
roscore
# 运行ros的核心功能
rqt_graph
# 图形界面
```

```shell
rosnode
# 命令行界面
Commands:
        rosnode ping    test connectivity to node
        rosnode list    list active nodes
        rosnode info    print information about node
        rosnode machine list nodes running on a particular machine or list machines
        rosnode kill    kill a running node
        rosnode cleanup purge registration information of unreachable nodes
```

```shell
rostopic
# 命令行工具

Commands:
        rostopic bw     display bandwidth used by topic
        rostopic delay  display delay of topic from timestamp in header
        rostopic echo   print messages to screen
        rostopic find   find topics by type
        rostopic hz     display publishing rate of topic
        rostopic info   print information about active topic
        rostopic list   list active topics
        rostopic pub    publish data to topic
        rostopic type   print topic or field type
```

```shell
# 发布运动的指令(pub),-r是频率参数,后面是对应的对象
rostopic pub -r 10 /turtle1/cmd_vel geometry_msgs/Twist \
"linear:
  x: 1.0
  y: 1.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.0" 
```

```shell
rosservice
# 命令行工具
Commands:
        rosservice args print service arguments
        rosservice call call the service with the provided args
        rosservice find find services by service type
        rosservice info print information about service
        rosservice list list active services
        rosservice type print service type
        rosservice uri  print service ROSRPC uri

```

```shell
rosbag
# 话题的记录和复现
rosbag record -a -O cmd_record
rosbag play cmd_record.bag
```

## 创建工作区

```shell
# 创建工作空间
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace

# 编译工作空间
cd ~/catkin_ws/
catkin_make

# 设置环境变量
source devel/setup.bash

# 检查环境变量
echo $ROS_PACKAGE_PATH

# 创建功能包
cd ~/catkin_ws/src
catkin_create_pkg test_pkg std_msgs rospy roscpp 
        # 后面跟一些依赖

cd ~/catkin_ws/src
catkin_create_pkg learning_topic std_msgs rospy roscpp geometry_msgs turtlesim

# 编译功能包
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.bash 
```

```shell
# 运行自己写的功能包
rosrun learning_topic velocity_publisher
rosrun learning_topic pose_subscriber
```

wsl --import Ubuntu-20.04 D:\export\ F:\linux\export.tar --version 2
