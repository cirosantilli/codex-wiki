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

fig,axs=plt.subplots(1,2,figsize=(12,5.7),facecolor='white')
a=axs[0];setup(a,(-3,3),(-2.7,2.7),'Five-membered osmate ester')
ps=[np.array(v) for v in [(-.7,-.8),(.7,-.8),(1.1,.4),(0,1.1),(-1.1,.4)]];d.ring(a,ps);txt(a,ps[0],'CH₂');txt(a,ps[1],'CH–R');txt(a,ps[2],'O');txt(a,ps[3],'Os');txt(a,ps[4],'O')
for dx in [-.7,.7]:d.bond(a,(0,1.1),(dx,2),2);txt(a,(dx,2.2),'O')
txt(a,(0,-1.8),'Hydrolysis cleaves Os–O, retaining both C–O bonds.',10);txt(a,(0,-2.3),'Product: HOCH₂–CH(OH)–R',11)
a=axs[1];setup(a,(-3.4,3.4),(-2.7,2.7),'O-directed trans hydroalumination')
# Cycle O–CH2–Cnear=Cfar–Al: H on Cnear opposite Al on Cfar.
ps=[np.array(v) for v in [(-1.6,.8),(-1.8,-.5),(-.6,-1.1),(.6,-.6),(0,1.0)]];d.ring(a,ps,{2:2});
for i,s in [(0,'O'),(1,'CH₂'),(2,'C'),(3,'C'),(4,'Al')]:txt(a,ps[i],s,13)
d.bond(a,ps[2],(-1,-2));txt(a,(-1.15,-2.25),'H');d.bond(a,ps[3],(1.9,-.85));txt(a,(2.3,-.95),'R');txt(a,(1.35,1.75),'[aluminate]',10,d.BLUE)
txt(a,(0,2.35),'Cnear–H and Cfar–Al are anti.',11);txt(a,(0,-2.6),'H₂O: C–Al → C–H, giving E allylic alcohol.',10)
save(fig,'paper-1-osmate-aluminate.png')
