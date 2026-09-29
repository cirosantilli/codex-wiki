"""Original weight sketches. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Run with cwd set to the desired media output directory; output is a cwd basename.
"""
import os
os.environ.setdefault('MPLCONFIGDIR',os.path.join(os.getcwd(),'.paper-2-mplconfig'))
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G21=[(-3,2,1),(-2,0,1),(-2,3,1),(-1,-2,1),(-1,1,2),(0,-1,2),(0,2,1),(1,-3,1),(1,0,2),(2,-2,1),(2,1,1),(3,-1,1)]
G10=[(1,0,1),(-1,1,1),(0,-1,1)]
G20=[(2,0,1),(0,1,1),(1,-1,1),(-2,2,1),(-1,0,1),(0,-2,1)]
def xy(a,b):return (a+b/2,math.sqrt(3)*b/2)
def draw(ax,data,title,highest):
    lo=min(xy(a,b)[0] for a,b,m in data)-.65;hi=max(xy(a,b)[0] for a,b,m in data)+.65
    bot=min(xy(a,b)[1] for a,b,m in data)-.65;top=max(xy(a,b)[1] for a,b,m in data)+.65
    offset=(data[0][0]-data[0][1])%3
    for a in range(-8,9):
        for b in range(-8,9):
            if (a-b)%3!=offset:continue
            x,y=xy(a,b)
            for da,db in [(2,-1),(-1,2),(1,1)]:
                x2,y2=xy(a+da,b+db);ax.plot([x,x2],[y,y2],color='#dfe5ec',lw=.65,zorder=0)
    for a,b,m in data:
        x,y=xy(a,b);color='#d27a00' if (a,b)==highest else '#185686'
        ax.scatter([x],[y],s=430 if len(data)>6 else 370,color=color,zorder=2)
        ax.text(x,y,str(m),ha='center',va='center',color='white',fontweight='bold',fontsize=12,zorder=3)
        ax.annotate(f'({a}, {b})',(x,y),xytext=(0,18),textcoords='offset points',ha='center',fontsize=10)
    ax.set_xlim(lo,hi);ax.set_ylim(bot,top);ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontsize=16,pad=20)
fig=plt.figure(figsize=(12.5,6.2),dpi=100,facecolor='white')
a1=fig.add_axes([.025,.14,.465,.68]);a2=fig.add_axes([.52,.14,.21,.68]);a3=fig.add_axes([.755,.14,.22,.68])
draw(a1,G21,r'$\Gamma_{2,1}$: dimension 15',(2,1));draw(a2,G10,r'$\Gamma_{1,0}$: dimension 3',(1,0));draw(a3,G20,r'$S^2\Gamma_{1,0}$: dimension 6',(2,0))
fig.suptitle('A₂ input weight diagrams',fontsize=21,y=.98)
fig.text(.5,.045,'Dot labels give multiplicities; coordinate labels are Dynkin labels (a, b). Orange marks each highest weight.',ha='center',fontsize=12)
fig.savefig('paper-2-input-weight-diagrams.png',dpi=100,facecolor='white',transparent=False)
