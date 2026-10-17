"""Original donor, acceptor and optical carrier-generation diagrams; NST IA Chemistry 2024."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,3,figsize=(10,4.7),facecolor='white')
for ax in axs:
    ax.set(xlim=(0,4),ylim=(-.5,4.6));ax.axis('off')
    ax.fill_between([.35,3.4],3.15,3.8,color='#c6dfed');ax.fill_between([.35,3.4],0,.65,color='#e7d6bf')
    ax.text(1.9,3.48,'conduction band',ha='center',fontsize=10);ax.text(1.9,.30,'valence band',ha='center',fontsize=10)
    ax.plot([.35,3.4],[3.15,3.15],color='black',lw=1.1);ax.plot([.35,3.4],[.65,.65],color='black',lw=1.1)
    ax.annotate('',(.12,3.15),(.12,.65),arrowprops={'arrowstyle':'<->','lw':.9});ax.text(.02,1.9,r'$E_g$',rotation=90,va='center')
def arrow(ax,x,y1,y2,label):
    ax.annotate('',(x,y2),(x,y1),arrowprops={'arrowstyle':'->','color':'#245f8a','lw':1.8});ax.text(x+.2,(y1+y2)/2,label,fontsize=10,va='center')
a=axs[0];a.set_title('1. Donor doping',fontsize=12)
a.plot([.6,2.1],[2.72,2.72],color='#a55129',lw=1.7);a.scatter([1.2],[2.72],s=26,color='black');arrow(a,1.2,2.78,3.2,'small ionization cost')
a.text(1.8,2.35,'occupied donor level',ha='center',fontsize=10);a.text(1.8,-.28,'mobile electrons; donor becomes +',ha='center',fontsize=9)
a=axs[1];a.set_title('2. Acceptor doping',fontsize=12)
a.plot([.6,2.1],[1.07,1.07],color='#a55129',lw=1.7);a.scatter([1.2],[.65],s=32,facecolor='white',edgecolor='black');arrow(a,1.2,.70,1.1,'electron accepted')
a.text(1.8,1.5,'acceptor level',ha='center',fontsize=10);a.text(1.8,-.28,'mobile valence hole remains',ha='center',fontsize=9)
a=axs[2];a.set_title('3. Above-gap light',fontsize=12)
arrow(a,1.15,.7,3.2,r'$h\nu\gtrsim E_g$');a.scatter([1.15],[3.25],s=26,color='black');a.scatter([1.15],[.65],s=32,facecolor='white',edgecolor='black')
a.text(1.8,-.28,'electron–hole pair generation',ha='center',fontsize=9)
fig.text(.5,.02,'Level separations are schematic; conductivity also depends on activation, trapping, recombination and mobility.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.07,1,1));fig.savefig('paper-1-band-diagrams.png',dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
