"""Original figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(8.0,4.6),layout='constrained')
a=-5/128;b=-1/128
ax.hlines(0,.08,.34,lw=2.8,color='.35');ax.text(.21,.003,'Unperturbed n = 2',ha='center');ax.text(.21,-.006,'8 substates',ha='center',fontsize=10)
for y in [a,b]:ax.plot([.34,.61],[0,y],':',color='.6');ax.hlines(y,.61,.96,lw=2.8,color='#225f8c')
ax.text(.79,a+.0025,r'$2S_{1/2},\ 2P_{1/2}$',ha='center');ax.text(.79,a-.004,'4 substates; fine-structure degeneracy',ha='center',fontsize=9)
ax.text(.79,b+.0025,r'$2P_{3/2}$',ha='center');ax.text(.79,b-.004,'4 substates',ha='center',fontsize=9)
ax.annotate('',(.54,a),(.54,b),arrowprops={'arrowstyle':'<->','color':'#99521f'});ax.text(.49,(a+b)/2,r'$1/32$',ha='right',va='center',color='#99521f')
ax.set(xlim=(0,1.03),ylim=(-.049,.011),ylabel=r'$\Delta E/(m_e c^2\alpha_{\rm fs}^4)$',title='Hydrogen n = 2: leading fine structure only');ax.set_xticks([]);ax.spines[['top','right','bottom']].set_visible(False);ax.grid(axis='y',alpha=.12)
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
