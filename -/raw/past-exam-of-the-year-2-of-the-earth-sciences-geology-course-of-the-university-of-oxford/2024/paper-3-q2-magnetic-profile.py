"""Original induced line-dipole cross section, opaque basename PNG to CWD.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
x is north, z is down; plotted horizontal coordinate runs north to south.
Infinite E-W strike; I=65 degrees is illustrative, not a measured local field.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def anomaly(s, inclination=65):
    i=np.radians(inclination); f=np.array([np.cos(i),np.sin(i)])
    r=np.array([-s,-np.ones_like(s)]); r2=np.sum(r*r,axis=0)
    field=2*r*np.sum(f[:,None]*r,axis=0)/r2**2-f[:,None]/r2
    return np.sum(f[:,None]*field,axis=0)


def main():
    plt.rcParams.update({'font.size':10})
    fig,(ax,bx)=plt.subplots(2,1,figsize=(8.5,5.6),layout='constrained',gridspec_kw={'height_ratios':[2,1.3]})
    s=np.linspace(-5,5,1201); y=anomaly(s)
    ax.plot(s,y,color='#175b89',lw=2)
    ax.axhline(0,color='0.5',lw=.7);ax.axvline(0,color='0.6',ls=':',lw=.8)
    ax.text(s[y.argmin()],y.min()-.08,'Northern low',ha='center');ax.text(s[y.argmax()],y.max()+.04,'Main positive lobe',ha='center')
    ax.set(xlim=(-5,5),ylim=(-.65,1.3),ylabel='Total-field anomaly\n(relative units)',title='Induced magnetization; northward and downward field (I = 65°)')
    ax.set_xticks([-5,0,5],['North','Body centre','South'])
    bx.add_patch(Polygon([(-.7,.15),(.7,.15),(1.1,1.5),(-1.1,1.5)],facecolor='#ead9bd',edgecolor='black'))
    bx.axhline(0,color='0.3');bx.annotate('',xy=(-.45,1.2),xytext=(.1,.15),arrowprops={'arrowstyle':'->','lw':2,'color':'#a42f21'})
    bx.text(.3,.8,'Induced magnetization\npoints down and north')
    bx.text(-4,.5,'E-W strike extends\ninto / out of page')
    bx.set(xlim=(-5,5),ylim=(1.7,-.25),xlabel='North → south; distance / characteristic depth',ylabel='Depth (relative)')
    fig.suptitle('Qualitative long-body response: amplitude and detailed shape are not specified')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
