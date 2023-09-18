from ast import keyword
from cgitb import text
from errno import ENETRESET
from getpass import getpass
import imp
from os import system
import os
import sys
from tkinter import *
from tkinter.font import BOLD, ITALIC
import abc as b

# stop screen after registration 
# ok button after click it will stop 
def delete():
    screen2.destroy()

# stop login  
# after login  select program your want!!!
def main():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("SELECT !!")
    screen7.geometry("400x400")
    screen7.resizable(0, 0)
    screen7.configure(background="#1C1C1C")
    Label(screen7 , text= "", background="#1C1C1C" ).pack()
    Label(screen7 , text="S E L E C T!!", width= "400", height= "2" , bg ="#008B8B" , font = ("Comic Sans MS", 18 , BOLD , ITALIC) ).pack()
    screen7.resizable(0, 0)
    screen7.title("S E L E C T")
    Label(screen7,text = "" , background="#1C1C1C").pack()
    Label(screen7,text = "" , background="#1C1C1C").pack()
    Button(screen7, text= " CALCULATOR ", width="20" , height="2", command= calculator , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) ).pack()
    Label(screen7,text = "", background="#1C1C1C").pack()
    Button(screen7,text = "PASS GENERATE ", width="20" , height="2", command= pass_genrate ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8)).pack()
    Label(screen7,text = "", background="#1C1C1C").pack()
    Button(screen7,text = "UNIT CONVERTOR ", width="20" , height="2", command= unit ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8)).pack()


