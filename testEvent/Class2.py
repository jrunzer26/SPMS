class Class2(object):
    x = 'global x'
    def __init__(self,reset,pause,play):
        print('in class 2')
        self.x = 'class 2 x'
        self.reset = reset
        #reset(self)
        pause(self)
        pause(self)
        play(self)


    def updateSong(self,songName):
        self.songName = songName
        self.reset(self)

    def displaySong(self):
        print self.songName