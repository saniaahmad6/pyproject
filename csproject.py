import pickle,tkinter,os

def i_write():
    
        
        def entry():
            f=open('database.dat','ab')
            d=dict()
            d['Admission No.']=k2.get()
            d['Name']=l2.get()
            d['Contact No.']=m2.get()
            d['Roll No']=n2.get()
            d['Class']=o2.get()
            d['Maths']=p2.get()
            d['English']=q2.get()
            d['Physics']=r2.get()
            d['Chemistry']=s2.get()
            d['Computer Science']=t2.get()
            pickle.dump(d,f)
            f.close()
            i_page.destroy()
        
    
        T=('Admission No.','Name','Contact No.','Roll No','Class','Maths','English','Physics','Chemistry','Computer Science')
        i_page=tkinter.Tk()
        i_page.geometry('700x700')
            
            
        i_page.title("Student Record")
        i_page.configure(bg='Yellow')
        h=tkinter.Label(i_page,text='RECORD ENTRY PAGE',bg='Yellow',font=("Aharoni",25,'bold','underline')).pack()
       
        h2=tkinter.Label(i_page,text='Please enter the following information:',font=("Time New Roman",15),bg="white")
        h2.place(x=1,y=50)
        k1=tkinter.Label(i_page,text='ENTER ADMN NO:',font=("Times New Roman",15),bg='yellow')
        k1.place(x=100,y=100)
        k2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        k2.place(x=400,y=100)
        l1=tkinter.Label(i_page,text='ENTER NAME:',font=("Times New Roman",15),bg='yellow')
        l1.place(x=100,y=150)
        l2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        l2.place(x=400,y=150)
        m1=tkinter.Label(i_page,text='ENTER CONTACT NO:',font=("Times New Roman",15),bg='yellow')
        m1.place(x=100,y=200)
        m2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        m2.place(x=400,y=200)
        n1=tkinter.Label(i_page,text='ENTER ROLL NO:',font=("Times New Roman",15),bg='yellow')
        n1.place(x=100,y=250)
        n2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        n2.place(x=400,y=250)
        o1=tkinter.Label(i_page,text='ENTER CLASS:',font=("Times New Roman",15),bg='yellow')
        o1.place(x=100,y=300)
        o2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        o2.place(x=400,y=300)
        h3=tkinter.Label(i_page,text='Please enter your marks in the following subjects:',font=("Time New Roman",15),bg="white")
        h3.place(x=1,y=350)
        p1=tkinter.Label(i_page,text='MATHEMATICS',font=("Times New Roman",15),bg='yellow')
        p1.place(x=100,y=400)
        p2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        p2.place(x=400,y=400)
        q1=tkinter.Label(i_page,text='ENGLISH',font=("Times New Roman",15),bg='yellow')
        q1.place(x=100,y=450)
        q2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        q2.place(x=400,y=450)
        r1=tkinter.Label(i_page,text='PHYSICS',font=("Times New Roman",15),bg='yellow')
        r1.place(x=100,y=500)
        r2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        r2.place(x=400,y=500)
        s1=tkinter.Label(i_page,text='CHEMISTRY',font=("Times New Roman",15),bg='yellow')
        s1.place(x=100,y=550)
        s2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        s2.place(x=400,y=550)
        t1=tkinter.Label(i_page,text='COMPUTER SC',font=("Times New Roman",15),bg='yellow')
        t1.place(x=100,y=600)
        t2=tkinter.Entry(i_page,width=20,font=("Times New Roman",15))
        t2.place(x=400,y=600)
        sub=tkinter.Button(i_page,text='SUBMIT',font=("Arial",15,'bold'),bg='Red',fg="white",command=entry)
        sub.place(x=285,y=650)
           
    
def d_page():
    def admin():
        def display():
            print('y')
            f1=open('another.dat','wb')
            f=open('database.dat','rb')
            try:
               
                while True:
                
                
                    d=pickle.load(f)
                    if d['Admission No.']!=e.get():
                        pickle.dump(d,f1)
                            
            except EOFError:
                pass
            f1.close()
            f.close()
            os.rename('database.dat','old.dat')
            os.remove('old.dat')
            os.rename('another.dat','database.dat')
                       

            
                   
            
            
            
            page.destroy()
            
        try:
            f=open('database.dat','rb')
            while True:
                p=pickle.load(f)
                if p['Admission No.']==e.get():
                    f.close()
                    display()
                    
                    break
                     
                
                
                    
            
        except EOFError:
            output=tkinter.Label(page,text='INVALID ADMISSION NO.',font=("Arial",10))
            output.place(x=220,y=150)
        f.close()
    page=tkinter.Tk()
    page.geometry('600x300')
    page.title("admin")
    page.configure(bg='mediumorchid1')
    heading=tkinter.Label(page,text='WELCOME',bg='white',font=("Time New Roman",25,'bold'),fg='black').pack()
    u=tkinter.Label(page,text='Enter admission no.',font=("Times New Roman",15),fg='black',bg="white")
    u.place(x=100,y=75)
    e=tkinter.Entry(page,width=20,font=("Arial",15))
    e.place(x=325,y=75)
    sub=tkinter.Button(page,text='DELETE',font=("Arial",15,'bold'),fg='black',bg="white",command=admin)
    sub.place(x=250,y=200)


    

