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
fig,axs=plt.subplots(2,3,figsize=(13,7),layout='constrained')
def cycle(a,labels,title):
 t=np.arange(8)*np.pi/4+np.pi/8;p=np.column_stack([1.25*np.cos(t),1.25*np.sin(t)]);ring(a,p)
 for xy,label in zip(p,labels):atom(a,xy,label,11,color='#245c9f' if 'Cu' in label or 'Li' in label else '0.2')
 a.text(0,0,'N = TMP nitrogen',ha='center',fontsize=8);finish(a,(-2,2),(-1.8,1.8),title)
cycle(axs[0,0],['Cu','N','Cu','N','Li','N','Li','N'],'C: adjacent like metals')
cycle(axs[0,1],['Cu','N','Li','N','Cu','N','Li','N'],r'D$_2$: alternating metal sites')
cycle(axs[0,2],['Cu','N','Li',r'C$_{ipso}$','Cu','N','Li',r'C$_{ipso}$'],r'F$_2$: head-to-tail mixed cuprate')
cycle(axs[1,0],['Cu',r'N$_1$','Li',r'N$_2$','Cu',r'N$_3$','Li',r'C$_{ipso}$'],'G: three TMP groups, one phenyl')
cycle(axs[1,1],['Cu',r'N$_1$','Li',r'N$_2$','Li',r'N$_3$','Li',r'C$_{ipso}$'],'H: Cu-bound TMP remains distinct')
a=axs[1,2];p=np.array([[-.8,0],[0,.65],[.8,0],[0,-.65]]);ring(a,p);atom(a,p[0],'Mg');atom(a,p[1],r'NR$_2$');atom(a,p[2],'Li');atom(a,p[3],r'NR$_2$');bond(a,p[0],[-1.6,0]);atom(a,[-1.8,0],r'NR$_2$');a.text(0,-1.25,r'R = SiMe$_3$; intramolecular Li···Me contacts',ha='center',fontsize=8);finish(a,(-2.4,2.0),(-1.7,1.8),'B: one LiMg formula unit')
fig.suptitle('Original connectivity projections; no metric or single fixed solution conformation implied',fontsize=12)
save(fig,'paper-2-amidometal-aggregates.png')
