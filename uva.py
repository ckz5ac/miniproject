name = "Ball Game"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

initState = 0

myimage = dw.loadImage("uva.png")


def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state, width/50))


def updateState(state):
    return(state+1)


def endState(state):
    if (state >= width):
        return True
    else:
        return False


def handleEvent(state,event): 
    return(state)

frameRate = 60
initState = 0


rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
