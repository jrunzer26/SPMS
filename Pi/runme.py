#!/usr/bin/python

__author__ = '100520993'
from User import User
from GUI import GUI
import serial
import pygame
import thread

    

pygame
pygame.init()
pygame.mixer.init()


finalSongList = []
songsPlayed = []
userList = []
userRemovedList = []
songIndex = 0
vipUser = User([00,00,00,00,00])
blankUser = User([0,0,0,0,0])
global gui



try:
    ser = serial.Serial('/dev/ttyACM1', 9600)
except Exception:
    ser = serial.Serial('/dev/ttyACM0', 9600)
pauseStatus = 0

# checks to see if a tag is tapped on the rfid reader


"""Adds or removes a user by rfid whether it has a text file or not
@param rfidTag the list that contains the RFID tag number
"""

def reset(self):
    print 'reset called'
    global userList
    global songIndex
    global vipUser
    global blankUser
    global finalSongList
    global songsPlayed

    userList = []
    songsPlayed = []
    finalSongList = []
    createPlaylist()
    songIndex = 0
    vipUser = blankUser

def checkVip(user):
    global  vipUser
    if vipUser.equals(user):
        return True
    return False
def removeVip():
    global vipUser
    global blankUser
    vipUser = blankUser


"""Adds or removes a user by rfid whether it has a text file or not
@param rfidTag the list that contains the RFID tag number
"""
def updateUser(rfidTag):
    global vipUser
    global blankUser
    #boolean variables to see if the tag is in one of the lists already
    inUserList = False
    inUserRemovedList = False
    user = User(rfidTag)


    if vipUser.equals(blankUser):
        vipUser = user

    #need to find the same user object reference whether it be in the userlist or in the removed user list
    equalsUser = user

    #checks if the user is in the userList
    for u in userList:
        inUserList = u.equals(user)
        # found the user that is already in the database that is currently using its songs and tapped off
        if inUserList:
            equalsUser = u
            break
    # if its not in the user list, then we should check if its in the other removed list, since all of their songs
    # might have been played
    if not inUserList:
        for u in userRemovedList:
            inUserRemovedList = u.equals(user)
            #found the user! now lets remove him from the system since he tapped off
            if inUserRemovedList:
                equalsUser = u # found the user that is already in the database and tapped off
                break



    #the user tapped on to enter the system
    if inUserList == False and not inUserRemovedList :
        userList.append(user)
        createPlaylist()
    #if the user tapped off and all the songs in his playlist were played
    elif inUserRemovedList:
        userRemovedList.remove(equalsUser)
        createPlaylist()
        if checkVip(equalsUser):
            removeVip()
    #this is when the user has tapped off of the system but he is not out of songs to play
    else:
        userList.remove(equalsUser)
        if checkVip(equalsUser):
            removeVip()
        createPlaylist()


"""Gets the song list for the users currently in the system"""
def getSongList():
    global userList
    songlist = []


    # Searches through all user
    for n in userList:
        # Gets songs from users
        n.resetSongIndex()
        nextsong = n.getNextSong()
        while nextsong != "OUTOFBOUNDS" and nextsong != "":
            songlist.append(nextsong)
            #print nextsong
            nextsong = n.getNextSong()
    # returns a list of songs
    print "SongList:"
    print songlist
    return songlist


"""Creates a playlist using the songs in the finalSongList"""
def createPlaylist():
    global finalSongList
    global userList
    global vipUser




    print "VIP USER: "
    print vipUser.getID()
    finalSongList = []
    songList = getSongList()
    if songList:
        uniqueSong = []
        groupList = []
        for n in range(len(userList)):
            groupList.append([])
            uniqueSong.append(songList[0])
        for n in songList:
            c = True
            for j in uniqueSong:
                if(n == j):
                    c = False
                    break
            if c:
                uniqueSong.append(n)
        """
        print uniqueSong
        """
        for n in uniqueSong:
            count = -1
            for j in songList:
                if n == j:
                    count += 1
            if count >= len(userList):
                count = len(userList)-1
            if count >= 0:
                groupList[count].append(n)
        #here is where you randomize groupList[count]



        for n in range(len(groupList)-1,-1, -1):
            for j in range(len(groupList[n])):
                finalSongList.append(groupList[n][j])
        """
        print "finalSongList"
        print finalSongList
        """
    else:
        finalSongList.append('')

"""Gets the next song to be played"""
def getNextSong():
    global finalSongList
    global songIndex
    global songsPlayed
    while(hasnotbeenPlayed(finalSongList[songIndex])):
        songIndex += 1
        if(songIndex >= (len(finalSongList))):
            songIndex = 0
            songsPlayed = []
    songsPlayed.append(finalSongList[songIndex])
    """
    print "Songs Played"
    print songsPlayed
    print "Song in get nextSong"
    print finalSongList[songIndex]
    """
    return finalSongList[songIndex]

"""Checks if the song has alreay been played"""
def hasnotbeenPlayed(song):
    global songsPlayed
    if not songsPlayed:
        songsPlayed.append(song)
        return False
    elif (song == "OUTOFBOUNDS" or song == ''):
            return True
    else:
        for n in songsPlayed:
            if(n == song):
                return True
        return False

"""Pauses the music currently being played"""
def pausePlay(self):
    global pauseStatus
    global userList
    if pauseStatus == 0 and not len(userList) == 0:
        pygame.mixer.music.pause()
        pauseStatus = 1
    elif len(finalSongList) > 0:

        pygame.mixer.music.unpause()
        pauseStatus = 0



def skip(self):
    global pauseStatus
    if len(userList) >= 1:
        pauseStatus = 0
        skipSongName = getNextSong()
        pygame.mixer.music.load(skipSongName)
        print "Playing: " + skipSongName
        ser.write(skipSongName)
        ser.write('(')
        pygame.mixer.music.play()
        gui.updateSkip('lets go to the next song')


"""This is the input stream from the arduino to the Pi"""
resetVar = False



def main(threadName):
    global gui
    firstSongLoaded = False
    while 1:
        x = ""

        if ser.inWaiting() > 0:
            x = ser.readline().rstrip()
            print "Arduino input:" + x

        lst = []

        if x == "RFID":

            for i in range(0, 5):
                lst.append(ser.readline().rstrip())
            if resetVar == False:

                updateUser(lst)
            else:
                if(checkVip(User(lst))):
                    reset()
                else:

                    ser.write("INVALID VIP")
                    ser.write(')')
                    print("INVALID VIP")
                resetVar = False



        if len(userList) > 0 and not pygame.mixer.music.get_busy()  :
            if( not firstSongLoaded):
                currentSong = getNextSong()
                nextSong = getNextSong()

            else:
                currentSong = nextSong
                nextSong = getNextSong()

            if(currentSong != ''):
                pygame.mixer.music.load(currentSong)

                gui.updateSong(currentSong)
                gui.updateNextSong(nextSong)

                pygame.mixer.music.play()


#create the GUI
gui = GUI(reset,pausePlay,skip)
thread.start_new(main,('main thread',))
gui.getRoot().mainloop()