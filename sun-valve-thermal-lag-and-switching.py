"""Chosen matched-rod thermal model, no historical data; PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
    length,alpha,area,ab,ar,capacity,conductance,irradiance=.2,20e-6,.002,.9,.1,5.,.2,600.
    tau=capacity/conductance
    steady=alpha*length*area*(ab-ar)*irradiance/conductance
    threshold=10e-6; stop=180.
    close=-tau*np.log1p(-threshold/steady)
    at_stop=steady*(-np.expm1(-stop/tau))
    reopen=stop+tau*np.log(at_stop/threshold)
    t=np.linspace(0,300,2001)
    displacement=np.where(t<=stop,steady*(-np.expm1(-t/tau)),at_stop*np.exp(-(t-stop)/tau))
    permission=(displacement<threshold).astype(float)
    fig,(ax,bx)=plt.subplots(2,1,figsize=(13,6.5),dpi=120,sharex=True,facecolor='white',gridspec_kw={'height_ratios':[2.2,1]})
    fig.subplots_adjust(left=.085,right=.98,bottom=.18,top=.87,hspace=.27)
    for panel in [ax,bx]:
        panel.axvspan(0,stop,color='#f5e4ab',alpha=.5)
        panel.grid(alpha=.2)
    ax.plot(t,displacement*1e6,color='#246898',linewidth=2.5,label='Relative rod extension')
    ax.axhline(threshold*1e6,color='#a44737',linestyle='--',label='Chosen 10 µm switching threshold')
    ax.set(ylabel='Relative extension (µm)',ylim=(0,22),xlim=(0,300))
    ax.legend(loc='lower right',fontsize=11)
    ax.text(90,20.5,'Illuminated',ha='center',fontsize=12)
    ax.text(240,20.5,'Dark',ha='center',fontsize=12)
    bx.step(t,permission,where='post',color='#397c50',linewidth=2.5)
    bx.set(yticks=[0,1],yticklabels=['Closed','Open'],ylim=(-.2,1.25),xlabel='Time (s)',ylabel='Main supply\npermission')
    for when,label in [(close,f'Closes at {close:.1f} s'),(reopen,f'Reopens at {reopen:.1f} s')]:
        ax.axvline(when,color='#777',linestyle=':',linewidth=1)
        bx.axvline(when,color='#777',linestyle=':',linewidth=1)
        bx.annotate(label,xy=(when,.5),xytext=(when+12,.8),fontsize=11,arrowprops={'arrowstyle':'->','color':'#555'})
    fig.suptitle('Differential heating gives a delayed mechanical switching signal',fontsize=17,y=.97)
    fig.text(.5,.07,'Chosen illumination: 600 W/m² for 180 s; matched thermal time constant: 25 s; steady extension: 19.2 µm.',ha='center',fontsize=11)
    fig.text(.5,.025,'Model calculation, not historical measurements. The lower trace gives permission, not a measured gas-flow rate.',ha='center',fontsize=11)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
