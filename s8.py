import random
import time
import sys
from psychopy import visual,core,event,data,gui
from psychopy.tools.filetools import fromFile,toFile

#phase = visual.TextStim(win=win,height= 30, color= 'white',text='This is the practice phase. \nWhen you are ready, please press the "Space" key to continue.')
#practiceVWM = visual.TextStim(win=win,text='Practice block of VWM task. \nPress the "Space" key to continue.',pos=(0,4),height= 30)

#setting
win = visual.Window(monitor='testMonitor',color="black", units='pix',fullscr = False)

t0 = core.getTime()

fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
fix.draw()
core.wait(.5)
win.flip()
t1 = core.getTime()

fix = visual.TextStim(win,text='+', height=80, color='white',pos=[0,0])

phase.draw()
win.flip()
event.waitKeys(keyList="space")
#practice
practiceVWM.draw()
win.flip()
event.waitKeys(keyList="space")

fix.draw()
core.wait(.5)
win.flip()

squ1 = visual.Rect(win,lineColor="black",size=[100,100])
squ2 = visual.Rect(win,lineColor="black",size=[100,100])
squ3 = visual.Rect(win,lineColor="black",size=[100,100])
squ4 = visual.Rect(win,lineColor="black",size=[100,100])
squ5 = visual.Rect(win,lineColor="black",size=[100,100])
squ6 = visual.Rect(win,lineColor="black",size=[100,100])
squ7 = visual.Rect(win,lineColor="black",size=[100,100])
squ8 = visual.Rect(win,lineColor="black",size=[100,100])

# 1. define 8 Colors
colors = ['#FF0000', '#FFA500', '#0000FF', '#2AA54C','#D1FF00','#394A83','#7D3A4B','#1E90FF']
# 2. define 8 positions.
location = [[-100,200],[-200,100],[-200,-100],[-100,-200],[100,-200],[200,-100],[200,100],[100,200]]

color = random.sample(colors, 8)


######same componet######
time = [.3 , 2.0, .3, 2.0, .3, 2.0, .3, 2.0]
t = random.sample(time, 2)
color1 = random.sample(color, 4)
location1 = random.sample(location, 4)

squ1.setPos(location[0])
squ1.setFillColor(color[1])
squ2.setPos(location[1])
squ2.setFillColor(color[2])
squ3.setPos(location[2])
squ3.setFillColor(color[3])
squ4.setFillColor(color[0])
squ4.setPos(location[3])
squ5.setPos(location[4])
squ5.setFillColor(color[4])
squ6.setPos(location[5])
squ6.setFillColor(color[5])
squ7.setPos(location[6])
squ7.setFillColor(color[6])
squ8.setPos(location[7])
squ8.setFillColor(color[7])

squ1.draw()
squ2.draw()
squ3.draw()
squ4.draw()
squ5.draw()
squ6.draw()
squ7.draw()
squ8.draw()
win.flip()
core.wait(2.0)
t2 = core.getTime()

###block1#####
cue1 = visual.Rect(win,lineColor="black",size=[100,100])
cue2 = visual.Rect(win,lineColor="black",size=[100,100])
cue1.setFillColor('white')
cue1.setPos(location1[0])
cue2.setFillColor('white')
cue2.setPos(location1[1])
cue1.draw()
cue2.draw()
win.flip()
core.wait(t[0])
t3 = core.getTime()# should be equal to t[0]

res1 = visual.Rect(win,lineColor="black",size=[100,100])
res1.setFillColor(color1[0])
res1.setPos(location1[0])
res1.draw()
win.flip()
resp1 = event.waitKeys(keyList = ['k','s'])
t4 = core.getTime()


res2 = visual.Rect(win,lineColor="black",size=[100,100])
res2.setFillColor(color1[1])
res2.setPos(location1[1])
res2.draw()
win.flip()
resp2 = event.waitKeys(keyList = ['k','s'])
t5 = core.getTime()

###block2#####
cue3 = visual.Rect(win,lineColor="black",size=[100,100])
cue4 = visual.Rect(win,lineColor="black",size=[100,100])
cue3.setFillColor('white')
cue3.setPos(location1[2])
cue4.setFillColor('white')
cue4.setPos(location1[3])
cue3.draw()
cue4.draw()
win.flip()
core.wait(t[1])
t6 = core.getTime()# should be equal to t[1]

res3 = visual.Rect(win,lineColor="black",size=[100,100])
res3.setFillColor(color1[2])
res3.setPos(location1[2])
res3.draw()
win.flip()
resp3 = event.waitKeys(keyList = ['k','s'])
t7 = core.getTime()

res4 = visual.Rect(win,lineColor="black",size=[100,100])
res4.setFillColor(color1[3])
res4.setPos(location1[3])
res4.draw()
win.flip()
resp4 = event.waitKeys(keyList = ['k','s'])
t8 = core.getTime()
########data################
#c = random.choice(col)
#print(c)
IC = [t[0], t[1]]
print("IntrsuionCost =")
print(IC)
###about blocka1
print("1st cue apear in")
print(t[0])
print("1st block should be")
print(color1[0])
print(color1[1])
print("this stimul=>")
print(color)
print(location)
print("1st block appear in ")
print(location1[0])
print(location1[1])
print(resp1)
print(resp2)
#####about block2
print("2nd cue apear in")
print(t[1])
print("this stimul show in")
print(location)
print("2nd block cues apear")
print(location1[2])
print(location1[3])
print("this stimul=>")
print(color)
print("2nd block should be")
print(color1[2])
print(color1[3])
print(resp3)
print(resp4)
RT = [t4, t5, t7, t8]
print(RT)
