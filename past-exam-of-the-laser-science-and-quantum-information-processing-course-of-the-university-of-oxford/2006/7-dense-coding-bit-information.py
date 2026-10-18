"""Original information comparison; produce the PNG in the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def h(p):return 0. if p in (0.,1.)else-p*np.log2(p)-(1-p)*np.log2(1-p)
values=[1-h(.2),1.,1-h(.2)/2,1-h(.1)]
labels=[r'Phase bit $u$',r'Parity bit $v$','Position known\nmean per bit','Position forgotten\npooled bit']
fig,ax=plt.subplots(figsize=(11,4.7),dpi=120);fig.patch.set_facecolor('white');ax.set_facecolor('white')
bars=ax.bar(range(4),values,width=.62,color=['#296b9d','#cf7b24','#30845f','#82599f'])
for bar,value in zip(bars,values):ax.text(bar.get_x()+bar.get_width()/2,value+.024,f'{value:.6f}',ha='center',fontsize=12)
ax.set(ylim=(0,1.14),ylabel='Mutual information (bits)',xticks=range(4),xticklabels=labels)
ax.tick_params(axis='x',labelsize=12);ax.tick_params(axis='y',labelsize=11);ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
fig.suptitle('Dense coding: the position label carries useful channel information',fontsize=16,y=.97)
fig.text(.5,.035,'Fair input bits; Bell-readout error 1/5 flips only the phase bit in the chosen labeling.',ha='center',fontsize=11,color='#38434c')
fig.subplots_adjust(left=.085,right=.98,top=.82,bottom=.20)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',metadata={'Software':'codex-wiki original figure'})
plt.close(fig)
