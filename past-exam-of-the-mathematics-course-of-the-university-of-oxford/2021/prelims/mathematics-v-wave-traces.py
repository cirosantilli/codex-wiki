"""Two dimensionless traces of the wave solution; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'savefig.facecolor':'white'})
    fig,axs=plt.subplots(1,2,figsize=(10.2,3.9),layout='constrained')
    x=np.linspace(-2,2,2001);z=np.abs(x)
    y=np.where(z<=.5,(x*x+.25)/2,np.where(z<=1.5,(1-(z-.5)**2)/4,0))
    axs[0].plot(x,y,color='#1565a7',lw=2.4);axs[0].set(xlabel='$x/L$',ylabel='$cy/L^2$',title=r'Spatial trace at $ct/L=1/2$',xlim=(-2,2),ylim=(-.015,.29))
    axs[0].scatter([-.5,0,.5],[.25,.125,.25],color='#1565a7',s=22,zorder=3)
    t=np.linspace(0,2.4,1501);y=np.where(t<=.5,t/2,np.where(t<=1.5,(1+(t-.5)**2)/4,.5))
    axs[1].plot(t,y,color='#c34b20',lw=2.4);axs[1].set(xlabel='$ct/L$',ylabel='$cy/L^2$',title=r'Time trace at $x/L=1/2$',xlim=(0,2.4),ylim=(-.015,.56))
    axs[1].scatter([.5,1.5],[.25,.5],color='#c34b20',s=22,zorder=3)
    axs[1].axhline(.5,color='#777777',ls=':',lw=.8)
    for ax in axs:ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
    fig.savefig(Path.cwd()/'mathematics-v-wave-traces.png',dpi=100,facecolor='white');plt.close(fig)


if __name__=='__main__':main()
