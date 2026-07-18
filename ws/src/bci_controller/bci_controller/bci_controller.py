import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EEGPublisher(Node):

    def __init__(self):
        super().__init__("eeg_publisher")

        self.publisher = self.create_publisher(
            String,
            "/eeg_command",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

        self.commands = [
            "LEFT",
            "RIGHT",
            "STOP",
            "NO ACTION"
        ]

        self.index = 0

        self.get_logger().info("EEG Publisher Started")

    def publish_message(self):

        msg = String()

        msg.data = self.commands[self.index]

        self.publisher.publish(msg)

        self.get_logger().info(f"Publishing: {msg.data}")

        self.index = (self.index + 1) % len(self.commands)


def main(args=None):

    rclpy.init(args=args)

    node = EEGPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()