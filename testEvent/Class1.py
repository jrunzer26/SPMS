from Class2 import Class2

class Class1(object):

    def function(self,message):
        print message
    def reset(self):
        print'reset'
        print self.x
    def pause(self):
        print 'pause'
    def play(self):
        print 'play'

    c2 = Class2(reset,pause,play)

    c2.updateSong('song of awesomeness')
    c2.displaySong()

