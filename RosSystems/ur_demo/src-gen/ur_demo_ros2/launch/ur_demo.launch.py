from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  ld = LaunchDescription()

  controller_stopper = Node(
    package="controller_stopper",
    executable="controller_stopper_node",
    name="controller_stopper",
    parameters=[
      { "consistent_controllers" : ["joint_state_controller", "speed_scaling_state_controller", "force_torque_sensor_controller", "robot_status_controller"] }
    ],
    remappings=[
      ("robot_running", "ur_hardware_interface/robot_program_running")]
  )
  ur_robot_state_helper = Node(
    package="ur_robot_driver",
    executable="robot_state_helper",
    name="ur_robot_state_helper",
    namespace="ur_hardware_interface",
    remappings=[
      ("safety_mode", "ur_hardware_interface/safety_mode"),
      ("robot_mode", "ur_hardware_interface/robot_mode"),
      ("set_mode", "ur_hardware_interface/set_mode")]
  )
  ros_control_controller_spawner = Node(
    package="controller_manager",
    executable="spawner",
    name="ros_control_controller_spawner",
    parameters=[
      { "/hardware_control_loop/loop_hz" : 500 },
      { "/ur_hardware_interface/joints" : ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"] },
      { "/joint_state_controller/type" : "joint_state_controller/JointStateController" },
      { "/joint_state_controller/publish_rate" : 500 },
      { "/force_torque_sensor_controller/type" : "force_torque_sensor_controller/ForceTorqueSensorController" },
      { "/force_torque_sensor_controller/publish_rate" : 500 },
      { "/speed_scaling_state_controller/type" : "ur_controllers/SpeedScalingStateController" },
      { "/speed_scaling_state_controller/publish_rate" : 500 },
      { "/joint_group_vel_controller/type" : "velocity_controllers/JointGroupVelocityController" },
      { "/robot_status_controller/type" : "industrial_robot_status_controller/IndustrialRobotStatusController" },
      { "/robot_status_controller/publish_rate" : 10 },
      { "/robot_status_controller/handle_name" : "industrial_robot_status_handle" },
      { "scaled_pos_joint_traj_controller/joints" : ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"] },
      { "scaled_pos_joint_traj_controller/type" : "position_controllers/ScaledJointTrajectoryController" },
      { "scaled_pos_joint_traj_controller/constraints" : [, , , , , , , ] },
      { "scaled_pos_joint_traj_controller/stop_trajectory_duration" : 0.5 },
      { "scaled_pos_joint_traj_controller/state_publish_rate" : 500.0 },
      { "scaled_pos_joint_traj_controller/action_monitor_rate" : 20 },
      { "pos_joint_traj_controller/type" : "position_controllers/JointTrajectoryController" },
      { "pos_joint_traj_controller/joints" : ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"] },
      { "pos_joint_traj_controller/constraints" : [, , , , , , , ] },
      { "pos_joint_traj_controller/stop_trajectory_duration" : 0.5 },
      { "pos_joint_traj_controller/state_publish_rate" : 500.0 },
      { "pos_joint_traj_controller/action_monitor_rate" : 20 },
      { "scaled_vel_joint_traj_controller/type" : "position_controllers/JointTrajectoryController" },
      { "scaled_vel_joint_traj_controller/joints" : ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"] },
      { "scaled_vel_joint_traj_controller/constraints" : [, , ] },
      { "scaled_vel_joint_traj_controller/gains" : [, , , , , ] },
      { "scaled_vel_joint_traj_controller/velocity_ff" : [, , , , , ] },
      { "scaled_vel_joint_traj_controller/stop_trajectory_duration" : 0.5 },
      { "scaled_vel_joint_traj_controller/state_publish_rate" : 500.0 },
      { "scaled_vel_joint_traj_controller/action_monitor_rate" : 20 },
      { "vel_joint_traj_controller/type" : "velocity_controllers/JointTrajectoryController" },
      { "vel_joint_traj_controller/joints" : ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"] },
      { "vel_joint_traj_controller/constraints" : [, , ] },
      { "vel_joint_traj_controller/gains" : [, , , , , ] },
      { "vel_joint_traj_controller/velocity_ff" : [, , , , , ] },
      { "vel_joint_traj_controller/stop_trajectory_duration" : 0.5 },
      { "vel_joint_traj_controller/state_publish_rate" : 500 },
      { "vel_joint_traj_controller/action_monitor_rate" : 20 }
    ],
    remappings=[
      ("set_mode", "ur_hardware_interface/set_mode")]
  )
  robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    name="robot_state_publisher"
  )
  ur_hardware_interface = Node(
    package="ur_robot_driver",
    executable="ur_robot_driver_node",
    name="ur_hardware_interface",
    parameters=[
      { "script_sender_port" : 50002 },
      { "use_tool_communication" : false },
      { "tf_prefix" : "" },
      { "input_recipe_file" : "" },
      { "script_file" : "" },
      { "robot_ip" : "192.168.56.101" },
      { "tool_tx_idle_chars" : 3.5 },
      { "tool_stop_bits" : 1 },
      { "output_recipe_file" : "" },
      { "tool_rx_idle_chars" : 1.5 },
      { "tool_voltage" : 0 },
      { "tool_baud_rate" : 115200 },
      { "tool_parity" : 0 },
      { "reverse_port" : 50001 },
      { "headless_mode" : false },
      { "kinematics/shoulder" : [, , , , , ] },
      { "kinematics/upper_arm" : [, , , , , ] },
      { "kinematics/forearm" : [, , , , , ] },
      { "kinematics/wrist_1" : [, , , , , ] },
      { "kinematics/wrist_2" : [, , , , , ] },
      { "kinematics/wrist_3" : [, , , , , ] },
      { "kinematics/hash" : "calib_12788084448423163542" }
    ]
  )

  ld.add_action(controller_stopper)
  ld.add_action(ur_robot_state_helper)
  ld.add_action(ros_control_controller_spawner)
  ld.add_action(robot_state_publisher)
  ld.add_action(ur_hardware_interface)

  return ld
