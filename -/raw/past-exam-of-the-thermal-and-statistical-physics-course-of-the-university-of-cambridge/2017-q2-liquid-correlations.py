"""Illustrative liquid pair structure, not measured data; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

r=np.linspace(0,5,1500)
g=np.zeros_like(r)
out=r>=1
g[out]=1+1.4*np.exp(-1.1*(r[out]-1))*np.cos(6*(r[out]-1))
fig,ax=plt.subplots(figsize=(6.8,4.2),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.axhline(1,color='#777777',lw=1,ls='--',label='Uncorrelated reference')
ax.plot(r,g,color='#165b99',lw=2,label='Illustrative liquid-like pair structure')
ax.axvspan(0,1,color='#e7e7e7')
ax.text(.48,.35,'Core\nexclusion',ha='center',fontsize=10)
ax.annotate('First coordination shell',xy=(1.03,2.34),xytext=(1.7,2.3),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.set(xlim=(0,5),ylim=(0,2.65),xlabel=r'$r/d$ (core diameter $d$)',ylabel=r'$g(r)$',title='Conditional pair density relative to the bulk density')
ax.legend(loc='upper right',fontsize=8,framealpha=.95)
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
