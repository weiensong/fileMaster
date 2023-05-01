from constants import *
from handle_robot.xianyujingji_file import XianYuJingJi


class Master:
    def __init__(self, default_config):
        self.path = default_config['path']
        self.task_type = default_config['task_type']

    def built_robot(self):
        if self.task_type == TaskType.XIANYUJINGJI:
            XianYuJingJi(self.path).run_task()


