from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def coords(U,V):
    u=2/np.pi*np.arctan(U);v=2/np.pi*np.arctan(V);return (v-u)/2,(v+u)/2

def main():
    fig,ax=plt.subplots(figsize=(9,5.4),dpi=100,facecolor='white');ax.set_facecolor('white')
    for sg in [-1,1]:
        ax.plot([-.5,.5],[sg*.5]*2,color='black',lw=3)
        ax.plot([sg*.5,sg,sg*.5],[.5,0,-.5],color='black',lw=1.3)
        ax.plot([-.5,.5],[-.5,.5],ls='--',color='#999',lw=1.1);ax.plot([-.5,.5],[.5,-.5],ls='--',color='#999',lw=1.1)
    ax.text(0,.54,'future r = 0 singularity',ha='center',fontsize=10);ax.text(0,-.57,'past r = 0 singularity',ha='center',fontsize=10)
    ax.text(.84,.22,'right\nexterior',ha='center',fontsize=10);ax.text(-.84,.22,'left\nexterior',ha='center',fontsize=10)
    ax.text(0,.30,'black hole',ha='center',fontsize=10);ax.text(0,-.30,'white hole',ha='center',fontsize=10)
    V=np.linspace(-40,1/.35,800);x,y=coords(np.full_like(V,.35),V);ax.plot(x,y,color='#16699b',lw=2,label='inextendible incomplete radial null geodesic')
    i=600;ax.annotate('',xy=(x[i+35],y[i+35]),xytext=(x[i],y[i]),arrowprops=dict(arrowstyle='->',color='#16699b',lw=2))
    V=np.linspace(.35,3.1,160);x,y=coords(-.8,V);ax.plot(x,y,ls=':',color='#964baa',lw=1.4)
    V=np.linspace(.7,1.6,90);x,y=coords(-.8,V);ax.plot(x,y,color='#964baa',lw=3,label='extendible radial null segment');ax.scatter([x[0],x[-1]],[y[0],y[-1]],s=20,color='#964baa')
    t=np.linspace(-44,44,700);q=np.sqrt(3*np.exp(4));x,y=coords(-q*np.exp(-t/4),q*np.exp(t/4));ax.plot(x,y,color='#bd7800',ls='-.',lw=2,label='complete circular timelike geodesic (nonradial)')
    V=np.linspace(-100,100,2000);x,y=coords(0,V);ax.plot(x,y,color='#208553',lw=1.8,label='complete radial null horizon geodesic')
    ax.text(.98,-.04,r'$i^0$',ha='center');ax.text(.54,.48,r'$i^+$');ax.text(.54,-.51,r'$i^-$')
    ax.set(xlim=(-1.07,1.07),ylim=(-.65,.67));ax.set_aspect('equal');ax.axis('off');ax.set_title('Kruskal geometry: no complete radial timelike geodesic',fontsize=13)
    ax.legend(loc='lower center',bbox_to_anchor=(.5,-.22),fontsize=9,framealpha=1,facecolor='white');fig.subplots_adjust(bottom=.22,top=.9,left=.06,right=.96)
    fig.savefig(Path.cwd()/'paper-311-kruskal.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
