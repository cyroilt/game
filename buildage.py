from tkinter import*
from resources import*
from mytools import *
from math import*
from people import human
from threading import Thread
from environmennt import forest,stones
import resources
woodcutters=[]
foresters=[]

o,o1,o2=0,0,0
x1,y1=0,0
linesto=0
linefor=0
textsto=0
peoprocess=[]
textfor=0
houses=[]
tsms=[]
stc=[]
qc=''
'''
--------------------------------
3 lvl = tooksmaker
4 lvl = house
*5lvl = stone mine, mason


--------------------------------
*
5lvl=arrower
'''
def get(name):
       global woodcutters,foresters,o,tsms,stc,qc,houses
       if name=='wc':
              return woodcutters
       elif name=='fst':
              return foresters
       elif name=='tsm':
              return tsms
       elif name=='house':
              return houses
       else:
              return stc
def get_all():
       returning='{ '
       for i in woodcutters:
              
                     for q in qc.coords(i):
                            returning+=str(q)+" "
       returning+='} '
       returning+=' { '
       for i in foresters:
              
                     for q in qc.coords(i):
                            returning+=str(q)+" "
       returning+='} '
       returning+=' { '
       for i in houses:
              
                     for q in qc.coords(i):
                            returning+=str(q)+" "
       returning+='} '
       returning+=' { '
       for i in tsms:
              
                     for q in qc.coords(i):
                            returning+=str(q)+" "
       returning+='} '
       returning+=' { '
       for i in stc:
              
                     for q in qc.coords(i):
                            returning+=str(q)+" "
       returning+='}'
       return returning
