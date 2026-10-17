#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the corresponding mirrored _media directory; writes a PNG basename to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

fig=plt.figure(figsize=(7.5,4));ax=fig.add_subplot(121,projection='polar');th=np.linspace(0,2*np.pi,800);ax.plot(th,np.sin(th)**2,color='#12669b',lw=2);ax.set_theta_zero_location('N');ax.set_title('Meridional intensity\nangle from the z axis');ax.set_rticks([.5,1])
bx=fig.add_subplot(122);bx.annotate('',(.5,.94),(.5,.08),arrowprops={'arrowstyle':'->','lw':1.5});bx.text(.54,.89,'Dipole z');bx.annotate('',(.9,.5),(.1,.5),arrowprops={'arrowstyle':'<->','color':'#12669b','lw':2});bx.text(.5,.35,'Maximum in xy plane',ha='center',fontsize=10);bx.text(.15,.74,'Zero on the z axis',fontsize=10);bx.text(.5,.1,'Scattered E is transverse\nand in the dipole-view plane',ha='center',fontsize=10);bx.set(xlim=(0,1),ylim=(0,1));bx.axis('off');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
