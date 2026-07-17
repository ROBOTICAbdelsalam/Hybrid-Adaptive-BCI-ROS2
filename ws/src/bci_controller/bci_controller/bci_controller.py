import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EEGPublisher(Node):

    def __init__(self):
        super().__init__('eeg_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'eeg_topic',
            10)

        self.timer = self.create_timer(
            1.0,
            self.publish_message)

    def publish_message(self):

        msg = String()

        msg.data = "EEG Signal"

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')


def main(args=None):

    rclpy.init(args=args)

    node = EEGPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()

