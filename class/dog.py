class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        '''初始化属性 name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + " is now sitting")

    def row_over(self):
        '''模拟小狗打滚'''
        print(self.name.title() + " is now row over")

mydog=Dog('wille',6)
print('my dog name is ' + mydog.name.title()+'.')
print('my dog age is' + str(mydog.age)+'.')
mydog.sit()
mydog.row_over()