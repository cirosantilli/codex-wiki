"""Original rate-equation example, not historical ammonia-maser data.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
Stipulated G=1e-4 s^-1 per molecule, gamma=1e4 s^-1,
kappa_int=1e6 s^-1, F=4e14 s^-1. Real rounded transition frequency
23.87 GHz read in Gordon et al., Phys. Rev. 95 (1954), Fig. 2 caption.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(11.4,7.7),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1.30,1.0],left=.085,right=.965,top=.81,bottom=.08,hspace=.60,wspace=.30)
ax=fig.add_subplot(gs[0,0]); bx=fig.add_subplot(gs[0,1]);cx=fig.add_subplot(gs[1,:]);cx.axis('off')
blue, orange, grey, green = '#17659b','#bd6218','#49586a','#287c52'
fig.text(.5,.96,'Gain must beat every loss — including useful output',ha='center',fontsize=17,weight='bold',color='#162c40')
fig.text(.5,.914,'Original teaching example • all rates stipulated; no historical measurements plotted',ha='center',fontsize=11,color=grey)
fig.text(.5,.872,r'$G=10^{-4}$ per molecule per s,  $\gamma=10^4$ s$^{-1}$,  $\kappa_{\rm int}=10^6$ s$^{-1}$,  $F=4\times10^{14}$ s$^{-1}$',ha='center',fontsize=11)
x=np.linspace(0,6,301)
ax.plot(x,x,color=blue,lw=2.5,label=r'Gain $GN_0$')
for loss,col,style in [(2,orange,'--'),(3.5,grey,':')]:
    ax.axhline(loss,color=col,linestyle=style,lw=2,label=fr'Total loss ${loss:g}\,\kappa_{{\rm int}}$')
    ax.plot(loss,loss,'o',color=col,ms=7)
ax.axvline(4,color=green,lw=1,alpha=.6)
ax.set(xlim=(0,6),ylim=(0,6),xlabel=r'Unsaturated inversion $N_0$ / $10^{10}$',ylabel=r'Gain or loss rate / $10^6$ s$^{-1}$')
ax.set_title('More selected molecules raise gain',fontsize=12,pad=12,weight='bold')
ax.text(4.06,.27,'Worked\nexample',color=green,fontsize=9)
ax.legend(loc='upper left',fontsize=9,frameon=True,facecolor='white',framealpha=1)
ax.grid(alpha=.15)
rho=np.linspace(0,4,501)
h=6.62607015e-34;nu=23.87e9;G=1e-4;gamma=1e4;ki=1e6;F=4e14;p=F*G/(gamma*ki)
n=np.maximum((F-gamma*ki*(1+rho)/G)/(2*ki*(1+rho)),0)
pout=ki*rho*h*nu*n*1e9
bx.plot(rho,pout,color=green,lw=2.5)
bx.plot(1,h*nu*5e13*1e9,'o',color=green,ms=7)
bx.axvline(3,color=orange,lw=1.5,linestyle='--')
bx.text(3.06,.58,'Onset:\nnonzero\nbranch ends',color=orange,fontsize=9)
bx.annotate('Maximum at ρ = 1',xy=(1,pout[np.argmin(abs(rho-1))]),xytext=(1.45,.85),arrowprops={'arrowstyle':'->','color':grey},fontsize=9,color=grey)
bx.set(xlim=(0,4),ylim=(0,1.05),xlabel=r'Output loading $\rho=\kappa_{\rm out}/\kappa_{\rm int}$',ylabel='Useful microwave output / nW')
bx.set_title('Extraction also increases the loss',fontsize=12,pad=12,weight='bold')
bx.grid(alpha=.15)
bx.text(.04,.95,r'$Q_{\rm L}=\omega/[\kappa_{\rm int}(1+\rho)]$',transform=bx.transAxes,fontsize=10,va='top',color=grey)

cx.set(xlim=(0,10),ylim=(0,2.6))
def box(x,y,w,hh,label,color):
    cx.add_patch(FancyBboxPatch((x,y),w,hh,boxstyle='round,pad=0.09',facecolor=color,edgecolor=grey,lw=1.2))
    cx.text(x+w/2,y+hh/2,label,ha='center',va='center',fontsize=11)
def arrow(a,b,col=grey):cx.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.8,color=col))
cx.text(5,2.58,'At ρ = 1: excitation power in = all three channels out',ha='center',fontsize=12,weight='bold')
box(.10,.85,2.15,1.05,'Incoming excitation\n6.327 nW','#e7f1fa')
box(3.03,.85,2.12,1.05,'Molecules + field\nsteady state','#f1f4f7')
box(6.24,1.75,3.35,.54,'Unused excitation: 4.745 nW','#f1f4f7')
box(6.24,.89,3.35,.54,'Wall dissipation: 0.791 nW','#fbefe3')
box(6.24,.14,3.35,.54,'Useful output: 0.791 nW','#e8f4ed')
arrow((2.35,1.37),(2.91,1.37),blue)
for yy,col in ((2.02,grey),(1.16,orange),(.41,green)):arrow((5.25,1.37),(6.12,yy),col)
cx.text(3.98,.34,r'$N_{\rm ss}=2\times10^{10},\quad n_{\rm ss}=5\times10^7$',ha='center',fontsize=10)
fig.text(.5,.025,'Excitation is measured relative to the lower level; source heat and translational energy are outside this budget.',ha='center',fontsize=10,color=grey)
fig.savefig(Path(__file__).stem+'.png',dpi=110,facecolor='white',transparent=False)
