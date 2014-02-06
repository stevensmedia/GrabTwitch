#! /usr/bin/env python

import Twitch
import Tkinter

def submit():
	channel = channelEntry.get()
	dataEntry.config(state=Tkinter.NORMAL)
	dataEntry.delete(0, Tkinter.END)
	dataEntry.insert(0, Twitch.grab(channel))
	dataEntry.config(state='readonly')

def copy():
	rootWindow.clipboard_clear()
	rootWindow.clipboard_append(dataEntry.get())

rootWindow = Tkinter.Tk()
rootWindow.geometry('600x120')
rootWindow.title("GrabTwitch")
channelEntry = Tkinter.Entry(rootWindow)
submitButton = Tkinter.Button(rootWindow, command=submit, text='Submit')
dataEntry = Tkinter.Entry(rootWindow, state='readonly')
copyButton = Tkinter.Button(rootWindow, command=copy, text='Copy')

channelEntry.pack(fill=Tkinter.X)
submitButton.pack(fill=Tkinter.X)
dataEntry.pack(fill=Tkinter.X)
copyButton.pack(fill=Tkinter.X)

rootWindow.mainloop()
