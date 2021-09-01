import tkinter as tk
import time
start_color=(0, 255, 0)
end_color=(255,0,0)
nc=start_color
current='s'
a=0
ov=0
class Button1():
       def kill(canvas):
              global ov,a
              canvas.delete(ov)
              canvas.delete(a)
              canvas.unbind('<Double-Button-1>')
       def getstate():
              if current=='s':
                     return 1
              else:
                     return 0
       def init(root='',canvas='',height=250,width=300,x=0,y=0):
              global a,ov
              def rgb(num):
                 b=hex(int(num))[2:]
                 if len(b)==2:
                   return b
                 else:
                   return '0'+b
              def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
                  points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

                  return canvas.create_polygon(points, **kwargs, smooth=True)

              ov = round_rectangle(x, y, width+x, height+y, radius=80,fill='#'+rgb(start_color[0])+rgb(start_color[1])+rgb(start_color[2]))

              a=canvas.create_text(x+width/4,y+height/2,text='on',font='Arial '+str(width//8))
              def change(e):
                global current,start_color,end_color,a
                if current=='s':
                 current=' '
                 for i in range(end_color[0]-start_color[0]):
                  nc=(start_color[0]+i*(end_color[0]-start_color[0])/255,start_color[1]+i*(end_color[1]-start_color[1])/255,start_color[2]+i*(end_color[2]-start_color[2])/255)
                  canvas.itemconfigure(ov,fill='#'+rgb(nc[0])+rgb(nc[1])+rgb(nc[2]))
                  canvas.update()
                  canvas.move(a,(width-(width/2))/end_color[0]-start_color[0],0)
                  time.sleep(0.001)
    
                 current='e'
                 canvas.itemconfigure(a,text='off')
                elif current=='e':
                 current=' '
                 for i in range(end_color[0]-start_color[0]):
                  nc=(end_color[0]+i*(start_color[0]-end_color[0])/255,end_color[1]+i*(start_color[1]-end_color[1])/255,end_color[2]+i*(start_color[2]-end_color[2])/255)
                  canvas.itemconfigure(ov,fill='#'+rgb(nc[0])+rgb(nc[1])+rgb(nc[2]))
                  canvas.update()
                  canvas.move(a,-1*(width-(width/2))/end_color[0]-start_color[0],0)
    
                  time.sleep(0.001)
                 current='s'
                 canvas.itemconfigure(a,text='on')
              canvas.bind('<Double-Button-1>',change)       
