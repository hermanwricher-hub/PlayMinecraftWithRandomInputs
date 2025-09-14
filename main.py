import random as rd
import keyboard as kb
import mouse
import time

def brianRichard(waitBeforeStart=5, timesToGo=100):
  time.sleep(waitBeforeStart)
  for i in range(timesToGo):
    doSprint = rd.randint(1,3)
    if doSprint == 1:
      kb.press("ctrl")
    else:
      doCroutch = rd.randint(1,20)
      if doCroutch == 1:
        kb.press("shift")
    chosenNum = rd.randint(1,20)
    if chosenNum < 6:
      kb.press("W")
      time.sleep(rd.randint(1,2))
      kb.release("W")
    elif chosenNum == 7:
      kb.press("A")
      time.sleep(1)
      kb.release("A")
    elif chosenNum == 8:
      kb.press("D")
      time.sleep(1)
      kb.release("D")
    elif chosenNum == 9:
      kb.press("S")
      time.sleep(1)
      kb.release("S")
    elif chosenNum < 12:
      kb.send("space")
    elif chosenNum < 14:
      kb.press("space")
      kb.press("W")
      time.sleep(1)
      kb.release("space")
      kb.release("W")
    elif chosenNum < 15:
      kb.press("space")
      kb.press("S")
      time.sleep(1)
      kb.release("space")
      kb.release("S")
    elif chosenNum == 15 or chosenNum == 16:
      mouse.click("right")
    elif chosenNum == 17 or chosenNum == 18:
      mouse.hold("left")
      time.sleep(rd.randint(1,4))
      mouse.release("left")
    elif chosenNum == 19 or chosenNum == 20:
      whatMove = rd.randint(1,4)
      if whatMove == 1:
        mouse.drag(0,0,100, 0, absolute=False, duration=rd.randint(1,10)/100)
      if whatMove == 2:
        mouse.drag(0,0,-100, 0, absolute=False, duration=rd.randint(1,10)/100)
      if whatMove == 3:
        mouse.drag(0,0,0, 100, absolute=False, duration=rd.randint(1,10)/100)
      if whatMove == 4:
        mouse.drag(0,0,0, -100, absolute=False, duration=rd.randint(1,10)/100)
    if doSprint == 1:
      kb.release("ctrl") 
    else:
      if doCroutch == 1:
        kb.release("shift")

brianRichard()