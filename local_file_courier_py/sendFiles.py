from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import random
import socket

listPlace = 0


def get_folder_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        get_folder_path()
    else:
        folderPath.set(folder_selected)
    # print(folderPath.get().split('/')[-1])

def go_back():
    gui.destroy()
    gui.quit()
    os.system('python main.py')


def random_port():
    random_portText.set(str(random.randint(0, 9))+str(random.randint(0, 9)) +
                        str(random.randint(0, 9))+str(random.randint(0, 9)))




def start_key():

    print("You pressed Start")
    gui.quit()
    gui.destroy()
    os.system(f'py sender_sockets.py --port {int(random_portText.get())} --file {folderPath.get()}')


def just_started():
    global listPlace
    listPlace += 1
    text_area.insert(listPlace, "Transported "+str(listPlace-2)+" Times..")
    text_area.select_clear(text_area.size() - 2)
    text_area.select_set(END)
    text_area.yview(END)
    start_key()


gui = Tk()
gui.geometry("300x260")
gui.iconbitmap('logo.ico')

gui.title("Send Files")
folderPath = StringVar()
folderPath.set('Folder Path Here')

random_portText = StringVar()
random_portText.set(str(random.randint(0, 9)) + 
                    str(random.randint(0, 9)) +
                    str(random.randint(0, 9)) +
                    str(random.randint(0, 9)))

default_ip_text = StringVar()
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
default_ip_text.set(local_ip)
c = ttk.Button(gui, text="Back", command=go_back)
c.place(x=0, y=5)

a = Label(gui, text="File")
a.place(x=0, y=35)
btnFind = ttk.Button(gui, text="Select Folder", command=get_folder_path)
btnFind.place(x=50, y=35)
E = Entry(gui, textvariable=folderPath, state='disabled')
E.place(x=150, y=35)

portLbl = Label(gui, text="Port")
portLbl.place(x=0, y=65)
buttonRandom = ttk.Button(gui, text="Gen Port", command=random_port)
buttonRandom.place(x=50, y=65)
portEntry = Entry(gui, textvariable=random_portText, state='disabled')
portEntry.place(x=150, y=65)

keyLbl = Label(gui, text="IP")
keyLbl.place(x=0, y=95)
KeyEntry = Entry(gui, textvariable=default_ip_text,width=37, state='disabled')
KeyEntry.place(x=50, y=95)

startButton = ttk.Button(gui, text="Start", command=just_started)
startButton.place(x=100, y=125)

progress = ttk.Progressbar(gui, orient=HORIZONTAL, value=10, length=290, mode='determinate')
progress.place(x=0, y=160)


log = Label(gui, text="Logs", font=("Times New Roman", 7))
log.place(x=0, y=185)
text_area = Listbox(gui, width=48, height=3, font=("Times New Roman", 10))
text_area.place(x=0, y=205)
text_area.insert(listPlace, "Press Start To Start Program")
listPlace += 1
text_area.insert(listPlace, "When u press the key from keys this program will send ")
listPlace += 1
text_area.insert(listPlace, 'to all other computer receiving with the same port')
text_area.select_set(END)
text_area.yview(END)
get_folder_path()

gui.resizable(False, False)
gui.mainloop()
