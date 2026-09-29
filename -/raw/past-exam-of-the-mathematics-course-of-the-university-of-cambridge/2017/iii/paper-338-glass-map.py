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

from matplotlib.patches import Polygon
fig,ax=plt.subplots(figsize=(9,5.2),dpi=100);fig.subplots_adjust(left=.10,right=.97,bottom=.14,top=.90)
crown=np.array([[95,1.44],[60,1.48],[45,1.58],[42,1.84],[56,1.85],[72,1.65],[95,1.50]])
flint=np.array([[60,1.50],[45,1.52],[20,1.76],[20,2.02],[40,1.96],[53,1.73]])
ax.add_patch(Polygon(crown,facecolor='#66b7e8',edgecolor='#116799',alpha=.3));ax.add_patch(Polygon(flint,facecolor='#ed9365',edgecolor='#bc500f',alpha=.3))
ax.text(78,1.59,'Crown families\nlarge $V_d$',color='#116799');ax.text(31,1.89,'Flint families\nsmall $V_d$',color='#a54812');ax.text(56,1.81,'High-index crowns\n(overlap is possible)',color='#116799',fontsize=10)
for V,n,label,offset in [(64.17,1.51680,'N-BK7HT',(5,-25)),(36.37,1.62004,'F2HT',(5,-22))]:ax.plot(V,n,'ko',ms=5);ax.annotate(label,(V,n),xytext=offset,textcoords='offset points',fontsize=10)
ax.set(xlim=(95,15),ylim=(1.43,2.04),xlabel=r'Abbe number $V_d=(n_d-1)/(n_F-n_C)$',ylabel=r'Refractive index $n_d$');ax.grid(alpha=.25);ax.set_title('Schematic Abbe diagram: representative optical-glass regions')
fig.savefig('paper-338-glass-map.png',dpi=100);plt.close(fig)
