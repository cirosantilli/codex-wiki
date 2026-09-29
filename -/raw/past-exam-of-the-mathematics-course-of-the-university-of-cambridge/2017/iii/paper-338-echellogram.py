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

fig,ax=plt.subplots(figsize=(9,5),dpi=100);fig.subplots_adjust(left=.11,right=.94,bottom=.15,top=.87)
for m,label,col in [(10,r'Order $m$','#1e7398'),(11,r'Order $m+1$','#a35121')]:
 lam=np.linspace(1/(m+.65),1/(m-.65),200);x=10*(m*lam-1);y=100*lam
 ax.plot(x,y,color=col,lw=2.5);ax.text(x[5],y[5]+.17,label,color=col);k=120;ax.annotate('',xy=(x[k+18],y[k+18]),xytext=(x[k],y[k]),arrowprops=dict(arrowstyle='->',color=col,lw=2));ax.text(x[k]+.02,y[k]-.26,r'$\lambda$ increases',color=col,fontsize=10)
 ax.plot(0,100/m,'o',color=col);ax.text(.04,100/m+.05,r'$K/m$' if m==10 else r'$K/(m+1)$',fontsize=10,color=col)
ax.axvline(0,color='#777777',ls='--');ax.set(xlim=(-.85,.85),ylim=(8.25,11.05),xlabel='Main echelle dispersion: increasing wavelength →',ylabel='Cross dispersion: increasing wavelength ↑');ax.set_xticks([]);ax.set_yticks([]);ax.grid(alpha=.15);ax.set_title('Two adjacent cross-dispersed echelle orders (schematic)')
ax.text(.01,10.88,'y axis / camera optical axis',fontsize=9,color='#666666')
fig.savefig('paper-338-echellogram.png',dpi=100);plt.close(fig)
