from master import Master
"""
任务类型：
1、广西县域文件处理
"""
default_config = {
    "task_type": 1,
    "path": "input/re.xlsx"
}

if __name__ == '__main__':
    Master(default_config).built_robot()
