def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)

    mixer.music.set_volume(0.4)
    ProgressbarVolumn['value']=40
    ProgressbarVolumnLabel['text']='40%'
    mixer.music.play()
    audiostatusLabel.configure(text='playing...........')



def pausemusic():
    mixer.music.pause()
    root.pauseButton.grid_remove()
    root.ResumeButton.grid()
    audiostatusLabel.configure(text='paused...........')


def resumemusic():
    root.ResumeButton.grid_remove()
    root.pauseButton.grid()
    mixer.music.unpause()
    audiostatusLabel.configure(text='playing...........')



def volumnup():
    vol=mixer.music.get_volume()

    mixer.music.set_volume(vol + 0.05)
    ProgressbarVolumnLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolumn['value']=mixer.music.get_volume()*100




def volumndown():
    vol=mixer.music.get_volume()

    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumnLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolumn['value']=mixer.music.get_volume()*100
    mixer.music.set_volume(vol - 0.1)


def stopmusic():
    mixer.music.stop()
    audiostatusLabel.configure(text='stopped...........')


def mutemusic():
    global currentval
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    currentval=mixer.music.get_volume()
    mixer.music.set_volume(0)


def unmutemusic():
    global currentval
    root.unmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentval)





###################################################################################to open file browser from search buttom
def musicurl():
    try:
        dd=filedialog.askopenfilename(initialdir='D:\swarup\music',title='select audio file',filetype=(('Mp3',
                                             '.*mp3'),('wav','*.wav')))
    except:
        dd=filedialog.askopenfilename(title='select audio file',filetype=(('Mp3',
                                             '.*mp3'),('wav','*.wav')))
    audiotrack.set(dd)







def createwidthes():
    #global implay
    global audiostatusLabel,ProgressbarVolumnLabel,ProgressbarVolumn,ProgressbarLabe
    #################################################################################################image add
    #implay=PhotoImage(file='play.png')


    #################################################################################################change size of image
    #implay=implay.subsample(1,0)


    #################################################################################### Label method
    trackLabel=Label(root,text='select audio track:',bg='deep sky blue',font=('arial',20,'italic bold'),fg='snow')
    trackLabel.grid(row=0,column=0,padx=20,pady=20)

    audiostatusLabel=Label(root,text='',bg='deep sky blue',font=('arial',20,'italic bold'),fg='snow',width=20)
    audiostatusLabel.grid(row=2,column=1)


    ##################################################################################### Entrybox
    trackLabelEntry=Entry(root,font=('arial',18,'italic bold'),width=35,textvariable=audiotrack)
    trackLabelEntry.grid(row=0,column=1,padx=20,pady=20)




    ######################################################################################button method
    browseButton= Button(root,text='search',bg='deeppink',fg='snow',width=15,font=('arial',14,'italic bold'),bd=10,activebackground='snow',command=musicurl)
    browseButton.grid(row=0,column=2,padx=20,pady=20)


    PlayButton = Button(root, text='Play', bg='green2', fg='black', width=15, font=('arial', 14, 'italic bold'), bd=10,
                      activebackground='purple2',command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)


    root.pauseButton = Button(root, text='pause', bg='orange', fg='snow', width=15, font=('arial', 14, 'italic bold'), bd=10,
                      activebackground='snow',command=pausemusic)
    root.pauseButton.grid(row=1, column=1, padx=20, pady=20)


    root.ResumeButton = Button(root, text='Resume', bg='orange', fg='snow', width=15, font=('arial', 14, 'italic bold'), bd=10,
                     activebackground='snow',command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    stopButton = Button(root, text='stop', bg='cyan3', fg='black', width=15, font=('arial', 14, 'italic bold'), bd=10,
                      activebackground='snow',command=stopmusic)
    stopButton.grid(row=2, column=0, padx=20, pady=20)


    volumnupButton = Button(root, text='volumn+', bg='oliveDrab1', fg='black', width=15, font=('arial', 14, 'italic bold'), bd=10,
                    activebackground='snow',command=volumnup)
    volumnupButton.grid(row=1, column=2, padx=20, pady=20)


    volumndownButton = Button(root, text='volumn-', bg='oliveDrab1', fg='black', width=15, font=('arial', 14, 'italic bold'), bd=10,
                    activebackground='snow',command=volumndown)
    volumndownButton.grid(row=2, column=2, padx=20, pady=20)

    root.muteButton=Button(root,text='mute',width=10,bg='yellow',activebackground='purple4',bd=5,command=mutemusic)
    root.muteButton.grid(row=3,column=3)


    root.unmuteButton=Button(root,text='unmute',width=15,bg='brown',activebackground='purple4',bd=5,command=unmutemusic)
    root.unmuteButton.grid(row=3,column=3)
    root.unmuteButton.grid_remove()

#########################################################################################progressbar method Volumn ka increase decrease show krne me use krte hai
    ProgressbarLabel=Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=1,column=3)


    ProgressbarVolumn=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                  value=40,length=190)
    ProgressbarVolumn.grid(row=0,column=0,ipadx=5)


####################################################to create volumn percent in the volumn progressbar
    ProgressbarVolumnLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumnLabel.grid(row=0,column=0)








##################################################################################root method
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar


root=Tk()
root.geometry('1200x600+200+50')
root.title('Simple music player')
root.iconbitmap('music.ico')
root.configure(bg='Deepskyblue')
root.resizable(False,False)



################################################################################################global variable
audiotrack=StringVar()
currentval=0



#############################################################################################create slider method
ss='welcome to music player'
count = 0
text= ''
introLabel=Label(root,text=ss,bg='deepskyblue',font=('arial',28,'italic bold'),fg='yellow')
introLabel.grid(row=4,column=1,padx=20,pady=20)

def sliderlabel():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        introLabel.configure(text=text)
    else:
        text=text+ss[count]
        introLabel.configure(text=text)
    count+=1
    introLabel.after(150,sliderlabel)
sliderlabel()



mixer.init()
createwidthes()
root.mainloop()

