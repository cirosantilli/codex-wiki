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

fig,axs=plt.subplots(2,1,figsize=(11,6.5),facecolor='white')
a=axs[0];setup(a,(-1,10),(-1.3,2.1),'1  Nucleophilic displacement at silicon, twice')
for p,s in [((0,0),'Me⁻'),((3,0),'SiMe₃'),((4.8,0),'O–R'),((7.3,0),'SiMe₄'),((9.3,0),'⁻O–R')]:txt(a,p,s,15)
d.bond(a,(3.55,0),(4.25,0));d.curly(a,(.65,.1),(2.3,.1),-.25);d.curly(a,(4.05,-.08),(4.8,-.3),.25);d.flow(a,(5.5,0),(6.4,0))
txt(a,(4.3,1.3),'R–O⁻ = enolate oxygen or phenoxide oxygen',12);txt(a,(4.3,-1),'Each liberated oxygen retains its original carbon attachment.',11)
a=axs[1];setup(a,(-1,10),(-1.8,2),'2  Addition–elimination at a chloroformate carbonyl')
for p,s in [((0,0),'R–O⁻'),((3,0),'C'),((3,1),'O'),((4.2,-.55),'O–allyl'),((1.9,-.55),'Cl'),((8,0),'R–O–C(O)–O–allyl')]:txt(a,p,s,14)
d.bond(a,(3,.2),(3,.8),2);d.bond(a,(3,0),(4,-.45));d.bond(a,(3,0),(2.1,-.45));d.curly(a,(.7,.15),(2.6,.15),-.25);d.curly(a,(3.08,.55),(3.35,.95),-.3);d.flow(a,(5,0),(6.2,0))
txt(a,(7.7,1),'via tetrahedral intermediate',11);txt(a,(4.2,-1.35),'Collapse expels Cl⁻; both anionic oxygen sites become carbonates.',11)
save(fig,'paper-1-oxygen-trapping.png')
