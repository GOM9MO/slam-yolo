from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

import yaml

def generate_launch_description():
    return LaunchDescription([
        # RealSense 相机节点
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='realsense_camera',
            parameters=[{
                'enable_depth': True,
                'align_depth': True,  # (可选) 对齐深度和彩色帧
                'depth_width': 640,   # (可选) 深度图分辨率
                'depth_height': 480,
                'no_device_power_mgmt': True,  # 禁用电源管理
                'kernel_driver_is_active': False  # 强制不使用内核驱动
            }],
            output='screen'  # 可选：打印日志到终端
        ),

        # 深度图转激光雷达节点
        Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            name='depthimage_to_laserscan',
            remappings=[
                ('image', '/camera/depth/image_rect_raw'),
                ('camera_info', '/camera/depth/camera_info'),
                ('scan', '/laser_scan')  # 可选：指定输出激光话题
            ],
            parameters=[{
                'scan_height': 1,       # 扫描高度（像素数）
                'output_frame': 'camera_link'  # 激光的参考坐标系
            }]
        ),
    ])
