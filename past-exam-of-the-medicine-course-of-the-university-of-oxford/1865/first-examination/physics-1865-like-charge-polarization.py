"""Leading induced-dipole model; outputs an opaque PNG in the working directory."""
from pathlib import Path
import os
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'ourbigbook.json').exists())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'_out/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

def draw():
    plt.rcParams.update({'font.size':11,'axes.titlesize':12})
    fig,(scheme,curve)=plt.subplots(1,2,figsize=(12,5),dpi=120,facecolor='white')
    scheme.add_patch(Circle((0,0),.85,facecolor='#e5f1fb',edgecolor='#0072B2',lw=2))
    scheme.add_patch(Circle((3.25,0),.43,facecolor='#f8f2e7',edgecolor='#555555',lw=2))
    for x,y in [(-.35,.35),(.35,.35),(-.35,-.35),(.35,-.35)]:scheme.text(x,y,'+',ha='center',va='center',fontsize=23,color='#0072B2')
    scheme.text(2.94,0,'−',ha='center',va='center',fontsize=25,color='#D55E00')
    for y in (-.24,0,.24):scheme.text(3.43,y,'+',ha='center',va='center',fontsize=15,color='#0072B2')
    scheme.text(0,-1.15,r'$Q_1>0$',ha='center',fontsize=14)
    scheme.text(3.25,-.88,r'$Q_2>0$',ha='center',fontsize=14)
    scheme.annotate('Induced negative patch',xy=(2.94,.15),xytext=(1.1,1.05),arrowprops={'arrowstyle':'->','color':'#D55E00'},fontsize=10)
    scheme.annotate('',xy=(2.17,-.25),xytext=(2.83,-.25),arrowprops={'arrowstyle':'->','color':'#D55E00','lw':2})
    scheme.text(1.95,-.6,'Attractive contribution',ha='center',fontsize=10,color='#A74400')
    scheme.text(1.6,-1.55,'Schematic, not to scale; signs indicate local polarity,\nnot counts of equal elementary charges.',ha='center',fontsize=9)
    scheme.set_xlim(-1.05,4.2);scheme.set_ylim(-1.75,1.6);scheme.set_aspect('equal');scheme.axis('off')
    scheme.set_title('Redistribution within insulated conductors')
    eta=.001;x=np.linspace(8,24,400);ratio=1-2/(eta*x**3);cross=(2/eta)**(1/3)
    curve.axhspan(-3.2,0,color='#f6e6de',zorder=0);curve.axhspan(0,1.15,color='#e8f2fa',zorder=0)
    curve.plot(x,ratio,color='#7A3E9D',lw=2.6,label=r'$1-2/[\eta(R/a)^3]$')
    curve.axhline(0,color='#333333',lw=1);curve.axhline(1,color='#0072B2',ls='--',lw=1.2,label='Point-charge approximation')
    curve.axvline(cross,color='#555555',ls=':',lw=1.2)
    curve.annotate(r'$R/a\simeq12.60$',xy=(cross,0),xytext=(14,-.9),arrowprops={'arrowstyle':'->'},fontsize=11)
    curve.text(18,-1.8,'Attraction',ha='center',color='#A74400');curve.text(20,.37,'Repulsion',ha='center',color='#005487')
    curve.set_xlim(8,24);curve.set_ylim(-3.2,1.15);curve.grid(alpha=.15)
    curve.set_xlabel(r'Centre separation $R/a$');curve.set_ylabel(r'$F_R\,/\,[kQ_1Q_2/R^2]$')
    curve.set_title(r'Leading small-sphere model, $\eta=Q_2/Q_1=0.001$')
    curve.legend(loc='lower right',fontsize=9,framealpha=.95)
    fig.suptitle('Like net charges can coexist with an attractive polarization contribution',fontsize=14)
    fig.tight_layout(rect=(0,0,1,.94));fig.savefig(Path.cwd()/'physics-1865-like-charge-polarization.png',facecolor='white',transparent=False);plt.close(fig)

if __name__=='__main__':draw()
