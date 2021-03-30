from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog,colorchooser
from Module.Calculator import *
from Module.Resonant import *
from Module.frozen_dir import * #冻结路径



root=Tk()
root.title('NJUGDS')



## Definite some grid variables
row1=0
col1=5

row_wz=6
col_wz=1

row_zw=7
col_zw=1

row_lambda=8
col_lambda=1

row_design=11
col_design=1


##  Calculator grid
Label(root,text="er：").grid(row=row1,column=col1)
Label(root,text="s：").grid(row=row1+1,column=col1)
Label(root,text="[um]").grid(row=row1+1,column=col1+2)

Label(root,text="h：").grid(row=row1+2,column=col1)
Label(root,text="[um]").grid(row=row1+2,column=col1+2)

Label(root,text="f0：").grid(row=row1+3,column=col1)
Label(root,text="[GHZ]").grid(row=row1+3,column=col1+2)

Label(root,text="w:").grid(row=row_wz,column=col_wz)
Label(root,text="[um]").grid(row=row_wz,column=col_wz+2)
Label(root,text=">>>").grid(row=row_wz,column=col_wz+4)
Label(root,text="Z0:").grid(row=row_wz,column=col_wz+5)
Label(root,text="[ohm]").grid(row=row_wz,column=col_wz+7)

Label(root,text="Z0:").grid(row=row_zw,column=col_zw)
Label(root,text="[ohm]").grid(row=row_zw,column=col_zw+2)
Label(root,text=">>>").grid(row=row_zw,column=5)
Label(root,text="w:").grid(row=row_zw,column=col_zw+5)
Label(root,text="[um]").grid(row=row_zw,column=col_zw+7)

Label(root,text="lambda/4:").grid(row=row_lambda,column=col_lambda)
Label(root,text="[um]").grid(row=row_lambda,column=col_lambda+2)


## Blank Space
Label(root,text="================================================================================").grid(row=4,rowspan=2,column=0,columnspan=10)
Label(root,text="================================================================================").grid(row=row_lambda+1,rowspan=2,column=0,columnspan=10)
Label(root,text="================================================================================").grid(row=row_design+3,rowspan=2,column=0,columnspan=10)



## Design GDS
Label(root,text="Resonant_Frequency_min").grid(row=row_design,column=1)
Label(root,text="[GHZ]").grid(row=row_design,column=3)
Label(root,text="Resonant_Frequency_max").grid(row=row_design,column=5)
Label(root,text="[GHZ]").grid(row=row_design,column=7)
Label(root,text="Resonant_Num").grid(row=row_design+1,column=1)
Label(root,text="Resonant_Interval").grid(row=row_design+2,column=1)
Label(root,text="[MHZ]").grid(row=row_design+2,column=3)

## Sample Box
Label(root,text="Sample Box:").grid(row=row_design+2,column=5)



# 这样可以加一个初始默认功能
V1=StringVar()
V2=StringVar()
V1.set(11.9)
V2.set(10)
V3=StringVar()
V3.set(450)
V4=StringVar()
V4.set(6.5)
V5=StringVar()
V5.set(6)
V6=StringVar()
V7=StringVar()
V7.set(50)
V8=StringVar()
V9=StringVar()


## Entry box
e1=Entry(root,textvariable=V1)
e1.grid(row=0,column=col1+1,padx=10,pady=5)
e2=Entry(root,textvariable=V2)
e2.grid(row=1,column=col1+1,padx=10,pady=5)
e3=Entry(root,textvariable=V3)
e3.grid(row=2,column=col1+1,padx=10,pady=5)
e4=Entry(root,textvariable=V4)
e4.grid(row=3,column=col1+1,padx=10,pady=5)


# w2z entry
e5=Entry(root,textvariable=V5)
e5.grid(row=row_wz,column=col_wz+1,padx=10,pady=5)
e6=Entry(root,state="readonly",textvariable=V6)
e6.grid(row=row_wz,column=col_wz+6,padx=10,pady=5)


# z2w entry
e7=Entry(root,textvariable=V7)
e7.grid(row=row_zw,column=col_zw+1,padx=10,pady=5)
e8=Entry(root,state="readonly",textvariable=V8)
e8.grid(row=row_zw,column=col_zw+6,padx=10,pady=5)

# lambda/4 entry
e9=Entry(root,textvariable=V9,state="readonly")
e9.grid(row=row_lambda,column=col_lambda+1,padx=10,pady=5)

# Design entry
e10=Entry(root)
e10.grid(row=row_design,column=2,padx=10,pady=5)
e11=Entry(root,state="readonly")
e11.grid(row=row_design,column=6,padx=10,pady=5)

