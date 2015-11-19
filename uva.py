import runWorld as rw
import drawWorld as dw

name = "UVA"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

initState = 0

myimage = dw.loadImage("uva.png")


mylabel = dw.makeLabel("Go Hoos!", "arial", 100, (255,255,255))

def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state, width/50))
    dw.draw(mylabel, (250,250))

#  (r,g,b)
# where 0 = black and 255 = white

    
def updateState(state):
    return(state+1)


def endState(state):
    if (state >= width):
        return True
    else:
        return False


def handleEvent(state,event): 
    return(state)

frameRate = 200
initState = 0


rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
