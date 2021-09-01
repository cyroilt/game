from tkinter import*
import resources as res
from math import*
from time import*
from environmennt import*
from mytools import *
from humanstate import*
peopl=[]
def pifagor(a,b):
    return sqrt(int(a)**2+int(b)**2)
class human():

  def findnearest(c,t1,t2):
                     x=c.coords(t1)[0]
                     y=c.coords(t1)[1]
                     mx=200000
                     my=200000
                     mi=-1

                     for i in c.find_withtag(t2):
                            if abs(x-c.coords(i)[0])<mx and abs(y-c.coords(i)[1])<my:
                                   mx=abs(x-c.coords(i)[0])
                                   my=abs(y-c.coords(i)[1])
                                   mi=i
                     return mi
  def motion(c,ob,frm,to):
              time= sqrt((c.bbox(frm)[0]-c.bbox(to)[0])**2+(c.bbox(frm)[1]-c.bbox(to)[1])**2)
              for i in range(round(time)):

                     sleep(0.01)
                     time= sqrt((c.bbox(frm)[0]-c.bbox(to)[0])**2+(c.bbox(frm)[1]-c.bbox(to)[1])**2)
                     c.move(ob,(c.bbox(to)[0]-c.bbox(frm)[0])/(time),(c.bbox(to)[1]-c.bbox(frm)[1])/(time))
                     c.update()
  def born(c,tag,destiny,pb,resource,ch,thing,chre,using,usingn,usingadd=0,usingnadd=0,time1=0,time2=0,res2=None,re2am=1):
    last=c.find_withtag('storage')[len(c.find_withtag('storage'))-1]
    last2=c.find_withtag(tag)[len(c.find_withtag(tag))-1]
    last3=human.findnearest(c,last2,destiny)
    x=c.coords(last)[0]
    y=c.coords(last)[1]
    x1=c.coords(last2)[0]
    y1=c.coords(last2)[1]
    x2=c.coords(last3)[0]
    y2=c.coords(last3)[1]
    nnnn=getcurrent()
    set_sleeping(nnnn,True)
    me=c.create_oval(x,y,x+5,y+5,tag=tag,fill='pink')
    using.change(-1*usingn)
    qqq=0
    if usingadd==0:
      pass
    else:
      usingadd.change(-1*usingnadd)

    while True:
      if get_sleeping(nnnn)==True:
        human.motion(c,me,last,last2)
        qqq=0
        human.motion(c,me,last2,last3)
        for i in range(1000+time1*100):
          sleep(0.01)
          c.update()
        if chre!=0:
          thing.cut(thing.ggget().index(last3),chre)
        human.motion(c,me,last3,last2)
        for i in range(500+time2*100):
          sleep(0.01)
          c.update()
        human.motion(c,me,last2,last)
        if res2!=None:
            res2.change(re2am)
        resource.change(ch)
        using.change(-1*usingn)
        if usingadd==0:
          pass
        else:
          usingadd.change(-1*usingnadd)
        labels_upd(pb,res.people.get(),res.freepeople.get(),res.money.get(),res.wood.get(),res.stone.get())

      else:
        if qqq==0:
          human.motion(c,me,me,last)
          qqq=1
        else:
          pass
