__author__ = '100520993'
import os
"""The user class containing the user identification and their playlist
"""
class User(object):
    playlist = []
    songIndex = 0


    """Creates a user with a tag identification
    @param tagID a list containing the RFID tag identification
    """
    def __init__(self,tagID):
        self.tagID = tagID
        self.updatePlaylist()


    """Returns the users identification as a list
    @return tadID
    """
    def getID(self):
        return self.tagID

    """Updates the playlist from the text file

    """
    def updatePlaylist(self):
        playListName = ""
        for i in self.tagID:
            playListName += str(i)
        playListName += ".txt"
        if(os.path.isfile(playListName) == False):
            playListFile = open(playListName, 'w')
            playListFile.close()

        with open(playListName, "r") as playListFile:
            self.playlist = playListFile.read().split("\n")

    """test function to check the textFile"""
    def getPlaylist(self):
        return self.playlist

    """Resets the song index"""
    def resetSongIndex(self):
        self.songIndex = 0

    """Gets the next song to be played from the users playlist. Returns "" if the playlist is out of songs.
    @return string, the song location
    """
    def getNextSong(self):

        if(len(self.playlist) > self.songIndex):
            self.songIndex += 1
            return self.playlist[self.songIndex - 1]
        elif self.playlist[self.songIndex - 1] == '':
            return "OUTOFBOUNDS"
        else:
            return "OUTOFBOUNDS" # just for a test, should return "" in final code

    """Checks if the it is the same user.
    """
    def equals(self,user):
        for i in range(0,len(self.tagID)):
            if self.tagID[i] != user.getID()[i]:
                return False
        return True







