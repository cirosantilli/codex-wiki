"""Original interval Green-kernel and step-forcing plots; output goes to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    x=np.linspace(-1,1,801)
    fig,axes=plt.subplots(1,2,figsize=(10.0,4.1),layout='constrained')
    for s in [-.5,0,.5]:
        kernel=np.sinh(1+np.minimum(x,s))*np.sinh(1-np.maximum(x,s))/np.sinh(2)
        axes[0].plot(x,kernel,label=f's = {s:g}',lw=1.8)
    axes[0].set(xlabel='Position x',ylabel='G(x,s)',title='A positive kernel with derivative jump −1');axes[0].legend(fontsize=9)
    c=(np.cosh(1)-1)/(2*np.cosh(1));b=np.cosh(1)*(np.cosh(1)-1)/np.sinh(2)
    y=np.where(x<=0,np.sinh(1+x)*(np.cosh(1)-1)/np.sinh(2),1+(c-1)*np.cosh(x)+b*np.sinh(x))
    axes[1].step([-1,0,1],[0,1,1],where='post',color='#a34722',ls='--',label='Step forcing f(x)')
    axes[1].plot(x,y,color='#176fa8',lw=2,label='Solution y(x)');axes[1].scatter([0],[c],s=23,color='#176fa8')
    axes[1].annotate(f'y(0) = {c:.4f}',(0,c),xytext=(-.8,.53),arrowprops=dict(arrowstyle='->',color='#176fa8'),fontsize=9)
    axes[1].set(xlabel='Position x',ylabel='Forcing / solution',title='The solution and its first derivative are continuous');axes[1].legend(fontsize=9,loc='upper left')
    for ax in axes:ax.grid(alpha=.17);ax.set_xlim(-1,1)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white');plt.close(fig)

if __name__=='__main__':
    main()
