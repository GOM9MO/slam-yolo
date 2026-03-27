# slam yolo

## 启动步骤

1. 启动一个docker容器`docker run -it --rm -v .:/opt/ros2_ws/project --privileged mot8js/ros2-realsense`并且进入了ros用户的bash终端
2. 使用命令`cd /opt/ros2_ws`切换到ros2的工作区目录，然后用`colcon build`构建包
3. 使用命令source `slam_yolo/install/setup.bash`安装刚才一步构建的包
4. 使用命令`ros2 launch slam_yolo depth_to_laserscan.launch.py`启动深度相机和深度转激光两个节点



