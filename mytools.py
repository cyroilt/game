import tkinter as tk
import os
import objects
import time
from PIL import Image,ImageTk
from humanstate import*
l1,l2,l3,l4,l5,i1,i2,i3,i4,i5=0,0,0,0,0,0,0,0,0,0
workingplace,x1,y1=0,0,0
mx=0
LOW ='low'
HIGH ='high'
STATE=LOW
AUTO=0
mysize=[200,200]
bar=[]
def settingsbuild(types,state,load=0,maxload=0,sleepbut=False,n=0):
       def sleepwork():
                     set_sleeping(n,bool(abs(int(get_sleeping(n))-1)))
       r1=tk.Tk()
       r1.title(types+' '+state)
       lstate=tk.Label(r1,text='state: '+state)
       if maxload>0:
              lload=tk.Label(r1,text="load level: "+str(load)+'/'+str(maxload))
              lload.pack()
       else:
              pass
       lstate.pack()
       
       if sleepbut==True:
              b1=tk.Button(r1,text="sleep"*int(get_sleeping(n))+"work"*int(get_sleeping(n)),bg='red',command=sleepwork)
              b1.pack()
def labels(canv,people,freepeople,money,wood,stone):
       global l1,l2,l3,l4,l5,i1,i2,i3,i4,i5,mysize,hum,sto,mon,woo
       hum=tk.PhotoImage(file='human.png')
       woo=tk.PhotoImage(file='wood.png')
       sto=tk.PhotoImage(file='stone.png')
       mon=tk.PhotoImage(file='money.png')
       i1=canv.create_image(20,50,image=hum)
       l1=canv.create_text(70,50,text=str(freepeople)+'/'+str(people))
       i2=canv.create_image(20,100,image=woo)
       l2=canv.create_text(70,100,text=str(wood))
       i3=canv.create_image(20,150,image=sto)
       l3=canv.create_text(70,150,text=str(stone))
       i4=canv.create_image(20,200,image=mon)
       l4=canv.create_text(70,200,text=str(money))
       canv.update()
def labels_upd(canv,people,freepeople,money,wood,stone):
       global l1,l2,l3,l4,l5,i1,i2,i3,i4,i5
       canv.delete(l1)
       canv.delete(l2)
       canv.delete(l3)
       canv.delete(l4)
       canv.delete(l5)
       canv.delete(i1)
       canv.delete(i2)
       canv.delete(i3)
       canv.delete(i4)
       canv.delete(i5)
       labels(canv,people,freepeople,money,wood,stone)
def labels_setsize(width,height):
       global mysize
       mysize=[width,height]
       print(mysize)
def autosaving(c,x,y,state=HIGH):
       global workingplace,STATE,AUTO,LOW,HIGH
       workingplace=c
       STATE=state
       im=tk.PhotoImage(file=STATE+'.png')
       AUTO=c.create_image(x,y,image=im)
       workingplace.update()
def changestate(state):
       global workingplace,STATE,AUTO,LOW,HIGH
       STATE=state
       im=tk.PhotoImage(file=STATE+'.png')
       workingplace.itemconfigure(AUTO,image=im)
       workingplace.update()
def bars(c,x,y,exp,maxexp,level,leng=100,color='green',leveltype='basis'):
       global bar
       bar.append(c.create_rectangle(x,y,x+leng*(exp/maxexp),y+20,fill=color,outline=''))
       bar.append(c.create_text(x+leng*(exp/maxexp)-10*(exp/maxexp),y+10,text=leveltype+' level  '+str(level)+'  '+str(exp)+'/'+str(maxexp)))
       bar.append(c)
       bar.append(leveltype)
       bar.append(leng)
       bar.append(x)
       bar.append(y)
       c.update()
       return len(bar)//7
def updatebar(n,exp,maxexp,level):
       global bar
       try:
              leveltype=bar[n*7-4]
              c=bar[n*7-5]
              color=c.itemcget(bar[n*7-7],'fill')
              c.delete(bar[n*7-7])
              c.delete(bar[n*7-6])
              x=bar[n*7-2]
              y=bar[n*7-1]
              leng=bar[n*7-3]
              bar[n*7-7]=(c.create_rectangle(x,y,x+leng*(exp/maxexp),y+20,fill=color,outline=''))
              bar[n*7-6]=(c.create_text(x+leng*(exp/maxexp)-10*(exp/maxexp),y+10,text=leveltype+' level  '+str(level)+'  '+str(exp)+'/'+str(maxexp)))
              bar[n*7-5]=(c)
              bar[n*7-4]=(leveltype)
              bar[n*7-3]=(leng)
              bar[n*7-2]=(x)
              bar[n*7-1]=(y)
              c.update()
              return len(bar)//7
       except:
              return 1
def sys_chat(r,c):
       def create_image(root,canvas,x1, y1, x2, y2, **kwargs):
            a=0
            images=[]
            b =0
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = root.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                images.append(ImageTk.PhotoImage(image))
                a=canvas.create_image(x1, y1, image=images[-1], anchor='nw')
            b=canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
            return a,b
       create_image(r,c,0,300,50,600,fill='red',alpha=.5)
                     
