"""Original electron-pair schemes for NST IA Chemistry 2025 Q3(a)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig,ax=plt.subplots(figsize=(11.5,6.4),facecolor='white')
ax.set(xlim=(0,14),ylim=(-.4,8.1));ax.axis('off')
def txt(x,y,s,fs=15):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def bond(x1,x2,y):ax.plot([x1,x2],[y,y],color='black',lw=1.4)
def flow(a,b,rad=.4):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',connectionstyle=f'arc3,rad={rad}',mutation_scale=14,lw=1.5,color='#245f90'))
def step(x1,x2,y):ax.annotate('',(x2,y),(x1,y),arrowprops={'arrowstyle':'->','lw':1.5})
# S_N2: electrophilic CH2 retains a butyl group above it.
txt(1.4,7.1,r'$\mathrm{N\equiv C{:}^-}$');txt(4.0,7.1,r'$\mathrm{CH_2}$');txt(6.1,7.1,r'$\mathrm{Cl}$')
bond(4.43,5.8,7.1);txt(4.0,7.65,r'$\mathrm{(CH_2)_3CH_3}$',12);ax.plot([4,4],[7.25,7.45],color='black',lw=1.2)
flow((1.95,7.0),(3.65,7.0),-.55);flow((5.0,7.12),(6.0,7.3),-.8)
step(6.6,7.4,7.1);txt(10.5,7.1,r'$\mathrm{CH_3(CH_2)_4C\equiv N+Cl^-}$')
txt(6.8,6.35,'SN2: one step; the C–C bond forms as the C–Cl bond breaks.',11)
# Ionization first, followed by capture and deprotonation.
txt(2,5.25,r'$\mathrm{Ph_3C}$');txt(4,5.25,r'$\mathrm{Cl}$');bond(2.55,3.7,5.25)
flow((3,5.27),(3.95,5.45),-.9);step(5,6.2,5.25);txt(9.1,5.25,r'$\mathrm{Ph_3C^++Cl^-}$')
txt(6.8,4.6,'SN1, slow step: C–Cl ionization gives a resonance-stabilized carbocation.',11)
txt(1.7,3.5,r'$\mathrm{Et-O{:}-H}$');txt(4.8,3.5,r'$\mathrm{C^+Ph_3}$')
flow((2.05,3.65),(4.25,3.65),-.45);step(6.0,7.0,3.5);txt(10.0,3.5,r'$\mathrm{Ph_3C-O^+(H)-Et}$')
txt(6.8,2.85,'Fast capture: an ethanol oxygen lone pair forms the new C–O bond.',11)
txt(1.1,1.6,r'$\mathrm{Py{:}}$');txt(3.6,1.6,r'$\mathrm{H}$');txt(5.4,1.6,r'$\mathrm{O^+(Et)(CPh_3)}$');bond(3.8,4.55,1.6)
flow((1.55,1.72),(3.42,1.72),-.5);flow((4.15,1.62),(4.9,1.82),-.8);step(7.0,7.8,1.6)
txt(10.8,1.6,r'$\mathrm{Ph_3COEt+PyH^+}$')
txt(6.8,.75,'Deprotonation: pyridine accepts H⁺; the O–H pair returns to oxygen.',11)
fig.tight_layout()
fig.savefig('2025-substitution-mechanisms.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
