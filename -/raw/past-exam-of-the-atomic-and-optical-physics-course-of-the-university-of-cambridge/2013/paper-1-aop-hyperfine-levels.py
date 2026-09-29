"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained');field=np.linspace(0,3,700);I=1.5;gJ=2;gI=0;S=I+.5
colors={-2:'#286aa0',-1:'#40a0aa',0:'#666666',1:'#d18a2d',2:'#b33c3c'}
for m in [-1,0,1]:
 root=np.sqrt(S*S+2*m*(gJ-gI)*field+(gJ-gI)**2*field**2)
 for sign,style,branch in [(1,'-','+'),(-1,'--','−')]:ax.plot(field,-.25+gI*m*field+sign*root/2,color=colors[m],ls=style,label=f'm = {m}, {branch} branch')
for sign in [-1,1]:
 m=sign*S;ax.plot(field,I/2+sign*field*(gJ/2+gI*I),color=colors[int(m)],lw=2,label=f'm = {int(m)}, stretched')
ax.text(.03,.85,'F = 2 at zero field',fontsize=9);ax.text(.03,-1.58,'F = 1 at zero field',fontsize=9)
ax.set(xlabel='field μB B / A',ylabel='energy / A',title='Illustrative J = 1/2, I = 3/2, A > 0, gJ = 2, gI = 0');ax.grid(alpha=.18);ax.legend(loc='center left',bbox_to_anchor=(1,.5),fontsize=8)
fig.suptitle('Hyperfine coupling crosses over to uncoupled electronic and nuclear projections')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