def u_page2():
    
    

    def admin():
        def display():
            def b():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Roll no']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                        pass
                
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def c():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Class']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def d():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Maths']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def e():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['English']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def f():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Physics']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def g():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Chemistry']=e2.get()
                        pickle.dump(d,f1)

                except EOFError:  
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def h():
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Computer Science']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            def a():
                
                try:
               
                    while True:
                
                
                        d=pickle.load(f)
                        if d['Admission No.']==x:
                            d['Contact No.']=e2.get()
                        pickle.dump(d,f1)
                            
                except EOFError:
                    pass
               
                f1.close()
                f.close()
                os.rename('database.dat','old.dat')
                os.remove('old.dat')
                os.rename('another.dat','database.dat')
                p_page.destroy()
            x=e1.get()
            f=open('database.dat','rb')
            f1=open('another.dat','wb')
            p_page=tkinter.Tk()
            p_page.geometry('700x200')
            p_page.title("update")
            p_page.title("UPDATE")
            p_page.configure(bg='red')
            if i.get()==1:
                l1=tkinter.Label(p_page, text="Enter New Contact no.:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=a,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            
            
            elif i.get()==2:
                l1=tkinter.Label(p_page, text="Enter New Roll no.:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=b,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            elif i.get()==3:
                l1=tkinter.Label(p_page, text="Enter New Class:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=c,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            elif i.get()==4:
                l1=tkinter.Label(p_page, text="Enter New marks:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)
                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=d,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            elif i.get()==5:
                l1=tkinter.Label(p_page, text="Enter New marks:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=e,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            elif i.get()==6:
                l1=tkinter.Label(p_page, text="Enter New marks:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)
                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=f,bg="White",fg="Black")
                bl.place(x=300,y=150)
                

               
            elif i.get()==7:
                l1=tkinter.Label(p_page, text="Enter New marks:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=g,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
            elif i.get()==8:
                l1=tkinter.Label(p_page, text="Enter New marks:",font=(15),fg="black",bg="white")
                l1.place(x=100,y=50)

                e2=tkinter.Entry(p_page,width=30, font=(15),bg="white")
                e2.place(x=300,y=50)
                bl=tkinter.Button(p_page,text="Submit",font=("Aharoni",15),command=h,bg="White",fg="Black")
                bl.place(x=300,y=150)
                
              
        try:
            f=open('database.dat','rb')
            while True:
                p=pickle.load(f)
                if p['Admission No.']==e1.get():
                    f.close()
                    display()
                    break
                     
              
                
                    
            
        except EOFError:
            output=tkinter.Label(win,text='INVALID ADMISSION NO.',font=("Arial",10))
            output.place(x=260,y=550)
        f.close()        



    win=tkinter.Tk()
    win.geometry("700x700")
    win.title("admin")
    frame1=tkinter.Frame(win,width=700,height=700,bg="mediumvioletred")
    frame1.place(x=0,y=0)

    x1=tkinter.Label(frame1, text="UPDATION",font=("Aharoni",25,"bold"),fg="black",bg="white")
    x1.place(x=250,y=0)

    l1=tkinter.Label(frame1, text="Enter Admission no:",font=(15),fg="black",bg="white")
    l1.place(x=100,y=100)

    e1=tkinter.Entry(frame1,width=30, font=(15),bg="white")
    e1.place(x=350,y=100) 

    l2=tkinter.Label(frame1,text="Select option for update:",font=(15),fg="black",bg="white")
    l2.place(x=100,y=150)

    i=tkinter.IntVar()

    rad1=tkinter.Radiobutton(frame1,text="Contact No.",font=(15),value=1,variable=i,fg="black",bg="white")
    rad2=tkinter.Radiobutton(frame1,text="Roll no",value=2, font=(15),variable=i,fg="black",bg="white")
    rad3=tkinter.Radiobutton(frame1,text="Class",font=(15),value=3,variable=i,fg="black",bg="white")
    rad4=tkinter.Radiobutton(frame1,text="Marks in MATH",font=(15),value=4,variable=i,fg="black",bg="white")
    rad5=tkinter.Radiobutton(frame1,text="Marks in ENGLISH",font=(15),value=5,variable=i,fg="black",bg="white")
    rad6=tkinter.Radiobutton(frame1,text="Marks in PHYSICS",font=(15),value=6,variable=i,fg="black",bg="white")
    rad7=tkinter.Radiobutton(frame1,text="Marks in CHEMISTRY",font=(15),value=7,variable=i,fg="black",bg="white")
    rad8=tkinter.Radiobutton(frame1,text="Marks in COMPUTER",font=(15),value=8,variable=i,fg="black",bg="white")
    rad1.place(x=350,y=150)
    rad2.place(x=350,y=200)
    rad3.place(x=350,y=250)
    rad4.place(x=350,y=300)
    rad5.place(x=350,y=350)
    rad6.place(x=350,y=400)
    rad7.place(x=350,y=450)
    rad8.place(x=350,y=500)

    

    
    bl=tkinter.Button(frame1,text="Submit",font=("Aharoni",15),command=admin,bg="White",fg="Black")
    bl.place(x=300,y=600)


def p_page():
    def admin():
        def display():
            
            try:
                f=open('database.dat','rb')
                while True:
                    p=pickle.load(f)
                    if p['Admission No.']==e.get():
                        a=p['Admission No.']
                        
                        b=p['Name']
                        c=p["Contact No."]
                        
                        d=p["Roll No"]
                        
                        e1=p["Class"]
                        
                        f=p["Maths"]
                        g=p["English"]
                        
                        h=p["Physics"]
                        i=p["Chemistry"]
                        j=p["Computer Science"]
                        
                        p_page=tkinter.Tk()
                        p_page.geometry('700x700')
                        p_page.title("Student Record")
                        p_page.configure(bg='lavender')
                        frame2=tkinter.Frame(p_page,width=575,height=150,bg="blue2")
                        frame2.place(x=50,y=75)
                        frame3=tkinter.Frame(p_page,width=575,height=275,bg="salmon")
                        frame3.place(x=50,y=325)

                        heading=tkinter.Label(p_page,text="REPORT CARD",font=("Aharoni",20),bg='gold')
                        heading.place(x=250,y=1)
                        
                        k1=tkinter.Label(frame2,text='ADMN NO:',font=("Times New Roman",15),bg="white")
                        k1.place(x=25,y=10)
                        
                        k2=tkinter.Label(frame2,text=a,font=("Times New Roman",15),bg='white')
                        k2.place(x=175,y=10)

                        n1=tkinter.Label(frame2,text='ROLL NO:',font=("Times New Roman",15),bg='white')
                        n1.place(x=360,y=10)
                        
                        n2=tkinter.Label(frame2,text=d,font=("Times New Roman",15),bg='white')
                        n2.place(x=475,y=10)
                        
                        l1=tkinter.Label(frame2,text='CLASS:',font=("Times New Roman",15),bg='white')
                        l1.place(x=360,y=60)
                        
                        l2=tkinter.Label(frame2,text=e1,font=("Times New Roman",15),bg='white')
                        l2.place(x=475,y=60)
                        
                        m1=tkinter.Label(frame2,text='CONTACT NO:',font=("Times New Roman",15),bg='white')
                        m1.place(x=25,y=110)
                        
                        m2=tkinter.Label(frame2,text=c,font=("Times New Roman",15),bg='white')
                        m2.place(x=175,y=110)
                        
                        o1=tkinter.Label(frame2,text='NAME:',font=("Times New Roman",15),bg='white')
                        o1.place(x=25,y=60)
                        
                        o2=tkinter.Label(frame2,text=b,font=("Times New Roman",15),bg='white')
                        o2.place(x=175,y=60)

                        heading2=tkinter.Label(p_page,text="MARKS OBTAINED BY STUDENT",font=("Aharoni",17),bg="gold")
                        heading2.place(x=175,y=280)
                        
                        p1=tkinter.Label(p_page,text='MATHS',font=("Times New Roman",15),bg='white')
                        p1.place(x=200,y=350)  
                        p2=tkinter.Label(p_page,text=f,font=("Times New Roman",15),bg='white')
                        p2.place(x=450,y=350)
                        q1=tkinter.Label(p_page,text='ENGLISH',font=("Times New Roman",15),bg='white')
                        q1.place(x=200,y=400)  
                        q2=tkinter.Label(p_page,text=g,font=("Times New Roman",15),bg='white')
                        q2.place(x=450,y=400)
                        
                        r1=tkinter.Label(p_page,text='PHYSICS',font=("Times New Roman",15),bg='white')
                        r1.place(x=200,y=450)  
                        r2=tkinter.Label(p_page,text=h,font=("Times New Roman",15),bg='white')
                        r2.place(x=450,y=450)
                        s1=tkinter.Label(p_page,text='CHEMISTRY',font=("Times New Roman",15),bg='white')
                        s1.place(x=200,y=500)  
                        s2=tkinter.Label(p_page,text=i,font=("Times New Roman",15),bg='white')
                        s2.place(x=450,y=500)
                        t1=tkinter.Label(p_page,text='COMPUTER SCIENCE',font=("Times New Roman",15),bg='white')
                        t1.place(x=200,y=550)  
                        t2=tkinter.Label(p_page,text=j,font=("Times New Roman",15),bg='white')
                        t2.place(x=450,y=550)
                        for i in [f,g,h,i,j]:
                            if int(i)<35:
                                v1=tkinter.Label(p_page,text='COMMENTS:',font=("Aharoni",15),bg='gold')
                                v1.place(x=200,y=650)
                                v2=tkinter.Label(p_page,text='FAIL',font=("Times New Roman",15),bg='orangered2')
                                v2.place(x=400,y=650)
                                break
                        else:
                            v1=tkinter.Label(p_page,text='COMMENTS:',font=("Aharoni",15),bg='gold')
                            v1.place(x=200,y=650)
                            v2=tkinter.Label(p_page,text='PASS',font=("Times New Roman",15),bg='springgreen')
                            v2.place(x=400,y=650)    
                        page.destroy()

                            
                   
            
            except EOFError:
                pass
            f.close()
        try:
            f=open('database.dat','rb')
            while True:
                p=pickle.load(f)
                if p['Admission No.']==e.get():
                    f.close()
                    display()
                    
                    break
                     
                
                
                    
            
        except EOFError:
            output=tkinter.Label(page,text='INVALID ADMISSION NO.',font=("Arial",10))
            output.place(x=225,y=150)
        f.close()    
    page=tkinter.Tk()
    page.geometry('600x300')
    page.title("admin")
    page.configure(bg='orangered2')
    heading=tkinter.Label(page,text='WELCOME',bg='white',font=("Time New Roman",25,'bold'),fg='black').pack()
    u=tkinter.Label(page,text='Enter admission no.',font=("Times New Roman",15),fg='black',bg="white")
    u.place(x=100,y=75)
    e=tkinter.Entry(page,width=20,font=("Arial",15))
    e.place(x=325,y=75)
    sub=tkinter.Button(page,text='SUBMIT',font=("Arial",15,'bold'),fg='black',bg="white",command=admin)
    sub.place(x=250,y=200)
    
        
        

def password():
    if e.get()=='sp' and e2.get()=='abc':
        mwindow=tkinter.Tk()
        mwindow.geometry('600x500')
        mwindow.title("PORTAL")
        mwindow.configure(bg='blue')
        l=tkinter.Label(mwindow,text='STUDENT REPORT PORTAL(PCM-CS)',fg='white',font=("Aharoni",20,'bold','underline'),bg='blue').pack()
        irec=tkinter.Button(mwindow,text='Enter Record',command=i_write,font=("Times New Roman",15),fg='black',bg="white")
        irec.place(x=240,y=50)
        urec=tkinter.Button(mwindow,text='Update previous record',command=u_page2,font=("Times New Roman",15),fg='black',bg="white")
        urec.place(x=201,y=110)
        prec=tkinter.Button(mwindow,text='Print Record',command=p_page,font=("Times New Roman",15),fg='black',bg="white")
        prec.place(x=244,y=170)
        drec=tkinter.Button(mwindow,text="Delete Record",command=d_page,font=("Times New Roman",15),fg="black",bg="white")
        drec.place(x=239,y=230)
        ep=tkinter.Button(mwindow,text='Exit Portal',font=("Times New Roman",15),fg='black',bg="white",command=mwindow.destroy)
        ep.place(x=250,y=290)
        pwindow.destroy()
    else:
        output=tkinter.Label(pwindow,text='LOGIN UNSUCCESSFUL',font=("Arial",10))
        output.place(x=210,y=175)
        


pwindow=tkinter.Tk()
pwindow.title("login")
pwindow.geometry('600x300')
pwindow.configure(bg='springgreen')
heading=tkinter.Label(pwindow,text='WELCOME',fg='white',font=("Time New Roman",25,'bold'),bg='red').pack()
u=tkinter.Label(pwindow,text='Enter username',font=("Times New Roman",15),bg='red',fg="white")
u.place(x=100,y=75)
e=tkinter.Entry(pwindow,width=20,font=("Arial",15))
e.place(x=275,y=75)
p=tkinter.Label(pwindow,text='Enter password',font=("Times New Roman",15),bg='red',fg="white")
p.place(x=100,y=135)
e2=tkinter.Entry(pwindow,width=20,font=("Arial",15),show='*')
e2.place(x=275,y=135)
sub=tkinter.Button(pwindow,text='LOGIN',font=("Arial",15,'bold'),bg='Red',fg="white",command=password)
sub.place(x=250,y=240)
