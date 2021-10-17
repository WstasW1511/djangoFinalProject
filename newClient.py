import socket
from tkinter import *
import datetime

client_socket = socket.socket()
now = datetime.datetime.now()


def connect():
    try:
        if len(nameEntry.get()) == 0:
            text.delete(1.0, END)
            text.insert(1.0, 'Enter Name')
            nameLabel = Label(window, text='Enter name:', font='Calibri 12', bg='red')
            nameLabel.grid(row=0, column=0, padx=20, pady=20)
        else:
            host = "192.168.82.119"
            port = 5000
            client_socket.connect((host, port))
            textConnect = Text(width=12, height=2, font="Calibri 8", bg="green", fg='white')
            textConnect.grid(row=1, column=2, padx=0, pady=0)
            textConnect.delete(1.0, END)
            textConnect.insert(1.0, 'Connected')
            nameLabel = Label(window, text='Enter name:', font='Calibri 12')
            nameLabel.grid(row=0, column=0, padx=20, pady=20)
            text.delete(1.0, END)
            btnDisconnect = Button(window, width=10, height=2, text="Disconnect", command=disconnect, font="Calibri 8",
                                   bg="black", fg="white")
            btnDisconnect.grid(row=3, column=2, padx=10, pady=10)
    except:
        textConnect = Text(width=12, height=2, font="Calibri 8", bg="red", fg='white')
        textConnect.grid(row=1, column=2, padx=0, pady=0)
        textConnect.delete(1.0, END)
        textConnect.insert(1.0, "Not Connected")


def send_message():
    message = message_entry.get()
    if message == '0':
        message = "!DISCONNECT"
        client_socket.send(message.encode())
        client_socket.close()
    client_socket.send(message.encode())
    data = client_socket.recv(2048).decode()
    text.insert(1.0, '\n' + now.strftime("%d-%m-%Y %H:%M ") + nameEntry.get() + ' : ' + data)
    message_entry.delete(0, END)
    print(data)


def clearMessage():
    text.delete(1.0, END)


def disconnect():
    message = "!DISCONNECT"
    client_socket.send(message.encode())
    client_socket.close()
    textConnect = Text(width=12, height=2, font="Calibri 8", bg="red", fg='white')
    textConnect.grid(row=1, column=2, padx=0, pady=0)
    textConnect.delete(1.0, END)
    textConnect.insert(1.0, 'Not Connected')
    btn = Button(window, width=10, height=2, text="Disconnect", command=connect, font="Calibri 8", bg="red",
                 fg="white")
    btn.grid(row=0, column=2, padx=10, pady=10)

    btnSms = Button(window, width=18, height=2, text="Send", command=send_message, font="Calibri 8", bg="red",
                    fg="white")
    btnSms.grid(row=7, column=1, padx=10, pady=10)


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
message_entry = Entry(window, fg='black', width=43, font="Calibri 12")
message_entry.grid(row=4, column=1, padx=10, pady=10)
sendLable = Label(window, text='Enter message: ', font='Calibri 12')
sendLable.grid(row=4, column=0, padx=10, pady=10)
btn = Button(window, width=10, height=2, text="Connected", command=connect, font="Calibri 8", bg="black", fg="white")
btn.grid(row=0, column=2, padx=10, pady=10)
btnSms = Button(window, width=18, height=2, text="Send", command=send_message, font="Calibri 8", bg="black", fg="white")
btnSms.grid(row=7, column=1, padx=10, pady=10)
btnClear = Button(window, width=10, height=2, text="Clear", command=clearMessage, font="Calibri 8", bg="black", fg="white")
btnClear.grid(row=7, column=2, padx=10, pady=10)
mainloop()
