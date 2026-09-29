"""Original local map atlas; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-65-map-regions.png to CWD; preserves supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def main():
    fig,ax=plt.subplots(figsize=(8,4.8),constrained_layout=True)
    aa=np.linspace(.001,1.4,1000);bb=np.linspace(.001,1,800);a,b=np.meshgrid(aa,bb)
    reg=np.zeros_like(a);reg[a>1]=1
    reg[(a<1)&(a>1/3)&(b>1-a)]=2
    reg[(a+b<1)&(b>(1-a)/2)&(b<a+1/3)]=3
    ax.pcolormesh(aa,bb,reg,cmap=ListedColormap(['#f1eff2','#cbd9e9','#ffe0b0','#b6e0c4']),vmin=0,vmax=3,shading='nearest',rasterized=True)
    ax.plot([1,1],[0,1],'k-',lw=1.3,label='origin–prey exchange: a=1')
    t=np.linspace(0,1,600);ax.plot(t,1-t,'k-',lw=1.3,label='predator invasion: a+b=1')
    ax.plot([1/3,1/3],[2/3,1],color='#a04b42',lw=1.8,label='prey flip: a=1/3')
    ax.plot(t,(1-t)/2,color='#416c96',lw=1.8,label='unit-modulus pair: a+2b=1')
    t=np.linspace(0,1/3,200);ax.plot(t,t+1/3,color='#86549b',lw=1.8,label='coexistence flip: b=a+1/3')
    ax.plot([1/9],[4/9],'ko',ms=5);ax.annotate('double −1',(1/9,4/9),xytext=(.02,.67),arrowprops={'arrowstyle':'-','lw':.8})
    for r in [1/7,1/5]:ax.plot(r,(1-r)/2,'s',color='#416c96',ms=4)
    ax.text(1.15,.66,'O sink',ha='center');ax.text(.73,.8,'E sink',ha='center');ax.text(.56,.27,'P sink',ha='center')
    ax.text(.18,.09,'No fixed-point sink',fontsize=9);ax.text(.02,.94,'Local stability atlas',fontsize=10)
    ax.set(xlim=(0,1.4),ylim=(0,1),xlabel='a',ylabel='b',title='Discrete predator–prey map: extra instability thresholds')
    ax.legend(loc='upper right',fontsize=8,framealpha=.96)
    fig.savefig('paper-65-map-regions.png',dpi=150,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
