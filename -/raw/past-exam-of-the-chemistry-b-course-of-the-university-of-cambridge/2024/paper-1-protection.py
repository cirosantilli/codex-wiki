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

fig,axs=plt.subplots(1,2,figsize=(12,5.5),facecolor='white')
a=axs[0];setup(a,(-3.4,3.4),(-2,2.8),'OH-directed epoxidation: same-face oxygen delivery')
ps=[(-2.2,-.3),(-.8,-.3),(.4,.6),(1.7,-.2)];
for i in range(3):d.bond(a,ps[i],ps[i+1],2 if i==0 else 1)
txt(a,(-2.95,.5),'Me');d.bond(a,ps[0],(-2.65,.35));txt(a,(2.2,-.4),'CH₂OPMB');d.wedge(a,ps[2],(.4,1.7),front=False);txt(a,(.4,1.9),'OH')
ox=(-1.55,.8);d.wedge(a,ps[0],ox,front=False);d.wedge(a,ps[1],ox,front=False);txt(a,ox,'O',15,'#b2472c');d.bond(a,(-1.2,1.3),(.1,1.8),style='dotted',color='#b2472c');txt(a,(-1.5,2.45),'Hydrogen-bonded peracid approach',10)
# Erase false retained alkene: epoxide C-C is single in product.
a.lines[0].remove();a.lines[0].remove();d.bond(a,ps[0],ps[1]);txt(a,(0,-1.5),'Rear/hashed epoxide face matches the original OH face.',10)
a=axs[1];setup(a,(-3.1,3.1),(-2.4,2.8),'Acetonide: original C–O configurations retained')
ps=[np.array(v) for v in [(-.65,.6),(.65,.6),(1.05,-.65),(0,-1.4),(-1.05,-.65)]];d.ring(a,ps);txt(a,ps[2],'O');txt(a,ps[4],'O');txt(a,ps[3],'CMe₂')
d.wedge(a,ps[0],(-1.9,1.5),front=False);txt(a,(-2.15,1.8),'alkynyl chain',10);d.wedge(a,ps[1],(1.8,1.5),front=True);txt(a,(2,1.8),'CH₂OPMB',10)
for i in [0,1]:txt(a,ps[i]+np.array([0,-.25]),'*',13,d.BLUE)
txt(a,(0,-2),'Side chains trans; acetal CMe₂ is not stereogenic.',10)
save(fig,'paper-1-protection.png')
