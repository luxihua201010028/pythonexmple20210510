# 默认参数
# def printstring(var1='hello', var2='world'):
#     tempstr = var1 + var2
#     print(tempstr)
#
#
# print(printstring(' val2'))
# 可变参数
# def getcomputer(*arg):
#     sum1 = 0
#     for item in arg:
#         sum1 += item
#     print(sum1)
#
#
# print(getcomputer(1, 2, 3, 4, 5, 6))

def keyfun(**arg):
    print(arg)

val1={'name':'peter','age':36}
keyfun(**val1)
keyfun(name='peter',age=35)