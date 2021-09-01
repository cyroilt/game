import random
forests=[]
forestload=[]
forestmaxload=[]
stones1=[]
stoneload=[]
stonemaxload=[]
frpl=[]
frpl1=[]
class forest():
  def genforest(n,maxgen):
    global forests,forestload,forestmaxload
    for i in range(n):
      forests.append([random.randint(0,maxgen),random.randint(0,maxgen)])
      forestload.append(random.randint(0,500))
    for i in forestload:
      forestmaxload.append(i)
    return forests,forestload
  def load(foresting,forestingl,forestingml):
    global forests,forestload,forestmaxload
    forests=foresting
    forestload=forestingl
    forestmaxload=forestingml
  def getlo():
    global forests,forestload
    return forests,forestload
  def cut(n,i):
    global forestload,forestmaxload
    forestload[n]-=i
  def get(n):
    return forestload[n]
  def stnw(f):
    global frpl
    frpl=f
  def ggget():
    global frpl
    return frpl
  def getmax(n):
     global forestmaxload
     return forestmaxload[n]
class stones():
  def genstone(n,maxgen):
    global stones1,stoneload,stonemaxload
    for i in range(n):
      stones1.append([random.randint(0,maxgen),random.randint(0,maxgen)])
      stoneload.append(random.randint(0,300))
    for i in stoneload:
      stonemaxload.append(i)
    return stones1,stoneload
  def load(stoneing,stoneingl,stoneingml):
    global stones1,stoneload,stonemaxload
    stones1=stoneing
    stoneload=stoneingl
    stonemaxload=stoneingml
  def getlo():
    global stones1,stoneload
    return stones1,stoneload
  def cut(n,i):
    global stoneload,stonemaxload
    stoneload[n]-=i
  def get(n):
    return stoneload[n]
  def stnw(f):
    global frpl1
    frpl1=f
  def ggget():
    global frpl1
    return frpl1
  def getmax(n):
     global stonemaxload
     return stonemaxload[n]
def get_all():
  return forests,forestload,forestmaxload,stones1,stoneload,stonemaxload
