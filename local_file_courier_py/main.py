from tkinter import *
import os


def sendFile():
    print('Sending Files')
    path = os.getcwd()+r'\sendFiles.py'
    print(os.getcwd()+r'\sendFiles.py')
    window.destroy()
    window.quit()
    os.system('python sendFiles.py')

def receiveFile():
    print('Receiving Files')
    window.destroy()
    window.quit()
    os.system('python receiveFiles.py')


window=Tk()
window.iconbitmap('logo.ico')
port_number=120489
window.title('Local File Courier')
window.geometry("300x150")
receiving_lbl=Label(window, text="LocalFileCourier", fg='black', font=("Garamond", 16))
receiving_lbl.place(x=70, y=10)
sendButton = Button ( window, text='Send', padx=20, pady=10, command=sendFile)
sendButton.place(x=110,y=50)

receiveButton = Button ( window, text='Receive', padx=13, pady=10, command=receiveFile)
receiveButton.place(x=110,y=100)


window.resizable(False, False)
window.mainloop()