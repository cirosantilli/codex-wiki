"""Original reduction products and electron flow, NST IA Chemistry 2025 Q3(b)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig,ax=plt.subplots(figsize=(10.3,7.4),facecolor='white')
ax.set(xlim=(-.1,13.4),ylim=(-2.8,7.4));ax.axis('off')
def txt(x,y,s,fs=13):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def line(a,b,lw=1.4):ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=lw)
def flow(a,b,rad=.4):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',connectionstyle=f'arc3,rad={rad}',mutation_scale=13,color='#245f90',lw=1.5))
def arrow(a,b):ax.annotate('',b,a,arrowprops={'arrowstyle':'->','lw':1.4})
def ring(cx,cy,lactam):
    pts=np.array([[0,-.7],[1,.05],[.62,1.2],[-.62,1.2],[-1,.05]])+np.array([cx,cy])
    for a,b in zip(pts,np.roll(pts,-1,axis=0)):line(a,b)
    txt(*pts[0],r'$\mathrm{N}$',15);txt(cx,cy-1.15,r'$\mathrm{CH_3}$',12);line((cx,cy-.85),(cx,cy-1.01))
    oh=pts[3]+[-.42,.66];line(pts[3],oh);txt(*(oh+[-.12,.22]),r'$\mathrm{OH}$',14)
    if lactam:
        c=pts[1];o=c+[.94,-.24];v=np.array([.03,.10])
        line(c+v,o+v);line(c-v,o-v);txt(*(o+[.19,-.03]),r'$\mathrm{O}$',15)
    return pts
ring(3.0,4.45,True);ring(9.4,4.45,False)
txt(3,7.05,'B: ketone reduced; lactam retained',12);txt(9.4,7.05,'C: both carbonyl groups reduced',12)
txt(3,2.7,r'$\mathrm{C_5H_9NO_2}$');txt(9.4,2.7,r'$\mathrm{C_5H_{11}NO}$')
txt(6.7,2.27,'Ketone: hydride addition, then protonating workup',12)
txt(1.0,1.25,r'$\mathrm{M-H}$');txt(3.1,1.25,r'$\mathrm{C}$');txt(3.1,2.0,r'$\mathrm{O}$')
line((3.04,1.43),(3.04,1.8));line((3.16,1.43),(3.16,1.8));line((2.92,1.15),(2.45,.85));line((3.28,1.15),(3.75,.85))
flow((1.45,1.26),(2.86,1.3),-.45);flow((3.15,1.61),(3.37,1.94),-.6)
arrow((4.0,1.25),(5.3,1.25));txt(6.3,1.25,r'$\mathrm{R_2CH-O^-}$');arrow((7.5,1.25),(8.8,1.25));txt(8.1,1.75,r'$\mathrm{H^+}$',11);txt(10.5,1.25,r'$\mathrm{R_2CH-OH}$')
txt(6.7,.1,'Lactam: tetrahedral adduct → iminium → amine (ring bonds retained)',12)
txt(1.4,-1.25,r'$\mathrm{R_2N{:}}$',12);txt(2.9,-1.25,r'$\mathrm{C}$',12)
txt(2.9,-.52,r'$\mathrm{O-Al}$',12);txt(2.9,-1.95,r'$\mathrm{H}$',12);txt(4.05,-1.25,r'$\mathrm{R^{\prime}}$',12)
line((1.95,-1.25),(2.7,-1.25));line((2.9,-1.04),(2.9,-.73));line((2.9,-1.43),(2.9,-1.74));line((3.1,-1.25),(3.8,-1.25))
flow((1.9,-1.11),(2.72,-1.10),-.8);flow((2.92,-.92),(3.10,-.6),-.6)
arrow((4.4,-1.25),(5.2,-1.25));txt(6.4,-1.25,r'$\mathrm{R_2N^+=CH-R^{\prime}}$',12)
txt(6.3,-2.05,r'$\mathrm{Al-H}$',12);flow((6.75,-1.97),(6.95,-1.43),.4)
# The iminium pi pair shifts back onto N as hydride adds at carbon.
flow((6.4,-1.1),(5.8,-.95),.5)
arrow((8.0,-1.25),(8.9,-1.25));txt(11.0,-1.25,r'$\mathrm{R_2N-CH_2-R^{\prime}}$',12)
txt(6.7,-2.6,'M–H denotes a reagent hydride bond; aluminium-bound intermediates are schematic.',10)
fig.tight_layout()
fig.savefig('2025-reduction-products.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
