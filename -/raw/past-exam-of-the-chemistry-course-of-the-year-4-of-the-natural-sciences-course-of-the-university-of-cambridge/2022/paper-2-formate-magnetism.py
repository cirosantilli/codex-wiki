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
fig,axs=plt.subplots(1,3,figsize=(13,4),layout='constrained')
a=axs[0]
for x in range(3):
 for y in range(3):
  a.plot(x,y,'o',color='#245c9f',ms=9)
  if x<2:a.plot([x,x+1],[y,y],color='0.5');a.text(x+.5,y+.055,'formate',ha='center',fontsize=6)
  if y<2:a.plot([x,x],[y,y+1],color='0.5')
a.text(1,-.35,'M nodes: six links in 3D\n(two further neighbours normal to plane)',ha='center',fontsize=9);a.set(xlim=(-.4,2.4),ylim=(-.7,2.5),aspect='equal');a.axis('off');a.set_title('Perovskite-like topology')
a=axs[1];h=np.linspace(-4,4,300);a.plot(h,.4*np.tanh((h-.45)*2.4)+.13*h);a.plot(h,.4*np.tanh((h+.45)*2.4)+.13*h);a.axhline(0,c='0.8',lw=.7);a.axvline(0,c='0.8',lw=.7);a.set(xlabel='Field (arbitrary)',ylabel='Magnetization (arbitrary)',title='Canted AFM: small hysteretic component');a.text(-3.8,.7,'full ionic saturation lies\nbeyond this low-field sketch',fontsize=8)
a=axs[2];levels=[(.7,[-.3,.3],r"$e''$: $d_{xz},d_{yz}$"),(1.5,[-.3,.3],r"$e'$: $d_{xy},d_{x^2-y^2}$"),(2.4,[0],r"$a_1'$: $d_{z^2}$")]
for y,xs,label in levels:
 for x in xs:a.plot([x-.18,x+.18],[y,y],c='black')
 a.text(.65,y,label,va='center',fontsize=10)
a.annotate('',(-.75,2.8),(-.75,.3),arrowprops={'arrowstyle':'->'});a.text(-1,1.5,'Energy',rotation=90,va='center');finish(a,(-1.2,2.4),(0,3),'Trigonal-bipyramidal d levels')
save(fig,'paper-2-formate-magnetism.png')
