"""Printed-metric Minkowski diamond and explicitly qualified AdS-cover strip.
Tested: Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Output: paper-59-causal-structures.png in caller CWD. Preserve caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10.3,5.4),dpi=135,facecolor='white')
a=axes[0]
x=[0,1,0,-1,0];y=[1,0,-1,0,1]
a.fill(x,y,color='#edf3fa');a.plot(x,y,color='#1d4b79',lw=2)
a.plot([-.98,.98],[0,0],color='#297b53',lw=2,label='Cauchy slice')
for end in [-1,1]:a.plot([0,end*.5],[0,.5],ls='--',color='#7794ad',lw=1.2)
a.scatter([0],[0],c='#1d4b79',s=25)
a.text(0,1.10,r'$i^+$',ha='center',fontsize=15);a.text(0,-1.17,r'$i^-$',ha='center',fontsize=15)
a.text(-1.13,0,r'$i^0$',ha='center',fontsize=15);a.text(1.13,0,r'$i^0$',ha='center',fontsize=15)
a.text(.77,.68,'future null infinity',rotation=-45,ha='center',fontsize=9)
a.text(.77,-.68,'past null infinity',rotation=45,ha='center',fontsize=9)
a.text(0,-.18,'Cauchy slice',ha='center',color='#297b53',fontsize=10)
a.set_title('Printed time-dependent lapse\nMinkowski diamond',fontsize=12)
a.set_xlim(-1.43,1.43);a.set_ylim(-1.5,1.5);a.set_aspect('equal');a.axis('off')
b=axes[1]
b.fill_between([-1,1],-1.48,1.48,color='#edf3fa')
for side in [-1,1]:
    b.plot([side,side],[-1.48,1.48],ls='--',lw=2,color='#a45724')
    b.text(side*1.35,0,'timelike\nboundary\n(excluded)',ha='center',va='center',fontsize=8.5,color='#91431c')
    b.plot([0,side],[0,1],lw=1.5,color='#1d4b79')
    b.plot([0,side],[0,-1],lw=1.5,color='#1d4b79')
    b.annotate('',xy=(side,1.55),xytext=(side,1.37),arrowprops={'arrowstyle':'->','color':'#a45724'})
    b.annotate('',xy=(side,-1.55),xytext=(side,-1.37),arrowprops={'arrowstyle':'->','color':'#a45724'})
b.plot([0,0],[-1.45,1.45],lw=1,color='#297b53')
b.text(0,1.18,'cover time is unbounded',ha='center',fontsize=8.5)
b.text(0,-1.22,r'$-\pi/2<\rho<\pi/2$',ha='center',fontsize=10)
b.scatter([0],[0],c='#1d4b79',s=25)
b.set_title('Qualified spatial-lapse interpretation\nAnti-de Sitter conformal strip',fontsize=12)
b.set_xlim(-1.65,1.65);b.set_ylim(-1.6,1.6);b.set_aspect('equal');b.axis('off')
fig.text(.5,.025,'Conformal boundaries are not part of either physical spacetime. Null rays are at 45 degrees.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.07,1,1]);fig.savefig('paper-59-causal-structures.png',facecolor='white',transparent=False);plt.close(fig)
