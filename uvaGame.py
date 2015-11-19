import runWorld as rw
import drawWorld as dw
import pygame as pg

name = "UVA"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

initState = (0,1)

myimage = dw.loadImage("uva.png")


mylabel = dw.makeLabel("Go Hoos!", "arial", 100, (0,0,255))

def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state[0], width/50))
    dw.draw(mylabel, (250,250))

    
def updateState(state):
    return((state[0]+state[1]),state[1])


def endState(state):
    if (state[0] >= width or state[0] < 0):
        return True
    else:
        return False


def handleEvent(state,event): 
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) == 1:
            newState = -1
        else:
            newState = 1
        return((state[0], newState))
    else:
        return(state)

frameRate = 200
initState = (0,1)


rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
