from payton.scene.controller import GUIController
import sdl2
from functools import partial
specialkeys={'F1':sdl2.SDLK_F1,
'F2':sdl2.SDLK_F2,
'F3':sdl2.SDLK_F3,
'F4':sdl2.SDLK_F4,
'F5':sdl2.SDLK_F5,
'F6':sdl2.SDLK_F6,
'F7':sdl2.SDLK_F7,
'F8':sdl2.SDLK_F8,
'F9':sdl2.SDLK_F9,
'F10':sdl2.SDLK_F10,
'F11':sdl2.SDLK_F11,
'F12':sdl2.SDLK_F12,
'CTRL_L':sdl2.SDLK_LCTRL,
'CTRL_R':sdl2.SDLK_RCTRL,
'SPACE':sdl2.SDLK_SPACE,
'SHIFT_L':sdl2.SDLK_LSHIFT,
'SHIFT_R':sdl2.SDLK_RSHIFT,
'DELETE':sdl2.SDLK_DELETE,
'TAB':sdl2.SDLK_TAB,
'UP':sdl2.SDLK_UP,
'DOWN':sdl2.SDLK_DOWN,
'LEFT':sdl2.SDLK_LEFT,
'RIGHT':sdl2.SDLK_RIGHT,
'ALT_L':sdl2.SDLK_LALT,
'ALT_R':sdl2.SDLK_RALT,
'ESCAPE':sdl2.SDLK_ESCAPE,
'KEY':None
}
additionaly=[]
grule=[]
binded=0
gfunc=[]
gret=[]
class event(GUIController):

            def keyboard(event, scene_1, *arg):
                    global grule,gfunc

                    if event.type == sdl2.SDL_QUIT:
                        scene_1.terminate()
                        for i in additionaly:
                            if i!=0:
                                i.destroy()
                        return True
                    tx=''
                    try:
                        tx=event.text.text.decode('utf-8')
                    except:
                        pass

                    ggrule=('')
                    if tx!='':
                        check=False
                        for i in grule:
                            try:
                                if tx==i[2]:

                                 check=True
                                 cm=gfunc[grule.index(i)]
                                 ggrule=i
                            except :
                                pass
                    try:
                        if event.key.keysym.sym!='':
                            for i in grule:
                                try:

                                    if event.key.keysym.sym==specialkeys[i[2]]:
                                     check=True
                                     cm=gfunc[grule.index(i)]
                                     ggrule=i
                                except Exception as e:
                                        pass


                    except:
                        pass
                    if len(ggrule)==3 and ggrule[1]=='Press' and check==True:
                           if gret[grule.index(i)]==True:
                                cm(event)
                           else:
                                cm()
                    elif len(ggrule)==3 and ggrule[1]=='Spec' and check==True:
                            if gret[grule.index(i)]==True:
                                cm(event)
                            else:
                                cm()

            def mouse(event, scene_1, *arg):
                for i in grule:
                    if len(i)==1:
                        if event.type==i[0]:
                            if gret[grule.index(i)]==True:
                                gfunc[grule.index(i)](event)
                            else:
                                gfunc[grule.index(i)]()
                    else:
                        if event.type==i[1] and event.button.button==i[0]:
                            if gret[grule.index(i)]==True:
                                gfunc[grule.index(i)](event)
                            else:
                                gfunc[grule.index(i)]()


            def set(rule,func,ret):
                global grule,gfunc,gret
                grule.append(rule)
                gfunc.append(func)
                gret.append(ret)
def cgh():
    global binded
    binded=1
class bind():
    global binded
    scene_11=0
    grule=''
    gfunc=''
    def __init__(self,scene,rule,withreturn=False,func=' 123',additional=0):
        global additionaly,grule
        scene_11=0
        mgrule=''
        scene_11=scene
        self.scene=scene
        self.func=func
        if rule.find('Mouse')!=-1:
            if rule.find('B1')!=-1:
                if rule.find('Motion')!=-1:
                    mgrule=(sdl2.SDL_BUTTON_LMASK,sdl2.SDL_MOUSEMOTION)
                else:
                    mgrule=(sdl2.SDL_BUTTON_LMASK,sdl2.SDL_MOUSEBUTTONDOWN)
            if rule.find('B2')!=-1:
                if rule.find('Motion')!=-1:
                    mgrule=(sdl2.SDL_BUTTON_MMASK,sdl2.SDL_MOUSEMOTION)
                else:
                    grule=(sdl2.SDL_BUTTON_MMASK,sdl2.SDL_MOUSEBUTTONDOWN)
            if rule.find('B3')!=-1:
                if rule.find('Motion')!=-1:
                    mgrule=(sdl2.SDL_BUTTON_RMASK,sdl2.SDL_MOUSEMOTION)
                else:
                    grule=(sdl2.SDL_BUTTON_RMASK,sdl2.SDL_MOUSEBUTTONDOWN)
            if rule.find('Wheel')!=-1:
                mgrule=(sdl2.SDL_MOUSEWHEEL,)
        if rule.find('Key')!=-1:
            symbol=rule.replace('Key','').replace('-','').replace(' ','')
            if not symbol in specialkeys.keys():
                mgrule=('Key','Press',symbol)
            else:
                mgrule=('Key','Spec',symbol)
        mgfunc=func
        if binded==0:
            scene.controller.add_controller(event)
            cgh()
        event.set(mgrule,mgfunc,withreturn)
        additionaly.append(additional)

