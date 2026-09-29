"""Original layered-flow diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Writes the same-basename opaque PNG to cwd. Respect caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,1,700);K=1+9*x
fig,ax=plt.subplots(figsize=(8,4),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.fill_between(x,0,x,color='#fddbc7');ax.fill_between(x,x,1,color='#d1e5f0')
ax.plot(x,x,color='black',lw=1.3,label='permeability interface')
for r in [.08,.25,.5,.75,.92]:
 y=np.where(r<=10*x/K,r*K/10,1-(1-r)*K)
 ax.plot(x,y,color='#2166ac',lw=1.8)
 j=360
 ax.annotate('',(x[j+18],y[j+18]),(x[j],y[j]),arrowprops={'arrowstyle':'->','color':'#2166ac'})
 ax.text(-.025,r,f'{r:g}',ha='right',va='center',fontsize=9)
ax.text(.70,.22,'Lower wedge: k₁ = 10 k₂',ha='center')
ax.text(.3,.87,'Upper wedge: k₂',ha='center')
ax.set(xlim=(0,1),ylim=(0,1),xlabel='x/L',ylabel='y/H',title='Conserved inlet stream labels r = y₀/H; vertical scale stretched')
ax.legend(loc='upper left',fontsize=8)
fig.savefig(Path(__file__).stem+'.png',dpi=100,facecolor='white',transparent=False)
