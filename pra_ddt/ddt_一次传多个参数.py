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

# test_data = [[1,2],[3,4]]
#
# @ddt
# class my_test(unittest.TestCase):
#     @data((1,2))
#     @unpack
#     def test_one(self,value1, value2):
#         print(value1,value2)
#         self.assertEqual(value1,value2)
#     @data([1,1], (1,2))
#     @unpack
#     def test_two(self,value1, value2):
#         print(value1, value2)
#         self.assertEqual(value1, value2)
#     @data(*test_data)
#     @unpack
#     def test_three(self,value1, value2):
#         print(value1, value2)
#         self.assertEqual(value1, value2)

test_dict = [{'value1': 1, 'value2': 1}, {'value1': 3, 'value2': 4}]


@ddt
class my_test2(unittest.TestCase):
    @data(*test_dict)
    @unpack
    def test_one(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1, value2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
