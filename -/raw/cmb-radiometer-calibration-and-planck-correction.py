"""Original stipulated calibration and exact thermal-mode Planck correction."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

H=6.62607015e-34
KB=1.380649e-23


def antenna_temperature(frequency,temperature):
    """Thermal available power divided by k_B, no zero-point contribution."""
    q=H*np.asarray(frequency)/KB
    return q/np.expm1(q/temperature)


def calibrate(sh,sc,ss,th,tc):
    gain=(sh-sc)/(th-tc)
    receiver=(th*sc-tc*sh)/(sh-sc)
    source=tc+(th-tc)*(ss-sc)/(sh-sc)
    return gain,receiver,source


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(12.6,5.5),gridspec_kw={'width_ratios':[1.05,1.1]},constrained_layout=True)
    ax.axis('off');ax.set_title('Stipulated response: S = 2(T + 40) mV',fontsize=14,pad=20)
    tab=ax.table(cellText=[['Warm reference','300','680'],['Cold reference','4.2','88.4'],['Unknown sky input','?','90']],colLabels=['Input','T (K)','S (mV)'],colWidths=[.5,.23,.27],cellLoc='center',loc='center')
    tab.auto_set_font_size(False);tab.set_fontsize(12);tab.scale(1,2.7)
    for (r,c),cell in tab.get_celld().items():cell.set_facecolor('#e6eff5'if r==0 else'white');cell.set_edgecolor('#c4cdd4')
    g,tr,ts=calibrate(680,88.4,90,300,4.2)
    ax.text(.5,.14,f'Recovered input: {ts:.1f} K\nAfter stipulated 2.0 K nuisance terms: 3.0 K',ha='center',va='center',transform=ax.transAxes,fontsize=12)
    nu=np.geomspace(1e9,300e9,400);ta=antenna_temperature(nu,3.)
    bx.semilogx(nu/1e9,ta,lw=2.4,color='#176f9c',label=r'Equivalent antenna temperature $T_A$')
    bx.axhline(3,color='#ad6b16',ls='--',lw=1.8,label='Thermodynamic temperature T = 3 K')
    point=float(antenna_temperature(4.08e9,3.));bx.scatter([4.08],[point],s=44,color='#8b2634',zorder=3)
    bx.annotate(f'4.080 GHz\n{point:.5f} K',xy=(4.08,point),xytext=(8,1.87),arrowprops={'arrowstyle':'->','color':'#8b2634'},fontsize=11)
    bx.set(xlim=(1,300),ylim=(0,3.7),xlabel='Frequency (GHz)',ylabel='Temperature (K)',title='One blackbody, different equivalent temperatures')
    bx.legend(loc='upper right',fontsize=10,frameon=False);bx.grid(alpha=.16);bx.spines[['top','right']].set_visible(False)
    fig.suptitle('Calibration does not identify every input contribution or establish a spectrum',fontsize=16)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)


if __name__=='__main__':
    main()
