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

fig,(ax,bx)=plt.subplots(1,2,figsize=(8,3.8));ax.bar(['x analyser','z analyser'],[1/15,1/5],color=['#b36b16','#12669b']);ax.set(ylabel='Intensity / (N K I0)',ylim=(0,.235),title='Independent random needles');ax.text(0,1/15+.008,'1/15',ha='center');ax.text(1,1/5+.008,'1/5',ha='center');ax.text(.5,.215,'Ix : Iz = 1 : 3',ha='center',fontsize=11)
bx.bar(['x component','z component'],[0,1/3],color=['#b36b16','#12669b']);bx.set(ylabel='Mean dipole amplitude / (alpha E0)',ylim=(0,.4),title='Coherent orientation average');bx.text(1,1/3+.012,'1/3',ha='center');bx.text(.5,.02,'Side intensity also depends\non spatial phase matching',ha='center',fontsize=9);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
