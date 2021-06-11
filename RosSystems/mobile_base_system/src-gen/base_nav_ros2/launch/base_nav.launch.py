from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  ld = LaunchDescription()

  scan_front = Node(
    package="hokuyo_node",
    executable="hokuyo_node",
    name="scan_front",
    namespace="scan_front",
    remappings=[
      ("scan", "scan_front/scan")]
  )
  scan_rear = Node(
    package="hokuyo_node",
    executable="hokuyo_node",
    name="scan_rear",
    namespace="scan_rear",
    remappings=[
      ("scan", "scan_rear/scan")]
  )
  base_driver = Node(
    package="ridgeback_base",
    executable="ridgeback_node",
    name="base_driver"
  )
  move_base = Node(
    package="move_base",
    executable="move_base",
    name="move_base"
  )
  robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    name="robot_state_publisher"
  )
  scan_unifier = Node(
    package="cob_scan_unifier",
    executable="scan_unifier_node",
    name="scan_unifier"
  )

  ld.add_action(scan_front)
  ld.add_action(scan_rear)
  ld.add_action(base_driver)
  ld.add_action(move_base)
  ld.add_action(robot_state_publisher)
  ld.add_action(scan_unifier)

  return ld
