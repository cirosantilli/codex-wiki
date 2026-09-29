"""Render a paraxial eye/astigmatism diagram into the working directory."""
from pathlib import Path
import os
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'ourbigbook.json').exists())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'_out/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def draw():
    plt.rcParams.update({'font.size':11,'axes.titlesize':12,'axes.labelsize':10})
    fig,axes=plt.subplots(1,2,figsize=(12,4.8),dpi=120,facecolor='white')
    left,right=axes
    for ax in axes:
        ax.axhline(0,color='0.45',lw=.8)
        ax.set_ylim(-1.05,1.05)
        ax.grid(alpha=.14)
        ax.set_xlabel('Axial distance (schematic units)')
    f=1.8;incident_slope=-.14
    colors=['#0072B2','#D55E00','#009E73']
    for y,c in zip([-.6,0,.6],colors):
        x0=np.linspace(-2.15,0,60);x1=np.linspace(0,f,60)
        left.plot(x0,y+incident_slope*x0,color=c,lw=2)
        left.plot(x1,y+(incident_slope-y/f)*x1,color=c,lw=2)
    left.annotate('',xy=(0,.86),xytext=(0,-.86),arrowprops={'arrowstyle':'<->','color':'#333333','lw':2})
    left.axvline(f,color='#777777',lw=3,alpha=.7)
    left.plot(f,f*incident_slope,'ko',ms=5)
    left.text(-2.06,.86,'Parallel pencil from one\ndistant object point',fontsize=10,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
    left.text(.08,-.91,'Equivalent lens',fontsize=10)
    left.text(f+.08,.68,'Retinal\nplane',fontsize=10)
    left.set_xlim(-2.2,2.35)
    left.set_ylabel('Ray height')
    left.set_title('Combined eye power: paraxial model')
    xf=np.linspace(0,2.65,120)
    for focal,c,label in [(1.3,'#0072B2','Principal meridian 1'),(2.15,'#D55E00','Principal meridian 2')]:
        for j,y in enumerate([-.68,.68]):
            right.plot(xf,y*(1-xf/focal),color=c,lw=2,label=label if j==0 else None)
        right.axvline(focal,color=c,ls=':',lw=1.1)
        right.text(focal,.92,r'$f_1$'if focal<2 else r'$f_2$',ha='center',color=c)
    right.set_xlim(-.12,2.7)
    right.set_title('Regular astigmatism: unequal focal distances')
    right.set_ylabel('Ray height in each meridional section')
    right.legend(loc='lower left',fontsize=9,framealpha=.95)
    right.text(.11,.68,'Two perpendicular ray sections;\n3-D foci are perpendicular lines.',fontsize=9,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
    fig.suptitle('Eye imaging and regular ocular astigmatism',fontsize=15)
    fig.tight_layout(rect=(0,0,1,.95))
    fig.savefig(Path.cwd()/'physics-1866-eye-ray-geometry.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':draw()
