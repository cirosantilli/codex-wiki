"""Original Argand diagram; write the PNG basename to the cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
R=525.;w=2*np.pi*9e6;X=w*3.2e-6-1/(w*.2e-9);phi=np.degrees(np.arctan2(X,R))
fig,ax=plt.subplots(figsize=(7.2,2.8),layout='constrained',facecolor='white')
ax.axhline(0,color='.5',lw=1);ax.axvline(0,color='.5',lw=1)
ax.annotate('',(R,X),(0,0),arrowprops={'arrowstyle':'->','lw':2.5,'color':'#245c9f'})
ax.plot([R,R],[0,X],'--',color='.5');ax.plot([0,R],[X,X],':',color='.65')
ax.add_patch(Arc((0,0),220,220,theta1=0,theta2=phi,color='#b45309',lw=1.5))
ax.text(120,18,f'{phi:.1f}°',color='#b45309');ax.text(280,65,'|Z| = 533 Ω',rotation=phi,fontsize=12)
ax.text(R+10,X,'Z = 525 + 92.5i Ω',va='center');ax.text(R/2,-19,'Resistance: 525 Ω',ha='center')
ax.set(xlim=(-15,690),ylim=(-40,145),xlabel='Real impedance (Ω)',ylabel='Imaginary impedance (Ω)',title='Net inductive reactance at 9 MHz')
ax.set_aspect('equal',adjustable='box')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-1-impedance.png'),dpi=130,facecolor='white');plt.close(fig)
