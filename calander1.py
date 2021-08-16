from tkinter import *
ii=Tk()
ii.geometry("500x500")
ii.title("calender")
ii.config(bg="white")
ca1=Frame(ii)
ca1.pack(side=TOP)
ca=Frame(ii)
ca.pack()
def call():
    if o1.index(q1.get())<7:
        if o1.index(q1.get())%2==0:
            c=31
        else:
            c=30
    else:
        if o1.index(q1.get())%2==0:
            c=30
        else:
            c=31
    if o1.index(q1.get())==1:
        c=28
    n=int(q.get())-1
    a=[1,2,3,4,5,6,7,8]
    a[1]="SUNDAY   "
    a[2]="MONDAY   "
    a[3]="TUESDAY  "
    a[4]="WEDNESDAY"
    a[5]="THURSDAY "
    a[6]="FRIDAY   "
    a[7]="SATURDAY "
    p=n
    ww=0
    zz=Label(ca,text=q1.get(),bg="white",fg="red").pack()
    while n>=1:
        s=a[ww+1]+"\t"+"\t"
        for i in range(8-n,c+1,7):
            s=s+str(i)+"\t"
        if ww==0:
            x=Label(ca,text=s,fg="red")
            x.pack(anchor=W)
        else:
            x=Label(ca,text=s)
            x.pack(anchor=W)
        ww+=1
        n=n-1
    j=1
    n=p
    while n<7:
        s=a[ww+1]
        for i in range(j,c+1,7):
            s=s+"\t"+str(i)
        if ww==0:
            x=Label(ca,text=s,fg="red")
            x.pack(anchor=W)
        else:
            x=Label(ca,text=s)
            x.pack(anchor=W)
        n=n+1
        j=j+1
        ww+=1
v1=Label(ca1,fg="green",text="This is program to display the calander of year.\nPlease  enter the starting number of day \nfrom sunday ::").pack()
o=[1,2,3,4,5,6,7]
q=StringVar(ii)
q.set(o[0])
w=OptionMenu(ca1,q,*o).pack(side=LEFT)
o1=["JANUVARY","FABRUARY","MARCH","APRILL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
q1=StringVar(ii)
q1.set(o1[2])
w=OptionMenu(ca1,q1,*o1).pack(side=LEFT)
v=Button(ca1,text="SUBMIT",command=call).pack(side=LEFT)
ii.mainloop()
