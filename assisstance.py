from tkinter import *

op = ""
def btn_click(num):
    global op
    op = op+str(num)
    txt_inp.set(op)

def AllClear():
    global op
    op=""
    txt_inp.set(op)

def equl():
    global op
    try:
        sumup = str(eval(op))
    except Exception as e:
        print("Exception",e)
        sumup = 0
        op = ""
        AllCleal()
    txt_inp.set(sumup)










root= Tk()
root.geometry('360x500')
root.config(bg='red')
root.title('Aalov calci')

txt_inp = StringVar()

e1=Entry(root,font=('arial',20,'bold'),textvariable=txt_inp , bd=30,bg= 'yellow',
           fg='black' , insertwidth = 8, justify ='right')
e1.grid(columnspan=4)
#========================FIRST ROW ========================
btn7 = Button(root,text= '7',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(7))
btn7.grid(row = 2,column=0)

btn8 = Button(root,text= '8',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(8))
btn8.grid(row = 2,column=1)

btn9 = Button(root,text= '9',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(9))
btn9.grid(row = 2,column=2)

btn_p = Button(root,text= '+',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click('+'))
btn_p.grid(row = 2,column=3)

#========================================SECOND ROW============================
btn4 = Button(root,text= '4',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(4))
btn4.grid(row = 3,column=0)

btn5 = Button(root,text= '5',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(5))
btn5.grid(row = 3,column=1)

btn6 = Button(root,text= '6',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(6))
btn6.grid(row = 3,column=2)

btn_m = Button(root,text= '-',font=('aral',20,'bold'),padx = 18,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click('-'))
btn_m.grid(row = 3,column=3)
#==========================================THIRD ROW============================
btn1 = Button(root,text= '1',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(1))
btn1.grid(row = 4,column=0)

btn2 = Button(root,text= '2',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(2))
btn2.grid(row = 4,column=1)

btn3 = Button(root,text= '3',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(3))
btn3.grid(row = 4,column=2)

btn_mu = Button(root,text= '*',font=('aral',20,'bold'),padx = 18,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click('*'))
btn_mu.grid(row = 4,column=3)

#==========================================FOURTH ROW============================
btn0 = Button(root,text= '0',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click(0))
btn0.grid(row = 5,column=0)

btnAC = Button(root,text= 'AC',font=('aral',20,'bold'),padx = 4,pady = 15,bd=6,bg='blue',
             fg='black',command=AllClear)
btnAC.grid(row = 5,column=1)

btneq = Button(root,text= '=',font=('aral',20,'bold'),padx = 15,pady = 15,bd=6,bg='blue',
             fg='black',command= equl)
btneq.grid(row = 5,column=2)

btn_div = Button(root,text= '/',font=('aral',20,'bold'),padx = 18,pady = 15,bd=6,bg='blue',
             fg='black',command=lambda:btn_click('/'))
btn_div.grid(row = 5,column=3)

root.mainloop()