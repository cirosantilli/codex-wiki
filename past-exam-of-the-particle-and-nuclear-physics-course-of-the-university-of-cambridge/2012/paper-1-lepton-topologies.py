"""Original leading gauge diagrams, zero electron-Yukawa approximation."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def ferm(ax,a,b,anti=False):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#24486a',lw=1.7)
    a,b=np.array(a),np.array(b);x=a+.4*(b-a);y=a+.64*(b-a)
    ax.add_patch(FancyArrowPatch(y if anti else x,x if anti else y,arrowstyle='-|>',mutation_scale=10,color='#24486a'))

def wave(ax,a,b):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);t=np.linspace(0,1,160);z=a+t[:,None]*d+.015*np.sin(12*np.pi*t)[:,None]*n
    ax.plot(z[:,0],z[:,1],color='#a34e24',lw=1.5)

def external(ax,right):
    for x,y,txt,ha in [(0,.85,'$e^-$','right'),(0,.15,'$e^+$','right'),(1,.85,right[0],'left'),(1,.15,right[1],'left')]:ax.text(x,y,txt,ha=ha,va='center',fontsize=12)

def schannel(ax,mid,right,bosons=False):
    a=(.3,.5);b=(.7,.5);ferm(ax,(.04,.85),a);ferm(ax,(.04,.15),a,True);wave(ax,a,b)
    if bosons:wave(ax,b,(.96,.85));wave(ax,b,(.96,.15))
    else:ferm(ax,b,(.96,.85));ferm(ax,b,(.96,.15),True)
    ax.text(.5,.59,mid,ha='center',fontsize=12);external(ax,right)

def tchannel(ax,mid,right,bosons=False):
    a=(.5,.8);b=(.5,.2);ferm(ax,(.04,.85),a);ferm(ax,(.04,.15),b,True)
    if bosons:ferm(ax,a,b);wave(ax,a,(.96,.85));wave(ax,b,(.96,.15))
    else:wave(ax,a,b);ferm(ax,a,(.96,.85));ferm(ax,b,(.96,.15),True)
    ax.text(.59,.5,mid,ha='left',fontsize=12);external(ax,right)

def main():
    fig,axs=plt.subplots(2,3,figsize=(11,6))
    for ax in axs.flat:ax.set(xlim=(-.2,1.2),ylim=(-.1,1.1));ax.axis('off')
    schannel(axs[0,0],r'$\gamma, Z$',(r'$\mu^-$',r'$\mu^+$'));axs[0,0].set_title('Muon pair: two s-channel diagrams',fontsize=11)
    schannel(axs[0,1],'$Z$',(r'$\nu_e$',r'$\bar\nu_e$'));axs[0,1].set_title('Neutrino pair: s channel',fontsize=11)
    tchannel(axs[0,2],'$W$',(r'$\nu_e$',r'$\bar\nu_e$'));axs[0,2].set_title('Neutrino pair: t channel',fontsize=11)
    schannel(axs[1,0],r'$\gamma, Z$',('$W^-$','$W^+$'),True);axs[1,0].set_title('W pair: two s-channel diagrams',fontsize=11)
    tchannel(axs[1,1],r'$\nu_e$',('$W^-$','$W^+$'),True);axs[1,1].set_title('W pair: t channel',fontsize=11)
    axs[1,2].text(.5,.7,'Sum amplitudes before squaring.',ha='center',fontsize=11)
    axs[1,2].text(.5,.4,'W-pair gauge diagrams interfere\nto cancel excessive energy growth.',ha='center',fontsize=11)
    axs[1,2].text(.5,.05,'Time increases to the right.\nFermion arrows show particle flow.',ha='center',fontsize=10)
    fig.tight_layout();fig.savefig('paper-1-lepton-topologies.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
