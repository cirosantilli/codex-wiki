"""Original circular-to-elliptic orbital change and effective-potential roots."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

f = .02
a = (1-f)/(1-2*f)
e = f/(1-f)
b = a*np.sqrt(1-e*e)
angle = np.linspace(0, 2*np.pi, 600)
fig, (ax, bx) = plt.subplots(1,2,figsize=(11,5),facecolor='white',layout='constrained')
ax.plot(np.cos(angle), np.sin(angle), '--', color='.5', label='Initial circle')
ax.plot(a*(np.cos(angle)-e), b*np.sin(angle), color='#176b87', lw=2, label='After 2% loss')
ax.plot([0],[0],'*',ms=13,color='#c05229',label='Star (focus)')
ax.plot([1,-25/24],[0,0],'o',color='#176b87')
ax.annotate('Pericentre: R', xy=(1,0), xytext=(.35,.35), fontsize=11,arrowprops={'arrowstyle':'->'})
ax.annotate('Apocentre: 25R/24', xy=(-25/24,0), xytext=(-1.1,-.45), fontsize=11,arrowprops={'arrowstyle':'->'})
ax.set(aspect='equal',xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel='x / R',ylabel='y / R',title='Same position and velocity at the mass loss')
ax.legend(loc='lower center',fontsize=9,frameon=False)
r = np.linspace(.97,1.075,400)
u = .5/r**2-(1-f)/r
energy = f-.5
bx.plot(r,u,color='#176b87',lw=2,label='New effective potential')
bx.axhline(energy,color='#c05229',ls='--',label='New orbital energy')
bx.plot([1,25/24],[energy,energy],'o',color='#c05229')
bx.axvline(1,color='.7',ls=':',lw=1)
bx.axvline(25/24,color='.7',ls=':',lw=1)
bx.text(1,energy+.00020,'R',ha='center',fontsize=12)
bx.text(25/24,energy+.00020,'25R/24',ha='center',fontsize=12)
bx.set(xlabel='r / R',ylabel='Specific energy / (GM / R)',title='Radial turning points after mass loss',ylim=(-.4803,-.4786))
bx.legend(frameon=False,loc='upper center',fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software':'matplotlib'})
