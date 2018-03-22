# -*- coding:utf-8 -*-
__author__ = u"北京 - 柳"
class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b


    # 加法
    def add(self):
        return (self.a + self.b)
    
    # 减法
    def sub(self):
        return (self.a - self.b)
    
    # 乘法
    def mul(self):
        return (self.a * self.b)


    # 除法
    def div(self):
        try:
            print (self.a / self.b)
        except ZeroDivisionError:
            print ("错误：第二个数不可以为零")
    '''
    def div(self):
        if b != 0:
            print round(self.a / self.b)
        raise "错误！第二个数是零"
    '''




    #重置
    def reset(self, a, b):
        self.a = a
        self.b = b

def test(calc):
    sumR = calc.add()
    subR = calc.sub()
    mulR = calc.mul()
    divR = calc.div()
    print( sumR, subR, mulR, divR)

if __name__ == "__main__":
   a  = int(input("请输入第一个数字："))
   b  = int(input("请输入第二个数字："))
   calc = Calc(a, b)
   test(calc)
   calc.reset(12, 7)
   test(calc)
 