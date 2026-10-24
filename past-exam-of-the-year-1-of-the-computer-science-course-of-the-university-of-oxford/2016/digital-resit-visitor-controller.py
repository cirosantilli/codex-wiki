"""Draw the complete four-state entry controller; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

def main():
    fig, ax = plt.subplots(figsize=(9,6),dpi=100,facecolor='white')
    pos={'A':(-1.7,1.25),'B':(1.7,1.25),'C':(1.7,-1.25),'I':(-1.7,-1.25)}
    for name,(x,y) in pos.items():
        ax.add_patch(Circle((x,y),.46,facecolor='#d9efdf'if name=='I'else'#edf2f8',edgecolor='#25364a',lw=1.6,zorder=3))
        ax.text(x,y+.08,name,ha='center',va='center',fontsize=17,zorder=4)
        ax.text(x,y-.18,'INC = '+str(int(name=='I')),ha='center',fontsize=10,zorder=4)
    def edge(src,dst,label,rad=0,offset=(0,0)):
        start,end=pos[src],pos[dst]
        ax.add_patch(FancyArrowPatch(start,end,connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=15,
                                   shrinkA=35,shrinkB=35,lw=1.5,color='#25364a',zorder=2))
        x=(start[0]+end[0])/2+offset[0];y=(start[1]+end[1])/2+offset[1]
        ax.text(x,y,label,ha='center',va='center',fontsize=12,bbox=dict(facecolor='white',edgecolor='none',pad=1),zorder=5)
    edge('A','B','01, 11',-.12,(0,.34));edge('B','A','00',-.12,(0,-.34))
    edge('B','C','10',-.13,(.43,0));edge('C','B','01, 11',-.13,(-.43,0))
    edge('C','I','00',0,(0,-.18));edge('I','A','00, 10',0,(-.46,0))
    edge('I','B','01, 11',0,(-.18,-.25))
    for name,label in [('A','00, 10'),('B','01, 11'),('C','10')]:
        x,y=pos[name]
        start=(x+.41,y+.22) if name=='C' else (x-.22,y+.41)
        end=(x+.41,y-.22) if name=='C' else (x+.22,y+.41)
        ax.add_patch(FancyArrowPatch(start,end,connectionstyle='arc3,rad=-2.4',arrowstyle='-|>',mutation_scale=14,lw=1.5,color='#25364a'))
        ax.text(x+.95 if name=='C' else x,y if name=='C' else y+1.0,label,ha='center',fontsize=11,bbox=dict(facecolor='white',edgecolor='none',pad=1))
    ax.annotate('reset',xy=(-2.16,1.25),xytext=(-2.9,1.25),ha='center',va='center',arrowprops=dict(arrowstyle='->',lw=1.5))
    ax.set_xlim(-3.2,3.0);ax.set_ylim(-2.0,2.7);ax.set_aspect('equal');ax.axis('off')
    fig.suptitle('Visitor entry controller — labels are x₁x₀',fontsize=15,y=.97)
    fig.text(.5,.035,'Only state I emits a pulse; every transition from I leaves it.',ha='center',fontsize=11)
    fig.subplots_adjust(left=.02,right=.98,top=.91,bottom=.09)
    fig.savefig(Path.cwd()/'digital-resit-visitor-controller.png',facecolor='white',transparent=False)
    plt.close(fig)
if __name__ == '__main__': main()
