"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(12,6.5),layout='constrained')
x=np.arange(7,dtype=float);y=np.array([0,4.5,2.0,3.9,1.0,2.6,-.6])
# Cosine interpolation makes every designated intermediate a stationary point.
xx=[];yy=[]
for i in range(6):
    t=np.linspace(0,1,80);xx.extend(i+t);yy.extend(y[i]+(y[i+1]-y[i])*(1-np.cos(np.pi*t))/2)
ax.plot(xx,yy,color=BLUE,lw=2.3)
labels=[r'$\mathrm{O_r-C1-O_{LG}}$'+'\n+ indole',r'$[\mathrm{O_r-C1^{\delta+}\cdots O_{LG}}]^\ddagger$',r'$\mathrm{O_r-C1^+\ \leftrightarrow\ O_r^+=C1}$'+'\nI1 + LG⁻',r'$[\mathrm{C1\cdots C2(H)_{ind}}]^\ddagger$',r'$\mathrm{C1-C2(H)-C3^+}$'+'\nI2 (nonaromatic)',r'$[\mathrm{B\cdots H\cdots C2-C3}]^\ddagger$',r'$\mathrm{C1-C2{=}C3}$'+'\naromatic product']
for j,(a,b,l) in enumerate(zip(x,y,labels)):
    ax.scatter(a,b,color=ORANGE,s=28,zorder=4)
    ax.annotate(l,(a,b),xytext=(a+(.05 if j in [0,6] else 0),b+(.55 if j%2 else -1.1)),ha='center',va='center',fontsize=10)
ax.set(xlim=(-.65,6.65),ylim=(-2.15,6),xlabel='Reaction coordinate',ylabel='Relative Gibbs free energy (illustrative units)')
ax.set_yticks([]);ax.spines[['right','top']].set_visible(False)
ax.set_title('Three barriers; oxocarbenium and arenium-ion minima\nStructures show reactive connectivity; unchanged groups are suppressed',fontsize=13)
ax.text(3,-1.9,'Oᵣ = sugar ring O; C1 = anomeric C; C2/C3 = indole C; no measured barrier heights',ha='center',fontsize=10)
save(fig,'paper-2-glycosylation-energy.png')
