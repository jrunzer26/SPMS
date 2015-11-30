#!/usr/bin/python

import sys
import subprocess

from Tkinter import *

class GUI (object):
    
    
    """ Calls the quit script
    @param calls itself
    """
    def quit(self): 
        print 'inside quit'
        subprocess.call('./quit.sh')
        #self.root.destroy()
        #sys.exit()
        #root.destroy()

    """ Updates the text of the song
    @param calls itself as well as the name of the current song playing
    """
    def updateSong(self,song):
        self.Csongtext["text"] = song

    """ Updates the text of the next song
    @param calls itself as well as the name of the next song playing
    """
    def updateNextSong(self,song):
        self.up_nexttext["text"] = song

    """ Updates the text of the song
    @param calls itself as well as the name of the current song playing
    """
    def updateRFID(self,tag):
        print tag
        self.rfidtext["text"] = tag
        
    """ Switches the pause to play and play to pause when button is pressed
    @param calls itselfs and the current status
    """    
    def updatePauseButton(self,status):
        self.pause2["text"] = status
        self.pause2.config(width = 7)


    def __init__(self,reset,pausePlay,skip, quit):
        # methods to play skip quir and reset
        def r ():
            reset()
        def p ():
            pausePlay()
        def s ():
            skip()
        def q ():
            quit()

         # sets the font
        font_style = "Arial"
        font_size = 20
        # intialize our gui
        self.root = Tk()

        # sets the width and height
        w = 850
        h = 350
        self.root.geometry("%dx%d+0+0"%(w,h))


        # makes the background and the textboxes
        rfidtag="5465923269"
        self.root.configure(background="#005c99")
        self.Csong = Label(text="What's playing now:",font=(font_style, font_size),relief=RIDGE,width=20)
        self.rfid = Label(text="Last RFID Tap",relief=RIDGE,font=(font_style, font_size),width=20)
        self.up_next = Label(text="Up next",relief=RIDGE,font=(font_style, font_size),width=20)
        self.Csongtext = Label(text="",relief=RIDGE,font=(font_style, font_size),width=30)
        self.rfidtext = Label(text = "",relief=RIDGE,font=(font_style, font_size),width=30)
        self.up_nexttext = Label(text="",relief=RIDGE,font=(font_style, font_size),width=30)

        # places the textboxs on the gui
        self.Csong.grid(row=1,column=1, padx =10, pady = 27)
        self.rfid.grid(row=2,column=1)
        self.up_next.grid(row=3,column=1, pady = 27)
        self.Csongtext.grid(row=1,column=2,columnspan=2, padx=10)
        self.rfidtext.grid(row=2,column=2,columnspan=2, pady=10)
        self.up_nexttext.grid(row=3,column=2,columnspan=2, pady = 10)



        # makes the buttons
        self.reset2 = Button(self.root, text ="Reset",bg = "red",font=(font_style, font_size), command = r)
        self.pause2 = Button(self.root, text ="Pause",relief=GROOVE,bg = "#00e64d", font=(font_style, font_size), command = p)
        self.pause2.config(width = 7)
        self.skip2 = Button(self.root, text ="Skip",bg = "orange", font=(font_style, font_size), command = s)

        # places the buttons on the gui        
        self.skip2.grid(row=4,column=1,ipadx=20, pady=30)
        self.pause2.grid(row=4,column=2,ipadx=14,padx=10)
        self.reset2.grid(row=4,column=3,ipadx=20,padx=10)
        #self.kill.grid(row=4,column =5, ipadx = 10, padx=10)


    """ Returns the root
    @param  calls itself
    @return the gui value
    """    
    def getRoot(self):
        return self.root
