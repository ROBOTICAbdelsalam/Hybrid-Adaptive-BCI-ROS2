#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotController(Node):

    def __init__(self):

        super().__init__("robot_controller")

        self.subscription = self.create_subscription(
            String,
            "eeg_command",
            self.command_callback,
            10
        )

        self.get_logger().info("Robot Controller Started")


    def command_callback(self, msg):

        command = msg.data

        if command == "LEFT":
            self.get_logger().info("Robot Turning LEFT")

        elif command == "RIGHT":
            self.get_logger().info("Robot Turning RIGHT")

        elif command == "STOP":
            self.get_logger().info("Robot STOPPED")

        elif command == "NO ACTION":
            self.get_logger().info("Waiting...")

        else:
            self.get_logger().warning(f"Unknown Command: {command}")


def main():

    rclpy.init()

    node = RobotController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()