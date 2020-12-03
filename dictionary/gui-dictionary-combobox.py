import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfile, askopenfile
from PIL import ImageTk, Image
from tkinter import font
import sys
import re
import smtplib
import random
from gtts import gTTS 
import playsound
import os 
from PyDictionary import PyDictionary
from tkinter import ttk


#===============================(Dictionary Window)===========================
def meaning():
    global word
    global result
    word = e2.get()
    dictionary = PyDictionary()
    result = dictionary.meaning(word)
    tx.set(str(result))
    #print(type(result))
    #w3 = tk.Label(window, text= 'result is :' + str(result), wraplength=250 )
    #w3.pack(expand=True, side=BOTTOM)

    #print(result)
    #explain =  f'{input("DO YOU WANT TO GET SYNONYM?(Yes, No :)")}' 
    #print(explain)
    explain  = tk.messagebox.askyesno(message='DO YOU WANT TO SEE SYNONYM ?')
    if explain == True:
        synonym()
    else:
        tk.messagebox.showinfo(message='SEE YOU SOON')
        #print('see you soon :)')
    return word
    return result

def synonym():
    global results
    dictionary = PyDictionary()
    results = dictionary.synonym(word)
    
    w4 = tk.Label(master = new2, text= 'synonym is :' + str(results))
    w4.pack(fill= BOTH, expand=True)
    w4.config(text = results)
    #print(results)

