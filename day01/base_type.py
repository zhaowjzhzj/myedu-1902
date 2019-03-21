# 注释
# model  模块
# main   主要的
# print  打印
# def  声明方法
# int  整数
# demo  例子
# 代码的层级关系是通过缩进来表示的
# class  类,类型
# str string 字符
# 合法标识符(变量名方法名):必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感,不可用关键字做标识符
# Ctrl+alt+L 格式化代码


# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量,并赋值 1
    aint = 1
    # 打印aint 的值
    print(aint)
    # 打印aint 的,类型;type(aint):获取aint的类型
    print(type(aint))


#
def add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint



    # 提取变量 ctrl+alt+v

    # result = add(1, 2)
    # print(result)


def sub(aint, bint):
    print(aint)
    print(bint)
    return aint - bint

def float_demo():
    afloat = 1.90
    print(afloat)

if __name__ == '__main__':
    # 调用add方法 传入1,2得到返回值,赋值给result变量
    # sub2 = sub(1,2)
    # print(sub2)
    # 加注释Ctrl+/
    float_demo()




