from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from module import *


# ================================= win ==========================
win = Tk()
win.title('YouTube_downloader')
win.geometry('460x300')
win.resizable(width=False, height=False)
win.config(bg='#e0e0e0')

# ================================= Label_entry ==========================
paste_lable = Label(win, text='Paste Link', font=(
    'mitra', 12, 'bold'), padx='2', pady='10', bg='#e0e0e0')
paste_lable.grid(row=0, column=0, padx='10', pady='10')

paste_list_text = StringVar()
paste_list = Text(win, font=('mitra', 10, 'bold'), width=47, height=2, bd='3')
paste_list.grid(row=0, column=1)


title_lable = Label(win, text='Title', font=(
    'mitra', 12, 'bold'), padx='10', pady='10', bg='#e0e0e0')
title_lable.grid(row=3, column=0, padx='5', pady='10')

title_entry_text = StringVar()
title_entry = Entry(win, font=('mitra', 10, 'bold'),
                    width='47', bd='1', textvariable=title_entry_text)
title_entry.place(x=110, y=109)


view_lable = Label(win, text='View', font=(
    'mitra', 12, 'bold'), padx='10', pady='10', bg='#e0e0e0')
view_lable.grid(row=4, column=0)

view_entry_text = StringVar()
view_entry = Entry(win, font=('mitra', 10, 'bold'),
                   width='15', bd='1', textvariable=view_entry_text)
view_entry.place(x=110, y=162)


time_lable = Label(win, text='Time', font=(
    'mitra', 12, 'bold'), padx='10', pady='10', bg='#e0e0e0')
time_lable.place(x=250, y=149)

time_entry_text = StringVar()
time_entry = Entry(win, font=('mitra', 10, 'bold'),
                   width='15', bd='1', textvariable=time_entry_text)
time_entry.place(x=330, y=162)


def submit_button_work():
    global submit
    try:
        submit = submit_link(paste_list.get('1.0', '2.0'))
        title_entry_text.set(submit.title_video())
        view_entry_text.set(submit.view_video())
        time_entry_text.set(submit.time_video())
        download_button = ttk.Button(
        win, text='Download', width='20', command=lambda: window_two())
        download_button.place(x=30, y=210)
    except:
        tkinter.messagebox.showerror('Error', 'wrong Link')
    


def download_video_hight():
    win2.destroy()
    submit.download_video_highest()
    print('complet')


def download_video_low():
    win2.destroy()
    submit.download_video_lowest()
    print('complet')


def window_two():
    global win2
    win2 = Toplevel(win)
    win2.title('Download')
    win2.geometry('350x110')
    win2.resizable(width=False, height=False)
    win2.config(bg='#ffffff')
    l1 = Label(win2, text='Choose Your Quality That You want',
               bg='#ffffff', font=('mitra', 12, 'bold'), padx='10', pady='20')
    l1.pack()
    high_quality = ttk.Button(
        win2, text='High Quality', width='15', command=lambda: download_video_hight())
    high_quality.pack(side='left', padx='40')
    low_quality = ttk.Button(win2, text='Low Quality',
                             width='18', command=lambda: download_video_low())
    low_quality.pack(side='right', padx='40')


# ================================= Button ==========================
submit_button = ttk.Button(
    win, text='Submit', width='20', command=lambda: submit_button_work())
submit_button.grid(row=2, column=1)



close_button = ttk.Button(win, text='Close', width='10', command=win.destroy)
close_button.place(x=370, y=210)


win.mainloop()
