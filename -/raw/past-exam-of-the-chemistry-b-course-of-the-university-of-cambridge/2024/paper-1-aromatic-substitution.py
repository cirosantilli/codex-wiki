"""Original solution diagram; Python 3.14, numpy, matplotlib. Output PNG goes to cwd."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import chemistry_diagram as d
plt.rcParams.update({'font.size':11})
def txt(a,p,s,size=12,color='0.15'):d.atom(a,p,s,size=size,color=color)
def setup(a,x=(-3,3),y=(-2.5,2.5),title=None):d.finish(a,x,y,title)
def save(fig,name):
 fig.tight_layout();fig.savefig(name,dpi=165,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)

fig,axs=plt.subplots(2,1,figsize=(12,7),facecolor='white')
for a in axs:setup(a,(-.4,12),(-1.6,2.1))
for a,title,end in [(axs[0],'Fluoride substitution: nucleophile retains OPh','p-NO₂–Ar–C(Ph)(OPh)CN'),(axs[1],'Hydrogen substitution: nucleophile sacrifices OPh','p-NO₂–Ar–CH(Ph)CN')]:
 a.set_title(title,fontsize=12,weight='bold');txt(a,(1,0),'PhC⁻(OPh)CN',13);d.flow(a,(2.5,0),(3.3,0));txt(a,(5,0),'σ-adduct',14);d.flow(a,(6.2,0),(7.2,0));txt(a,(9.7,0),end,12)
txt(axs[0],(5,.9),'ipso carbon bears F',12);txt(axs[0],(5,-.9),'F⁻ leaves; aromaticity returns',11)
txt(axs[1],(5,.9),'addition carbon still bears H',12);txt(axs[1],(5,-.8),'base removes H; OPh⁻ leaves',11);txt(axs[1],(9.5,-.8),'aromatic side-chain anion → H⁺ workup',10)
fig.text(.5,.03,'The sigma-H adduct is not rearomatized by expelling H⁻. The nucleophile-borne leaving group enables elimination.',ha='center',fontsize=10)
save(fig,'paper-1-aromatic-substitution.png')
