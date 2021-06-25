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
from ddt import ddt,data,unpack,file_data

@ddt
class TestMy(unittest.TestCase):
    @file_data('data.json')
    def test_fun(self,a):
        print(type(a))

if __name__ == '__main__':
    unittest.main()