# coding:utf-8

from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import sys

def choose1():
    wen = askdirectory()
    if wen:
        wenjianjia.set(wen)
    else:
        return
def ok():
    with open('path.txt','w') as file:
        file.write(wenjianjia.get())
        file.close()
        messagebox.showinfo('提示','安装程序成功！')
        sys.exit()
def continue_the_installer():
    global wenjianjia
    '''继续安装'''
    a.pack_forget()
    b.pack_forget()
    c = LabelFrame(root,text='请回答下面的问题，以便我们继续安装')
    wenjianjia = StringVar(c)
    wenjianjia.set('这是您要保存相片文件的地址')
    d = Label(c,textvariable=wenjianjia)
    d.pack()
    e = Button(c,text='选择文件夹',command=choose1)
    e.pack()
    c.pack()
    Button(root,text='确定',command=ok).pack()
root = Tk()
root.title('车牌识别系统安装过程')
msg='欢迎使用车牌识别系统安装教程！\n\
该教程可以指引您安装车牌识别系统。\n\
请注意！这个软件虽然可以用，但需要您自己在您的电脑上\
人工创建文件夹，使用起来不方便，所以才做了一个安装教程。\n\
点击“继续”来执行。'
a = Label(root,text=msg)
a.pack()
b = Button(root,text='继续',command=continue_the_installer)
b.pack()
root.mainloop()