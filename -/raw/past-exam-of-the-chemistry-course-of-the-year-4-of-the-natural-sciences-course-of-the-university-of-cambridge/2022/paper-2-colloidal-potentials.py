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
fig,axs=plt.subplots(1,3,figsize=(13,3.8),layout='constrained')
a=axs[0];h=np.linspace(.13,8,600)
for B,k,label in [(18,1.25,'high barrier'),(9,1.5,'secondary minimum'),(3,3,'screened / coagulating')]:
 u=B*np.exp(-k*h)-2/h;a.plot(h,u,label=label)
a.axhline(0,c='0.7',lw=.7);a.set(xlabel='Separation (arbitrary)',ylabel='Pair potential (arbitrary)',ylim=(-6,10),title='DLVO schematics');a.legend(fontsize=8)
a=axs[1];h=np.linspace(0,4,100);a.plot(h,-np.maximum(2-h,0),lw=2);a.axhline(0,c='0.7',lw=.7);a.set(xlabel=r'$h/\delta$',ylabel=r'$W/(\Pi\delta)$',title='Ideal free-polymer depletion');a.axvline(2,c='0.7',ls='--');a.text(.2,-.25,'mobile depletants required',fontsize=8)
a=axs[2];D=10;b=2;N=1e4;x=np.linspace(-.8,.8,100)
for xx in [-.65,-.35,-.05,.25,.55]:a.plot(xx+.025*np.sin(np.arange(100)*.6),np.linspace(0,1.5,100),color='#245c9f')
a.plot([-.9,.9],[0,0],c='black');a.annotate('',(.8,1.5),(.8,0),arrowprops={'arrowstyle':'<->'});a.text(.9,.75,'h',va='center');a.text(0,-.25,r'$\Sigma=D^{-2}$; $h\sim Nb(b/D)^{2/3}$',ha='center',fontsize=10);finish(a,(-1.1,1.4),(-.5,1.9),'Good-solvent grafted brush')
save(fig,'paper-2-colloidal-potentials.png')
