"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Output is a PNG basename in cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(8.5,3.8),layout='constrained');th=np.linspace(0,2*np.pi,22,endpoint=False)
for t in th:
 a.plot([.4*np.cos(t),np.cos(t)],[.4*np.sin(t),np.sin(t)],color='#c78124',lw=2);a.add_patch(Circle((np.cos(t),np.sin(t)),.105,facecolor='#5c9ed1',edgecolor='#1766a5'))
a.text(0,0,'tail-rich\ncore',ha='center',va='center');a.annotate('solvent-compatible heads',(.75,.8),(-1.3,1.5),arrowprops=dict(arrowstyle='->'),fontsize=9);a.set(xlim=(-1.7,1.7),ylim=(-1.5,1.8),title='Generic spherical micelle (schematic)');a.set_aspect('equal');a.axis('off')
x=np.linspace(.02,3,500);mon=.5*(x+1-np.sqrt((x-1)**2+.015**2));b.plot(x,mon,label='Free monomers (illustrative)');b.plot(x,np.maximum(x-mon,0),label='In aggregates (molecular units)');b.axvline(1,color='gray',ls=':');b.set(xlabel='Total concentration / chosen CMC',ylabel='Concentration (scaled)',title='Finite-size crossover, not a sharp transition');b.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-micelle.png',dpi=150);plt.close(fig)
