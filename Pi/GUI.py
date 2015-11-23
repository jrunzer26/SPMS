#!/usr/bin/python

import sys
from Tkinter import *

class GUI (object):
   def updateSong(self,message):
      Csong.set(message)
  
   
   def __init__(self,reset,pausePlay,skip):
      self.reset = reset
      self.pausePlay = pausePlay
      self.skip = skip
      
      font_style = "Arial"
      font_size = 20
      root = Tk()
      w = root.winfo_screenwidth()
      h = root.winfo_screenheight()
      root.geometry("%dx%d+0+0"%(w,h))
         
      rfidString = StringVar()
      rfidString.set('reset stuff')

      rfidtag="5465923269"
      root.configure(background="#005c99")
      Csong = Label(text="What's playing now:",bg = "#00e64d",font=(font_style, font_size),relief=RIDGE,width=20)
      rfid = Label(text="Last Rfid Tap",relief=RIDGE,font=(font_style, font_size),width=20)
      up_next = Label(text="Up next",relief=RIDGE,font=(font_style, font_size),width=20)
      Csongtext = Label(text="Current Song",relief=RIDGE,font=(font_style, font_size),width=30)
      rfidtext = Label(textvariable = rfidString,relief=RIDGE,font=(font_style, font_size),width=30)
      up_nexttext = Label(text="Up Next Song",relief=RIDGE,font=(font_style, font_size),width=30)
       

      Csong.grid(row=1,column=1, padx =10, pady = 27)
      rfid.grid(row=2,column=1)
      up_next.grid(row=3,column=1, pady = 27)
      Csongtext.grid(row=1,column=4,columnspan=2, padx=10)
      rfidtext.grid(row=2,column=4,columnspan=2)
      up_nexttext.grid(row=3,column=4,columnspan=2)




      reset2 = Button(root, text ="Reset",bg = "red",font=(font_style, font_size), command = self.reset(self))
      pause2 = Button(root, text ="Pause",relief=GROOVE,bg = "#00e64d", font=(font_style, font_size),
                      command = self.pausePlay(self))
      play2 = Button(root, text ="Play",font=(font_style, font_size), command = self.pausePlay(self))
      skip2 = Button(root, text ="Skip", font=(font_style, font_size), command = self.skip(self))
      skip2.grid(row=4,column=1,ipadx=20, pady=30)
      pause2.grid(row=4,column=3,ipadx=14,padx=10)
      reset2.grid(row=4,column=4,ipadx=20,padx=10)



      root.mainloop()
