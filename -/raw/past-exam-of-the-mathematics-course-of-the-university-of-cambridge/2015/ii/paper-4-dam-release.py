"""Original characteristic sketch; PNG output goes only to the current directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,2,figsize=(10,6),dpi=100,facecolor='white')
for ax, tmax in zip(axs,[1.,2.5]):
    t=np.linspace(.002,tmax,500)
    front=np.where(t<=1,t,3*np.cbrt(t)-2*t)
    ax.fill_betweenx(t,-2*t,front,color='#d9edf7',alpha=.7)
    ax.fill_betweenx(t,front,1,color='#eeeeee',alpha=.7)
    for speed in np.linspace(-1.85,.95,12):
        x=speed*t
        ax.plot(np.where(x<=front,x,np.nan),t,color='#0072b2',lw=.8)
    for tb in [.2,.4,.6,.8,1.]:
        tt=np.linspace(tb,tmax,500)
        xx=3*tb**(2/3)*tt**(1/3)-2*tt
        valid=(xx>=-2*tt)&(xx<=np.where(tt<=1,tt,3*np.cbrt(tt)-2*tt))
        ax.plot(np.where(valid,xx,np.nan),tt,color='#009e73',lw=.9)
        ax.plot([tb,1],[tb,0],color='#009e73',lw=.9)
    ax.plot(-2*t,t,color='#333333',lw=1.7,label='Dry front')
    ax.plot(t[t<=1],t[t<=1],color='#0072b2',lw=2,label='Leading release ray')
    ax.axvline(1,color='#333333',lw=2,label='Wall')
    if tmax>1:
        tr=np.linspace(1,tmax,400)
        ax.plot(3*np.cbrt(tr)-2*tr,tr,color='#d55e00',lw=2.7,label='First reflected signal')
        ax.text(.67,1.62,'Reflected\nregion',fontsize=9,ha='center')
    else:ax.text(.68,.23,'Undisturbed\npool',fontsize=9,ha='center')
    ax.text(-1.18,.65,'Rarefaction',fontsize=10)
    ax.set(xlim=(-2*tmax,1.17),ylim=(0,tmax),xlabel='x/a',ylabel='c₀t/a')
    ax.grid(alpha=.18)
axs[0].set_title('Before the first wall interaction')
axs[1].set_title('Unaffected fan and reflected front')
axs[1].legend(loc='lower left',fontsize=8,framealpha=.95)
fig.suptitle('Shallow-water release: blue C₊ rays and green C₋ rays',fontsize=13)
fig.subplots_adjust(left=.08,right=.98,bottom=.12,top=.86,wspace=.23)
fig.savefig('paper-4-dam-release.png',facecolor='white',transparent=False)
