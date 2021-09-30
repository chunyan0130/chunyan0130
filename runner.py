# run_test.py test_register.py register.py同一个目录下

import unittest
from unittest import loader
from test_register import *
from HTMLTestRunner import *



#步骤一 创建一个测试套件
#步骤二 将测试用例添加到测试套件
suite = unittest.TestSuite()

# # #方法1
# case=TestRegister("test_register_success")
# suite.addTest(case)


#方法2
# case1=TestRegister("test_username_isnull")
# case2=TestRegister("test_register_success")
# suite.addTests([case1,case2])


#方法3 
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))

# #方法4? 导入的就是model，这里该怎么写？
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(TestRegister))

# #方法5
# loader=unittest.TestLoader()
# suite.addTest(loader.discover(r"/Users/didi/testbranch/wangcyPython"))

#方法6
loader=unittest.TestLoader()
suite.addTest(loader.discover(start_dir =r"/Users/didi/testbranch/chunyan0130", pattern="test_*.py"))


if __name__=="__main__":
   # 存放报告路径
   filepath = '/Users/didi/testbranch/chunyan0130/report/report.html'
   fp=open(filepath,'wb')
   #定义测试报告的标题与描述
   runner = HTMLTestRunner(stream=fp,verbosity=1,title='我是风起怨江南的测试报告标题',description='我是风起怨江南的测试报告描述',)
   runner.run(suite)
   fp.close()