def run(c,resourceplace,wcs,fsts,hs,tsmss,stcs):
       global woodcutters,foresters,o,tsms,stc,qc,peoprocess
       qc=c
       for i in range(0,len(wcs)-3,4):
              woodcutters.append(c.create_rectangle(wcs[i],wcs[i+1],wcs[i+2],wcs[i+3],fill="brown",tag='woodcut'))
              peoprocessx=(Thread(target=human.born,args=(c,"woodcut",'forest',resourceplace,wood,1,forest,1,instruments,1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       for i in range(0,len(fsts)-3,4):
              foresters.append(c.create_rectangle(fsts[i],fsts[i+1],fsts[i+2],fsts[i+3],fill="darkgreen",tag='forester'))
              peoprocessx=(Thread(target=human.born,args=(c,"forester",'forest',resourceplace,wood,0,forest,-1,instruments,-1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       for i in range(0,len(stcs)-3,4):
              stc.append(c.create_rectangle(stcs[i],stcs[i+1],stcs[i+2],stcs[i+3],fill="grey90",tag='stc'))
              peoprocessx=(Thread(target=human.born,args=(c,"stc",'stone',resourceplace,stone,1,stones,1,instruments,1),kwargs={'time1':2,"time2":3}))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       for i in range(0,len(tsmss)-3,4):
              tsms.append(c.create_rectangle(tsmss[i],tsmss[i+1],tsmss[i+2],tsmss[i+3],fill="grey30",tag='tsm'))
              peoprocessx=(Thread(target=human.born,args=(c,"tsm",'tsm',resourceplace,wood,-1,forest,0,instruments,-1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       for i in range(0,len(hs)-3,4):
              houses.append(c.create_rectangle(hs[i],hs[i+1],hs[i+2],hs[i+3],fill="red",tag='house'))
              peoprocessx=(Thread(target=human.born,args=(c,"house",'stone',resourceplace,people,1,stones,0,instruments,0),kwargs={'time1':15,"time2":-5}))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
def creation_basic(c,resourceplace,basislevel,l):
       global woodcutters,foresters,o,tsms,stc,qc
       qc=c
       
       def stop1(e): #-woodcuter.stop--------------------------------------------------------------------------------------------------------------------------
              global o,x1,y1,linesto,linefor,textsto,textfor,peoprocess
              c.unbind('<Motion>')
              money.change(-10)
              freepeople.change(-1)
              labels_upd(resourceplace,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(resources.stone.get()))
              c.unbind('<Button-2>')
              c.delete(textfor)
              c.delete(textsto)
              c.delete(linefor)
              c.delete(linesto)
              o=0
              levels.changebasis(50)
              peoprocessx=(Thread(target=human.born,args=(c,"woodcut",'forest',resourceplace,wood,1,forest,1,instruments,1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       def mo1(e):#-woodcuter.mo--------------------------------------------------------------------------------------------------------------------------
              global o,x1,y1,linesto,linefor,textsto,textfor
              if o==0:
                     x1,y1=e.x,e.y
                     o=1
                     woodcutters.append(c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="brown",tag='woodcut'))
                     mini=human.findnearest(c,woodcutters[len(woodcutters)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,woodcutters[len(woodcutters)-1],'forest')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to forest'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
              else:
                     aaaa=woodcutters[len(woodcutters)-1]
                     woodcutters[len(woodcutters)-1]=c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="brown",tag='woodcut')
                     c.delete(aaaa)
                     c.delete(linesto)
                     c.delete(linefor)
                     c.delete(textsto)
                     c.delete(textfor)
                     x1,y1=e.x,e.y
                     mini=human.findnearest(c,woodcutters[len(woodcutters)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,woodcutters[len(woodcutters)-1],'forest')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to forest'+str(round(sqrt(abs(int(min1)^2)+abs(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
       def stop2(e):#-forester.stop--------------------------------------------------------------------------------------------------------------------------
              global o1,x1,y1,linesto,linefor,textsto,textfor,peoprocess
              c.unbind('<Motion>')
              money.change(-10)
              freepeople.change(-1)
              wood.change(-3)
              labels_upd(resourceplace,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(resources.stone.get()))
              c.unbind('<Button-2>')
              c.delete(textfor)
              c.delete(textsto)
              c.delete(linefor)
              c.delete(linesto)
              o1=0
              levels.changebasis(100)
              peoprocessx=(Thread(target=human.born,args=(c,"forester",'forest',resourceplace,wood,0,forest,-1,instruments,-1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       def mo2(e):#-forester.mo--------------------------------------------------------------------------------------------------------------------------
              global o1,x1,y1,linesto,linefor,textsto,textfor
              if o1==0:
                     x1,y1=e.x,e.y
                     o1=1
                     foresters.append(c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="darkgreen",tag='forester'))
                     mini=human.findnearest(c,foresters[len(foresters)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,foresters[len(foresters)-1],'forest')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to forest'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
              else:
                     aaaa=foresters[len(foresters)-1]
                     foresters[len(foresters)-1]=c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="darkgreen",tag='forester')
                     c.delete(aaaa)
                     c.delete(linesto)
                     c.delete(linefor)
                     c.delete(textsto)
                     c.delete(textfor)
                     x1,y1=e.x,e.y
                     mini=human.findnearest(c,foresters[len(foresters)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,foresters[len(foresters)-1],'forest')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to forest'+str(round(sqrt(abs(int(min1)^2)+abs(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
       def stop3(e):#-toolsmakerstop--------------------------------------------------------------------------------------------------------------------------
              global o2,x1,y1,linesto,linefor,textsto,textfor,peoprocess
              c.unbind('<Motion>')
              money.change(-6)
              freepeople.change(-1)
              labels_upd(resourceplace,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(resources.stone.get()))
              c.unbind('<Button-2>')
              c.delete(textfor)
              c.delete(textsto)
              c.delete(linefor)
              c.delete(linesto)
              o2=0
              levels.changebasis(150)
              peoprocessx=(Thread(target=human.born,args=(c,"tsm",'tsm',resourceplace,wood,-1,forest,0,instruments,-1)))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       def mo3(e):#-toolsmaker.mo--------------------------------------------------------------------------------------------------------------------------
              global o2,x1,y1,linesto,linefor,textsto,textfor
              if o2==0:
                     x1,y1=e.x,e.y
                     o2=1
                     tsms.append(c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="grey9",tag='tsm'))
                     mini=human.findnearest(c,tsms[len(tsms)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))

                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     
              else:
                     aaaa=tsms[len(tsms)-1]
                     tsms[len(tsms)-1]=c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="grey30",tag='tsm')
                     c.delete(aaaa)
                     c.delete(linesto)
                     c.delete(textsto)
                     x1,y1=e.x,e.y
                     mini=human.findnearest(c,tsms[len(tsms)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
       def stop4(e):#-stonecutter.stop--------------------------------------------------------------------------------------------------------------------------
              global o2,x1,y1,linesto,linefor,textsto,textfor,peoprocess
              c.unbind('<Motion>')
              money.change(-3)
              freepeople.change(-1)
              wood.change(-10)
              labels_upd(resourceplace,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(resources.stone.get()))
              c.unbind('<Button-2>')
              c.delete(textfor)
              c.delete(textsto)
              c.delete(linefor)
              c.delete(linesto)
              o2=0
              levels.changebasis(100)
              peoprocessx=(Thread(target=human.born,args=(c,"stc",'stone',resourceplace,stone,1,stones,1,instruments,1),kwargs={'time1':2,"time2":3}))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       def mo4(e):#-house.mo--------------------------------------------------------------------------------------------------------------------------
              global o2,x1,y1,linesto,linefor,textsto,textfor
              if o2==0:
                     x1,y1=e.x,e.y
                     o2=1
                     stc.append(c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="grey9",tag='stc'))
                     mini=human.findnearest(c,stc[len(stc)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,stc[len(stc)-1],'stone')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to stones'+str(round(sqrt(abs(int(min1)^2)+abs(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
              else:
                     aaaa=stc[len(stc)-1]
                     stc[len(stc)-1]=c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="grey90",tag='stc')
                     c.delete(aaaa)
                     c.delete(linesto)
                     c.delete(textsto)
                     c.delete(linefor)
                     c.delete(textfor)
                     x1,y1=e.x,e.y
                     mini=human.findnearest(c,stc[len(stc)-1],'storage')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linesto=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textsto=c.create_text(x1-30,y1-30,text='to storage'+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")
                     mini=human.findnearest(c,stc[len(stc)-1],'stone')
                     min1=c.coords(mini)[0]
                     min2=c.coords(mini)[1]
                     linefor=c.create_line(x1,y1,c.coords(mini)[0],c.coords(mini)[1],dash=(5,2))
                     textfor=c.create_text(x1+30,y1+30,text='to stones'+str(round(sqrt(abs(int(min1)^2)+abs(int(min2)^2)),2))+" meters"+" ~"+str(round(sqrt(int(int(min1)^2)+int(int(min2)^2))/30,2))+" minutes",font="Arial 10")

       def stop5(e):#-house.stop--------------------------------------------------------------------------------------------------------------------------     
              global o2,x1,y1,linesto,linefor,textsto,textfor,peoprocess
              c.unbind('<Motion>')
              stone.change(-2)
              people.change(1)
              wood.change(-8)
              labels_upd(resourceplace,people.get(),int(freepeople.get()),int(money.get()),int(wood.get()),int(resources.stone.get()))
              c.unbind('<Button-2>')
              o2=0
              levels.changebasis(100)
              peoprocessx=(Thread(target=human.born,args=(c,"house",'stone',resourceplace,people,1,stones,0,instruments,0),kwargs={'time1':15,"time2":-5,'res2':resources.money,'res2am':round(resources.happieness.get()/100)}))
              peoprocess.append(peoprocessx)
              peoprocessx.start()
       def mo5(e):#-stonecutter.mo--------------------------------------------------------------------------------------------------------------------------
              global o2,x1,y1,linesto,linefor,textsto,textfor
              if o2==0:
                     x1,y1=e.x,e.y
                     o2=1
                     houses.append(c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="grey9",tag='house'))
              else:
                     aaaa=houses[len(houses)-1]
                     houses[len(houses)-1]=c.create_rectangle(x1,y1,x1+(20*scale.get()),y1+(20*scale.get()),fill="red",tag='house')
                     c.delete(aaaa)
                     x1,y1=e.x,e.y
       def woodcutter():
              if money.get()>=10 and freepeople.get()>=1:
                     menu.destroy()
                     c.bind('<Motion>',mo1)
                     c.bind('<Button-2>',stop1)
       def forester():
              if money.get()>=10 and freepeople.get()>=1 and wood.get()>=3:
                     menu.destroy()
                     c.bind('<Motion>',mo2)
                     c.bind('<Button-2>',stop2)
       def toolsm():
              if money.get()>=3 and freepeople.get()>=1:
                     menu.destroy()
                     c.bind('<Motion>',mo3)
                     c.bind('<Button-2>',stop3)
       def stonema():
              if money.get()>=3 and freepeople.get()>=1 and wood.get()>=10:
                     menu.destroy()
                     c.bind('<Motion>',mo4)
                     c.bind('<Button-2>',stop4)
       def homa():
              if wood.get()>=8 and stone.get()>=2:
                     menu.destroy()
                     c.bind('<Motion>',mo5)
                     c.bind('<Button-2>',stop5)       
       if levels.getbasis()>=1:
              menu=Tk()
              wola=Label(menu,text='woodcutter: 10 money, 1 human')
              wola.pack()
              wola.place(x=0,y=0)
              woocu=Button(menu,text="build woodcutter house",command=woodcutter)
              woocu.pack()
              woocu.place(x=0,y=30)
              if levels.getbasis()>=2:
                     forla=Label(menu,text='forestry: 10 money, 1 human, 3 wood')
                     forla.pack()
                     forla.place(x=190,y=0)
                     forocu=Button(menu,text="build forestry",command=forester)
                     forocu.pack()
                     forocu.place(x=190,y=30)
                     if levels.getbasis()>=3:
                            tmla=Label(menu,text='tools maker: 6 money, 1 human')
                            tmla.pack()
                            tmla.place(x=0,y=70)
                            tmocu=Button(menu,text="build tools maker house",command=toolsm)
                            tmocu.pack()
                            tmocu.place(x=0,y=100)
                            if levels.getbasis()>=4:
                                   smla=Label(menu,text='stone cutter: 3 money, 1 human, 10 wood')
                                   smla.pack()
                                   smla.place(x=190,y=70)
                                   smcu=Button(menu,text="build stone cutter house",command=stonema)
                                   smcu.pack()
                                   smcu.place(x=190,y=100)
                                   hla=Label(menu,text='house: 2 stone, 8 wood')
                                   hla.pack()
                                   hla.place(x=0,y=140)
                                   hcu=Button(menu,text="build a house",command=homa)
                                   hcu.pack()
                                   hcu.place(x=0,y=170)
