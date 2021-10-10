from tkinter import *
import socket
import datetime
from threading import Thread

client_socket = socket.socket()  # instantiate
now = datetime.datetime.now()

def connect():
    try:
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number
        client_socket.connect((host, port))  # connect to the server
        textConnect = Text(width=12, height=2, font="Calibri 8", bg="green", fg='white')
        textConnect.grid(row=1, column=2, padx=0, pady=0)
        textConnect.delete(1.0, END)
        textConnect.insert(1.0, 'Connected')
    except:
        textConnect = Text(width=12, height=2, font="Calibri 8", bg="red", fg='black')
        textConnect.grid(row=1, column=2, padx=0, pady=0)
        textConnect.delete(1.0, END)
        textConnect.insert(1.0, "Not Connected")


def sendMessage():
    try:
        message = send.get()
        client_socket.send(message.encode())  # send message
        text.insert(1.0, '\n' + now.strftime("%d-%m-%Y %H:%M ") + nameEntry.get() + ': ' + message)
        data = client_socket.recv(1024).decode()  # receive response
        text.insert(1.0, '\n' + now.strftime("%d-%m-%Y %H:%M") + ' server tell: ' + data)
    except:
        text.delete(1.0, END)
        text.insert(1.0, "Can't send Message!")

def receivMessage():
    pass



def clearMessage():
    text.delete(1.0, END)




window = Tk()
window.geometry('580x500')

nameLabel = Label(window, text='Enter name:', font='Calibri 12')
nameLabel.grid(row=0, column=0, padx=20, pady=20)
nameEntry = Entry(window, fg='black', width=43, font="Calibri 12")
nameEntry.grid(row=0, column=1, padx=0, pady=0)

text = Text(width=50, height=15, font="Calibri 10", fg='black', wrap=WORD)
text.grid(row=2, column=1, padx=0, pady=0)

lable = Label(window)
lable.grid(row=1, column=2, padx=10, pady=10)
lable = Label(window)
lable.grid(row=3, column=2, padx=10, pady=10)

send = Entry(window, fg='black', width=43, font="Calibri 12")
send.grid(row=4, column=1, padx=10, pady=10)
sendLable = Label(window, text='Enter message: ', font='Calibri 12')
sendLable.grid(row=4, column=0, padx=10, pady=10)

btn = Button(window, width=10, height=2, text="Connected", command=connect, font="Calibri 8", bg="black", fg="white")
btn.grid(row=0, column=2, padx=10, pady=10)

btnSms = Button(window, width=18, height=2, text="Send", command=sendMessage, font="Calibri 8", bg="black", fg="white")
btnSms.grid(row=7, column=1, padx=10, pady=10)

btnClear = Button(window, width=10, height=2, text="Clear", command=clearMessage, font="Calibri 8", bg="black", fg="white")
btnClear.grid(row=7, column=2, padx=10, pady=10)

# th = Thread(target=sendMessage())
#
# th.start()




mainloop()
