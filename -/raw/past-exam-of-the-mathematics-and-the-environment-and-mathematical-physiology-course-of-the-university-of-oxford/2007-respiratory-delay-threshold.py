"""Original equilibrium and characteristic-root diagrams; output in cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    n=3; pstar=.8
    p=np.linspace(0,2,500);removal=p**(n+1)/(1+p**n)
    a=pstar**n/(1+pstar**n);b=n*pstar**n/(1+pstar**n)**2
    production=pstar*a;omega=np.sqrt(b*b-a*a);tau=np.arccos(-a/b)/omega
    fig, axes=plt.subplots(1,2,figsize=(10.3,4.2),layout='constrained')
    ax=axes[0];ax.plot(p,removal,lw=2,label='Removal pV(p)');ax.axhline(production,color='#a34722',ls='--',label='Production M')
    ax.scatter([pstar],[production],color='black',zorder=5);ax.annotate('Unique positive equilibrium',(pstar,production),xytext=(.2,.85),textcoords='axes fraction',arrowprops=dict(arrowstyle='->'),fontsize=9)
    ax.set(xlabel='Carbon-dioxide pressure p',ylabel='Production / removal',title='Monotone removal gives one equilibrium');ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.15)
    ax=axes[1]
    for start,end,color,label in [((0,0),(a,0),'#176fa8','A'),((a,0),(a,omega),'#087a70','iω'),((a,omega),(0,0),'#a34722','B exp(−iωτ)')]:
        ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=color,lw=2.4))
        mid=(np.asarray(start)+end)/2;shift={'A':(0,-16),'iω':(10,0),'B exp(−iωτ)':(-95,2)}[label]
        ax.annotate(label,mid,xytext=shift,textcoords='offset points',color=color,fontsize=10)
    ax.axhline(0,color='#bbb',lw=.8);ax.axvline(0,color='#bbb',lw=.8)
    ax.text(.05,.94,f'A = {a:.3f}, B = {b:.3f}\nω = {omega:.3f}, τc = {tau:.3f}',transform=ax.transAxes,va='top',fontsize=9)
    ax.set(xlim=(-.3,a+.25),ylim=(-.14,omega+.18),xlabel='Real part',ylabel='Imaginary part',title='At onset: iω + A + B exp(−iωτ) = 0');ax.set_aspect('equal',adjustable='datalim');ax.grid(alpha=.15)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white');plt.close(fig)

if __name__=='__main__':
    main()
