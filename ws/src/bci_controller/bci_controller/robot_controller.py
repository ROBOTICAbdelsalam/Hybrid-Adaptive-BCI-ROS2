import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist


class RobotController(Node):

    def __init__(self):

        super().__init__("robot_controller")

        self.subscription = self.create_subscription(
    String,
    "/eeg_command",
    self.command_callback,
    10
)

        self.cmd_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.get_logger().info("Robot Controller Started")


    def command_callback(self, msg):

        cmd = Twist()

        if msg.data == "LEFT":

            cmd.angular.z = 1.0

            self.get_logger().info("Robot Turning LEFT")

        elif msg.data == "RIGHT":

            cmd.angular.z = -1.0

            self.get_logger().info("Robot Turning RIGHT")

        elif msg.data == "STOP":

            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

            self.get_logger().info("Robot STOPPED")

        elif msg.data == "NO ACTION":

            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

            self.get_logger().info("Waiting...")

        self.cmd_pub.publish(cmd)


def main():

    rclpy.init()

    node = RobotController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()