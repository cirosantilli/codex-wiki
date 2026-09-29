"""Original solution intermediates and electron flow for NST IA Chemistry 2024 Q3(b)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig,ax=plt.subplots(figsize=(11.2,7),facecolor='white');ax.set(xlim=(0,15),ylim=(-.4,10));ax.axis('off')
def txt(x,y,s,fs=13):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def line(a,b,n=1):
    for dy in ([0] if n==1 else [-.045,.045]):ax.plot([a[0],b[0]],[a[1]+dy,b[1]+dy],color='black',lw=1.3)
def flow(a,b,rad=.4):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',connectionstyle=f'arc3,rad={rad}',mutation_scale=13,color='#245f8a',lw=1.5))
def step(x1,x2,y):ax.annotate('',(x2,y),(x1,y),arrowprops={'arrowstyle':'->','lw':1.4})
txt(7.5,9.6,'Two eliminations: R = cyclohexyl',13)
txt(1.0,8.15,r'$\mathrm{B{:}^-}$');txt(3.1,8.15,r'$\mathrm{C(Cl)R}$');txt(5.0,8.15,r'$\mathrm{CH_2}$');line((3.75,8.15),(4.6,8.15))
txt(3.1,9,r'$\mathrm{Cl}$');line((3.1,8.4),(3.1,8.78));txt(5.0,9,r'$\mathrm{H}$');line((5,8.4),(5,8.78))
flow((1.5,8.35),(4.8,8.95),-.25);flow((4.9,8.6),(4.2,8.33),.5);flow((3.14,8.6),(3.32,8.95),-.6)
step(6,6.6,8.15);txt(8.3,8.15,r'$\mathrm{R-C(Cl)=CH_2}$',13);step(10.2,10.9,8.15);txt(10.55,8.75,'base / heat',10);txt(13,8.15,r'$\mathrm{R-C\equiv CH}$',14)
txt(7.5,7.3,'Repeat base → H, C–H → C–C, and C–Cl → Cl to form the triple bond.',10)
txt(7.5,6.55,'Lactone: addition–elimination opens the ring; a second addition gives the diol',12)
txt(1.0,5.2,r'$\mathrm{Me^-}$');txt(3.5,5.2,r'$\mathrm{C}$');txt(3.5,6,r'$\mathrm{O}$');line((3.44,5.42),(3.44,5.78));line((3.56,5.42),(3.56,5.78))
txt(2.25,5.2,r'$\mathrm{R}$');txt(4.85,5.2,r'$\mathrm{OR^{\prime}}$');line((2.5,5.2),(3.28,5.2));line((3.73,5.2),(4.4,5.2))
flow((1.45,5.36),(3.28,5.38),-.55);flow((3.62,5.6),(3.78,5.95),-.55)
step(5.6,6.3,5.2);txt(8.5,5.2,r'$\mathrm{^-O(CH_2)_4C(=O)Me}$',12)
step(10.65,11.3,5.2);txt(11,5.85,'MeMgI; H₂O',10);txt(13.1,5.2,r'$\mathrm{HO(CH_2)_4C(OH)Me_2}$',11)
txt(7.5,4.35,'First tetrahedral adduct collapses: O⁻ → C=O and acyl C–O → O, breaking the ring.',10)
txt(7.5,3.65,'Acid: water departure gives a tertiary cation, then intramolecular O attack closes six atoms',12)
txt(2.5,2.4,r'$\mathrm{HO(CH_2)_4C(OH_2^+)Me_2}$',12);flow((3.1,2.65),(4.1,2.9),-.5)
step(5.15,5.8,2.4);txt(8.0,2.4,r'$\mathrm{HO(CH_2)_4C^+Me_2}$',12)
# A broad return arrow indicates terminal alcohol O attack on tertiary C.
flow((6.55,2.65),(8.9,2.65),-.65)
step(10.3,11,2.4);txt(12.8,2.4,'cyclic oxonium',12)
txt(7.5,1.4,'Lose H⁺ → 2,2-dimethyloxane. Ring sequence: O–C(Me)₂–CH₂–CH₂–CH₂–CH₂.',11)
txt(7.5,.25,'Me⁻ indicates the carbon end of a Grignard reagent, not a freely solvated methyl anion.\nThe written open-chain ketone is the intermediate after acyl–oxygen cleavage.',10)
fig.tight_layout();fig.savefig('paper-1-organic-mechanisms.png',dpi=140,facecolor='white',bbox_inches='tight');plt.close(fig)
