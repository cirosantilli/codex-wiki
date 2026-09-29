"""Original figure-eight closed-braid diagram. Python 3.14, root matplotlib.
Write only the PNG basename to CWD; respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def segment(ax,p,color='#173c64',lw=2):
    ax.plot(*zip(*p),color=color,lw=lw,solid_capstyle='round',solid_joinstyle='round')
def arrow(ax,p,q,color='#173c64'):
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':color,'lw':1.2,'mutation_scale':12})
def main():
    fig,ax=plt.subplots(figsize=(7.5,6),layout='constrained',facecolor='white')
    xs=[0,1.2,2.4]
    word=[(0,True),(1,False),(0,True),(1,False)]
    for row,(i,positive) in enumerate(word):
        top=4-row;bottom=top-1;a,b=xs[i:i+2]
        u=[(a,top),(b,bottom)];v=[(b,top),(a,bottom)]
        under,over=(v,u) if positive else (u,v)
        segment(ax,under);segment(ax,over,'white',7);segment(ax,over)
        j=next(j for j in range(3) if j not in [i,i+1]);segment(ax,[(xs[j],top),(xs[j],bottom)])
        ax.text(-.65,(top+bottom)/2,r'$\sigma_1$' if positive else r'$\sigma_2^{-1}$',ha='right',va='center',fontsize=13)
        arrow(ax,(a+.15,top-.125),(a+.39,top-.325))
    for i,x in enumerate(xs):
        outer=5.4-.8*i;high=4.5+.32*(2-i);low=-.5-.32*(2-i)
        segment(ax,[(x,0),(x,low),(outer,low),(outer,high),(x,high),(x,4)],'#6b7887',1.35)
        arrow(ax,(outer,1.1),(outer,1.45),'#6b7887')
        ax.text(x,4.16,chr(97+i),ha='center',va='bottom',fontsize=13,color='#173c64',bbox={'facecolor':'white','edgecolor':'none','pad':1})
    ax.set_xlim(-1.5,5.8);ax.set_ylim(-1.4,5.5);ax.set_aspect('equal');ax.axis('off')
    ax.set_title(r'Figure-eight knot: closure of $(\sigma_1\sigma_2^{-1})^2$',fontsize=14)
    ax.text(1.8,-1.32,'All braid strands point down; return arcs close matching endpoints.',ha='center',fontsize=10)
    fig.savefig(Path('paper-24-figure-eight-braid.png'),dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
