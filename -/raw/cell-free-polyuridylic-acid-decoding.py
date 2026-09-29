"""Original qualitative schematic of the 1961 poly-U assay, not measured data.

Source: Nirenberg and Matthaei, PNAS 47, 1588–1602 (1961),
Methods; Table 1 assay; Tables 6–9; Figure 6.
Tested with Python 3.14 and matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def draw():
    fig, ax = plt.subplots(figsize=(10, 5.4),dpi=110,facecolor='white')
    ax.set(xlim=(0,10),ylim=(0,6))
    ax.axis('off')
    ink='#243349'
    def box(x,y,w,h,text,color='#e7eff7',size=12):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06',facecolor=color,edgecolor='#607086',linewidth=1.2))
        ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=ink,linespacing=1.45)
    def arrow(a,b):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#607086'})
    ax.text(.2,5.65,'Cell-free decoding: impose a template, assay incorporation',fontsize=17,weight='bold',color=ink)
    ax.text(.2,5.14,'Original schematic of the published experiment • qualitative readout',fontsize=12,color=ink)
    box(.25,3.95,2.3,.74,'E. coli: grind; centrifuge')
    arrow((2.63,4.32),(2.97,4.32))
    box(3.05,3.95,6.65,.74,'Extract + ATP regeneration + ¹⁴C-phenylalanine')
    arrow((4.65,3.88),(2.62,3.45))
    arrow((7.65,3.88),(7.28,3.45))
    box(.85,2.45,3.65,.88,'+ poly-U',color='#dff2e8',size=14)
    box(5.45,2.45,3.65,.88,'No poly-U',color='#f0f1f3',size=14)
    arrow((2.67,2.36),(2.67,1.91))
    arrow((7.27,2.36),(7.27,1.91))
    box(.85,1.25,3.65,.56,'Incubate; TCA; wash; count',size=12)
    box(5.45,1.25,3.65,.56,'Incubate; TCA; wash; count',size=12)
    ax.text(2.67,.89,'Strong incorporation',ha='center',fontsize=13,color='#226342',weight='bold')
    ax.text(7.27,.89,'Low background',ha='center',fontsize=13,color='#596573',weight='bold')
    ax.text(.25,.30,'Omit ribosomes or ATP regeneration → incorporation suppressed',fontsize=12,color=ink)
    fig.subplots_adjust(left=.015,right=.99,top=.99,bottom=.025)
    fig.savefig(Path(__file__).stem+'.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':
    draw()
