"""Original explanatory diagram; Python 3.14 with numpy and matplotlib.
The PNG basename is written to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,3,figsize=(13,4.5),layout='constrained')
def arrow(ax,p,q,label,color=BLUE):
 ax.annotate('',q,p,arrowprops={'arrowstyle':'->','color':color,'lw':1.8});mid=(np.array(p)+np.array(q))/2;ax.text(*(mid+np.array([.12,.15])),label,color=color,fontsize=10)
ax=axs[0];arrow(ax,(0,0),(28.625,0),'normal: 28.625');arrow(ax,(28.625,0),(28.625,7.646),'anomalous',ORANGE);arrow(ax,(0,0),(28.625,7.646),'F₁₁₀');ax.axhline(0,color='.7');ax.axvline(0,color='.7');ax.set(xlim=(-3,35),ylim=(-3,13),xlabel='Real (electrons)',ylabel='Imaginary (electrons)',title='Bromine-only 110')
ax=axs[1];A=2+.8j;B=.3+.7j
for aa,bb,label,color in [(A,B,'F(h)',BLUE),(A.conjugate(),B.conjugate(),'F(−h)',ORANGE)]:
 q=aa+1j*bb;arrow(ax,(0,0),(aa.real,aa.imag),'A or A*',color);arrow(ax,(aa.real,aa.imag),(q.real,q.imag),'iB or iB*',color);arrow(ax,(0,0),(q.real,q.imag),label,color)
ax.axhline(0,color='.7');ax.axvline(0,color='.7');ax.set(xlim=(-.3,3.2),ylim=(-1.5,1.7),xlabel='Real',ylabel='Imaginary',title='General Friedel pair: unequal moduli');ax.set_aspect('equal')
ax=axs[2];ax.add_patch(Circle((0,0),2,fill=False,ec=BLUE));ax.add_patch(Circle((-1,0),1.7,fill=False,ec=ORANGE));yy=np.sqrt(4-1.055**2)
for sy in [-1,1]:arrow(ax,(0,0),(-1.055,sy*yy),'φ₁' if sy==1 else 'φ₂')
ax.scatter([0,-1],[0,0],c=['#245c9f','#b45309']);ax.text(.1,.1,'0');ax.text(-1.1,-.25,'−ΔF');ax.set(xlim=(-3,2.5),ylim=(-2.5,2.5),xlabel='Real',ylabel='Imaginary',title='Two isomorphous phase solutions');ax.set_aspect('equal')
fig.suptitle('Original Argand constructions; middle and right panels use illustrative scales',fontsize=12)
save(fig,'paper-4-diffraction-phases.png')
