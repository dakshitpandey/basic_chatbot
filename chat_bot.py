from tkinter import *
import time
from PIL import ImageTk,Image
import pywhatkit
window = Tk()
window.title("CHAT BOT")
window.geometry('400x500')


def send():
    send ="you:"+messagewindow.get()

    chatarea.insert(END,"\n"+send)
    got = messagewindow.get()
    got = got.lower()

    if(got == 'hi' or got== "hello" ):
        chatarea.insert(END,"\n"+"BOT: hello")
    elif(got == "what is your name"):
        chatarea.insert(END,"\n"+"BOT: my name is botox")
    elif(got == "how are you"):
        chatarea.insert(END,"\n"+"BOT: I am fime. what about you")
    elif(got == "i am fine"):
        chatarea.insert(END,"\n"+"BOT: good to hear that")
    elif ('time' in got):
        curr_time = time.strftime('%H:%M:%S')
        chatarea.insert(END,"\n"+f"BOT: {curr_time}")
    elif ('play' in got):
        search = got.split(' ')
        pywhatkit.playonyt(search[1])
    else :
        chatarea.insert(END,"\n"+"BOT: I didn't get that")

    messagewindow.delete(0,END)




chatarea = Text(window,bg='black',width=50,height=8,fg="white")
chatarea.place(x=6,y=6, height=385,width=370)



messagewindow = Entry(window,bg='black',width= 30,fg="white")
messagewindow.place(x=128,y=400,height=81,width=260)

img=ImageTk.PhotoImage(Image.open("icons8-sent-24.png"))
send = Button(window,image=img,command= send)
send.place(x=6,y=400,height=70,width=110)


window.mainloop()