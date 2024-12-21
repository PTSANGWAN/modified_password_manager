from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    Letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    Numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    Symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', ',', '/', '?', '~']

    p=random.randint(5,8)
    s=random.randint(2,4)
    n=random.randint(2,4)

    list1=[random.choice(Letters) for _ in range(p)]
    list2=[random.choice(Numbers) for _ in range(s)]
    list3=[random.choice(Symbols) for _ in range(n)]

    list_final=list1+list2+list3

    random.shuffle(list_final)

    pwd_generated="".join(list_final)
    pwd_entry.insert(0,pwd_generated)
    pyperclip.copy(pwd_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_pwd():
    
        try:
            with open("data.json","r") as f:
                data_dict=json.load(f)
            if web_entry.get() in data_dict:
                messagebox.showinfo(title="Details", message=f"email: {data_dict[web_entry.get()]["email"]} \npassword: {data_dict[web_entry.get()]["password"]}")
            else:
                messagebox.showinfo(title="Details", message="Website password not stored.")

        except FileNotFoundError:
            messagebox.showinfo(title="Details", message="Website password not stored.")

def add_action():
    web_entered=web_entry.get()
    cred_entered=cred_entry.get() 
    pwd_entered=pwd_entry.get()
    json_dict={web_entered:{"email": cred_entered, "password": pwd_entered}}
    if len(web_entered)==0 or len(pwd_entered)==0 or len(cred_entered)==0:
        messagebox.showwarning(title="Ooops!!", message="Do not leave any fields empty.")

    else:
        # confirmation=messagebox.askyesno(title="Confirmation Box", message=f"These are the details entered: \nWebsite: {web_entered} \nUsernae/email: {cred_entered} \nPassword: {pwd_entered} \nDo you want to save it? ")
        # if confirmation:
        try:
            with open("data.json","r") as f:
                d=json.load(f)
                d.update(json_dict)
            with open("data.json","w") as f:
                json.dump(d, f, indent=4)
               
        except FileNotFoundError:
            with open("data.json","w") as f:
                json.dump(json_dict,f,indent=4)

        finally:
            messagebox.showinfo(title="Hurray", message="Your details are saved in password storage document. You may check that out.")
            web_entry.delete(0,END)
            pwd_entry.delete(0,END)


      
        

        

# ---------------------------- UI SETUP ------------------------------- #

# Creating our app Window
pwd_window=Tk()
pwd_window.title("PASSWORD MANAGER")
pwd_window.config(padx=50,pady=50)

# Canvas setting
my_can=Canvas(width=200, height=200)
img=PhotoImage(file="tkinter\password_manager\logo.png")
my_can.create_image(100,100,image=img)
my_can.grid(row=0, column=1)

#Labels
web=Label(text="Website:")
web.grid(row=1, column=0)

cred=Label(text="Email/ Username:")
cred.grid(row=2, column=0)

pwd=Label(text="Password:")
pwd.grid(row=3, column=0)

# Entries

web_entry= Entry(width=20)
web_entry.focus()
web_entry.grid(row=1,column=1)

cred_entry= Entry(width=40)
cred_entry.insert(0,"sangwanpriti22@gmail.com")
cred_entry.grid(row=2,column=1, columnspan=2)

pwd_entry= Entry()
pwd_entry.grid(row=3,column=1)

# Buttons
gen_pwd = Button(text="Generate password", width=16, command=generate_password)
gen_pwd.grid(row=3, column=2)

add_pwd = Button(text="Add", width=34, command=add_action)
add_pwd.grid(row=4, column=1, columnspan=2)

search_web=Button(text="Search", width=16, command=search_pwd)
search_web.grid(row=1, column=2)




pwd_window.mainloop()