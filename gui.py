from tkinter import *
import time
from datetime import datetime as dt

web_list=[]
window=Tk()

def add_web():
    new=e1_value.get()
    web_list.append(new)
    length=len(web_list)
    line=web_list[length-1:length]
    l1.insert(END,line)
    print(web_list)
    e1.delete(0,'end')

def web_block():
    hosts_temp="hosts"
    host_path=r"C:\Windows\System32\drivers\etc\hosts"
    redirect="127.0.0.1"
    start=int(e2_value.get())
    end=int(e3_value.get())

    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end):
            print("Working Hours")
            with open(host_path,'r+') as file:
                content=file.read()
                for website in web_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+ " "+website+"\n")
        else:
            with open(host_path,'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in web_list):
                        file.write(line)
                file.truncate()

            print("Fun hours")
        time.sleep(5)

def pop_web():
    l1.delete(len(web_list)-1)
    web_list.pop()
    print(web_list)


Label(window,text='Website Blocker',font=('Times New Roman','15')).grid(row=0,column=0)
b1=Button(window,text="+",command=add_web)
b1.grid(row=1,column=2)

b3=Button(window,text="-",command=pop_web)
b3.grid(row=2,column=2)


b2=Button(window,text="Block",command=web_block)
b2.grid(row=2,column=3,padx=20,pady=10,ipadx=20)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.place(x=10,y=10,width=200,height=100)
e1.grid(row=1,column=1,padx=20,pady=10,ipadx=20)

Label(window,text='Enter Website URL',font=('Arial','10')).grid(row=1,column=0)
Label(window,text='Start Time   -->',font=('Arial','10')).grid(row=2,column=0)
Label(window,text='End Time     -->',font=('Arial','10')).grid(row=3,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=2,column=1)

e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=3,column=1)

s1=Scrollbar(window)
s1.grid(row=1,column=4)
l1=Listbox(window,yscrollcommand=s1.set)
l1.grid(row=1,column=3,padx=10,pady=10,ipadx=20)
s1.config(command=l1.yview)

window.mainloop()
print(web_list)
