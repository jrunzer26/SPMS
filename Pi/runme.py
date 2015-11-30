#!/usr/bin/python

__author__ = '100520993'
from User import User
from GUI import GUI
import serial
import pygame
import thread
import sys
import subprocess
# Variables 
finalSongList = []
songsPlayed = []
userList = []
userRemovedList = []
songIndex = 0
vipUser = User([00,00,00,00,00])
blankUser = User([0,0,0,0,0])
global gui
global firstSongLoaded
global currentSong
global nextSong
global skipBool
global initialized
initialized = False

# Try catch loop for serial 
try:
    ser = serial.Serial('/dev/ttyACM1', 9600)
except Exception:
    ser = serial.Serial('/dev/ttyACM0', 9600)
pauseStatus = 0

"""Calls the script to exit on clicking the windows close button
"""
def quit():
    print 'inside quit 2'
    subprocess.call('./quit.sh')

"""Call back for quit
"""
def quit_callback():
    gui.quit()

"""Call back for reset
"""
def resetCallback():
    gui.updateRFID('Tap VIP User')
    global resetVar
    resetVar = True
"""Adds or removes a user by rfid whether it has a text file or not
@param rfidTag the list that contains the RFID tag number
"""

"""Resets all the variables when reset is pressed
"""
def reset():
    print 'reset called'
    global userList
    global songIndex
    global vipUser
    global blankUser
    global finalSongList
    global songsPlayed
    global firstSongLoaded
    global gui
    global nextSong

    userList = []
    songsPlayed = []
    finalSongList = []
    createPlaylist()
    songIndex = 0
    vipUser = blankUser
    nextSong = ''
    gui.updateNextSong(nextSong)
    firstSongLoaded = False


"""Checks for vip user 
@param user is an user id
@return boolean
"""
def checkVip(user):
    # Gets global variables
    global  vipUser
    # Checks if the user is a vip user
    if vipUser.equals(user):
        return True
    return False
"""Sets the vip user to an empty user 
"""
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
    gui.updateRFID(rfidTag)


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
    # Checks uf the song list is not emo=pty
    if songList:
        # resets the lists to empty array
        uniqueSong = []
        groupList = []
        # gets all the songs for user list
        for n in range(len(userList)):
            groupList.append([])
            uniqueSong.append(songList[0])
        # gets all the songs for unique songs
        for n in songList:
            c = True
            for j in uniqueSong:
                if(n == j):
                    c = False
                    break
            if c:
                uniqueSong.append(n)
        # for each song in the list we add a counter for the same values
        for n in uniqueSong:
            count = -1
            for j in songList:
                if n == j:
                    count += 1
            if count >= len(userList):
                count = len(userList)-1
            if count >= 0:
                groupList[count].append(n)

        # adds the songs to the current list that is 
        for n in range(len(groupList)-1,-1, -1):
            for j in range(len(groupList[n])):
                finalSongList.append(groupList[n][j])

    else:
        finalSongList.append('')




"""Gets the next song to be played
@return nest song
"""
def getNextSong():
    global finalSongList
    global songIndex
    global songsPlayed
    # Checks if final song list is going to go out of bounds
    if(songIndex >= len(finalSongList)):
        # resets value to 0
        songIndex = 0
    # Gets the next song to be played
    while(hasnotbeenPlayed(finalSongList[songIndex])):
        songIndex += 1
        if(songIndex >= (len(finalSongList))):
            songIndex = 0
            songsPlayed = []
    # adds to songs played
    songsPlayed.append(finalSongList[songIndex])
    return finalSongList[songIndex]

"""Checks if the song has alreay been played
@param the song
@return a boolean value if the song is played or not"""
def hasnotbeenPlayed(song):
    global songsPlayed
    # checks if the songs are played
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
def pausePlay():
    print 'pause play called'
    # gets the global variables
    global pauseStatus
    global userList
    global gui
    global pygame
    # check if paused
    if pauseStatus == 0:
        # calls pause from py game
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            pauseStatus = 1
            gui.updatePauseButton("Play")
    elif len(finalSongList) > 0:
        gui.updatePauseButton("Pause")
        pygame.mixer.music.unpause()
        pauseStatus = 0


"""Skip the current song being played
"""
def skip():
    # calling global variables
    global pauseStatus
    global firstSongLoaded
    global currentSong
    global nextSong
    global skipBool
    global initialized
    global gui
    skipBool = True
    # checks if the intialized is set to true
    if initialized:
        # Checks if the length of the user list is greater than 1
        if len(userList) >= 1:
            # Checks if the first song was not loaded
            if( not firstSongLoaded):
                # gets the next song of the list sets it to trye
                currentSong = getNextSong()
                firstSongLoaded = True
            else:
                # gets the song next song 
                currentSong = nextSong
            # gets the next song and stores it
            nextSong = getNextSong()
            # does all the calls for playing the next song
            pygame.mixer.music.load(currentSong)
            gui.updateSong(currentSong)
            gui.updateNextSong(nextSong)
            pygame.mixer.music.play()
    skipBool = False
    print 'skip called'


"""This is the input stream from the arduino to the Pi"""
resetVar = False


"""
Main program that loops 
@param theardName a string for the main programs thread
"""
def main(threadName):
    # get global variables
    global gui
    global resetVar
    # starts our music playing library pygame
    pygame
    pygame.init()
    pygame.mixer.init()

    global skipBool
    skipBool = False

    global firstSongLoaded
    firstSongLoaded = False
    global currentSong
    global nextSong
    global initialized
    print 'main thread called'
    counter = 0;
    initialized = True

    # infinite loop to continously check for actions from the gui and arduino controller
    while 1:

        x = ""
        # Checks for an input from serial
        if ser.inWaiting() > 0:
            # Gets the input from serial
            x = ser.readline().rstrip()
            print "Arduino input:" + x

        # resests the lst to emptu
        lst = []
        # Checks if x has an RFID value
        if x == "RFID":
            
            # spits the RFID tage value to an array of 5
            for i in range(0, 5):
                lst.append(ser.readline().rstrip())
            # Checks if reset button was pressed
            if resetVar == False:
                # update user list 
                updateUser(lst)
                # Checks if the length of user if equal to 0
                if(len(userList) == 0):
                    # sends updates to the qui
                    print 'updating song'
                    nextSong = ''
                    gui.updateNextSong(nextSong)
                    firstSongLoaded = False
            else:
                # check if a vip user was pressed
                if(checkVip(User(lst))):
                    reset()
                else:
                    # invalid vip user
                    gui.updateRFID('INVALID VIP')
                    print("INVALID VIP")
                resetVar = False


        # Checks if their are users in a list and if the skip
        if len(userList) > 0 and not pygame.mixer.music.get_busy() and skipBool == False:
            skip()
            print 'in skip loop'
            skipBool = False





#create the GUI
nextSong = ""
gui = GUI(resetCallback,pausePlay,skip, quit_callback)
thread.start_new(main,('main thread',))
gui.getRoot().wm_protocol('WM_DELETE_WINDOW', quit)
gui.getRoot().mainloop()
