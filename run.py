import os
import time
import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner




if __name__ == '__main__':
    current_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(current_path)  # 项目路径
    case_path = BASE_DIR + os.sep + "test" + os.sep + "case"
    report_file = BASE_DIR + os.sep + "report" + os.sep + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".html"
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    discover_suite = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')

    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=report_title, description=desc)
        runner.run(discover_suite)