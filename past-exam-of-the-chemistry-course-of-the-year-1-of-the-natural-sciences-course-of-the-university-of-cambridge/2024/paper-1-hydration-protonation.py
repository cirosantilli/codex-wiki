"""Original electron-pair arrows for hydration and carbide protonation."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig,ax=plt.subplots(figsize=(11,6.3),facecolor='white');ax.set(xlim=(-.2,14.8),ylim=(-.7,8));ax.axis('off')
def txt(x,y,s,fs=13):ax.text(x,y,s,ha='center',va='center',fontsize=fs,bbox={'facecolor':'white','edgecolor':'none','pad':1})
def bond(a,b,n=1):
    for off in ([0] if n==1 else [-.05,.05] if n==2 else [-.08,0,.08]):ax.plot([a[0],b[0]],[a[1]+off,b[1]+off],color='black',lw=1.3)
def flow(a,b,rad=.4):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',connectionstyle=f'arc3,rad={rad}',mutation_scale=13,color='#245f8a',lw=1.5))
def step(x1,x2,y):ax.annotate('',(x2,y),(x1,y),arrowprops={'arrowstyle':'->','lw':1.4})
txt(7.2,7.7,'Water donates a lone pair to the electrophilic carbon',12)
for x,s in [(1.8,r'$\mathrm{O}$'),(3.4,r'$\mathrm{C}$'),(5,r'$\mathrm{O}$')]:txt(x,6.25,s)
bond((2,6.25),(3.2,6.25),2);bond((3.6,6.25),(4.8,6.25),2)
txt(3.4,7.1,r'$\mathrm{H_2O{:}}$');flow((3.82,6.95),(3.5,6.42),-.5);flow((4.2,6.32),(4.85,6.48),-.7)
step(5.7,6.3,6.25);txt(8.1,6.25,r'$\mathrm{^-O-C(=O)-OH_2^+}$',12)
step(9.8,10.5,6.25);txt(10.2,6.8,'proton relay',10);txt(12.8,6.25,r'$\mathrm{HO-C(=O)-OH}$',13)
txt(7.2,5.35,'Allene branch: protonate each terminal carbanion twice',12)
def start(cy,leftcharge,bonds):
    txt(.9,cy,leftcharge);txt(2.4,cy,r'$\mathrm{C}$');txt(3.9,cy,r'$\mathrm{C^-}$' if bonds[0]==1 else r'$\mathrm{C^{2-}}$')
    bond((1.2,cy),(2.2,cy),bonds[0]);bond((2.6,cy),(3.6,cy),bonds[1])
    txt(.9,cy+.9,r'$\mathrm{H}$');txt(2.3,cy+.9,r'$\mathrm{OH}$');bond((1.12,cy+.9),(1.96,cy+.9))
    flow((.7,cy+.16),(.73,cy+.73),-.45);flow((1.55,cy+.95),(2.1,cy+1.1),-.7)
start(3.7,r'$\mathrm{C^{2-}{:}}$',[2,2]);step(4.65,5.25,3.7);txt(7.2,3.7,r'$\mathrm{HC^-=C=C^{2-}}$',12)
step(9,9.75,3.7);txt(9.4,4.3,'3 more H₂O',10);txt(12.1,3.7,r'$\mathrm{CH_2=C=CH_2}$',14)
txt(7.2,2.6,'Propyne branch: three H at one end, one H at the acetylide end',12)
start(.95,r'$\mathrm{C^{3-}{:}}$',[1,3]);step(4.65,5.25,.95);txt(7.2,.95,r'$\mathrm{HC^{2-}-C\equiv C^-}$',12)
step(9,9.75,.95);txt(9.4,1.55,'3 more H₂O',10);txt(12.1,.95,r'$\mathrm{CH_3-C\equiv CH}$',14)
txt(7.2,-.25,'Each water proton transfer moves O–H electrons onto O and releases OH⁻.\nCharged starting drawings are resonance contributors, not separately isolated reactants.',10)
fig.tight_layout();fig.savefig('paper-1-hydration-protonation.png',dpi=140,facecolor='white',bbox_inches='tight');plt.close(fig)
