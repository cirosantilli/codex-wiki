"""Original wedge/dash structures; configurations independently checked."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
from tools.chemistry_diagram import *
fig,axs=plt.subplots(3,2,figsize=(11,10.2),layout='constrained',facecolor='white')
entries=[('cis: (2R,3S)',(1,1),False),('cis: (2S,3R)',(-1,-1),False),('trans: (2R,3R)',(1,-1),False),('trans: (2S,3S)',(-1,1),False),('Epoxide: front face',(1,1),True),('Epoxide: mirror image',(-1,-1),True)]
for ax,(title,faces,epox) in zip(axs.flat,entries):
 indanone(ax,epoxide=epox,faces=faces);finish(ax,(-2.3,2.4),(-2.2,1.85),title)
fig.suptitle('Top rows: implicit H is opposite each drawn Ph wedge. Bottom row: the carbonyl is retained.',fontsize=12)
save(fig,'paper-1-indanone-stereoisomers.png')
