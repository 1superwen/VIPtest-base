#__author__ = 'lc'
'''
���ܣ�
    1.����unittestװ�����淶

'''



class Aplus:
    member = "this is a test."
    def __init__(self):
        pass

    @classmethod
    def Print1(cls):
        print("print 1: ", cls.member)

    def Print2(self):
        print("print 1: ", self.member)


    @classmethod
    def Print3(paraTest):
        print("print 3: ", paraTest.member)

    @staticmethod
    def print4():
        print("hello")


a = Aplus()
Aplus.Print1()
a.Print1()
#A.Print2()
a.Print2()
Aplus.Print3()
a.Print3()
Aplus.print4()
