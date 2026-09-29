"""Temperature-salinity trajectories for Paper 71's declared diffusion model.
Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Requires adjacent paper-71-fields.py. PNG output is a cwd basename.
"""
from pathlib import Path
import importlib.util,os,tempfile,sys
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('paper71_fields',Path(__file__).with_name('paper-71-fields.py'))
fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)

def main():
    cache=None
    if 'MPLCONFIGDIR' not in os.environ:
        cache=tempfile.TemporaryDirectory(prefix='paper-71-mpl-')
        os.environ['MPLCONFIGDIR']=cache.name
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    m=fields.solve_model()
    fig,ax=plt.subplots(figsize=(8.4,6.2),dpi=100,facecolor='white')
    C=np.linspace(0,2,300);ax.plot(C,-m['R']*C,color='#333',lw=2,label='ice liquidus: $T=T_m-mC$')
    ax.fill_between(C,-m['R']*C,.15,color='#edf5fa',zorder=-1)
    ax.text(.6,-.45,'liquid solution',color='#456')
    ax.text(.77,-1.95,'ice + liquid solution',color='#456')
    us=np.concatenate([np.linspace(-4,-.003,800),np.linspace(-.003,m['a'],700)])
    cs=[fields.concentration(float(u)/m['eps'],m) for u in us]
    ts=[fields.temperature(float(u),m) for u in us]
    ax.plot(cs,ts,color='#2786a8',lw=2.5,label='spatial path: far brine toward interface')
    ax.plot([m['c'],0],[-m['theta'],-m['theta']],color='#b44b35',lw=2)
    ax.plot([0,0],[-m['theta'],0],color='#b44b35',lw=3,label='ice: $C=0$')
    ax.scatter([1,m['c'],0],[ -1,-m['theta'],0],color=['#2786a8','#2786a8','#b44b35'],zorder=5)
    ax.annotate('far brine $(C_0,T_\\infty)$',xy=(1,-1),xytext=(.56,-1.15),arrowprops=dict(arrowstyle='->'),fontsize=10)
    ax.annotate('interface $(C_i,T_i)$',xy=(m['c'],-m['theta']),xytext=(.18,-.42),arrowprops=dict(arrowstyle='->'),fontsize=10)
    ax.annotate('fresh water $(0,T_m)$',xy=(0,0),xytext=(.24,-.16),arrowprops=dict(arrowstyle='->'),fontsize=10)
    ax.annotate('',xy=(.8,-.017),xytext=(.96,-.017),arrowprops=dict(arrowstyle='->',color='#2786a8',lw=2))
    ax.annotate('',xy=(1,-.25),xytext=(1,-.65),arrowprops=dict(arrowstyle='->',color='#2786a8',lw=2))
    ins=ax.inset_axes([.07,.12,.42,.32])
    local=np.linspace(-.002,m['a'],400)
    ins.plot([fields.concentration(float(u)/m['eps'],m) for u in local],[fields.temperature(float(u),m) for u in local],color='#2786a8')
    ins.plot([0,m['c']],[-m['theta'],-m['theta']],color='#b44b35')
    ins.plot([0,0],[0,-m['theta']],color='#b44b35',lw=2)
    ins.plot([0,.045],[0,-m['R']*.045],color='#333',lw=1)
    ins.annotate('',xy=(0,-m['theta']*.8),xytext=(0,-m['theta']*.15),arrowprops=dict(arrowstyle='->',color='#825b9c'))
    ins.annotate('',xy=(.036,-m['theta']-.00006),xytext=(m['c'],-m['theta']),arrowprops=dict(arrowstyle='->',color='#825b9c'))
    ins.set(xlim=(-.003,.07),ylim=(-m['theta']*1.8,.002),title='Near the interface: enlarged')
    ins.tick_params(labelsize=8);ins.title.set_size(9)
    ax.scatter([2],[-4],marker='D',color='#333',s=25)
    ax.annotate('schematic eutectic: $C_E=2C_0$',xy=(2,-4),xytext=(1.1,-3.4),arrowprops=dict(arrowstyle='->'),fontsize=9)
    ax.set(xlim=(-.04,2.08),ylim=(-4.2,.16),xlabel='Salinity $C/C_0$',ylabel='Temperature $(T-T_m)/\\Delta T$',title='Sub-eutectic phase diagram and temperature–salinity trajectory')
    ax.legend(loc='upper right',fontsize=9)
    ax.grid(alpha=.18)
    fig.text(.5,.032,'Blue: spatial liquid profile. Purple inset arrows: a point initially in fresh water cools in ice, then melts into dilute brine.\nThe eutectic is schematic at $C_E=2C_0$; transport uses only the sub-eutectic branch.',ha='center',fontsize=9)
    fig.subplots_adjust(left=.12,right=.96,bottom=.16,top=.91)
    fig.savefig('paper-71-phase-trajectory.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
    if cache:cache.cleanup()
if __name__=='__main__':main()
