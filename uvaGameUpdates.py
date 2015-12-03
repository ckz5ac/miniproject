import runWorld as rw
import drawWorld as dw
import pygame as pg

name = "UVA"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

class State:
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY

initState = State(0, 1)

myimage = dw.loadImage("uva.png")

mylabel = dw.makeLabel("Go Hoos!", "arial", 100, (0,0,255))
otherlabel = dw.makeLabel("Don't lose the Hoos", "serif", 80, (255,255,255))

def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(otherlabel, (150,100))
    dw.draw(myimage, (state.x, width/50))
    dw.draw(mylabel, (250,250))

    
def updateState(state):
    state.x = state.x+state.y
    return state


def endState(state):
    if (state.x >= width or state.x < -width):
        return True
    else:
        return False


def handleEvent(state,event): 
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state.y) == 1:
            newState = -1
        else:
            newState = 1
        state.y = newState
        return(state)
    else:
        return(state)

frameRate = 375
# initState = (0,1)


rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
