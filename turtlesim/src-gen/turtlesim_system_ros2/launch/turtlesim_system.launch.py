from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="turtlesim_node"
    )

    teleop = Node(
        package="turtlesim",
        executable="turtle_teleop_key",
        name="teleop"
    )


    ld.add_action(turtlesim_node)
    ld.add_action(teleop)

    return ld
