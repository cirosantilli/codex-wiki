"""Functional detector sketch and a fully conserved original toy event.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; emits this script's basename with .png in the working directory.
"""
from pathlib import Path
import runpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    model = runpy.run_path(str(Path(__file__).with_name('tau-pair-missing-mass-phase-space.py')))
    events, x = model['generate']()
    model['checks'](events, x)
    _, missing, acop = model['diagnostics'](events)
    # Choose a readable projection from valid generated cases, not a historical event.
    mask = (acop > 65) & (acop < 90) & (events[:, 0, 0, 2] > .4) & (events[:, 1, 0, 1] > .4)
    i = int(np.flatnonzero(mask)[0])
    e, mu = events[i, 0, 0], events[i, 1, 0]
    q = missing[i]
    assert np.max(np.abs(e + mu + q - [6, 0, 0, 0])) < 1e-10
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig, (a,b) = plt.subplots(1,2,figsize=(10,5.5),layout='constrained',gridspec_kw={'width_ratios':[1,1.1]})
    a.set(xlim=(0,10),ylim=(0,10),title='Functional identification paths')
    a.axis('off')
    for y, label, color in [(6.9,r'$e^-$: large shower pulse','#0072b2'),(3.8,r'$\mu^+$: small pulse + outer hit','#c65d00')]:
        endpoint = 4.7 if y > 5 else 9
        a.annotate('',(endpoint,y),(.5,y),arrowprops={'arrowstyle':'->','color':color,'lw':2})
        a.text(.5,y+.65,label,color=color,fontsize=11)
    for left,width,label,col in [(2,1.25,'Tracking\ncharge / p','#e8f3fa'),(4,1.4,'Lead +\nscintillator','#fff5ce'),(6.2,1.0,'Iron\nreturn','#ddd'),(8.1,1.1,'Outer\nchambers','#e6f1df')]:
        a.add_patch(Rectangle((left,2.7),width,5,facecolor=col,edgecolor='#888',zorder=0))
        a.text(left+width/2,2.4,label,ha='center',va='top',fontsize=9)
    a.scatter([4.7],[6.9],s=280,color='#0072b2',marker='*',zorder=3)
    a.scatter([4.7,8.65],[3.8,3.8],s=[35,45],color='#c65d00',zorder=3)
    a.text(.4,.15,'Schematic paths separated for readability.\nNo detector scale or reconstructed tau flight.\nUndetected neutrinos leave no track here.',fontsize=9)
    b.set(title='Conserved toy event: transverse projection',xlabel=r'$p_x$ (GeV)',ylabel=r'$p_y$ (GeV)',aspect='equal')
    vectors=[(e,r'$e^-$','#0072b2','-'),(mu,r'$\mu^+$','#c65d00','-'),(q,r'$\sum\nu$: inferred recoil','#7851a9','--')]
    for p,label,color,style in vectors:
        b.annotate('',p[1:3],(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':2,'linestyle':style})
        labelpos = 1.14*p[1:3]
        if style == '--':
            labelpos = np.array([-.7, -.6])
        b.text(*labelpos,label,color=color,ha='center',fontsize=10)
    b.axhline(0,color='#ddd',lw=.7); b.axvline(0,color='#ddd',lw=.7)
    b.plot(0,0,'ko',ms=4)
    limit=1.5*max(np.max(np.abs(e[1:3])),np.max(np.abs(mu[1:3])),np.max(np.abs(q[1:3])))
    b.set(xlim=(-limit,limit),ylim=(-limit,limit))
    rows=[f'{label}: ({p[0]:.3f}; {p[1]:+.3f}, {p[2]:+.3f}, {p[3]:+.3f})' for label,p in [('e-',e),('mu+',mu),('sum nu',q)]]
    fig.suptitle(r'Visible $e^-\mu^+$ plus invisible recoil',fontsize=15)
    fig.supxlabel('Chosen event, massless daughters; four-vectors (E; px, py, pz) in GeV\n'+'\n'.join(rows)+'\nTotal = (6; 0, 0, 0), charge = 0; dashed arrow is a sum, not one particle',fontsize=9)
    fig.savefig(Path(__file__).stem+'.png',dpi=120,facecolor='white')
    plt.close(fig)
    print('geometry_event_index',i,'four_vectors',rows)


if __name__ == '__main__':
    main()
