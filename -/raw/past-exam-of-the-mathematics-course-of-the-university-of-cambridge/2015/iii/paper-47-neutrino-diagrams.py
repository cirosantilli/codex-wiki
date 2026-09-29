"""All relevant tree diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
def fermion(ax,a,b,reverse=False):
    a=np.asarray(a);b=np.asarray(b);ax.plot([a[0],b[0]],[a[1],b[1]],color='#222222',lw=1.5)
    mid=(a+b)/2;delta=(b-a)*.1
    first,last=(mid+delta,mid-delta) if reverse else (mid-delta,mid+delta)
    ax.add_patch(FancyArrowPatch(first,last,arrowstyle='-|>',mutation_scale=10,color='#222222',lw=1.2))
def wave(ax,a,b,label):
    a=np.asarray(a);b=np.asarray(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,301);p=a+t[:,None]*d+.02*np.sin(12*np.pi*t)[:,None]*n
    ax.plot(p[:,0],p[:,1],color='#225c91',lw=1.6)
    mid=(a+b)/2;ax.text(mid[0]+(.07 if abs(d[1])>.1 else 0),mid[1]+(0 if abs(d[1])>.1 else .08),label,ha='left' if abs(d[1])>.1 else 'center',va='center',fontsize=12,color='#225c91')
def crossed(ax,kind):
    top=(.5,.66);bot=(.5,.34);lt=(.06,.83);rt=(.94,.83);lb=(.06,.17);rb=(.94,.17)
    anti=kind=='antinu';charged=kind=='cc'
    fermion(ax,lt,top,anti);fermion(ax,top,rt,anti)
    fermion(ax,lb,bot);fermion(ax,bot,rb)
    wave(ax,bot,top,r'$W^+$' if charged else r'$Z^0$')
    if charged:labels=[r'$\nu_e(k)$',r'$e^-(p^\prime)$',r'$e^-(p)$',r'$\nu_e(k^\prime)$']
    else:
        nu=r'\bar\nu_e' if anti else (r'\nu_\mu' if kind=='mu' else r'\nu_e')
        labels=['$'+nu+r'(k)$','$'+nu+r'(k^\prime)$',r'$e^-(p)$',r'$e^-(p^\prime)$']
    for pos,label in zip([lt,rt,lb,rb],labels):
        ax.text(pos[0],pos[1]+(.055 if pos[1]>.5 else -.075),label,ha='left' if pos[0]<.5 else 'right',fontsize=10)
def annihilation(ax):
    a=(.35,.5);b=(.65,.5);end=[(.06,.83),(.06,.17),(.94,.83),(.94,.17)]
    fermion(ax,end[0],a,True);fermion(ax,end[1],a)
    fermion(ax,b,end[2],True);fermion(ax,b,end[3]);wave(ax,a,b,r'$W^-$')
    labels=[r'$\bar\nu_e(k)$',r'$e^-(p)$',r'$\bar\nu_e(k^\prime)$',r'$e^-(p^\prime)$']
    for pos,label in zip(end,labels):
        ax.text(pos[0],pos[1]+(.055 if pos[1]>.5 else -.075),label,ha='left' if pos[0]<.5 else 'right',fontsize=10)
fig,axs=plt.subplots(2,3,figsize=(9,6.2),dpi=100,facecolor='white')
for ax in axs.ravel():
    ax.set(xlim=(0,1),ylim=(0,1));ax.set_facecolor('white');ax.axis('off')
for ax,kind,title in [
    (axs[0,0],'mu',r'(i) $\nu_\mu e^-:\ t$-channel $Z$'),
    (axs[0,1],'e',r'(ii) $\nu_e e^-:\ t$-channel $Z$'),
    (axs[0,2],'cc',r'(ii) $\nu_e e^-:\ u$-channel $W$'),
    (axs[1,0],'antinu',r'(iii) $\bar\nu_e e^-:\ t$-channel $Z$')]:
    crossed(ax,kind);ax.set_title(title,fontsize=11,pad=15)
annihilation(axs[1,1]);axs[1,1].set_title(r'(iii) $\bar\nu_e e^-:\ s$-channel $W$',fontsize=11,pad=15)
axs[1,2].text(.05,.7,'Solid arrows:\nfermion-number flow\n\nWavy lines:\ngauge-boson propagators',fontsize=11,va='top')
fig.subplots_adjust(left=.035,right=.965,bottom=.06,top=.9,wspace=.13,hspace=.5)
fig.savefig(Path.cwd()/'paper-47-neutrino-diagrams.png',facecolor='white',transparent=False)
plt.close(fig)
