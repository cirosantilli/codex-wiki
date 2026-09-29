# Original exam-solution diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
# Run beside the eventual paper with its working directory set to the mirrored _media directory.
import os
import tempfile
from pathlib import Path
# A caller may reuse its fresh publication namespace; standalone runs create one.
_cache_root = Path(os.environ['PAPER_338_PUBLICATION_CACHE']) if os.environ.get('PAPER_338_PUBLICATION_CACHE') else Path(tempfile.mkdtemp(prefix='2017-iii-paper-338-publication-', dir='/tmp'))
os.environ['MPLCONFIGDIR'] = str(_cache_root / 'mpl-cache')
os.environ['XDG_CACHE_HOME'] = str(_cache_root / 'xdg-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white','savefig.transparent':False})

from matplotlib.patches import Ellipse
fig=plt.figure(figsize=(11,5.6),dpi=100);ax=fig.add_axes([.02,.24,.68,.64]);pr=fig.add_axes([.75,.28,.22,.55])
ax.set(xlim=(-.8,10.7),ylim=(-1.7,5.6));ax.set_aspect('equal');ax.axis('off')
ax.plot([0,0],[-1,1],color='#174b83',lw=4);ax.text(-.55,-1.5,'Telescope')
ax.plot([2,2],[-.9,-.12],color='black',lw=3);ax.plot([2,2],[.12,.9],color='black',lw=3);ax.text(1.7,-1.3,'Slit')
ax.add_patch(Ellipse((4,0),.22,1.7,fill=False,edgecolor='#174b83',lw=2));ax.text(3.3,-1.3,'Collimator')
ax.plot([5.4,6.6],[.6,-.6],color='black',lw=4);ax.text(5.65,-1.25,'Grating')
# Emergent beam inclined towards camera and detector.
cam=np.array([8.,2.]);det=np.array([10.,4.]);normal=np.array([1.,-1.])/np.sqrt(2)
ax.plot(*(np.array([cam-.8*normal,cam+.8*normal]).T),color='#174b83',lw=4);ax.text(7.55,1.05,'Camera')
ax.plot(*(np.array([det-.5*normal,det+.5*normal]).T),color='black',lw=4);ax.text(9.6,4.7,'Detector')
for y in [-.55,.55]:
 ax.plot([0,2,4,6-y],[y,0,y,y],color='#d67000',lw=1.3)
 start=np.array([6.-y,y]);end=cam+np.array([-y,y]);ax.plot(*np.array([start,end,det]).T,color='#d67000',lw=1.3)
for a,b in [((.4,.35),(1.1,.1)),((4.4,.55),(5.2,.55)),((6.5,1),(7.2,1.65))]:ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color='#d67000'))
pr.plot([-1.1,-.5,-.5,.5,.5,1.1],[0,0,1,1,0,0],color='#1c709e',lw=2);pr.set(xlim=(-1.2,1.2),ylim=(-.22,1.25),xticks=[-.5,.5],xticklabels=[r'$-p/2$',r'$p/2$'],yticks=[0,1],xlabel='Detector position',ylabel='Intensity');pr.set_title('Uniform monochromatic\nslit image',fontsize=11)
pr.annotate('',xy=(.5,-.12),xytext=(-.5,-.12),arrowprops=dict(arrowstyle='<->'));pr.text(0,-.17,r'$p$',ha='center');pr.spines[['top','right']].set_visible(False)
fig.text(.08,.08,r'Slit-limited separation: $\Delta\lambda=p/q$, resolving power $R=\lambda q/p$',fontsize=13)
fig.suptitle('Reflection-grating spectrograph and slit-limited profile',fontsize=14)
fig.savefig('paper-338-spectrograph.png',dpi=100);plt.close(fig)
