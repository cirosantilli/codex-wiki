"""Original solution figure. Tested with Python 3.14, numpy and matplotlib.
The PNG basename is written to the current working directory for Make's _media target.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, flow, finish, save

fig=plt.figure(figsize=(11,8.3));gs=fig.add_gridspec(2,2,height_ratios=[2.2,1.0],hspace=.48)
a=fig.add_subplot(gs[0,:]);a.set(xlim=(-.4,1.5),ylim=(-18.3,-2.9));a.axis('off')
# Product endpoint energies are illustrative only; ordering within each symmetry is the constraint.
rows=[(-16.1,-16.4,r'$\pi_{O,z}$',r'$\sigma_+$','A₁','#245c9f',2,2),(-10.5,-6.7,r'$\pi_C$',r'$\sigma_+^*$','A₁','#245c9f',2,0),(-12.1,-14.9,r'$\pi_{O,z}^*$',r'$\sigma_-$','B₁','#b45309',1,2),(-5.5,-4.4,r'$\pi_C^*$',r'$\sigma_-^*$','B₁','#b45309',0,0),(-16.1,-11.7,r'$\pi_{O,y}$',r'$n_+$','B₂','#21633d',2,2),(-12.1,-10.2,r'$\pi_{O,y}^*$',r'$n_-$','A₂','#8654a0',1,2)]
for yl,yr,ll,rr,sym,c,occl,occr in rows:
 x=np.linspace(.14,.86,100);t=(x-.14)/.72;y=yl+(yr-yl)*(3*t*t-2*t*t*t)
 # Offset the exactly degenerate separated pi partners into short labelled subcolumns.
 leftx=.05 if sym in ['A₁','B₁'] else -.08
 a.plot([leftx-.05,leftx+.05],[yl,yl],color=c,lw=2);a.plot([.95,1.06],[yr,yr],color=c,lw=2);a.plot(x,y,color=c,lw=1.5)
 label_y=yl+(.65 if sym in ['A₁','B₁'] else -.65) if yl in [-16.1,-12.1] else yl
 a.text(-.2,label_y,ll+' '+sym,ha='right',va='center',fontsize=11)
 a.text(1.1,yr,rr+' '+sym,va='center',fontsize=11)
 if occl:a.text(leftx,yl+.3,'↑↓' if occl==2 else '↑',ha='center',fontsize=12)
 if occr:a.text(1.0,yr+.28,'↑↓',ha='center',fontsize=12)
a.text(-.05,-3.1,'Reactants: neutral triplet reference',ha='center',fontsize=12,weight='bold');a.text(1.02,-3.1,'Product: singlet ground filling',ha='center',fontsize=12,weight='bold')
a.text(.5,-18.2,'Curves join symmetry partners; product energies and intermediate shapes are schematic.\nThe carbon π pair correlates to an antibonding product orbital.',ha='center',fontsize=10)
x=np.linspace(0,1,300);a=fig.add_subplot(gs[1,0]);ER=5*x;EP=5-8*x;couple=.35
lo=(ER+EP)/2-np.sqrt(((ER-EP)/2)**2+couple**2);hi=(ER+EP)/2+np.sqrt(((ER-EP)/2)**2+couple**2)
a.plot(x,ER,':',color='.55');a.plot(x,EP,':',color='.55');a.plot(x,lo,color='#245c9f');a.plot(x,hi,color='#245c9f',alpha=.45);a.set(title='Singlet A₁: configuration avoided crossing',xlabel='Symmetric approach',ylabel='Schematic state energy',xticks=[],yticks=[]);a.text(.03,.07,'reactant singlet',transform=a.transAxes,fontsize=9);a.text(.57,.05,'product ground singlet',transform=a.transAxes,fontsize=9)
a=fig.add_subplot(gs[1,1]);a.plot(x,4*x*x,color='#b45309',label='triplet-correlated state');a.plot(x,5-8*x,color='#245c9f',label='product-ground singlet');a.set(title='Triplet: no direct spin-conserving ground-state link',xlabel='Symmetric approach',xticks=[],yticks=[]);a.legend(fontsize=8,loc='upper left');a.text(.45,.08,'An intersystem crossing is a different process.',transform=a.transAxes,fontsize=8,ha='center')
fig.subplots_adjust(left=.08,right=.89,top=.96,bottom=.07);save(fig,'paper-2a-correlation.png')
