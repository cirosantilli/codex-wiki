"""Original solution diagram. Python 3.14 / matplotlib 3.10 / numpy 2.3.
Run from the mirrored media directory; output is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,ring,curly,flow,finish,save,BLUE,ORANGE

fig,ax=plt.subplots(figsize=(11,4.4));finish(ax,(-1,13),(-1.7,3.2),'A Grignard route to the racemic epoxide')
atom(ax,(.6,2),'Ar–MgBr',16);atom(ax,(4.2,2),'Ar–CH(OH)–CH₃',16);atom(ax,(9.2,2),'Ar–CH=CH₂',16)
flow(ax,(1.8,2),(2.6,2),'1. CH₃CHO; 2. H₃O⁺');flow(ax,(6.1,2),(7.7,2),'cat. TsOH; heat')
ax.text(.6,2.8,'From ArBr: Mg, dry ether',ha='center',fontsize=10,color=BLUE)
flow(ax,(9.2,1.5),(9.2,.4),'mCPBA')
a=(8.7,-.3);b=(10,-.3);o=(9.35,-1.2);ring(ax,[a,b,o]);atom(ax,o,'O');bond(ax,a,(7.8,-.3));atom(ax,(7.4,-.3),'Ar')
ax.text(3.2,-.15,'Ar = 4-methoxyphenyl',ha='center',fontsize=13,color=BLUE);ax.text(3.2,-.85,'Planar alkene → attack on either face',ha='center',fontsize=11)
save(fig,Path(__file__).with_suffix('.png').name)
