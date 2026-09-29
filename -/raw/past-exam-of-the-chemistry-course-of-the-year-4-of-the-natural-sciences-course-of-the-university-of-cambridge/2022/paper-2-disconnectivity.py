"""Original explanatory figure. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run through the root Makefile; the PNG basename is written to the current directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(12,5.5),layout='constrained');a=axs[0]
energy={1:-10,2:-10,3:-10,4:0,5:0,6:-15,7:-15,8:-20,9:-20};order=[1,2,3,4,5,6,7,8,9];nodes={i:(float(j),energy[i]) for j,i in enumerate(order)}
# Each cluster is represented by its current horizontal centre and merge height.
def merge(keys,new,height):
 vals=[nodes.pop(k) for k in keys]
 for x,y in vals:a.plot([x,x],[y,height],c='#245c9f')
 a.plot([min(v[0] for v in vals),max(v[0] for v in vals)],[height,height],c='#245c9f');nodes[new]=(np.mean([v[0] for v in vals]),height)
for i,x in enumerate(order):a.text(i,energy[x]-1.1,str(x),ha='center',fontsize=10)
merge([8,9],'89',-18);merge([6,7],'67',-14);merge([2,3],'23',-8);merge([4,5],'45',2);merge(['23','45'],'2345',6);merge(['2345','67'],'234567',8);merge([1,'234567'],'allbut89',10);merge(['allbut89','89'],'all',12)
a.set(xlabel='Minimum labels (horizontal position arbitrary)',ylabel='Superbasin energy threshold',title='Two-unit threshold tree',ylim=(-23,14));a.set_xticks([]);a.set_yticks(np.arange(-20,13,4));a.grid(axis='y',alpha=.15)
a=axs[1];x=np.logspace(-3,2,400);mean=1-x/np.expm1(x);a.loglog(x,mean,lw=2,label='conditional mean');a.loglog(x,x/2,ls='--',c='0.5',label='short-time x/2');a.axhline(1,c='0.7',ls=':');a.set(xlabel=r'$\nu T$',ylabel=r'$\nu\,\mathcal{T}(T)$',title='One exponential mode',ylim=(3e-4,2));a.legend()
save(fig,'paper-2-disconnectivity.png')
