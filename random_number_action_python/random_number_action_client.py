import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from randomnumberactioninterface.action import RandomNumber


class RandomNumberActionClient(Node):

    def __init__(self):
        super().__init__('random_number_action_client')
        self._action_client = ActionClient(self, RandomNumber, 'random_number')

    # 1번
    def send_goal(self, num1, num2):
        goal_msg = RandomNumber.Goal() # action파일의 goal 생성
        goal_msg.num1 = num1 # request시 사용할 데이터 지정 
        goal_msg.num2 = num2 # request시 사용할 데이터 지정 

        self._action_client.wait_for_server() # action server가 응답할때까지 대기
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.c_feedback_callback)
        self._send_goal_future.add_done_callback(self.c_goal_response_callback)

    # 2번
    def c_goal_response_callback(self, future):
        goal_handle = future.result() # Goal Service에서의 response
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async() # 3번
        self._get_result_future.add_done_callback(self.c_get_result_callback)

    # 5번
    def c_get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result_number : {0}'.format(result.result_number))
        rclpy.shutdown()

    # 4번
    def c_feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.temporary_number))


def main(args=None):
    rclpy.init(args=args)
    action_client = RandomNumberActionClient()
    action_client.send_goal(1,10)
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()