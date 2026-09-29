"""Original ester/acetal electron-flow schemes for NST IA Chemistry 2025 Q3(c)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig,ax=plt.subplots(figsize=(11,8),facecolor='white')
ax.set(xlim=(0,15.2),ylim=(-.7,10.4));ax.axis('off')
def txt(x,y,s,fs=13):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def line(a,b):ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.4)
def flow(a,b,rad=.4):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',connectionstyle=f'arc3,rad={rad}',mutation_scale=13,color='#245f90',lw=1.5))
def arrow(x1,x2,y):ax.annotate('',(x2,y),(x1,y),arrowprops={'arrowstyle':'->','lw':1.4})
txt(7.5,10,'D: methyl ester formed; dimethyl acetal retained',13)
txt(7.5,9.45,r'$\mathrm{(MeO)_2CHCH_2CH_2C(=O)OMe}$',15)
# Carbonyl addition, followed by tetrahedral-intermediate collapse.
txt(1,8,r'$\mathrm{MeO{:}^-}$');txt(2.65,8,r'$\mathrm{R}$');txt(3.8,8,r'$\mathrm{C}$');txt(5.1,8,r'$\mathrm{OEt}$');txt(3.8,8.85,r'$\mathrm{O}$')
line((2.88,8),(3.56,8));line((4.04,8),(4.72,8));line((3.74,8.2),(3.74,8.64));line((3.86,8.2),(3.86,8.64))
flow((1.55,8.16),(3.55,8.16),-.6);flow((3.9,8.4),(4.02,8.79),-.65)
arrow(5.75,6.5,8)
txt(7.25,8,r'$\mathrm{R}$');txt(8.5,8,r'$\mathrm{C}$');txt(8.5,8.85,r'$\mathrm{O^-}$');txt(8.5,7.15,r'$\mathrm{OMe}$');txt(10,8,r'$\mathrm{OEt}$')
line((7.47,8),(8.28,8));line((8.5,8.2),(8.5,8.6));line((8.5,7.8),(8.5,7.4));line((8.72,8),(9.6,8))
flow((8.25,8.72),(8.28,8.18),.7);flow((9.2,8.03),(9.9,8.21),-.7)
arrow(10.75,11.4,8);txt(13.2,8,r'$\mathrm{R-CO_2Me}$',14)
txt(7.5,6.55,'Addition → tetrahedral intermediate → ethoxide departure.',11)
txt(7.5,5.95,'E: aldehyde unmasked; ethyl ester retained',13)
txt(7.5,5.4,r'$\mathrm{OHCCH_2CH_2CO_2Et}$',15)
# Acetal activation and water capture. Alkoxy O is explicitly protonated.
def centre(cx,cy,upper,right):
    txt(cx,cy,r'$\mathrm{C}$');txt(cx-1.15,cy,r'$\mathrm{R^{\prime}}$');txt(cx,cy-.7,r'$\mathrm{H}$');txt(cx,cy+.75,upper);txt(cx+1.65,cy,right)
    line((cx-.9,cy),(cx-.23,cy));line((cx,cy-.2),(cx,cy-.49));line((cx,cy+.2),(cx,cy+.51));line((cx+.23,cy),(cx+1.0,cy))
centre(3.0,3.8,r'$\mathrm{OMe}$',r'$\mathrm{O^+(H)Me}$')
flow((3.6,3.86),(4.4,4.04),-.75)
arrow(5.65,6.3,3.8)
txt(7.3,3.8,r'$\mathrm{R^{\prime}}$');txt(8.5,3.8,r'$\mathrm{C^+}$');txt(8.5,3.1,r'$\mathrm{H}$');txt(8.5,4.55,r'$\mathrm{OMe}$')
line((7.6,3.8),(8.22,3.8));line((8.5,3.58),(8.5,3.31));line((8.5,4.02),(8.5,4.31))
txt(10.1,4.7,r'$\mathrm{H_2O{:}}$');flow((9.75,4.58),(8.75,3.98),.4)
arrow(10.2,10.9,3.8);txt(13.2,3.8,r'$\mathrm{R^{\prime}CH(OH)(OMe)}$',11)
txt(7.5,2.65,'After water capture, remove H⁺; then protonate the remaining methoxy O.',11)
# Protonated hemiacetal collapse forms the aldehyde carbonyl.
centre(3.0,1.25,r'$\mathrm{OH{:}}$',r'$\mathrm{O^+(H)Me}$')
flow((3.22,1.88),(3.23,1.47),.7);flow((3.6,1.31),(4.4,1.49),-.75)
arrow(5.65,6.3,1.25);txt(8.3,1.25,r'$\mathrm{R^{\prime}CH=O^+H}$',13)
arrow(10.2,10.9,1.25);txt(10.55,1.8,r'$-\mathrm{H^+}$',11);txt(13.2,1.25,r'$\mathrm{R^{\prime}CHO}$',14)
txt(7.5,.22,'Release MeOH while C=O forms; deprotonation regenerates the acid catalyst.',11)
txt(7.5,-.38,'R = (MeO)₂CHCH₂CH₂; R′ = CH₂CH₂CO₂Et. Curved arrows move electron pairs.',10)
fig.tight_layout()
fig.savefig('2025-ester-acetal-mechanisms.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
