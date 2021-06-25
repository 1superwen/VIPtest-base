"""
功能描述：
编写人：SongXuwen
编写日期：
实现逻辑：
    1.
    2.
    3.

"""
import unittest


# from myfun import *

class myTest(unittest.TestCase):

    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        print('执行test_add')
        self.assertEqual(3, 3)

    def test_mul(self):
        print('执行test_mul')
        self.assertEqual(1, 2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(myTest('test_add'))
    # suite.addTest(myTest('test_mul'))
    suite.addTests((myTest('test_add'), myTest('test_mul')))
    # print(suite)

    # suite = unittest.TestLoader().discover(start_dir='D:/code/VIPtest-base/Pra_unittest', pattern='test*.py')
    # print('---', suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)
