"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,3,figsize=(11,3.7),layout='constrained')
data=[
('α-secondary, normal','Tetrahedral → trigonal\nC–L retained',r'$k_H/k_D=1.18$'),
('Vinylic addition, inverse','Trigonal → tetrahedral\nTwo C–L bonds retained',r'$k_H/k_D=0.86$'),
('β-secondary, normal','σ(C–H) donation into empty p\nAlignment controls the effect',r'$k_H/k_D=2.06$ (four labels)')]
for ax,(title,note,result) in zip(axes,data):
    ax.text(.5,.85,title,ha='center',fontsize=12,transform=ax.transAxes)
    ax.text(.5,.55,note,ha='center',va='center',fontsize=11,transform=ax.transAxes)
    ax.text(.5,.20,result,ha='center',fontsize=12,color='#2166ac',transform=ax.transAxes)
    ax.axis('off')
fig.suptitle('Secondary isotope effects probe retained-bond vibrations and geometry')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
