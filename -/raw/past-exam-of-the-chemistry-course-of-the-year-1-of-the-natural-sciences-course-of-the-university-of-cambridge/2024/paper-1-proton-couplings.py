"""Original explicit-hydrogen and coupling map for NST IA Chemistry 2024 Q1."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig,axs=plt.subplots(2,1,figsize=(10.4,5.7),facecolor='white')
def label(ax,x,y,s,fs=14):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def bond(ax,a,b,n=1):
    dx,dy=b[0]-a[0],b[1]-a[1]
    length=(dx*dx+dy*dy)**.5
    for offset in ([0] if n==1 else [-.055,.055]):
        ox,oy=-dy*offset/length,dx*offset/length
        ax.plot([a[0]+ox,b[0]+ox],[a[1]+oy,b[1]+oy],color='black',lw=1.2)
def arc(ax,a,b,t,rad,xy):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='<->',connectionstyle=f'arc3,rad={rad}',shrinkA=8,shrinkB=8,mutation_scale=12,color='#245f8a',lw=1.5));label(ax,*xy,t,11)
for ax in axs:ax.axis('off');ax.set(xlim=(-.4,10.5),ylim=(-2.1,1.9))
a=axs[0];xs=[1,2.8,4.6,6.4,7.7,9.2]
# Left crotonyl fragment with all methyl H shown separately.
for xx in xs[:4]:label(a,xx,0,r'$\mathrm{C}$')
for i in range(3):bond(a,(xs[i]+.15,0),(xs[i+1]-.15,0),2 if i==1 else 1)
label(a,6.4,1,r'$\mathrm{O}$');bond(a,(6.4,.18),(6.4,.82),2)
label(a,7.7,0,r'$\mathrm{O}$');bond(a,(6.6,0),(7.5,0));bond(a,(7.9,0),(9.0,0));label(a,9.2,0,'vinyl',12)
for pt in [(0,0),(1,1),(1,-1)]:label(a,*pt,r'$\mathrm{H}_a$');bond(a,(1,0),pt)
label(a,2.8,1,r'$\mathrm{H}_b$');bond(a,(2.8,.15),(2.8,.82))
label(a,4.6,-1,r'$\mathrm{H}_c$');bond(a,(4.6,-.15),(4.6,-.82))
arc(a,(2.8,.85),(4.6,-.9),'15.3',-.55,(4.1,.9))
arc(a,(1,-1.0),(2.8,1.0),'6.9',.65,(1.55,-1.45))
arc(a,(1,-1.0),(4.6,-1.0),'1.8',.28,(3.1,-1.65))
a.text(0,1.65,'Crotonyl end: a = 1.9215, b = 7.108, c = 5.8765 ppm',fontsize=11,weight='bold')
a=axs[1]
label(a,1.3,0,r'$\mathrm{R-C(=O)-O}$',13);bond(a,(2.6,0),(3.9,0));label(a,4.1,0,r'$\mathrm{C}$');label(a,6.8,0,r'$\mathrm{C}$');bond(a,(4.3,0),(6.6,0),2)
label(a,4.1,1,r'$\mathrm{H}_d$');bond(a,(4.1,.15),(4.1,.82))
label(a,7.7,-1,r'$\mathrm{H}_e$');bond(a,(6.95,-.12),(7.5,-.82))
label(a,7.7,1,r'$\mathrm{H}_f$');bond(a,(6.95,.12),(7.5,.82))
arc(a,(4.1,1.05),(7.7,-1.05),'14.1',.5,(5.4,-.9))
arc(a,(4.1,1.05),(7.7,1.05),'6.3',-.25,(6.1,1.6))
arc(a,(7.9,-1),(7.9,1),'1.5',.55,(8.6,0))
a.text(0,-1.6,'d = 7.343, e = 4.906, f = 4.576 ppm; blue arrows give J in Hz.',fontsize=10)
fig.tight_layout(h_pad=1.5)
fig.savefig('paper-1-proton-couplings.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
