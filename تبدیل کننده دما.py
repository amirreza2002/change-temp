from tkinter import *
#creat base of gui
win = Tk()
win.geometry("600x150")
win.title("CHANGE TEMP")

#creat requirement label
l1 = Label(text="تبدیل دمای سانتیگراد به فارنهایت",fg="black", font=('B titr',17,'bold'))
l1.grid(padx=0,pady=0)
l2 = Label(text="دمای سانتیگراد", fg="black",font=('B nazanin',15))
l2.grid(padx=0,pady=20)
l3 = Label(text="دمای فارنهایت", fg="black",font=('B nazanin',15))
l3.place(x=90,y=105)

#for get input entry
input_user = StringVar()

#function that do calculate
def fun1():
    text1=int(input_user.get())
    res=(1.8*text1)+32
    l2 = Label(text=res , bg="yellow",fg="black",font=('B nazanin',15))
    l2.place(x=210,y=105)
    
#box that user enter information
en1 = Entry(win,textvariable=input_user)
en1.place(x=210,y=75)

#button for show result
b1 = Button(text="کلیک کنید",fg="black",command=fun1)
b1.place(x=375,y=70)

#run gui
win.mainloop()