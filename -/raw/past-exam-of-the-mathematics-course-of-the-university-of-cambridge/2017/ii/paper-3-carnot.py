"""2017 II3 Q34. Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
Dimensionless ideal-gas example, Nk_B = 1, γ = 5/3, T_h = 2, T_c = 1.
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/2017-ii-paper-3-mplconfig")
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,(ax,bx)=plt.subplots(1,2,figsize=(11,4.5),dpi=100,facecolor='white')
g=5/3;va,vb=1.,2.;vc=vb*2**(1/(g-1));vd=va*2**(1/(g-1))
legs=[(np.linspace(va,vb,150),lambda v:2/v,'#a34a35'),(np.linspace(vb,vc,150),lambda v:2*vb**(g-1)/v**g,'#555555'),(np.linspace(vc,vd,150),lambda v:1/v,'#1e537a'),(np.linspace(vd,va,150),lambda v:vd**(g-1)/v**g,'#555555')]
for v,p,col in legs:
 y=p(v);ax.plot(v,y,color=col,lw=2);j=65;ax.annotate('',xy=(v[j+16],y[j+16]),xytext=(v[j],y[j]),arrowprops=dict(arrowstyle='->',color=col,lw=2))
for label,v,p in [('A',va,2/va),('B',vb,2/vb),('C',vc,1/vc),('D',vd,1/vd)]:ax.scatter(v,p,color='black',s=16);ax.annotate(label,(v,p),xytext=(4,5),textcoords='offset points')
ax.set(xlabel='Volume V',ylabel='Pressure p',title='p–V cycle (clockwise engine)');ax.grid(alpha=.15)
sa=0.;sb=np.log(2)
pts=[(sa,2),(sb,2),(sb,1),(sa,1),(sa,2)]
for j,col in enumerate(['#a34a35','#555555','#1e537a','#555555']):
 a=np.array(pts[j]);b=np.array(pts[j+1]);bx.plot([a[0],b[0]],[a[1],b[1]],color=col,lw=2);bx.annotate('',xy=a+.65*(b-a),xytext=a+.35*(b-a),arrowprops=dict(arrowstyle='->',color=col,lw=2))
for label,(s,t) in zip('ABCD',pts):bx.annotate(label,(s,t),xytext=(5,5),textcoords='offset points')
bx.text(sb/2,2.1,'Heat absorbed',ha='center',color='#a34a35');bx.text(sb/2,.85,'Heat emitted',ha='center',color='#1e537a');bx.set(xlim=(-.15,.88),ylim=(.7,2.3),xlabel='Entropy S',ylabel='Temperature T',title='T–S cycle');bx.grid(alpha=.15)
fig.tight_layout();fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False);plt.close(fig)
