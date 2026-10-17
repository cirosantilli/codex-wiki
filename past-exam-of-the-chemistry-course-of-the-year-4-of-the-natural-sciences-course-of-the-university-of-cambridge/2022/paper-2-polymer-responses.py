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
fig,axs=plt.subplots(1,3,figsize=(13,3.7),layout='constrained')
a=axs[0];lam=np.linspace(1,4,200);a.plot(lam-1,lam-lam**-2,label='ideal network');a.plot(lam-1,.72*(lam-lam**-2),ls='--',label='relaxed unloading');a.set(xlabel='Engineering strain',ylabel='Nominal stress / G',title='Reversible network (schematic)');a.legend(fontsize=8)
a=axs[1];v=np.linspace(0,10,300);a.plot(v,np.exp(-((v-3)/.7)**2),label='intact block polymer');a.plot(v,.65*np.exp(-((v-5)/.65)**2)+.4*np.exp(-((v-8.5)/.45)**2),label='after ester hydrolysis');a.set(xlabel='Elution volume (arbitrary)',ylabel='Detector signal (schematic)',title='Size-exclusion shift');a.legend(fontsize=8)
a=axs[2];a.add_patch(Circle((0,0),.65,color='#c87032'))
for t in np.linspace(0,2*np.pi,14,endpoint=False):
 r=np.linspace(.62,1.2,50);a.plot(r*np.cos(t)+.035*np.sin(r*45)*np.sin(t),r*np.sin(t)+.035*np.sin(r*45)*np.cos(t),color='#2464a0')
a.text(0,0,'PS\ncore',ha='center',va='center',color='white');a.text(0,1.35,'hydrated PEO corona',ha='center',color='#2464a0');a.text(0,-1.45,'water-selective assembly',ha='center');finish(a,(-1.6,1.6),(-1.65,1.65),'Representative spherical micelle')
save(fig,'paper-2-polymer-responses.png')
