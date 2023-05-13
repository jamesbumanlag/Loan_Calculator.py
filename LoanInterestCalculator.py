import tkinter as tk
import tkinter.font as font
from tkinter import *

#click the CLEAR Button
def clearButton(root):    
    for widget in root.winfo_children():
        if not isinstance(widget,tk.Entry):
            clearButton(widget)
        elif isinstance(widget,tk.Entry):
            widget.delete(0, tk.END)
    clear_label()

#clear result label         
def clear_label():
    lbl_TotalPaymentVar.config(text='')
    lbl_MonthlyPaymentVar.config(text='')
    lbl_InterestVar.config(text='')
    
# show invalid input
def invalid_input():
    lbl_TotalPaymentVar.config(text='Invalid Input', fg='red')
    lbl_MonthlyPaymentVar.config(text='')
    lbl_InterestVar.config(text='')
    
#click the COMPUTE Button

def computeButton():
    
    if entYearsPayVar.get(): 

        if entLoanVar.get():

            #allow user to input float number in loan amount, interest and years entry
            try:
                float(entLoanVar.get())
                float(entInterestVar.get())
                float(entYearsPayVar.get())
                                             
            except ValueError:
                invalid_input()
           
        else:
            invalid_input()

    else:
        invalid_input()
    # assign variable from user input   
    loanVar = float(entLoanVar.get())
    years = float(entYearsPayVar.get())
    interest = float(entInterestVar.get())

    # Calculation by calling function
    total_interest =computeTotalInterest(loanVar,interest,years)
    total_payment = computeTotalPayment(loanVar, total_interest)
    monthlyPay=computeMonthlyPayment(total_payment, years)     
        
    #Display values
    lbl_TotalPaymentVar.config(text=f'{total_payment:,.2f}',fg='black')
    lbl_MonthlyPaymentVar.config(text=f'{monthlyPay:,.2f}')
    lbl_InterestVar.config(text=f'{total_interest:,.2f}')
#Compute Monthly Payment
def computeMonthlyPayment(totalPayment,years):
    monthlyPay = totalPayment / (years*12)
    return(monthlyPay)

#Compute Total Payment
def computeTotalPayment(loanVar,totalInterest):
    totalPayment = loanVar + totalInterest  
    return(totalPayment)  

#Compute Total Interest
def computeTotalInterest(loanVar, interest, years):
    totalInterest = (loanVar * interest * years) / 100
    return(totalInterest)

#Initialize the main window    
root = tk.Tk()
root.title("Loan Calculator")
root.resizable(False,False)
root.geometry("284x497+500+100")

#icon beside the title
image_icon = tk.PhotoImage(file="C:\images\profit.png")
root.iconphoto(False,image_icon)

#top image (Loan Calculator)
logo_image = tk.PhotoImage(file="C:\images\imagetop1.png")
Label(root,image=logo_image).place(x=0, y=-2)

#loan amount
Label(root, text="Loan Amount").place(x=20, y=99)

#Interest Rate
Label(root, text="Annual Interest Rate").place(x=20, y=149)

#years to pay
Label(root,text="Years to Pay").place(x=20, y=199)

#Monthly Payment
Label(root, text="Monthly Payment ").place(x=20, y=328)

#Total Payment
Label(root, text="Total Payment ").place(x=20, y=368)

#Total Interest
Label(root, text="Total Interest").place(x=20, y=409)

#footer
Label(root, text="Created by: SoftDev TM", bg='light blue').place(x=71, y=457)

#create clear button
Button(root, text="CLEAR", bg='#676767', fg='white', command=lambda:clearButton(root)).place(x=30, y=250, width=100, height=30)

#create compute button
Button(root, text="COMPUTE", bg='#676767', fg='white',command=computeButton).place(x=150, y=250, width=100, height=30)

#Line Separator
line_between = tk.PhotoImage(file="C:\images\Group3.png" )
Label(root, image=line_between).place(x=0, y=300, width=284)

#taking inputs for loan
#loanVar =  StringVar()
entLoanVar = Entry(root, bd=2, font="bold", justify=LEFT)
#taking inputs for interest rate
#annualInterestVar = StringVar()
entInterestVar = Entry(root, bd=2, font="bold", justify=LEFT)
#taking inputs for Years to pay
#yearsPayVar = StringVar()
entYearsPayVar = Entry(root, bd=2, font="bold", justify=LEFT)
#output for Monthly payment
# monthlyPaymentVar = StringVar()
lbl_MonthlyPaymentVar = Label(root, font="bold", justify=LEFT)

#output for total Payment
# totalPaymentVar = StringVar()
Label(root, font="bold",  justify=LEFT).place(x=141, y=362)
lbl_TotalPaymentVar = Label(root, text='',font="bold", justify=LEFT)

#output for total interest
# totalInterestVar = StringVar()
lbl_InterestVar =Label(root, font="bold", justify=LEFT)

# show entry variables to the screen
entLoanVar.place(x=140, y=90, width=126, height=30)
entInterestVar.place(x=140, y=140, width=81, height=30)
entYearsPayVar.place(x=140, y=189, width=81, height=30)

# show result labels to the screen
lbl_TotalPaymentVar.place(x=141, y=362)
lbl_MonthlyPaymentVar.place(x=141,y=322)
lbl_InterestVar.place(x=141, y=402)


root.mainloop()


    


