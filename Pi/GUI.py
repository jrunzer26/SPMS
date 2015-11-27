#!/usr/bin/python

import sys
import subprocess

from Tkinter import *

class GUI (object):
    
    
    def quit(self): 
        print 'inside quit'
        subprocess.call('./lol.sh')
        #self.root.destroy()
        #sys.exit()
        #root.destroy()

    def updateSong(self,song):
        self.Csongtext["text"] = song

    def updateNextSong(self,song):
        self.up_nexttext["text"] = song

    def updateRFID(self,tag):
        print tag
        self.rfidtext["text"] = tag
        

    def updatePauseButton(self,status):
        self.pause2["text"] = status
        self.pause2.config(width = 10)


    def __init__(self,reset,pausePlay,skip, quit):
        def r ():
            reset()
        def p ():
            pausePlay()
        def s ():
            skip()
        def q ():
            quit()

        font_style = "Arial"
        font_size = 20
        self.root = Tk()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0"%(w,h))



        rfidtag="5465923269"
        self.root.configure(background="#005c99")
        self.Csong = Label(text="What's playing now:",bg = "#00e64d",font=(font_style, font_size),relief=RIDGE,width=20)
        self.rfid = Label(text="Last Rfid Tap",relief=RIDGE,font=(font_style, font_size),width=20)
        self.up_next = Label(text="Up next",relief=RIDGE,font=(font_style, font_size),width=20)
        self.Csongtext = Label(text="Current Song",relief=RIDGE,font=(font_style, font_size),width=30)
        self.rfidtext = Label(text = "RFID STUFF",relief=RIDGE,font=(font_style, font_size),width=30)
        self.up_nexttext = Label(text="Up Next Song",relief=RIDGE,font=(font_style, font_size),width=30)


        self.Csong.grid(row=1,column=1, padx =10, pady = 27)
        self.rfid.grid(row=2,column=1)
        self.up_next.grid(row=3,column=1, pady = 27)
        self.Csongtext.grid(row=1,column=4,columnspan=2, padx=10)
        self.rfidtext.grid(row=2,column=4,columnspan=2)
        self.up_nexttext.grid(row=3,column=4,columnspan=2)




        self.reset2 = Button(self.root, text ="Reset",bg = "red",font=(font_style, font_size), command = r)
        self.pause2 = Button(self.root, text ="Pause",relief=GROOVE,bg = "#00e64d", font=(font_style, font_size), command = p)
        self.pause2.config(width = 10)
        self.skip2 = Button(self.root, text ="Skip", font=(font_style, font_size), command = s)

        #self.kill = Button(self.root, text = "BYE", bg = "orange", font = (font_style, font_size), command = self.root.destroy)
        self.kill = Button(self.root, text = "BYE", bg = "orange", font = (font_style, font_size), command = self.quit)
        self.skip2.grid(row=4,column=1,ipadx=20, pady=30)
        self.pause2.grid(row=4,column=3,ipadx=14,padx=10)
        self.reset2.grid(row=4,column=4,ipadx=20,padx=10)
        self.kill.grid(row=4,column =5, ipadx = 10, padx=10)


    def getRoot(self):
        return self.root
