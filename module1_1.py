import math
from math import sin,cos,radians
import os
import sdl2
from payton.scene import SHADOW_HIGH,SHADOW_LOW, Scene,SHADOW_NONE
from payton.scene.geometry import Cube, Plane,Cylinder
from payton.scene.gui import Button, EditBox, Hud, Theme, Window, WindowAlignment
from payton.scene.controller import GUIController,Controller
import datetime
from mytools import settingsbuild,labels,sys_chat,autosaving,bars,updatebar
from buildage import *
from resources import*
from server import *
import graphics
import resources
from PIL import Image,ImageTk
from threading import Thread
from controllers_update import *
import tkinter as tk
from tkinter import*
from tkinter import ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter,Floodgauge
import sys
import ctypes
from time import sleep
root = tk.Tk()
root.geometry('1000x1000')
style = Style('darkrest-blue',themes_file='ttkbootstrap_themes.json')
expwindow = style.master
settingsb=ttk.Button(expwindow, text="Settings")
settingsb.pack(side='left', padx=5, pady=10)
settingsb.place(x=30,y=30)
m1 = Meter(metersize=130, padding=10, amountused=0, metertype='semi', labeltext='current basis level', interactive=True,amounttotal=100,stripethickness=0)
m1.pack()
m2 = Meter(metersize=130, padding=10, amountused=0, metertype='semi', labeltext='current army level', interactive=True,amounttotal=100,stripethickness=0)
m2.pack()

screen_width = root.winfo_screenwidth()
#screen_width =600
screen_height = root.winfo_screenheight()
#screen_height=600
cc=Canvas(expwindow,height=screen_height,width=100,bg='darkgreen')
cc.pack()
cc.place(x=screen_width-100,y=0)
m1.place(x=screen_width//3,y=screen_height-200)
m2.place(x=screen_width-screen_width//3,y=screen_height-200)
cubes=[]
scene = Scene(width=screen_width,height=screen_height+10)
colors=[]
times=[]
kh,ku=1,1
scene.background.set_time(21,0)
w, d, h = 1.0, 1.0, 1.0
texture_file = os.path.join(os.path.dirname(__file__), "images.jpg")
tx_2 = os.path.join(os.path.dirname(__file__), "wood.jpg")


def move(period, total):
    angle = (total * 60) % 360
    px = math.cos(math.radians(angle)) * 8
    #py = math.sin(math.radians(angle)) * 8
    scene.lights[0].position = [px, 50, 6.0, 6.0]
def cubrun(period, total):
    global cubes,kh,ku,scene,tx_2
    ku+=1

    cubes.append(Cylinder(meridians=360,height=15))
    if ku==2:
        pl=0
        ply=0
    elif ku==3:
        pl=6
        ply=6
    elif ku==4:
        pl=0
        ply=12
    elif ku==5:
        pl=-6
        ply=6
    cubes[-1].position = [pl, ply, kh]
    cubes[-1].rotate_around_y(math.radians(90))
    cubes[-1].rotate_around_x(math.radians(90*ku))
    cubes[-1].material.texture=tx_2
    scene.add_object("log"+str(len(cubes)), cubes[-1])
    if ku==5:
        ku=1
        kh+=1
class woodcutter():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.level=1
        self.elements=[]
        self.build_start()
    def build_start(self):
        pass
ground = Plane(width=100, height=100)
scene.lights[0].position = [5.0, 30.0, 6.0]
#scene.create_clock("mm", 0.1, move)
#scene.create_clock("mm1", 0.01, cubrun)
ground.material.texture = texture_file
scene.add_object("ground", ground)
scene.grid.visible = False
k=0
k2=0
kkn=0
kn=0
angles=()
def move_u(e):
    global k,k2,kkn
    k+=10
    scene.cameras[0].mouse_move(3,False,False,10+k2,10+k,0,0,scene.window_width,scene.window_height)
  #  scene.cameras[0].mouse_wheel(kkn)
def move_d(e):
    global k,k2,kkn
    k-=10
    scene.cameras[0].mouse_move(3,False,False,10+k2,10+k,0,0,scene.window_width,scene.window_height)
  #  scene.cameras[0].mouse_wheel(kkn)
def move_r(e):
    global k2,k,kkn
    k2+=10
    scene.cameras[0].mouse_move(3,False,False,10+k2,10+k,0,0,scene.window_width,scene.window_height)
  #  scene.cameras[0].mouse_wheel(kkn)
def move_l(e):
    global k2,k,kkn
    k2-=10
    zoom=kkn
    scene.cameras[0].mouse_move(3,False,False,10+k2,10+k,0,0,scene.window_width,scene.window_height)
def move_f(e):
    global k2,k,kn,kkn
    global k2,k,kn,scene,angles
    kn=-1
    kkn+=kn
    scene.cameras[0].mouse_wheel(kn)
def move_b(e):
    global k2,k,kn,scene,angles,kkn
    kn=1
    kkn+=kn
    scene.cameras[0].mouse_wheel(kn)


def move_ban(e):
    ctypes.windll.user32.MessageBoxW(
                None, 'hi u stopped the window', u"Stop", 0)
    from os import system
    system('taskkill /F /FI "WINDOWTITLE eq Payton Scene" ')
def rbr(event):
    scene.cameras[0].mouse_move(
                2,
                False,
                False,
                event.motion.x,
                event.motion.y,
                event.motion.xrel,
                event.motion.yrel,
                scene.window_width,
                scene.window_height,
            )
def aaaaaaa(e):
    from os import system
    system('taskkill /F /FI "WINDOWTITLE eq Payton Scene" ')
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer

def getForegroundWindowTitle(e) -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    # 1-liner alternative: return buf.value if buf.value else None
    print(buf.value)
def checker():
    pass
def move_window():
    user32 = ctypes.windll.user32

    # get screen resolution of primary monitor
    res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    # res is (2293, 960) for 3440x1440 display at 150% scaling
    user32.SetProcessDPIAware()
    handle = user32.FindWindowW(None, u'Payton Scene')
    user32.ShowWindow(handle, 6)
    # maximize window using handle
    user32.ShowWindow(handle, 9)
    user32.MoveWindow(handle, 0, 0, screen_height, screen_width, True)
# move window using handle
# MoveWindow(handle, x, y, height, width, repaint(bool))
a=bind(scene,'Key-SPACE',func=move_u,additional=root)
b=bind(scene,'Key-SHIFT_L',func=move_d)
abba=bind(scene,'Key-a',func=move_r)
baab=bind(scene,'Key-d',func=move_l)
bab=bind(scene,'Key-w',func=move_f)
baaa=bind(scene,'Key-h',func=move_ban)
bas=bind(scene,'Key-s',func=move_b)
dddd=bind(scene,'Key-ESCAPE',func=aaaaaaa)
root.call("wm", "attributes", ".", "-topmost", True)
das=bind(scene,'Mouse-B1Motion',func=rbr,withreturn=True)
root.call("wm", "attributes", ".", "-fullscreen", True)

root.overrideredirect(True)

scene.controller._controllers.pop(1)

root.wm_attributes("-transparentcolor", "white")
#root.resizable( True,False)


labels(cc,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(stone.get()))
labels_setsize(root.winfo_screenwidth(),root.winfo_screenheight())
threadB = Thread(target = scene.run)
threadB.start()
sleep(1.1)
#move_window()

threadA = Thread(target = root.mainloop)
threadA.run()
# Do work indepedent of loopA and loopB
threadA.join()
threadB.join()

