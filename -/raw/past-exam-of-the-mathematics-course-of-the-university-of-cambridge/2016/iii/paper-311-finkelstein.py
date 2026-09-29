from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,ax=plt.subplots(figsize=(8,4.8),dpi=100,facecolor='white');ax.set_facecolor('white')
    ax.axvspan(0,2,color='#fff0ef');ax.axvline(0,color='black',lw=3);ax.axvline(2,color='#c02c31',lw=2)
    for C in [-2,1,4,7,10]:
        r=np.linspace(.04,6,400);T=C-r;ax.plot(r,T,color='#17659b',lw=1.35)
        j=np.where((T>-4.8)&(T<5.8)&(r>1))[0]
        if len(j):i=j[len(j)//2];ax.annotate('',xy=(r[i]-.3,T[i]+.3),xytext=(r[i],T[i]),arrowprops=dict(arrowstyle='->',color='#17659b',lw=1.8))
    for C in [-4,0,4,8]:
        for r in [np.linspace(2.015,6,700),np.linspace(1.98,.05,700)]:
            T=r+4*np.log(abs(r/2-1))+C;ax.plot(r,T,color='#bf7500',lw=1.5)
            j=np.where((T>-4.5)&(T<5.2))[0]
            if len(j)>15:i=j[len(j)//2];k=i+12;ax.annotate('',xy=(r[k],T[k]),xytext=(r[i],T[i]),arrowprops=dict(arrowstyle='->',color='#bf7500',lw=1.8))
    ax.annotate('',xy=(2,3.6),xytext=(2,2.3),arrowprops=dict(arrowstyle='->',color='#c02c31',lw=2))
    ax.text(.2,6.4,'black-hole interior',fontsize=11);ax.text(3.35,6.4,'exterior',fontsize=11)
    ax.text(2.06,-5.2,'horizon',color='#c02c31',fontsize=10);ax.text(.12,-5.2,'r = 0',fontsize=10)
    ax.plot([],[],color='#17659b',label='ingoing: v constant');ax.plot([],[],color='#bf7500',label='outgoing: dr/dv = (1 − 2M/r)/2')
    ax.set(xlim=(-.1,6),ylim=(-5.6,7),xlabel='areal radius r / M',ylabel='T / M = (v − r) / M',title='Radial light rays across the Schwarzschild horizon')
    ax.legend(loc='lower right',fontsize=10,facecolor='white',framealpha=1);ax.grid(alpha=.12);fig.tight_layout();fig.savefig(Path.cwd()/'paper-311-finkelstein.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
