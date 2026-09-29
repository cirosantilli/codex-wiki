"""Original generic-physics solution diagram; Python3.14.4,numpy2.3.5,matplotlib3.10.7.
Run from mirrored _media directory; save basename in cwd. No biological model.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
J=np.array([[1.,-2.],[2.,-2.]]);q=np.linspace(0,1.3,700);growth=np.array([np.linalg.eigvals(J-k*k*np.diag([1.,20.])).real.max() for k in q]);equal=np.array([np.linalg.eigvals(J-k*k*np.eye(2)).real.max() for k in q]);A=18.;roots=np.roots([20.,-A,2.]);bounds=np.sort(np.sqrt(roots));fig,ax=plt.subplots(figsize=(8.2,4.7));ax.plot(q,growth,lw=2,label='Du = 1, Dv = 20');ax.plot(q,equal,'--',lw=2,label='Du = Dv = 1');ax.axhline(0,color='.4',lw=1);ax.axvspan(*bounds,color='#e78b28',alpha=.12,label='Unstable finite-q band');ax.set(xlabel='Wavevector magnitude / illustrative unit',ylabel='Largest growth-rate real part',title='A reaction-stable Jacobian can be destabilized by unequal diffusion');ax.legend(fontsize=9);ax.grid(alpha=.15);fig.text(.5,.01,'Illustrative linear Jacobian J = [[1, −2], [2, −2]], tr J = −1, det J = 2; no biological kinetics.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.05,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
