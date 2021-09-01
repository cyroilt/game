import json
#data1=json.dumps({'building':{'money':10,'human':1},'working':{'woktype':'wc','resource':'forest','use1':'instruments 1','use2':'meal 1','resuse':1,'result':'wood 1'},'skin':'wc.png'})
#data2=json.dumps({'building':{'money':10,'wood':3,'human':1},'working':{'woktype':'frsr','resource':'forest','use1':'instruments 1','use2':'meal 1','resuse':-1,'result':'wood 0'},'skin':'forester.png'})
#data3=json.dumps({'building':{'money':6,'human':1},'working':{'woktype':'tsm','resource':'tsm','use1':'wood 1','use2':'meal 1','resuse':0,'result':'tools 1'},'skin':'toolsmaker.png'})
#f=open('recepies.json','w')
#f.write(data1+'\n'+data2+'\n'+data3)
#f.close()
def self_run():
    f=open('recepies.json','r+')
    data=f.read().split('\n')
    associations={'woodcutter':json.loads(data[0]),'forester':json.loads(data[1]),'tools maker':json.loads(data[2])}
    f.close()
    return associations
