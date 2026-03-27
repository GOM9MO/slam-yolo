#!/bin/bash
docker run --rm -it -v .:/opt/project mot8js/ros2-realsense colcon build --build-base /opt/project