from tkinter import *
import math
import re
import tkinter
class text:
    def __init__(self, ct):
        self.ct = ct
        self.creat()
        self.key = None
    def creat(self):
        # 创建一个输入组件
        # self.aw = Label
        self.face = Label(relief=RAISED, font=('宋体', 24),height = 2,width=17, bg='white', anchor=SE)
        self.face.pack(side=TOP, pady=10)
        self.face1 = Label(relief=RAISED, font=('宋体', 24), height= 2, width=17, bg='white', anchor=SE)
        self.face1.pack(side=TOP, pady=10)
        self.face['text'] = '0'
        #容器的布局
        p = Frame(self.ct)
        p.pack()
        # 定义元组
        #//是求商
        # Key_tuple = ("AC", "←" , "/" , "*" ,
        #              "1","2", "3" , "-" ,
        #              "4" , "5" , "6", "+" ,
        #              "7", "8", "9", "//" ,
        #              "." , "0" , "%", "=",
        #              '**','(',')','')

        # num = len(Key_tuple)
        # for i in range(num):
        #     # 创建一个Button容器，将Button放入p组件中
        #     b = Button(p, text=Key_tuple[i], font=('微软雅黑', 20),height = 1, width=5,bd = 1)
        #     #grid按键的布局
        #     b.grid(row=i // 4, column=i % 4)
        b= tkinter.Button(self.ct, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=0, y=285, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=70, y=285, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=140, y=285, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=0, y=340, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=70, y=340, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=140, y=340, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=0, y=395, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=70, y=395, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=140, y=395, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=70, y=450, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        # 运算符号按钮
        b = tkinter.Button(self.ct, text='AC', bd=0.5, font=('黑体', 20), fg='orange')
        b.place(x=0, y=230, width=70, height=55)
        b.bind('<Button-1>', self.clean)
        b = tkinter.Button(self.ct, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5)
        b.place(x=70, y=230, width=70, height=55)
        b.bind('<Button-1>', self.tuige)
        b = tkinter.Button(self.ct, text='/', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5)
        b.place(x=140, y=230, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='*', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5,)
        b.place(x=210, y=230, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=210, y=285, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b= tkinter.Button(self.ct, text='+', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=210, y=340, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='+', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=210, y=395, width=70, height=55)
        b= tkinter.Button(self.ct, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=210, y=450, width=70, height=110)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='%', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=0, y=450, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=140, y=450, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='(', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=0, y=505, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text=')', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=70, y=505, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        b = tkinter.Button(self.ct, text='**', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
        b.place(x=140, y=505, width=70, height=55)
        b.bind('<Button-1>', self.dj)
        if b['text'] == 'AC':
            b.bind('<Button-1>', self.clean)
        if b['text'] == '←':
            b.bind('<Button-1>',self.tuige)
        # 定义一个记录输入数字次数的变量
        self.i = 0
    def dj(self, event):
        # 如果用户单击的是数字键或点号
        if(event.widget['text'] in ('0', '1', '2', '3','4', '5', '6', '7', '8', '9', '.','(',')')):
            # 判断self.i是否为0，0的话清空face['text']的值
            if self.face['text'] == '0':
                self.face['text'] = event.widget['text']
            else:
                # self.face['text'] = ''
                self.face['text'] = self.face['text'] + event.widget['text']
                self.i = self.i + 1
            print(self.i)
        # 如果用户单击了运算符
        elif(event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//','(',')')):

            # 把输入的数字与输入的字符相结合，组成一个数学运算式
            self.face['text'] = self.face['text'] + event.widget['text']

        elif (event.widget['text'] in ('√')):
            self.face['text'] = self.face['text'] + event.widget['text']
        elif(event.widget['text'] == '=' and self.face['text'] is not None):
            # 赋值给self.key
            self.key = self.face['text']
            print(self.key)
            # num1 = len(self.key)
            # if '√' in self.key:
            #     self.key.replace('√','pow()')
            # 使用eval函数计算表达式的值
            self.face1['text'] = str(eval(self.key))
            self.key = None
            self.i = 0
    # 点击c按钮时清空程序
    def clean(self, event):
        self.key = None
        self.face['text'] = '0'
        self.face1['text'] = '0'
    def tuige(self,event):
        # self.key = None
        k = []
        k = self.face['text']
        c = k[0:-1]
        self.face['text'] = c



Calculator = Tk()
Calculator.minsize(280,560)
Calculator.title("超级计算器")
text(Calculator)
Calculator.mainloop()