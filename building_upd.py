from tkinter import *
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import dicttry
from functools import*
from resources import *
import math
buildroot=0
c=0
root=Tk()
imags=[]
paths=[]
costs=[]
k=0
money.change(100000000000)
freepeople.change(125465323553)
runnerd=dicttry.self_run()
for i in runnerd.keys():
    imags.append(ImageTk.PhotoImage(Image.open(runnerd[i]['skin']),master=root))
    paths.append(runnerd[i]['skin'])
    costs.append(runnerd[i]['building'])
print(costs)
def newobj(imagepath,n):
    money.change(100000000000)
    freepeople.change(125465323553)
    global c,root,imags,paths,k
    a=0
    def moveo(e):
        selfx, selfy = c.coords(a)
        mousex, mousey = e.x,e.y
        directDist = math.sqrt(((mousex-selfx) ** 2) + ((mousey-selfy) ** 2))
        speed = 4
        movex = (mousex-selfx) / directDist
        movey = (mousey-selfy) / directDist
        c.move(a, movex*speed, movey*speed)
    if checkcosts(n)!=0:
        a=c.create_image(200+100*k,100+100*k,image=imags[paths.index(imagepath)])
        k+=1
        print(c.bbox(a))
        deletecost(n)
        c.bind('<Motion>',moveo)
    else:
        mb.showerror(
            "You can't build this building",
            "Sorry, you can't build this building, because you dont have enough resources")
def bwinnew():
    global buildroot
    def on_closing():
        global buildroot
        buildroot.destroy()
        buildroot=0

    if buildroot==0:
     buildroot=Tk()
     buildroot.attributes('-topmost', True)
     buildroot.protocol("WM_DELETE_WINDOW", on_closing)
     buildroot.call("wm", "attributes", ".", "-alpha", "0.8")
     for i in runnerd.keys():
        Button(buildroot,text=i+' '+str(runnerd[i]['building']).replace("'",'').replace(",",'').replace("{",'').replace("}",''),command=partial(newobj,runnerd[i]['skin'],runnerd[i]['building'])).pack()
    else:
        print('--window is opened already--')

b=Button(text='gfd;k;grerge',command=bwinnew)
b.pack()
c=Canvas(root,width=1000,height=1000,bg='#90EE90')
c.pack()
root.mainloop()