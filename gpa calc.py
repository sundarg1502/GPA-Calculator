from tkinter import *

root=Tk()
root.title("GPA calculator")
#message window

m=Message(root,text="Grades_and_points Grade_O_=10 Grade_A+_=9 Grade_A_=8 Grade_b+_=7 Grade_b_=6 Grade_c_=5")
m.grid(row=0,column=0)

#creating lables

#title lable
subject_title=Label(root,text="subjects",fg="blue")
subject_title.grid(row=4,column=0)

subject_grade=Label(root,text="grade",fg="blue")
subject_grade.grid(row=4,column=1)

grade_got=Label(root,text="credit",fg="blue")
grade_got.grid(row=4,column=2)

#sybject lable
t1=Label(root,text="subject 1")
t1.grid(row=5,column=0)

t2=Label(root,text="subject 2")
t2.grid(row=6,column=0)

t3=Label(root,text="subject 3")
t3.grid(row=7,column=0)

t4=Label(root,text="subject 4")
t4.grid(row=8,column=0)

t5=Label(root,text="subject 5")
t5.grid(row=9,column=0)

t6=Label(root,text="subject 6")
t6.grid(row=10,column=0)
 
t7=Label(root,text="subject 7")
t7.grid(row=11,column=0)

t8=Label(root,text="subject 8")
t8.grid(row=12,column=0)

t9=Label(root,text="subject 9")
t9.grid(row=13,column=0)

t10=Label(root,text="subject 10")
t10.grid(row=14,column=0)

#creating entries

#grade entry
e1=Entry(root)
e1.grid(row=5,column=1)

e2=Entry(root)
e2.grid(row=6,column=1)

e3=Entry(root)
e3.grid(row=7,column=1)

e4=Entry(root)
e4.grid(row=8,column=1)

e5=Entry(root)
e5.grid(row=9,column=1)

e6=Entry(root)
e6.grid(row=10,column=1)

e7=Entry(root)
e7.grid(row=11,column=1)

e8=Entry(root)
e8.grid(row=12,column=1)

e9=Entry(root)
e9.grid(row=13,column=1)

e10=Entry(root)
e10.grid(row=14,column=1)

#credit entry

got_1=Entry(root)
got_1.grid(row=5,column=2,)

got_2=Entry(root)
got_2.grid(row=6,column=2)

got_3=Entry(root)
got_3.grid(row=7,column=2)

got_4=Entry(root)
got_4.grid(row=8,column=2)

got_5=Entry(root)
got_5.grid(row=9,column=2)

got_6=Entry(root)
got_6.grid(row=10,column=2)

got_7=Entry(root)
got_7.grid(row=11,column=2)

got_8=Entry(root)
got_8.grid(row=12,column=2)

got_9=Entry(root)
got_9.grid(row=13,column=2)

got_10=Entry(root)
got_10.grid(row=14,column=2)
#definig function for gatting  entry data

def get_entry_grade():
    grade_1=int(e1.get())
    grade_2=int(e2.get())
    grade_3=int(e3.get())
    grade_4=int(e4.get())
    grade_5=int(e5.get())
    grade_6=int(e6.get())
    grade_7=int(e7.get())
    grade_8=int(e8.get())
    grade_9=int(e9.get())
    grade_10=int(e10.get())
    credit_1=int(got_1.get())
    credit_2=int(got_2.get())
    credit_3=int(got_3.get())
    credit_4=int(got_4.get())
    credit_5=int(got_5.get())
    credit_6=int(got_6.get())
    credit_7=int(got_7.get())
    credit_8=int(got_8.get())
    credit_9=int(got_9.get())
    credit_10=int(got_10.get())
    grade_list=[grade_1,grade_2,grade_3,grade_4,grade_5,grade_6,grade_7,grade_8,grade_9,grade_10]
    credit_list=[credit_1,credit_2,credit_3,credit_4,credit_5,credit_6,credit_7,credit_8,credit_9,credit_10]
    credit_sum=0
    for i in credit_list:
        credit_sum+=i
    grade_x_credit=0
    overall=0
    for i in range(9):
        grade_x_credit=grade_list[i]*credit_list[i]
        overall+=grade_x_credit
        grade_x_credit=0
    return overall/credit_sum
    
    

#defining a function for button

def calculator():
    result=get_entry_grade()
    final_result=Label(root,text="Calculated GPA is   " + str(result))
    final_result.grid()
    
#creating button

button=Button(root,text="calculate",command=calculator)
button.grid(row=16,column=1)

root.mainloop()
