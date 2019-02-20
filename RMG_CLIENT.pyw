#! python2
from midiutil.MidiFile import MIDIFile;
from pygame import mixer as mix
from pygame import display as disp
from pygame import event
import pygame as pg
import random as rng

##
## Parts are defined by lists
## sectBlah = [Speed,
##              Duration of notes,
##              Amount of notes,
##              notes...,notes,notes,notes]
##

def determineRange():
    noteRange=0
    height = rng.randint(3,7)
    if(height==1):
        noteRange=24
    elif(height==2):
        noteRange=36
    elif(height==3):
        noteRange=48
    elif(height==4):
        noteRange=60
    elif(height==5):
        noteRange=72
    elif(height==6):
        noteRange=84
    return noteRange

def determineSpeed():
    speed = rng.choice([.5,.5,1,2,3])
    return speed 
    
    
def writeNote(pitch,time,duration,track,channel,volume):
    mf.addNote(track, channel, pitch, time, duration, volume)

def getNote(note):
    iteration = -3
    while(note > -1):
        note -= 12
        iteration += 1
    if(note==-12):
        noteType = "C"
    elif(note==-11):
        noteType = "C#"
    elif(note==-10):
        noteType = "D"
    elif(note==-9):
        noteType = "D#"
    elif(note==-8):
        noteType = "E"
    elif(note==-7):
        noteType = "F"
    elif(note==-6):
        noteType = "F#"
    elif(note==-5):
        noteType = "G"
    elif(note==-4):
        noteType = "G#"
    elif(note==-3):
        noteType = "A"
    elif(note==-2):
        noteType = "A#"
    elif(note==-1):
        noteType = "B"
    return note + str(iteration)

def genSect(speed,sec,noteRange):
    dur = 1.5
    if(speed==.5):
        dur = 3
    sect = [speed,dur,int(speed*sec)]
    for i in range(0,int(speed*sec),1):
        sect.append(rng.choice([noteRange,noteRange+2,noteRange+4,noteRange+5,noteRange+7,noteRange+9,noteRange+11,-100,-100,-100,-100]))
    return sect

def genBase(speed,noteRange):
    dur = 1.5
    if(speed==.5):
        dur = 3
    if(noteRange==24):
        noteRange=36
    else:
        noteRange-=12
    sect = [speed,dur,int(speed*4)]
    for i in range(0,int(speed*4),1):
        sect.append(rng.choice([noteRange,noteRange+2,noteRange+4,noteRange+5,noteRange+7,noteRange+9,noteRange+11,-100,-100,-100,-100,-100,-100,-100]))
    return sect
    

def genMusic(sects):
    time = 0
    for sect in sects:
        for i in range(3,len(sect)):
            if(sect[i]!=-100):
                writeNote(sect[i],float(time)/sect[0],sect[1],0,0,100)
            time+=1

def main():
    noteRange=determineRange()
    speed=determineSpeed()
    allSections=[]
    finalTime = 64
    ellapsedTime = 0
    
    while(ellapsedTime<=finalTime):
        time = rng.choice([2,4,8])
        allSections.append(genSect(speed,time,noteRange))
        ellapsedTime += time

    for i in range(0,len(allSections)*20):
        allSections.append(allSections[rng.randint(0,len(allSections)-1)])
    rng.shuffle(allSections)
    
    num=0
    numNotes = 0
    for sect in allSections:
        num+=1
        for i in range(3,len(sect)-1):
            numNotes+=1
    print(numNotes)
    genMusic(allSections)

    
    allSections=[]
    numNotes/=6 
    ellapsedNotes = 0
    while(ellapsedNotes<numNotes-(numNotes*.18)):
        allSections.append(genBase(speed,noteRange))
        counter=0
        for sect in allSections:
            for i in range(3,len(sect)-1):
                counter+=1
        ellapsedNotes = counter

    for i in range(0,len(allSections)*6):
        allSections.append(allSections[rng.randint(0,len(allSections)-1)])
    rng.shuffle(allSections)

    genMusic(allSections)

    num=0
    numNotes = 0
    for sect in allSections:
        num+=1
        for i in range(3,len(sect)-1):
            numNotes+=1
    print(numNotes)
    
    with open("Songs\output.mid", 'wb') as outf:
        mf.writeFile(outf)
    
    mix.init()
    mix.music.load("Songs\output.mid")
    mix.music.play()

    
disp.init()
disp.set_caption("Random Music Generator")
window = disp.set_mode((400,200))
image = pg.image.load("Resources\RandomMusicGen.BMP")
window.blit(image,[0,0])
pg.display.flip()
go = True
while go:
    mf = MIDIFile(1)
    mf.addTrackName(0,0,"Randomnesss")
    mf.addTempo(0,0,rng.choice([60,80,100,120,150,180,200,220,250,280]))
    main()
    wait = True
    while wait:
        for event in pg.event.get():
            if(event.type==pg.QUIT):
                go=False
            if(event.type==pg.MOUSEBUTTONDOWN):
                wait=False

pg.quit()
exit


           
