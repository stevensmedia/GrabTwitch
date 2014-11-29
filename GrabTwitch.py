#! /usr/bin/env python

isMac = True
try:
	import Foundation
except ImportError:
	isMac = False

import Twitch
import Tkinter
import os

def setButtons(s):
	copyButton.config(state=s)
	qtpButton.config(state=s)
	vlcmacButton.config(state=s)

def submit():
	channel = channelEntry.get()
	data = Twitch.grab(channel)
	if data == '':
		data = 'OFFLINE'

	dataEntry.config(state=Tkinter.NORMAL)
	dataEntry.delete(0, Tkinter.END)
	dataEntry.insert(0, data)
	dataEntry.config(state='readonly')

	if data == 'OFFLINE':
		setButtons(Tkinter.DISABLED)
	else:
		setButtons(Tkinter.NORMAL)

def copy():
	rootWindow.clipboard_clear()
	rootWindow.clipboard_append(dataEntry.get())

def vlcmac():
	script = 'do shell script "open -na /Applications/VLC.app --args --quiet --open " & quote & ' + dataEntry.get() + ' & quote"'
	Foundation.NSAppleScript.alloc().initWithSource_(script).executeAndReturnError_(None)

def qtp():
	script = 'tell app "Quicktime Player" to open URL "' + dataEntry.get() + '"'
	Foundation.NSAppleScript.alloc().initWithSource_(script).executeAndReturnError_(None)
	script = 'tell app "Quicktime Player" to set audio volume of last document to 0.5'
	Foundation.NSAppleScript.alloc().initWithSource_(script).executeAndReturnError_(None)


rootWindow = Tkinter.Tk()
if isMac:
	rootWindow.geometry('600x170')
else:
	rootWindow.geometry('600x110')
rootWindow.title("GrabTwitch")
channelEntry = Tkinter.Entry(rootWindow)
submitButton = Tkinter.Button(rootWindow, command=submit, text='Submit')
dataEntry = Tkinter.Entry(rootWindow, state='readonly')
copyButton = Tkinter.Button(rootWindow, command=copy, text='Copy')
qtpButton = Tkinter.Button(rootWindow, command=qtp, text='Open in Quicktime Player')
vlcmacButton = Tkinter.Button(rootWindow, command=qtp, text='Open in VLC')
setButtons(Tkinter.DISABLED)

rootWindow.bind("<Return>", lambda x: submit())

channelEntry.pack(fill=Tkinter.X)
submitButton.pack(fill=Tkinter.X)
dataEntry.pack(fill=Tkinter.X)
copyButton.pack(fill=Tkinter.X)
if isMac:
	qtpButton.pack(fill=Tkinter.X)
	vlcmacButton.pack(fill=Tkinter.X)


rootWindow.mainloop()
