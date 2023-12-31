import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.i = 0
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: {0}'.format(self.i)
        self.i += 1
        self.get_logger().info('Publishing: "{0}"'.format(msg.data))
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    try:
        talker = Talker()
        rclpy.spin(talker)
    finally:
        talker.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()