import unittest
from Greeter import MyGreeter

class MyGreeterTest(unittest.TestCase):  # 继承unittest.TestCase
    def test_Client(self):
        g = MyGreeter()
        result = g.Client()
        self.assertEqual(result, 'Good morning')

if __name__ == '__main__':
    unittest.main()#运行所有的测试用例