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
fig,axs=plt.subplots(1,2,figsize=(11.6,4.5),layout='constrained');ax=axs[0]
t=np.linspace(0,14,600);p=np.piecewise(t,[t<1,(t>=1)&(t<3),(t>=3)&(t<12),t>=12],[0,1,lambda z:1-.83*np.exp(-.5*(z-3)),0]);ax.plot(t,p,color=BLUE);ax.axhline(1,color='.6',ls='--');ax.annotate('flag removed; sample exposed',(3,.17),(4.0,.38),arrowprops={'arrowstyle':'->'},fontsize=10);ax.annotate('nonadsorbing flag',(1.7,1),(2,1.24),arrowprops={'arrowstyle':'->'},fontsize=10);ax.text(10.7,.08,'beam off',fontsize=10);ax.set(xlabel='Time (illustrative)',ylabel='Beam-induced pressure / reference rise',ylim=(-.08,1.42),title='King and Wells pressure deficit')
ax=axs[1];th=np.arange(6)/10;s=np.array([.83,.81,.77,.71,.59,.31]);X=th/(.55-th);Y=.83/s-1;K=X@Y/(X@X)
ax.scatter(X,Y,c=ORANGE,label='transformed source data');xx=np.linspace(0,10,100);ax.plot(xx,K*xx,color=BLUE,label=f'origin fit K = {K:.3f}');ax.set(xlabel='X = θ / (0.55 − θ)',ylabel='Y = 0.83 / s − 1',title='Approximate precursor-model linearity');ax.legend(fontsize=9)
save(fig,'paper-4-adsorption-fit.png')