def speak():
    tts = gTTS(text=str(result), lang='en', slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#meaning(word) 
#=============================================================================
def dictionary():
    global new2
    global e2
    global tx
    
    new2 = tk.Toplevel(window)
    new2.geometry('500x500')
    new2.title('Cambridge Dictionary')
    img = Image.open('4.jpg')
    img = ImageTk.PhotoImage(img)
    
    
    #myimage = ImageTk.PhotoImage(Image.open('4.jpg'))

    
    w0 = tk.Label(master = new2, text = 'Welcome', font = 14, image = img)
    w0.image = img
    w0.pack(fill= BOTH, expand=True)
    
    appHighlightFont = font.Font(family='Helvetica', size=18, weight='bold')
    
    w2 = tk.Label(master = new2, text='Enter The Vocablulary:', font=appHighlightFont)
    w2.pack(fill= BOTH, expand=True)
    
    e2 = tk.Entry(new2, width='10')
    e2.pack(fill= BOTH, expand=True)
    
    tx = tk.StringVar(master = new2)
    tx.set('')
    
    w3 = tk.Label(master = new2, textvariable = tx, wraplength=250 )
    w3.pack()
    
    b2 = tk.Button(master = new2, text='Click', command=meaning, font=appHighlightFont)
    b2.pack(fill= BOTH, expand=True, side=RIGHT)
    
    #myicon = PhotoImage(file = r'voceicon.png')
    #print(myicon)
    #iconresize = myicon.subsample(1, 1)
    
    b3 = tk.Button(master = new2, text='voice', command=speak, font = appHighlightFont)
    b3.pack(fill = BOTH, expand =True, side = RIGHT)


#==============================(Creat DataBase)===============================

sqliteConnection = sqlite3.connect('time.db')
cursor = sqliteConnection.cursor()
print("Connected to SQLite")

sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS new_developers(
                                       name TEXT NOT NULL,
                                       password integer NOT NULL,
                                       email TEXT,
                                       joiningDate timestamp,
                                       expiretime timestamp)"""


cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
sqliteConnection.close()
#=============================(Make Random Number)============================
r1 = random.randint(10,20 )
r2 = random.randint(20, 30)
r3 = random.randint(40, 55)
r = str(r1) + str(r2) + str(r3)
print(r)
#=========================(Creat DataBase)===================================
def add():
    global result_expiretime
    global result_jointime
    global acc_name
    global acc_email

    with sqlite3.connect('time.db') as db :
        cursor = db.cursor()
        insert = 'INSERT INTO new_developers(name, password, email, joiningDate, expiretime) VALUES (?,?,?,?,?)'
        if len(nusername.get()) == 0:
            tk.messagebox.showerror('', 'lost username field')
        elif len(npassword.get()) == 0:
            tk.messagebox.showerror('', 'lost password field')
        else:   
            cursor.execute(insert,[(nusername.get()), (npassword.get()), email.get(), datetime.now(), my_date])
            db.commit()
            tk.messagebox.showinfo('', 'creat account succesfuly')
        db.commit()
        
    cur = cursor.execute("SELECT joiningDate  FROM new_developers")
    rows_join = cur.fetchall()
    result_jointime = []
    for t in rows_join: 
            #print(t)
            for x in t: 
                result_jointime.append(x)
                
    cur1 = cursor.execute("SELECT expiretime  FROM new_developers")
    rows_expire = cur1.fetchall()
    result_expiretime = []
    for z in rows_expire:
            #print(z)
            for y in z:
                #print(y)
                result_expiretime.append(y)
    cur2 = cursor.execute("SELECT name  FROM new_developers")
    rows_name = cur2.fetchall()
    acc_name = []
    for q in rows_name:
            #print(z)
            for o in q:
                #print(y)
                acc_name.append(o)
    cur3 = cursor.execute("SELECT email  FROM new_developers")
    rows_email = cur3.fetchall()
    acc_email = []
    for b in rows_email:
            #print(z)
            for h in b:
                #print(y)
                acc_email.append(h)                
    
    print("Developer added successfully \n")
    expire()
    return result_expiretime
    return result_jointime

#==========================(Creat Gui Page)===================================
window = tk.Tk()
window.geometry('300x370')
window.title('LogIn')

#=================================(LogIn)=====================================

def login():
    with sqlite3.connect('time.db') as db:
        c = db.cursor()
        find = ('SELECT * FROM new_developers WHERE name = ? and password = ?')
        if len(username.get()) == 0:
            tk.messagebox.showerror('', 'Enter Username Please')
        elif len(password.get()) == 0:
            tk.messagebox.showerror('', 'Enter Password Please')
        else:
            c.execute(find, [(username.get()), (password.get())])
            log = c.fetchall()
            #print(log)
        if log:
            tk.messagebox.showinfo('', 'Username And Password Correct')
            #print('Your Username And Password Correct')
            expire()
            
        else:
            print('Not Valid')                

#=============================(Window Creat Account)==========================

def creataccount():
     from tkinter import ttk
     global new
     global nusername
     global npassword
     global email
     global accept
     #----------------------(Creat New Tab)-----------------------------------
     new = tk.Toplevel(window)
     new.title('creat account')
     #new.geometry('300x300')
     #-----------------------(Define Label And Bottom)------------------------
     nusernamelabel = tk.Label(master = new, text = 'Enter New Username : ', font = appHighlightFont)
     nusernamelabel.grid(row = 0, column =0, pady = 0, padx = 0)
     nusername = tk.Entry(new)
     nusername.grid(row = 0, column = 1,  pady = 0, padx = 0)
     
     npasswordlabel = tk.Label(master = new, text = 'Enter New Password : ', font = appHighlightFont)
     npasswordlabel.grid(row = 1, column = 0, sticky = W, pady = 0)
     npassword = tk.Entry(new,show = '*')
     npassword.grid(row = 1, column = 1, pady = 0)
     
     emailabel = tk.Label(master = new, text = ' Enter Email : ', font = appHighlightFont)
     emailabel.grid(row = 2, column = 0, sticky = W, pady = 2)
     email = tk.Entry(new)
     email.grid(row = 2, column = 1, pady = 2)

     buttoncreat = tk.Button(master=new, text='submit account', command=valid_email) 
     buttoncreat.grid(row = 3, column = 1)

     #cmblabel = ttk.Label(master = new, text = 'choose expiretime:', font = appHighlightFont)
     #cmblabel.grid(row = 4, column = 0, sticky = W, pady = 2)
     #cmb = ttk.Combobox(master =new, width="10",text = 'choose:' ,values=("1 Month","3 Month","6 Month","1 Year"))
     #cmb.grid(row = 4, column = 1, pady = 2)
    #---------------------------------(For Valid Code)------------------------
     acceptlabel = tk.Label(master = new, text = ' Enter Your Code That Send Into Your Email : ', font = appHighlightFont)
     acceptlabel.grid(row = 5, column = 1, pady = 2)
     accept = tk.Entry(new)
     accept.grid(row = 6, column = 1, pady = 2)      
     
     
     butvalidcode = tk.Button(master=new, text='Check Valid Code', command=checkcode)
     butvalidcode.grid(row = 7, column = 1 )
#============================(Check Valid Email)==============================
def valid_email():
    
    sample = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(sample, email.get()):
        tk.messagebox.showerror('', 'Your Email Valid')
        print('valid')
        send_info()
    else:
        tk.messagebox.showerror('', 'Your Email  Not Valid')
        print('Not Valid')
#==================================(Creat ExpireDate)=========================
time_now = str(datetime.now())
time_now =  datetime.strptime(time_now,'%Y-%m-%d %H:%M:%S.%f')

print(time_now)
        
expire_date = timedelta(minutes=10)
# your calculated date
my_date = time_now + expire_date
#=============================(Charge Accoutnt)==============================
def charge():
    global usernew3
    global passwordnew3
    global cmb
    new3 = tk.Toplevel(window)
    new3.title('Charge Account')
    cmb = ttk.Combobox(master = new3, width="10", values=("1 Month","3 Month","6 Month","1 Year"))

    labelusernew3 = tk.Label(master = new3, text='Enter Your UserName:')
    labelusernew3.pack(expand= True)

    usernew3 = tk.Entry(new3)
    usernew3.pack()

    freelabel = tk.Label(master = new3, text='choose the expite time:')
    freelabel.pack()

    cmb.pack()
    btn = ttk.Button(master = new3, text="Get Value",command=checkcmbo)
    btn.pack()
def checkcmbo():

    db = sqlite3.connect('time.db')
    c = db.cursor()
    time_new3 = datetime.now()
    update = ('UPDATE new_developers SET expiretime = ? WHERE name =?')
    if cmb.get() == "1 Month":
        expire_date = timedelta(days=30)
        my_date = time_new3 + expire_date
        print(my_date)
        messagebox.showinfo("", "Your Account Expire at : {}".format(my_date))
        c.execute(update, [(my_date), (usernew3.get())])
        db.commit()

    elif cmb.get() == "3 Month":
        expire_date = timedelta(days=90)
        my_date = time_now + expire_date
        print(my_date)
        messagebox.showinfo("", "Your Account Expire at : {}".format(my_date))
        c.execute(update, [(my_date), (usernew3.get())])
        db.commit()

    elif cmb.get() == "6 Month":
        expire_date = timedelta(days=180)
        my_date = time_now + expire_date
        print(my_date)
        messagebox.showinfo("", "Your Account Expire at : {}".format(my_date))
        c.execute(update, [(my_date), (usernew3.get())])
        db.commit()

    elif cmb.get() == "1 Year":
        expire_date = timedelta(days=365)
        my_date = time_now + expire_date
        print(my_date)
        messagebox.showinfo("", "Your Account Expire at : {}".format(my_date))
        c.execute(update, [(my_date), (usernew3.get())])
        db.commit()

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")    
#=============================(Check Expire)==================================
def expire():
    with sqlite3.connect('time.db') as db:
        c = db.cursor()
        find = ('SELECT expiretime FROM new_developers WHERE name = ? and password = ?')
        c.execute(find, [(username.get()), (password.get())])
        e = c.fetchall()
        #print(e)
        res = [list(ele) for ele in e]
        for q in res[0]:
            a = datetime.strptime(str(q), '%Y-%m-%d %H:%M:%S.%f')
            if time_now > a:
                print('Your account expire ')
                charge() 
            else:
                tk.messagebox.showinfo('', 'Your Account Expire At {}'.format(res[0]))
                dictionary()
#================================(Send Code To Email)=========================
def send_info():   

    smtpserver = 'smtp.gmail.com'
    smtport = 465
    user = 'ma288664@gmail.com'
    passwordd = 'lenovov310'
    
    subject = 'This Is Validation Code And Information Your Account:'
    
    msbody =' ' + 'Validation Code' + ' '+ r + ' ' + 'username:' + nusername.get()  + ' ' + 'password:' + npassword.get()
    
    message = 'TO:' + email.get() + '\r\n'
    
    message = message + 'Subject: ' + subject + '\r\n'
    
    message = message + msbody
    
    server = smtplib.SMTP_SSL(smtpserver, smtport)
    server.login(user, passwordd)
    server.sendmail(user, email.get(), message)
    server.close()
    print('sucessfuly sned email')
    checkcode()

#====================================(Check Code)=============================
def checkcode():

    if accept.get() == r:
        print('welcome')
        add()
    else:
        print('Not Valid Email')

#=============================================================================
            
def date():
    x = datetime.now()
    date = (x.strftime('%c'))
    tk.messagebox.showinfo('Today', date)
    return date

#=======================(Save Text On Menu Bar)===============================
def text():

    new1 = tk.Toplevel(window)
    new1.title('text editor ')
    new1.geometry('300x320')

    sendlabel = tk.Label(master = new1, text = ' Enter Your Text :',
                         font = ('Times New Roman', 16),
                         foreground = 'white')
    sendlabel.pack()
    text_area = scrolledtext.ScrolledText(new1, width = 40, height = 10,font = ('Times New Roman', 16))
    text_area.pack()
    text_area.focus()
    botonsave = tk.Button(new1, text = 'save', command = lambda : save())
    botonsave.pack()
    botomopen = tk.Button(new1, text='open', command = lambda : open_file())
    botomopen.pack()
    
    
    def save():
        files = [('ALL Files', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        
    def open_file():
        file = askopenfile(mode = 'r', filetypes=[('Python Files', '*.py')])
        if file is not None:
            content = file.read()

#=============================(Main Page Label And Logo)======================

menubar = Menu(window)
file  = Menu(menubar, tearoff=0)
file.add_command(label='text',command = text)
file.add_command(label='Date',command = date)
file.add_command(label='Exit',command = window.destroy)
file.add_separator()
menubar.add_cascade(label = 'Option', menu = file)



appHighlightFont = font.Font(family = 'Helvetica', size = 14, weight = 'bold')
myimage0 = ImageTk.PhotoImage(Image.open('3.jpg'))


center = tk.Label(fg = 'white', bg = 'black',width = 5, height = 10, image=myimage0)
center.pack(fill= BOTH, expand = True)

usernamelabel = tk.Label(text = 'Enter  Username : ', font = appHighlightFont)
usernamelabel.pack()
username = tk.Entry(window)
username.pack()

passwordlabel = tk.Label(text = 'Enter  Password : ', font = appHighlightFont)
passwordlabel.pack()
password = tk.Entry(window, show = '*')
password.pack()

buttonsubmit = tk.Button(master = window, text = 'LogIn', command = login) 
buttonsubmit.pack()

buttoncreat = tk.Button(master = window, text = 'creat account', command = creataccount) 
buttoncreat.pack()

window.config(menu=menubar)
window.mainloop()