#Calculator  
def calculator():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("CALCULATOR !!")
    screen8.configure(background="#1C1C1C")
    screen7.resizable(0, 0)
    
    e = Entry(screen8, width= 35 ,borderwidth= 2)
    e.grid(row=0 , column= 0 , columnspan= 3 , padx= 10 , pady=10)
    def button_click(number):
        current = e.get()
        e.delete(0 , END)
        e.insert(0,  str(current) + str(number))

    def button_clear():
        e.delete(0, END) 

    def button_divide():
        d1_number = e.get()
        global b2
        b2 = int(d1_number)
        e.delete(0, END)

    def button_subtract():
        s1_number = e.get()
        global a1
        a1 = int(s1_number)
        e.delete(0, END)

    def button_add():
        first_number = e.get()
        global f_num
        f_num = int(first_number)
        e.delete(0, END)
    def button_equal():
        second_number= e.get()
        e.delete(0,END) 
        e.insert(0, b2 / int(second_number))

    button1 = Button(screen8, text= 1 ,padx= 40, pady=20 , command= lambda :button_click(1) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button2 = Button(screen8, text= 2 ,padx= 40, pady=20 , command= lambda :button_click(2) ,bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button3 = Button(screen8, text= 3 ,padx= 40, pady=20 , command= lambda :button_click(3) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button4 = Button(screen8, text= 4 ,padx= 40, pady=20 , command= lambda :button_click(4) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button5 = Button(screen8, text= 5 ,padx= 40, pady=20 , command= lambda :button_click(5) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button6 = Button(screen8, text= 6 ,padx= 40, pady=20 , command= lambda :button_click(6) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button7 = Button(screen8, text= 7 ,padx= 40, pady=20 , command= lambda :button_click(7) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button8 = Button(screen8, text= 8 ,padx= 40, pady=20 , command= lambda :button_click(8) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button9 = Button(screen8, text= 9 ,padx= 40, pady=20 , command= lambda :button_click(9) , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    button0 = Button(screen8, text= 0 ,padx= 40, pady=20 , command= lambda :button_click(0), bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    add     = Button(screen8, text= "+" ,padx= 40, pady=20 , command= button_add , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    subtract = Button(screen8, text= "-" ,padx= 40, pady=20 , command= button_subtract , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    divide = Button(screen8, text= "/" ,padx= 40, pady=20 , command= button_divide , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    equal   = Button(screen8, text= "=" ,padx= 40, pady=20 , command= button_equal , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    clear   = Button(screen8, text= "C" ,padx= 40, pady=20 , command= button_clear , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) )
    
    # display button on screen 
    button1.grid(row = 3, column= 0)
    button2.grid(row = 3, column= 1)
    button3.grid(row = 3, column= 2)

    button4.grid(row= 2 , column= 0)
    button5.grid(row= 2 , column= 1)
    button6.grid(row= 2 , column= 2)

    button7.grid(row= 1 , column= 0)
    button8.grid(row= 1 , column= 1)
    button9.grid(row= 1 , column= 2)

    button0.grid(row= 4 , column= 0)
    divide.grid(row=4 , column=1)
    
    
    add.grid(row= 5 , column= 0 )
    subtract.grid(row= 5 , column= 1 )

    equal.grid(row= 7, column= 1 ) 
    clear.grid(row= 7 , column= 2 )

#PAss Generator 
def pass_genrate():
    screen7.destroy()

#Unit convertor 
def unit():
    main()

    
# stop after password failure 
def delete2():
    screen5.destroy()  
# user failure error 
def delete3():
    screen6.destroy()  
# login success 
def login_sucess():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success!!")
    screen4.geometry("250x100")
    screen4.resizable(0, 0)
    screen4.configure(background="#1C1C1C")
    Label(screen4 , text= "", background="#1C1C1C" ).pack()
    Button(screen4 , text="OK", width= "10" , height= "1" , command= main ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

# password failure screen
def  password_error():
        global screen5
        screen5 = Toplevel(screen)
        screen5.title("PASSWORD ERROR!!")
        screen5.geometry("250x100")
        screen5.resizable(0, 0)
        screen5.configure(background="#1C1C1C")
        Label(screen5 , text="PASSWORD ERROR!!",  fg= "#00C957" , font= ("Comic Sans MS", 11) ,  background="#1C1C1C").pack()
        Button(screen5 , text="OK", width= "10" , height= "1" , command= delete2 ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

# user failure error
def user_not_found():
        global screen6
        screen6 = Toplevel(screen)
        screen6.title("USER ERROR!!")
        screen6.geometry("250x100")
        screen6.configure(background="#1C1C1C")
        Label(screen6 , text="USER NOT FOUND!!",  fg= "#00C957" , font= ("Comic Sans MS", 11) ,  background="#1C1C1C").pack()
        Button(screen6 , text="OK", width= "10" , height= "1" , command= delete3 ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

# registration backend
def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info , "w")
    file.write(username_info + "\n" )
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry. delete(0, END)


    global screen2
    screen2 = Toplevel(screen)
    screen2.title("REGISTER")
    screen2.geometry("200x100")
    screen2.resizable(0, 0)
    screen2.configure(background="#1C1C1C")
    Label(screen2 ,text= "DONE!!!!" , fg= "#00C957" , font= ("Comic Sans MS", 11) ,  background="#1C1C1C").pack()
    Button(screen2 , text= "OK!!" , width= "10" , height= "1" , command= delete ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()
    

# registration 
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("REGISTER")
    screen1.resizable(0, 0)
    screen1.geometry("300x300")
    screen1.configure(background="#1C1C1C")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1 , text= "ENTER YOUR DETAIL BELOW" , fg = "#000000" , background="#008B8B" ,  width= "400", height= "2" , font = ("Comic Sans MS", 10 ,BOLD) ).pack()

    Label(screen1 , text= "" , background="#1C1C1C" ).pack()

    Label(screen1 , text= "USERNAME  " , fg = "#008B8B" , background="#1C1C1C" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

    Label(screen1 , text= "" , background="#1C1C1C").pack()

    username_entry = Entry(screen1 , textvariable= username)
    username_entry.pack()

    Label(screen1 , text= "" , background="#1C1C1C" ).pack()

    Label(screen1 , text= "PASSWORD  " ,  fg = "#008B8B" , background="#1C1C1C" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

    Label(screen1 , text= "" , background="#1C1C1C").pack()

    password_entry = Entry(screen1 , textvariable= password)
    password_entry.pack()
    
    Label(screen1 , text= "", background="#1C1C1C" ).pack()

    Button(screen1 , text= "Register" , width= "10" , height= "1" , command= register_user ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

#login verify 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_error()
    else:
        user_not_found()


#login page 
def login():
        global screen3
        screen3 = Toplevel(screen)
        screen3.title("LOGIN")
        screen3.geometry("300x300")
        screen3.resizable(0, 0)
        screen3.configure(background="#1C1C1C")
        

        Label(screen3 , text= "ENTER YOUR DETAIL FOR LOGIN", fg = "#000000" , background="#008B8B" ,  width= "400", height= "2" , font = ("Comic Sans MS", 10 ,BOLD)).pack()
        Label(screen3 , text= "" , background="#1C1C1C"  ).pack()

        global username_verify 
        global password_verify
        global username_entry1
        global password_entry1

        username_verify = StringVar()
        password_verify = StringVar()

        Label(screen3 , text= "USERNAME  " , fg = "#008B8B" , background="#1C1C1C" , font = ("Comic Sans MS", 10 ,BOLD) ).pack()
        username_entry1 = Entry(screen3, textvariable= username_verify)
        username_entry1.pack()
        Label(screen3 , text= "" ,  background="#1C1C1C" ,).pack()

        Label(screen3 , text= "PASSWORD  " ,  fg = "#008B8B" , background="#1C1C1C" , font = ("Comic Sans MS", 10 ,BOLD)).pack()
        password_entry1 = Entry(screen3, textvariable= password_verify)
        password_entry1.pack()
        Label(screen3 , text= "" ,  background="#1C1C1C" ,).pack()
        Button(screen3 , text= "LOGIN" , width= "10" , height= "1" , command= login_verify ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 10 ,BOLD)).pack()

# main screen 
def main_srceen():
    global screen
    screen = Tk()
    screen.configure(background="#1C1C1C")
    screen.geometry("300x300")
    screen.resizable(0, 0)
    screen.title("M A I N")
    Label(text = "L O G I N", width= "400", height= "2" , bg ="#008B8B" , font = ("Comic Sans MS", 13)).pack()
    Label(text = "" , background="#1C1C1C").pack()
    Button(text= "LOGIN", width="20" , height="2", command= login , bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8) ).pack()
    Label(text = "", background="#1C1C1C").pack()
    Button(text = "REGISTER", width="20" , height="2", command= register ,  bg= "#636363" , fg= "#00CDCD" , font = ("Comic Sans MS", 8)).pack()
    screen.mainloop()

main_srceen()