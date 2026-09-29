"""Generate a periodic two-state motor occupancy sketch; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

Delta=1.;x1=.1;x2=.65;k1=6.;k2=10.;u=.3
A=np.exp(-k1*x1/u);B=np.exp(-k2*(Delta-x2)/u)
pb=(1-A)/(1-A*B);p0=B*pb
x=np.linspace(0,Delta,3001)
p=np.where(x<x1,1-(1-p0)*np.exp(-k1*x/u),np.where(x<x2,pb,pb*np.exp(-k2*(x-x2)/u)))
fig,ax=plt.subplots(figsize=(7.2,4.2),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.axvspan(0,x1,color='#dbeed5');ax.axvspan(x1,x2,color='#e9eef5');ax.axvspan(x2,1,color='#fbe5d0')
ax.plot(x,p,color='#1764a0',lw=2)
ax.set(xlim=(0,1),ylim=(-.02,1.05),xlabel=r'Phase $x/\Delta$',ylabel=r'Bound probability $P_{\rm ss}$',title='Attachment, protected interval, detachment')
ax.set_xticks([0,x1,x2,1],['0',r'$x_1/\Delta$',r'$x_2/\Delta$','1'])
ax.axhline(pb,color='.45',lw=.8,ls='--');ax.text(.4,pb+.04,r'$p_b\simeq1-e^{-k_1x_1/u}$',ha='center')
ax.text(.03,.37,'Rising',rotation=80);ax.text(.4,.40,'Plateau',ha='center');ax.text(.81,.4,'Tail',ha='center')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white',transparent=False)