# num
e12=Entry(root)
e12.grid(row=row_design+1,column=2,padx=10,pady=5)

# interval
e13=Entry(root)
e13.grid(row=row_design+2,column=2,padx=10,pady=5)



## Sample box choices
OPTIONS=[
        '',
        "10mm*10mm(24)",
         "10mm*10mm(28)",
         "16mm*16mm(44)",
]
variable1=StringVar()
variable1.set("None")
sb=ttk.OptionMenu(root,variable1,*OPTIONS)
sb.grid(row=row_design+2,column=6)




## Photo Insertion
fileaddress=app_path()
photo=PhotoImage(file='%s/../pics/cpw.gif'%fileaddress)
# 注意Tkinter只支持gif图片，就算改后缀也没用!

imageLabel=Label(root,image=photo)
imageLabel.grid(row=0,rowspan=3,column=1,columnspan=4,padx=10,pady=5)


## functions of button
def ana():
    e0=float(e1.get())
    s=float(e2.get())/1000
    h=float(e3.get())/1000
    f0=float(e4.get())*1000
    w0=float(e5.get())/1000
    obj=CALC(e0,s,h,f0,w0=w0)
    result=obj.analyse()
    V6.set(str(result[0]))
    V9.set(str(result[1]*1000))

def syn():
    e0 = float(e1.get())
    s = float(e2.get())/1000
    h = float(e3.get())/1000
    f0 = float(e4.get())*1000
    z0=float(e7.get())
    obj=CALC(e0,s,h,f0,z0=z0)
    result=obj.synthesis()
    V8.set(str(result[0]*1000))
    V9.set(str(result[1]*1000))

def saveaddress():
    fileName=filedialog.asksaveasfilename(defaultextension=".gds",filetypes=[("GDS",".gds")])
    # 限定和自动添加文件后缀
    print(fileName)

    X=0     # 第一个比特位置（默认为0，在选取样品盒大小后略作修改）
    b=CPW(10,6)
    e0 = float(e1.get())
    s = float(e2.get()) / 1000
    h = float(e3.get()) / 1000
    f_min=float(e10.get())*1000
    interval=float(e13.get())
    num=int(e12.get())
    X-=int(num/2)*384

    if variable1.get()=="10mm*10mm(24)":
        print("The Choice:10*10!")
        t1=10000/7
        half_distance=10000/2
        edge = half_distance - 400
        for i in range(6):
            b.pad(-edge, (i+1)*t1-half_distance, "right")
            b.pad(edge, (i+1)*t1-half_distance, "left")
            b.pad((i+1)*t1-half_distance, -edge, "up")
            b.pad((i+1)*t1-half_distance, edge, "down")

    elif variable1.get()=="10mm*10mm(28)":
        t2=10000/8
        half_distance=10000/2
        edge=half_distance-400
        for i in range(7):
            b.pad(-edge, (i+1)*t2-half_distance, "right")
            b.pad(edge, (i+1)*t2-half_distance, "left")
            b.pad((i+1)*t2-half_distance, -edge, "up")
            b.pad((i+1)*t2-half_distance, edge, "down")
    elif variable1.get()=="16mm*16mm(44)":
        t3=16000/12
        half_distance=16000/2
        edge=half_distance-400
        for i in range(11):
            b.pad(-edge, (i+1)*t3-half_distance, "right")
            b.pad(edge, (i+1)*t3-half_distance, "left")
            b.pad((i+1)*t3-half_distance, -edge, "up")
            b.pad((i+1)*t3-half_distance, edge, "down")
    else:
        pass

    while num:
        cal=CALC(e0,s,h,f_min)
        res = cal.analyse()
        length=res[1]*1000
        b.resonator(length,X=X)
        b.sink(X=X)
        b.ten(X=X)
        b.drive_line(X=X)
        X+=384
        num-=1
        f_min+=interval

    b.save(fileName)



## buttons
ttk.Button(root,text="Analyze",width=10,command=ana)\
    .grid(row=row_wz,column=4,sticky=W,padx=10,pady=5)
ttk.Button(root,text="Synthesis",width=10,command=syn)\
    .grid(row=row_zw,column=col_zw+3,sticky=W,padx=10,pady=5)
ttk.Button(root,text="Quit",width=10,command=root.quit)\
    .grid(row=row_design+6,column=7,sticky=E,padx=10,pady=5)

# Draw Button
ttk.Button(root,text="Draw!",width=10,command=saveaddress)\
    .grid(row=row_design+6,column=4,sticky=E,padx=10,pady=5)

# e.delete(0,END)
# e.insert(0,"默认文本")

mainloop()