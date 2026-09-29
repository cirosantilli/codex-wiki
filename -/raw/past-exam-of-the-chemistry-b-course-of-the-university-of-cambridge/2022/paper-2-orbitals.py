"""Original solution diagram; Python 3.14, numpy and matplotlib.
Write the PNG basename to the current working directory (Make supplies _media).
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, ring, wedge, flow, finish, save

fig=plt.figure(figsize=(10,9.2));gs=fig.add_gridspec(2,1,height_ratios=[2.25,1],hspace=.27)
ax=fig.add_subplot(gs[0]);ax.set(xlim=(-.5,11.2),ylim=(-.65,8.1));ax.axis('off')
def levels(x,y,n,label='',occupied=False,color='#245c9f'):
 for i in range(n):
  xx=x+(i-(n-1)/2)*.34;ax.plot([xx-.13,xx+.13],[y,y],lw=1.7,color=color)
  if occupied:ax.text(xx,y+.06,'↑↓',ha='center',fontsize=12)
 if label:ax.text(x+.3+n*.17,y,label,va='center',fontsize=11)
levels(1,3,5,r'$3d$');levels(1,5.3,1,r'$4s$');levels(1,7.3,3,r'$4p$')
for y,n,label in [(0,1,r'$a_{1g}$'),(.6,3,r'$t_{1u}$'),(1.2,2,r'$e_g$')]:levels(5,y,n,label,True)
levels(5,3.1,3,r'$t_{2g}$: metal, nonbonding')
levels(5,4.7,2,r'$e_g^*$: metal–ligand antibonding')
levels(5,6.3,1,r'$a_{1g}^*$');levels(5,7.2,3,r'$t_{1u}^*$')
levels(9.4,2.05,6,'',True,color='#21633d')
ax.text(9.4,1.55,'six donor orbitals\n'+r'$a_{1g}+e_g+t_{1u}$',ha='center',fontsize=11)
for y0,y1 in [(3,1.2),(3,4.7),(5.3,0),(5.3,6.3),(7.3,.6),(7.3,7.2)]:ax.plot([1.85,4.45],[y0,y1],ls=':',lw=.8,color='.65',zorder=0)
for y in [0,.6,1.2,4.7,6.3,7.2]:ax.plot([5.5,8.45],[y,2.05],ls=':',lw=.8,color='.76',zorder=0)
ax.annotate('',(3.7,4.7),(3.7,3.1),arrowprops={'arrowstyle':'<->','color':'#b45309'})
ax.text(3.5,3.9,r'$\Delta_o$',ha='right',fontsize=13)
for x,t in [(1,'Metal orbitals'),(5,'Octahedral sigma-only complex'),(9.4,'Ligand orbitals')]:ax.text(x,7.85,t,ha='center',fontsize=12,weight='bold')
ax.annotate('',(-.25,7.6),(-.25,0),arrowprops={'arrowstyle':'->'});ax.text(-.38,4,'Energy',rotation=90,va='center')
ax.text(5,-.5,'12 electrons fill the six sigma-bonding orbitals; add the metal d electrons above.',ha='center',fontsize=10)
sub=gs[1].subgridspec(1,3,wspace=.38)
for j,(title,donor,acceptor) in enumerate([('Sigma donation',r'$N_2\ 3\sigma_g$',r'$M\ \sigma$'),('Pi backbonding (x)',r'$M\ d_{xz}$',r'$N_2\ \pi_x^*$'),('Pi backbonding (y)',r'$M\ d_{yz}$',r'$N_2\ \pi_y^*$')]):
 a=fig.add_subplot(sub[j]);a.set(xlim=(0,4),ylim=(-.6,3.3));a.axis('off');a.set_title(title,fontsize=11)
 for x,y in [(.5,1),(3.5,2),(2,0),(2,3)]:a.plot([x-.24,x+.24],[y,y],color='#245c9f',lw=1.8)
 for x,y in [(.5,1),(2,0)]:a.text(x,y+.1,'↑↓',ha='center',fontsize=12)
 for x,y in [(.5,1),(3.5,2)]:
  for yy in [0,3]:a.plot([x,2],[y,yy],':',color='.7',lw=.9,zorder=0)
 a.text(.5,.6,donor,ha='center',fontsize=11);a.text(3.5,2.25,acceptor,ha='center',fontsize=11);a.text(2,-.5,'bonding',ha='center',fontsize=10);a.text(2,3.1,'antibonding',ha='center',fontsize=10)
fig.subplots_adjust(left=.06,right=.97,top=.96,bottom=.04)
save(fig,'paper-2-orbitals.png')
