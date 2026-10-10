"""Original functional schematic. Python 3.14, matplotlib 3.10.7.
Run from _media; writes the matching PNG to the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig = plt.figure(figsize=(10, 6.6), facecolor='white')
ax = fig.add_axes([.03,.51,.94,.40]); ax.set(xlim=(0,10),ylim=(0,4)); ax.axis('off')
blue, orange, gray = '#245a81', '#ac4c12', '#40515d'
fig.suptitle('Lamb–Retherford: detect the atoms that remain metastable', fontsize=16, y=.97)
labels = [('Hot tungsten oven\nH₂ → H + H', .1, 1.4), ('Slit + electron impact\nprepare some H(2S)',2.35,1.4), ('Microwave region\ninside static B',4.85,1.4), ('Metal target\n+ electron collector',7.5,1.4)]
for label,x,y in labels:
    ax.add_patch(FancyBboxPatch((x,y),2.05,1.1,boxstyle='round,pad=0.04',facecolor='#eef5fa',edgecolor=blue,lw=1.4))
    ax.text(x+1.025,y+.55,label,ha='center',va='center',fontsize=10)
for x1,x2 in [(2.18,2.28),(4.48,4.78),(6.98,7.43)]:
    ax.annotate('',(x2,1.95),(x1,1.95),arrowprops=dict(arrowstyle='->',color=blue,lw=2))
ax.text(5.88,3.3,'Microwaves on resonance: 2S → 2P → 1S',ha='center',color=orange,fontsize=11)
ax.annotate('Crossing electron stream', (3.35,2.5),(3.35,3.5),ha='center',arrowprops=dict(arrowstyle='->',color=gray),fontsize=10)
ax.text(1.1,.65,'Neutral hydrogen beam →',ha='center',fontsize=10,color=blue)
ax.text(8.53,.65,'Ejected electrons → current I',ha='center',fontsize=10,color=blue)
ax.annotate('',(8.53,.95),(8.53,1.35),arrowprops=dict(arrowstyle='->',color=blue))
ax2=fig.add_axes([.08,.13,.43,.32]);ax2.set(xlim=(0,6),ylim=(0,4));ax2.axis('off')
for y,label in [(3.2,r'$2S_{1/2}$: long lived'),(2.35,r'$2P_{1/2}$: short lived'),(.3,r'$1S_{1/2}$: ground state')]:
    ax2.plot([.15,2.1],[y,y],lw=2,color=blue);ax2.text(2.35,y,label,va='center',fontsize=11)
ax2.annotate('',(1.0,2.38),(1.0,3.17),arrowprops=dict(arrowstyle='->',color=orange,lw=2))
ax2.text(.9,2.78,'microwave',ha='right',fontsize=9,color=orange)
ax2.annotate('',(1.5,.35),(1.5,2.3),arrowprops=dict(arrowstyle='->',color=gray,lw=2))
ax2.text(1.65,1.35,'rapid photon\nemission',fontsize=10,color=gray)
fig.text(.56,.39,'At a fixed microwave frequency, sweep B.',fontsize=12)
fig.text(.56,.32,'On resonance, fewer 2S atoms survive.',fontsize=12,color=orange)
fig.text(.56,.25,'The ground-state atoms give no useful',fontsize=11)
fig.text(.56,.20,'metastable-electron-ejection signal.',fontsize=11)
fig.text(.56,.13,'Readout: I(off) − I(on) > 0.',fontsize=12,color=blue)
fig.text(.5,.035,'Original functional schematic; one zero-field level pair shown. Geometry and energy gaps are not to scale.',ha='center',fontsize=10,color=gray)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'),dpi=140,facecolor='white')
plt.close(fig)
