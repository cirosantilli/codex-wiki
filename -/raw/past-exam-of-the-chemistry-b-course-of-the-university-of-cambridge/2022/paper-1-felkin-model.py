"""Original solution diagram; Python 3.14, numpy and matplotlib.
The PNG output basename is relative to the current working directory.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, wedge, atom, ring, curly, flow, finish, save, BLUE, ORANGE, GREEN
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(a,b)=plt.subplots(1,2,figsize=(11,5))
a.add_patch(Circle((0,0),.43,fill=False,color=BLUE,lw=1.6));a.plot(0,0,'o',color='0.1',ms=6)
# View down carbonyl C -> alpha C. Back substituents are blue.
for angle,label in [(90,'Ph (large)'),(-30,'vinyl (medium)'),(210,'H (small)')]:
 th=np.deg2rad(angle);u=np.array([np.sin(th),np.cos(th)]);bond(a,.43*u,1.35*u,color=BLUE);atom(a,1.65*u,label,11,color=BLUE)
bond(a,(0,0),(0,1.25),2);atom(a,(0,1.5),'O',14);bond(a,(0,0),(0,-1.25));atom(a,(0,-1.55),'Ph of ketone',10)
a.annotate('',(-.15,-.15),(-2,-.61),arrowprops={'arrowstyle':'->','lw':2,'color':ORANGE});a.text(-1.9,-2.05,'nPr⁻: past H,\naway from alpha Ph',ha='center',fontsize=10,color=ORANGE);a.text(0,2.1,'Front: carbonyl C. Blue circle: alpha C.',ha='center',fontsize=10);finish(a,(-2.9,2.5),(-2.3,2.5),'Preferred Felkin–Anh Newman arrangement')
k=np.array([-.6,0]);ca=np.array([.8,-.7]);bond(b,k,ca);bond(b,k,(-1.7,-.7));atom(b,(-1.7,-.7),'Ph');bond(b,ca,(1.85,0));atom(b,(1.85,0),'Ph');wedge(b,k,(-1.15,1),True);atom(b,(-1.15,1),'OH');wedge(b,k,(.1,1.15),False);atom(b,(.1,1.15),'nPr');wedge(b,ca,(.8,-1.8),False);atom(b,(.8,-1.8),'vinyl');b.text(0,2.1,'A: OH forward, nPr backward.',ha='center',fontsize=11,color=ORANGE);b.text(0,-2.35,'The original alpha-carbon configuration is retained.',ha='center',fontsize=10);finish(b,(-2.5,2.5),(-2.7,2.5),'Product A, independently reconstructed local structure')
fig.tight_layout();fig.savefig('paper-1-felkin-model.png',dpi=140,facecolor='white',bbox_inches='tight',pad_inches=.18);plt.close(fig)
