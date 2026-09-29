"""Reduced film solutions and J(delta); cwd opaque PNG, caller-owned MPLCONFIGDIR."""
from pathlib import Path
import os
if not os.environ.get('MPLCONFIGDIR'):raise RuntimeError('Supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(10,6.2),dpi=100,facecolor='white');gs=fig.add_gridspec(2,2,height_ratios=[1.1,1])
a0=fig.add_subplot(gs[0,0]);a1=fig.add_subplot(gs[0,1]);a2=fig.add_subplot(gs[1,:])
for ax in [a0,a1,a2]:ax.set_facecolor('white');ax.grid(alpha=.15)
X=np.linspace(0,1,600);H0=.55;delta=.55;Q=-delta*(H0*H0+2*delta)/6
H=(H0**4-48*Q*X)**.25
Hfun=lambda xx:(H0**4-48*Q*xx)**.25
hp=lambda hh:-12*Q/hh**3
for ax,hvals,label in [(a0,H,'J = 0: rising film, leftward liquid flow')]:
 ax.fill_between(X,0,hvals,color='#dfebf2');ax.plot(X,hvals,color='#286890',lw=2)
 for xx in [.25,.55,.82]:
  hh=Hfun(xx);Y=np.linspace(0,hh,80);U=.5*hp(hh)*Y*(Y-hh);scale=.065/max(abs(U))
  ax.plot(xx+scale*U,Y,color='#9b4635',lw=1.1)
  for yy in hh*np.array([.25,.55,.78]):
   uu=.5*hp(hh)*yy*(yy-hh);ax.arrow(xx,yy,scale*uu,0,head_width=.032,head_length=.016,length_includes_head=True,color='#9b4635')
 ax.set_title(label,fontsize=10);ax.set_ylim(0,1.9);ax.set_xlim(0,1);ax.set_xlabel('X');ax.set_ylabel('H and local height Y')
delta2=.65;J=delta2**1.5*(1-3*delta2/5)/(2*np.sqrt(3));end=np.sqrt(3*delta2)
hgrid=np.linspace(0,end,2000);xgrid=(hgrid**3/3-hgrid**5/15)/(6*J);H2=np.interp(X,xgrid,hgrid)
a1.fill_between(X,0,H2,color='#e4eee0');a1.plot(X,H2,color='#357047',lw=2)
for xx in [.25,.55,.82]:
 hh=np.interp(xx,xgrid,hgrid);Gamma=1-hh*hh/3;der=6*J/(hh*hh*Gamma);Y=np.linspace(0,hh,100);U=.5*der*Y*(Y-2*hh/3);scale=.065/max(abs(U))
 a1.plot(xx+scale*U,Y,color='#9b4635',lw=1.1);a1.plot([xx,xx],[0,hh],color='#999999',lw=.5,ls=':')
 for yy in hh*np.array([.22,.5,.83,.97]):
  uu=.5*der*yy*(yy-2*hh/3);a1.arrow(xx,yy,scale*uu,0,head_width=.032,head_length=.016,length_includes_head=True,color='#9b4635')
a1.set_title('Q = 0: lower backflow, upper forward flow',fontsize=10);a1.set_xlim(0,1);a1.set_ylim(0,1.9);a1.set_xlabel('X');a1.set_ylabel('H and local height Y')
d=np.linspace(0,1,400);flux=d**1.5*(1-3*d/5)/(2*np.sqrt(3));a2.plot(d,flux,color='#614a91',lw=2)
a2.scatter([1],[1/(5*np.sqrt(3))],color='#614a91');a2.annotate('Formal maximum at complete depletion\n(endpoint velocity is singular)',xy=(1,flux[-1]),xytext=(.15,.10),arrowprops={'arrowstyle':'->'},fontsize=9)
a2.set_xlim(0,1.035);a2.set_ylim(0,.13);a2.set_xlabel(r'Concentration drop $\delta$');a2.set_ylabel('J for Q = 0, initial height 0')
fig.subplots_adjust(left=.08,right=.98,top=.90,bottom=.14,hspace=.45,wspace=.26)
fig.suptitle('Reduced surfactant films: profiles, velocity signs and flux',fontsize=13,y=.975)
fig.text(.5,.025,'Velocity-profile horizontal offsets are schematic. Dry/depleted edge regions are not resolved.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
