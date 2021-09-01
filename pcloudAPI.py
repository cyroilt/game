
import requests
import time
from io import BytesIO
import json as happiness
import random
import crypt
import hashlib
nick,passw=0,0
serv=''
files=[]
myname=''
def json(n):
    q=str(n)
    q= q.split(',')
    a=[]
    a1=dict()
    for i in q:
        n=i.replace('{','').replace('}','').replace("'",'')
        n=n.split(':')
        a.append(n)
    for i in a:
        a1[i[0]]=i[1]
    a=a1
    return a
class pcloud():
    def login(nickname,password,server='e'):#server 'e'-europe,''-other
        global nick,passw,serv
        nick=nickname
        passw=password
        serv=server
    def currentserver():
        global serv
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/currentserver')
        return info.json()
    def getapiserver():
        global serv
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/getapiserver')
        return info.json()
    def get_ip():
        global serv
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/getip')
        return info.json()
#working with file
    def stat(path,filename):#path example '/ch' filename example '/changelog.txt'
        global serv,nick,passw
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/stat?username='+nick+'&password='+passw+'&path='+path+'&name='+filename)
        return info.json()
    
    def open(path,flag):#flags are w w+ e
        global serv,nick,passw,files
        files.append(path)
        
        flag=flag.replace('w+','0x0400').replace('e','0x0040').replace('w','0x0002')
        files.append(flag)
        
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/file_open?username='+nick+'&password='+passw+'&path='+path+'&flags='+flag)
        print(info.json())
        files.append(info.json()['fd'])
        
        return files[-1]
    def get_size(fd):
        global serv,nick,passw,files
        path=files[files.index(fd)-2]
        flag=files[files.index(fd)-1]
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/file_open?username='+nick+'&password='+passw+'&path='+path+'&flags='+flag)
        fd= json(info.json())[' fd'][1:]
        addr='https://'+serv+'api.pcloud.com/file_size?username='+nick+'&password='+passw+'&fd='+fd
        info=session.post(addr)
        return info.json()['size']
    def close(fd):
        global serv,nick,passw,files
        files=files[files.index(fd)-2:files.index(fd)]
    def read(fd):
        global serv,nick,passw,files
        path=files[files.index(fd)-2]
        flag=files[files.index(fd)-1]
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/file_open?username='+nick+'&password='+passw+'&path='+path+'&flags='+flag)
        fd= info.json()['fd']
        info=session.post('https://'+serv+'api.pcloud.com/file_read?username='+nick+'&password='+passw+'&fd='+str(fd)+'&count='+str(pcloud.get_size(fd)))
        return info.content.decode('utf-8')
    
    def write(fd,text):
        global serv,nick,passw,files
        path=files[files.index(fd)-2]
        flag=files[files.index(fd)-1]
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/file_open?username='+nick+'&password='+passw+'&path='+path+'&flags='+flag)
        fd= info.json()['fd']
        if type(text)!=bytes:
            info=session.post('https://'+serv+'api.pcloud.com/file_write',files={'me.txt':text.encode('utf-8')},data={'username':nick,'password':passw,'fd':fd})
        else:
            info=session.post('https://'+serv+'api.pcloud.com/file_write',files={'me.txt':text},data={'username':nick,'password':passw,'fd':fd})
        return info.json()
    def clear(fd):
        global serv,nick,passw,files
        path=files[files.index(fd)-2]
        flag=files[files.index(fd)-1]
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/file_open?username='+nick+'&password='+passw+'&path='+path+'&flags='+flag)
        fd= json(info.json())[' fd'][1:]
        info=session.post('https://'+serv+'api.pcloud.com/file_truncate?username='+nick+'&password='+passw+'&fd='+str(fd)+'&length=0')
# working with folder
    def create(path,name):
        global serv,nick,passw
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/createfolder?username='+nick+'&password='+passw+'&path='+path+'/'+name)
        return info.json()
    def list_users():
        global serv,nick,passw
        users=[]
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/listfolder?username='+nick+'&password='+passw+'&path=/main')
        for i in info.json()['metadata']['contents']:
            users.append(i['name'])
        return users
    def delete_file(path):
        global serv,nick,passw
        session = requests.Session()
        info=session.post('https://'+serv+'api.pcloud.com/deletefile?username='+nick+'&password='+passw+'&path='+path)
        return info.json()
def check(name):
    users=pcloud.list_users()
    if name in users:
        a=name+str(random.randint(1,4500))
        a=check(a)
        return a
    else:
        return name
def new_player(name,email,password):
    global myname 
    name=check(name)
    pcloud.create('/main',name)
    a=pcloud.open('/main/'+name+'/save.autosave','e')
    pcloud.close(a)
    try:
        f=pcloud.open('/main/associations.names','w+')
    except:
        f=pcloud.open('/main/associations.names','e')
        pcloud.close(f)
        f=pcloud.open('/main/associations.names','w+')
    pcloud.write(f,name+' '+email+' ')
    pcloud.close(f)
    f=pcloud.open('/main/'+name+'/info.data','e')
    pcloud.close(f)
    pcloud.open('/main/'+name+'/info.data','w+')
    pcloud.write(f,password)
    myname=name
    return name
def get_data():
    global myname
    pcloud.login('alqholder@gmail.com','PC0erF0lX9cDG2')
    f=pcloud.open('/main/'+hashlib.sha3_384(myname.encode()).hexdigest()+'/dat.autosave','w+')
    key=pcloud.read(f)
    pcloud.close(f)
    pcloud.login('alqservru@gmail.com','ur1IAbg1Kt6Xp5')
    f=pcloud.open('/main/'+myname+'/save.autosave','w+')
    print(key.encode())
    return crypt.crypto.decrypt(pcloud.read(f).encode(),key)
def login(name,password):
    global myname
    if name.find('@')==-1:
        f=pcloud.open('/main/'+name+'/info.data','w+')
        q=pcloud.read(f)
        pcloud.close(f)
        if q==password:
            myname=name
            return myname
        else:
            return 'password_incorrect'
    else:
        qq=pcloud.open('/main/associations.names','w+')
        a=pcloud.read(qq).split()
        x=a.index(name)
        pcloud.close(qq)
        f=pcloud.open('/main/'+a[x-1]+'/info.data','w+')
        q=pcloud.read(f)
        pcloud.close(f)
        name=a[x-1]
        if q==password:
            myname= name
            return myname
        else:
            return 'password_incorrect'
def login_get():
    global myname
    return myname
