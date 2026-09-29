"""Plot a chosen ideal binary-mixture model, not historical data; output to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
    rgas=8.31446261815324
    mn,ma=.028,.040
    pressure,volume,temperature=100000.,.002,300.
    fraction=.01
    mean_molar_mass=(1-fraction)*mn+fraction*ma
    density_ratio=mean_molar_mass/mn
    colder=temperature/density_ratio
    reference_mass=pressure*volume*mn/(rgas*temperature)
    mixture_mass=pressure*volume*mean_molar_mass/(rgas*temperature)
    colder_mass=pressure*volume*mn/(rgas*colder)
    assert abs(mixture_mass-colder_mass)<1e-15
    assert abs(density_ratio-1.0042857142857142)<1e-14
    fig,(ax,bx)=plt.subplots(1,2,figsize=(13,5.8),dpi=120,facecolor='white')
    fig.subplots_adjust(left=.065,right=.98,bottom=.23,top=.83,wspace=.29)
    x=np.linspace(0,.02,250)
    ax.plot(100*x,100*x*(ma/mn-1),color='#24659a',linewidth=2.5)
    ax.scatter([1],[100*(density_ratio-1)],color='#ba3b3b',s=65,zorder=4)
    ax.annotate('1% argon gives\n0.429% extra density',xy=(1,100*(density_ratio-1)),
                xytext=(.12,.66),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=12)
    ax.set(xlim=(0,2),ylim=(0,.9),xlabel='Argon mole fraction (%)',
           ylabel='Density excess above pure nitrogen (%)',title='Equal pressure and temperature')
    ax.grid(alpha=.22)
    excess=np.array([0,mixture_mass-reference_mass,colder_mass-reference_mass])*1e6
    bx.bar([0,1,2],excess,color=['#9ca9af','#be5b39','#438865'],width=.64)
    bx.set_xticks([0,1,2],['Pure nitrogen\n300 K','1% argon mixture\n300 K',f'Pure nitrogen\n{colder:.3f} K'])
    bx.tick_params(axis='x',labelsize=11)
    bx.set(ylabel='Extra gas mass above reference (mg)',ylim=(0,12),title='Chosen 2.00 L globe at 100 kPa')
    for i,value in enumerate(excess):
        bx.text(i,value+.35,f'{value:.2f} mg',ha='center',fontsize=12)
    bx.grid(axis='y',alpha=.22)
    bx.set_axisbelow(True)
    bx.text(.5,-.23,f'Reference gas mass: {reference_mass*1000:.5f} g',transform=bx.transAxes,ha='center',fontsize=11)
    fig.suptitle('Composition and temperature can give the same weighing signal',fontsize=17,y=.96)
    fig.text(.5,.025,'Ideal-gas calculation with stipulated molar masses 28 and 40 g/mol. These are not historical measurements.',
             ha='center',fontsize=11)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
