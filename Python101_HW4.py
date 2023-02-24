from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#################

from datetime import datetime

#################
import  csv

def writecsv(datalist):
    with open ('data.csv','a',encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open ('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

##################

Gui = Tk()
Gui.title('โปรแกรมบันทึกข้อมูลคนไข้')
Gui.geometry('500x1000')

L1 = Label(Gui, text='ลงทะเบียนผู้ป่วยใหม่', font =('Angsana New',20), fg='white')
L1.place(x=165, y=50)

LF1 = ttk.LabelFrame(Gui, text='หมายเลขประจำตัวคนไข้')
LF1.place (x=140, y=150)

LF2 = ttk.LabelFrame(Gui, text='หมายเลขบัตรประชาชน')
LF2.place(x=140, y=250)

LF3 = ttk.LabelFrame(Gui, text='ชื่อ-นามสกุล')
LF3.place(x=140,y=350)

####################
HN_data = StringVar()
Box1 = ttk.Entry(LF1, textvariable=HN_data, font=('Angsana New',16))
Box1.pack (ipadx = 5, ipady = 5)

ID_data = StringVar()
Box2 = ttk.Entry(LF2, textvariable=ID_data, font=('Angsana New',16))
Box2.pack (ipadx = 5, ipady = 5)

Name_data = StringVar()
Box3 = ttk.Entry(LF3, textvariable=Name_data, font=('Angsana New',16))
Box3.pack (ipadx=5, ipady=5)

def saveData ():
    t = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    data = [HN_data.get(),ID_data.get(),Name_data.get()]
    text = [t,data]
    writecsv(text)
    HN_data.set('')
    ID_data.set('')
    Name_data.set('')

B1 = ttk.Button (Gui, text='บันทึกข้อมูล', command=saveData)
B1.pack(ipadx=10,ipady=10)
B1.place(x=200, y=450)

Gui.mainloop()
