#import every think from tkinter
from tkinter import *
#create window object
root=Tk()
root.title("LoginForm")
root.geometry("600x300")
root.configure(bg="#003e53")
title=Label(root, text="LoginForm", fg="white", bg="#003e53", font=("bold", 14))
title.place(x=288, y=18 )
uname=Label(root,text="User Name", fg="white", bg="#003e53", font=("bold", 14))
uname.place(x=120, y=58)
password=Label(root,text="Password", fg="white", bg="#003e53", font=("bold", 14))
password.place(x=120, y=88)
uname_t=Entry()
uname_t.place(x=238, y=65)
pass_t=Entry()
pass_t.place(x=238, y=95)
submit=Button(root, text="Submit")
submit.place(x=238, y=129)

root.mainloop()



