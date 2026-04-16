from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(package='nav2_controller', executable='controller_server'),
        Node(package='nav2_planner', executable='planner_server'),
        Node(package='nav2_bt_navigator', executable='bt_navigator'),
        Node(package='nav2_costmap_2d', executable='costmap_2d_node'),
    ])
