"""Original twin-clock diagram. Python 3.14, NumPy/Matplotlib root dependencies.

Write opaque PNG basename to caller CWD; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    beta=.65
    fig,(space,age)=plt.subplots(1,2,figsize=(11.2,5.2),dpi=100,facecolor='white')
    fig.subplots_adjust(left=.07,right=.96,bottom=.24,top=.76,wspace=.30)
    space.plot([0,0],[0,1],color='black',lw=2,label="Alice")
    space.plot([0,beta/2,0],[0,.5,1],color='#b74438',lw=2.5,label="Bob")
    x=np.linspace(0,.5,200)
    out=.5+beta*(x-beta/2)
    inc=.5-beta*(x-beta/2)
    space.plot(x,out,color='#276fa3',ls='--',lw=1.4,label="Outbound simultaneity")
    space.plot(x,inc,color='#338b55',ls='--',lw=1.4,label="Inbound simultaneity")
    space.plot([0,beta/2],[(1-beta)/2,.5],color='#c29430',lw=1.5,ls=':',label="Light received at turn")
    space.scatter([0,beta/2,0],[0,.5,1],color='black',s=20,zorder=4)
    space.text(beta/2+.018,.5,'Turn',va='center',fontsize=10)
    space.set(xlim=(-.035,.50),ylim=(-.015,1.045),xlabel=r'$x/(cT)$',ylabel=r'$t/T$')
    space.set_title("Alice's inertial coordinates",fontsize=12,pad=15)
    space.set_aspect('equal',adjustable='box')
    space.legend(loc='upper left',bbox_to_anchor=(.01,-.17),fontsize=8,ncol=2,frameon=False)
    q=np.linspace(0,1,1001)
    optical=np.where(q<=.5,(1-beta)*q,(1+beta)*q-beta)
    age.plot(q,optical,color='#c29430',lw=2.4,label='Age received by light')
    qo=np.linspace(0,.5,301);qi=np.linspace(.5,1,301)
    age.plot(qo,(1-beta**2)*qo,color='#276fa3',ls='--',lw=2,label='Age assigned as simultaneous')
    age.plot(qi,(1-beta**2)*qi+beta**2,color='#276fa3',ls='--',lw=2)
    age.plot([.5,.5],[(1-beta**2)/2,(1+beta**2)/2],color='#276fa3',ls=':',lw=1.2)
    age.annotate('Rest-frame change',xy=(.5,.52),xytext=(.62,.32),fontsize=10,
                 arrowprops={'arrowstyle':'->','color':'0.35'})
    age.set(xlim=(0,1),ylim=(0,1.04),xlabel=r"Bob proper time / total Bob proper time",ylabel='Alice age / T')
    age.set_title('Received signals versus simultaneity',fontsize=12,pad=15)
    age.legend(loc='upper left',fontsize=9,frameon=False)
    for ax in (space,age):
        ax.set_facecolor('white');ax.grid(alpha=.12)
        ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
    fig.suptitle(r'Twin voyage with $v/c=0.65$: two inertial legs and a short turnaround',fontsize=14,y=.96)
    fig.savefig(Path.cwd()/'paper-2-twin-clocks.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
