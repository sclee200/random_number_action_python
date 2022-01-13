import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from randomnumberactioninterface.action import RandomNumber
import random


'''
난수가 5이면 respose, 그렇지 않으면 feedback
'''


class RandomNumberActionServer(Node):

    def __init__(self):
        super().__init__('random_number_action_server')
        self._action_server = ActionServer(
            self,
            RandomNumber,
            'random_number',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        feedback_msg = RandomNumber.Feedback()
        
        while True:
            x = random.randint(goal_handle.request.num1,goal_handle.request.num2)
            self.get_logger().info('generated random number : {0}'.format(x))

            if x == 5: # response
                goal_handle.succeed()
                result = RandomNumber.Result()
                result.result_number = x
                return result

            else:  #feedback
                feedback_msg.temporary_number = x
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1)

 

def main(args=None):
    rclpy.init(args=args)
    random_number_action_server = RandomNumberActionServer()
    rclpy.spin(random_number_action_server)


if __name__ == '__main__':
    main()