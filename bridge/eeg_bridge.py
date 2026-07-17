#!/usr/bin/env python3

import time
import pandas as pd
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


COMMAND_FILE = "/home/abdelsalam/Hybrid-Adaptive-BCI/realtime/results/realtime_commands.csv"


class EEGBridge(Node):

    def __init__(self):
        super().__init__("eeg_bridge")

        self.publisher = self.create_publisher(
            String,
            "eeg_command",
            10
        )

        self.last_command = None

        self.timer = self.create_timer(
            0.5,
            self.publish_command
        )

        self.get_logger().info("EEG Bridge Started")

    def publish_command(self):

        try:

            data = pd.read_csv(COMMAND_FILE)

            command = data.iloc[-1]["Command"]

            if command != self.last_command:

                msg = String()
                msg.data = command

                self.publisher.publish(msg)

                self.get_logger().info(
                    f"Published: {command}"
                )

                self.last_command = command

        except Exception as e:

            self.get_logger().warning(str(e))


def main():

    rclpy.init()

    node = EEGBridge()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()