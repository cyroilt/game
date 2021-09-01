sleeping=[]
def get_sleeping(n):
    global sleeping
    return sleeping[n]
def set_sleeping(n,state):
    global sleeping
    if len(sleeping)-1>n:
        sleeping[n]=state
    else:
        sleeping.append(state)
def getcurrent():
    global sleeping
    return len(sleeping)-1
