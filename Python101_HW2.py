from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title ('คำถามชวนปวดหัว')
GUI.geometry('1000x1000')

L1 = Label (GUI, text ='คำถาม: ถ้าเจอเหรียญบาดจะทำอย่างไร?', font =('Helvetica',30),fg='black')
L1.place (x=250,y=50)

F1 = Frame (GUI)
F1.place (x=412, y=120)

def Button1():
    text = 'ข้อหนึ่งห้ามลักทรัพย์เจ้าของหลับเราก็หยิบ'
    messagebox.showwarning ('ผิด', text)

def Button2 ():
    text = 'โธ่ว... พ่อคุณเหรียญบาดไป รพ.'
    messagebox.showwarning ('ผิด', text)
    
def Button3 ():
    text = 'เก่งมากเดี๋ยวลุงพาไปกินหนม'
    messagebox.showinfo ('ผิด', text)

def Button4 ():
    text = 'ช่างเป็นคนดีเสียจริง'
    messagebox.showwarning ('ผิด', text)

def Button5 ():
    text = 'เติมมาใช่ไหมสารภาพ'
    messagebox.showwarning ('ผิด', text)
    
def Button6 ():
    text = 'เออมามารำด้วยกันสิ'
    messagebox.showwarning ('ผิด', text)
    
B1 = ttk.Button(F1,text='1. เก็บใส่กระเป๋า', command=Button1)
B1.pack (ipadx=25, ipady=20)

B2 = ttk.Button(F1,text='2. ไปโรงพยาบาล', command=Button2)
B2.pack (ipadx=22, ipady=20)

B3 = ttk.Button(F1,text='3.ปล่อยไว้อย่างงั้น', command=Button3)
B3.pack (ipadx=20, ipady=20,)

B4 = ttk.Button(F1,text='4.เก็บไปคืนเจ้าของ', command=Button4)
B4.pack (ipadx=19, ipady=20)

B5 = ttk.Button(F1,text='5.ส่งยิ้มหวานให้', command=Button5)
B5.pack (ipadx=28, ipady=20)

B5 = ttk.Button(F1,text='6.รำขอเหรียญถวาย', command=Button6)
B5.pack (ipadx=18, ipady=20)

GUI.mainloop()

