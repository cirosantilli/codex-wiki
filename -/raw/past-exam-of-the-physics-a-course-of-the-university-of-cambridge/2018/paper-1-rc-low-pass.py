"""Original RC diagram and response; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,(circuit,ax)=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
circuit.set(xlim=(0,8),ylim=(-2,2.5));circuit.axis('off')
wire=lambda x,y:circuit.plot(x,y,color='#334155',lw=1.5)
wire([.4,1.5],[1,1]);wire([3,7],[1,1]);circuit.add_patch(Rectangle((1.5,.8),1.5,.4,fill=False,lw=1.5))
circuit.text(2.25,1.5,'R = 10 kΩ',ha='center');circuit.text(.4,.4,'Vin',ha='center');circuit.text(7,.4,'Vout',ha='center')
wire([5,5],[1,0]);wire([4.5,5.5],[0,0]);wire([4.5,5.5],[-.25,-.25]);wire([5,5],[-.25,-1.2]);circuit.plot(5,1,'o',color='#334155',ms=4)
for j,w in enumerate([.45,.3,.15]):wire([5-w,5+w],[-1.2-.15*j,-1.2-.15*j])
circuit.text(5.6,-.2,'C = 100 pF',va='center');circuit.set_title('Output measured across C; no load')
f=np.logspace(2.5,7.5,700);fc=1/(2*np.pi*1e-6)
ax.semilogx(f,-10*np.log10(1+(f/fc)**2),lw=2,label='Exact magnitude')
ax.semilogx(f,np.minimum(0,-20*np.log10(f/fc)),ls='--',lw=1.3,label='Bode asymptotes')
ax.plot([fc],[-10*np.log10(2)],'o',color='#dc2626');ax.axvline(fc,ls=':',color='#64748b',lw=1)
ax.text(fc*1.15,-7,'fc = 159 kHz',fontsize=9)
ax.set(xlabel='Frequency (Hz)',ylabel='Gain (dB)',title='First-order low-pass response',ylim=(-48,3))
ax.grid(alpha=.2);ax.legend(loc='lower left',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
