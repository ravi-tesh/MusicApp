import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
from PIL import ImageTk, Image  

musicplayer= tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("550x650")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist= tkr.Listbox(musicplayer , font="Cambria 14  bold" , bg="cyan" , selectmode=tkr.SINGLE)

for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1


pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()






Button1 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 20 bold", text="PlayMusic", command=play, bg="lime green",fg="black")
Button2 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 20 bold", text="StopMusic", command=ExitMusicPlayer, bg="red",fg="black")
Button3 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 16 bold", text="PauseMusic", command=pause, bg="yellow", fg="black")
Button4 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 16 bold", text="ResumeMusic", command=resume, bg="skyblue", fg="black")
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Helvetica 12 bold", textvariable=var)
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

image1 = Image.open("C:/Users/ravis/Documents/Python/AppMusic.png")
#image1 = img.resize((50, 50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkr.Label(image=test)
label1.image = test
label1.place(x=200, y=200)


musicplayer.mainloop()




