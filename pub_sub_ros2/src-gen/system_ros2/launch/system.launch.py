from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    publisher_component = Node(
        package="examples_rclcpp_minimal_publisher",
        executable="publisher_lambda",
        name="publisher_component"
    )

    subscriber_component = Node(
        package="examples_rclcpp_minimal_subscriber",
        executable="subscriber_lambda",
        name="subscriber_component"
    )


    ld.add_action(publisher_component)
    ld.add_action(subscriber_component)

    return ld
