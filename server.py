
from datetime import*
from resources import*
import buildage
import environmennt
import time
from pcloudAPI import*
from threading import Thread
from crypt import *
import hashlib
import mytools
fj=True
def datacollector(save=False,oncloud=True):
    data='{ '
    for i in get_all():
            data+=str(i)+" "
    data+="} { "
    for i in environmennt.get_all():
        data+='[ '+str(len(i))+" ] "
        for j in i:
            if type(j)==list:
                for m in j:
                    data+=str(m)+" "
            else:
                data+=str(j)+" "
    data+="}"
    data+=" "+buildage.get_all()
    if save==False:
        return data
    else:
        if oncloud==True:
            pcloud.login('alqholder@gmail.com','PC0erF0lX9cDG2')
            pcloud.create('/main',hashlib.sha3_384(login_get().encode()).hexdigest())
            f=pcloud.open('/main/'+hashlib.sha3_384(login_get().encode()).hexdigest()+'/dat.autosave','e')
            pcloud.close(f)
            f=pcloud.open('/main/'+hashlib.sha3_384(login_get().encode()).hexdigest()+'/dat.autosave','w')
            pcloud.clear(f)
            key=crypto.gen_nkey()
            pcloud.write(f,key)
            pcloud.close(f)
            pcloud.login('alqservru@gmail.com','ur1IAbg1Kt6Xp5')
            f=pcloud.open('/main/'+login_get()+'/save.autosave','w')
            pcloud.write(f,crypto.encrypt(data,key))
            time.sleep(1)
        else:
            f=open("save.autosave",'w')
            f.write(data)
def firstjoin_get():
    global fj
    return fj
def firstjoin():
    pass
def fjs(f):
    global fj
    fj=f
def cycle(**kwargs):
    while True:
        datacollector(kwargs)
        for i in range(60*100):
            time.sleep(0.01)
        print('sync is done')
def myloop(**kwargs):
    configuration=Thread(target=cycle,kwargs=(kwargs))
    configuration.start()
def inter(lista):
    for i in range (len(lista)):
        lista[i]=int(lista[i])
    return lista
def parinter(lista):
    for i in range (0,len(lista)):
        lista[i][0],lista[i][1]=int(lista[i][0]),int(lista[i][1])
    return lista
def makepares(l):
    ql=[]
    for i in range(0,len(l)-1,2):
        ql.append([l[i],l[i+1]])
    return ql
def configure(oncloud=False):
     if oncloud==True:
         obj1=[]
         alldat=get_data().split()
         obj=[]
         first=0
         level=[]
         second=0
         for i in range (len(alldat)):
             if alldat[i]=='{':
                 first=i
             elif alldat[i]=='}':
                obj.append(alldat[first+1:i])
         wood.set(int(obj[0][0]))
         stone.set(int(obj[0][1]))
         money.set(int(obj[0][2]))
         instruments.set(int(obj[0][3]))
         levels.changebasis(int(obj[0][4]))
         people.set(int(obj[0][5]))
         freepeople.set(int(obj[0][6]))
         meal.set(int(obj[0][7]))
         forestcoords=[]
         
         for i in range(len(obj[1])):
            if obj[1][i]==']':
                level.append(int(obj[1][i-1]))
         forestcoords=obj[1][3:level[0]*2+3]
         forestcoords=makepares(forestcoords)
         forestload=obj[1][level[0]*2+6:level[0]*2+level[1]+6]
         forestloadmax=obj[1][level[0]*2+level[1]+9:level[0]*2+level[2]+level[1]+9]
         stonecoords=obj[1][level[0]*2+level[2]+level[1]+12:level[0]*2+level[2]+level[1]+level[3]*2+12]
         stonecoords=makepares(stonecoords)
         stoneload=obj[1][level[0]*2+level[2]+level[1]+level[3]*2+15:level[0]*2+level[2]+level[1]+level[3]*2+15+level[4]]
         stoneloadmax=obj[1][level[0]*2+level[2]+level[1]+level[3]*2+18+level[4]:level[0]*2+level[2]+level[1]+level[3]*2+18+level[4]+level[5]]
         environmennt.forest.load(parinter(forestcoords),inter(forestload),inter(forestloadmax))
         environmennt.stones.load(parinter(stonecoords),inter(stoneload),inter(stoneloadmax))
         return obj[2],obj[3],obj[4],obj[5],obj[6]

     else:
         f=open("save.autosave",'r+')
         alldat=f.read().split()
         obj=[]
         first=0
         level=[]
         second=0
         for i in range (len(alldat)):
             if alldat[i]=='{':
                 first=i
             elif alldat[i]=='}':
                obj.append(alldat[first+1:i])
         wood.set(int(obj[0][0]))
         stone.set(int(obj[0][1]))
         money.set(int(obj[0][2]))
         instruments.set(int(obj[0][3]))
         levels.changebasis(int(obj[0][4]))
         people.set(int(obj[0][5]))
         freepeople.set(int(obj[0][6]))
         forestcoords=[]
         
         for i in range(len(obj[1])):
            if obj[1][i]==']':
                level.append(int(obj[1][i-1]))
         forestcoords=obj[1][3:level[0]*2+3]
         forestcoords=makepares(forestcoords)
         forestload=obj[1][level[0]*2+6:level[0]*2+level[1]+6]
         forestloadmax=obj[1][level[0]*2+level[1]+9:level[0]*2+level[2]+level[1]+9]
         stonecoords=obj[1][level[0]*2+level[2]+level[1]+12:level[0]*2+level[2]+level[1]+level[3]*2+12]
         stonecoords=makepares(stonecoords)
         stoneload=obj[1][level[0]*2+level[2]+level[1]+level[3]*2+15:level[0]*2+level[2]+level[1]+level[3]*2+15+level[4]]
         stoneloadmax=obj[1][level[0]*2+level[2]+level[1]+level[3]*2+18+level[4]:level[0]*2+level[2]+level[1]+level[3]*2+18+level[4]+level[5]]
         environmennt.forest.load(parinter(forestcoords),inter(forestload),inter(forestloadmax))
         environmennt.stones.load(parinter(stonecoords),inter(stoneload),inter(stoneloadmax))
         return obj[2],obj[3],obj[4],obj[5],obj[6]
