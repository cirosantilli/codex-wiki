"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
time=np.linspace(0,13,1201);fig,ax=plt.subplots(figsize=(8,4.6),layout='constrained')
for zeta,color,label in [(.2,'#2a6a9b','Underdamped'),(1,'#a14c29','Critically damped'),(2,'#2c7c57','Overdamped')]:
 if zeta<1:
  w=np.sqrt(1-zeta*zeta);response=np.exp(-zeta*time)*(np.cos(w*time)+zeta*np.sin(w*time)/w)
 elif zeta==1:response=(1+time)*np.exp(-time)
 else:
  rp=-zeta+np.sqrt(zeta*zeta-1);rm=-zeta-np.sqrt(zeta*zeta-1);response=(-rm*np.exp(rp*time)+rp*np.exp(rm*time))/(rp-rm)
 ax.plot(time,response,color=color,label=label,lw=2)
ax.axhline(0,color='gray',lw=.7);ax.set(xlabel='Time × natural angular frequency',ylabel='Displacement / initial displacement',title='Free release with zero initial velocity',ylim=(-.65,1.1));ax.grid(alpha=.2);ax.legend(fontsize=10)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
