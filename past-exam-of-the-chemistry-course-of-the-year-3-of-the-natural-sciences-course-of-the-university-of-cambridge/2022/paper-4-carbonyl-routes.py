"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(3,1,figsize=(10.8,6.5),layout='constrained')
rows=[
('CDI amidation',[
r'$\mathrm{RCO_2^- + ImCOIm}$',r'$\mathrm{RCO{-}O{-}COIm}$',r'$\mathrm{RCOIm + CO_2}$',r'$\mathrm{RCONHR^\prime}$']),
('Hydroxylactam opening / HWE / aza-Michael',[
'Cyclic hemiaminal',r'$\mathrm{MeNHCO{-}CH(OBn){-}CH_2{-}CHO}$','Open-chain enone','5-Acetonyl lactam']),
('Propargyl activation / indole closure / carbene trapping',[
'Activated propargyl alcohol','Propargyl ↔ allenyl cation','Indole–C:(Ph)','Arene expansion or C–H insertion'])]
for ax,(title,labels) in zip(axes,rows):
    for i,label in enumerate(labels):
        x=i*3.2
        ax.text(x,0,label,ha='center',va='center',fontsize=9,bbox={'boxstyle':'round,pad=.45','facecolor':'#eef4fa','edgecolor':'#2166ac'})
        if i<3:ax.annotate('',xy=(x+2.25,-.25),xytext=(x+.95,-.25),arrowprops={'arrowstyle':'->','color':'.25'})
    ax.set(xlim=(-1.5,11),ylim=(-.7,.7),title=title);ax.axis('off')
fig.suptitle('Distinct activation and bond-forming steps; structures abbreviated')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
