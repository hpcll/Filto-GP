import os
import unittest
from case import Case_list
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    name = open(os.getcwd()+"report.html","wb")
    runner = HTMLTestRunner(stream=name, verbosity=1,
                   title="Filto-GP自动化测试报告", description="报告如下")
    runner.run(unittest.main())