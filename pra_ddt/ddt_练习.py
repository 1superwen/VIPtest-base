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
from ddt import ddt, data, unpack

list1 = [5, 6, 7]
@ddt
class my_test(unittest.TestCase):
    @data(1)
    def test_one(self,value):
        print(value)
        self.assertEqual(value, 1)
    @data(1,2,3,4,5,6)
    def test_two(self,value):
        print(value)
        self.assertEqual(value, 2)
    @data(*list1)
    def test_three(self,value):
        print(value)
        self.assertEqual(value, 1)

if __name__ == '__main__':
    unittest.main()