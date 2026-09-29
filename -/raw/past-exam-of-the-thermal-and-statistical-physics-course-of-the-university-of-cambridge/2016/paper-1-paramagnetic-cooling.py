#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Run from mirrored _media directory; PNG basename goes to cwd.
All plotted parameter choices are illustrative and do not assert provided exam data.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

x=np.linspace(0,6,500);s=np.log(2*np.cosh(x))-x*np.tanh(x)
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.6,3.8));ax.plot(x,s,color='#12669b',lw=2);ax.set(xlabel='x = magnetic moment x B / (kBT)',ylabel='Magnetic entropy / (N kB)',ylim=(0,.74),title='Independent spin-half moments');ax.grid(alpha=.2)
b=np.linspace(0,1.12,100);bx.plot(b,b,color='#12669b',label='Constant magnetic entropy');bx.annotate('',(.36,.36),(.92,.92),arrowprops={'arrowstyle':'->','lw':2,'color':'#12669b'});bx.annotate('',(1,1),(.28,1),arrowprops={'arrowstyle':'->','lw':2,'color':'#af701c'});bx.text(.25,1.045,'Isothermal magnetization',fontsize=9,color='#9c6115');bx.text(.6,.3,'Adiabatic\ndemagnetization',fontsize=9,color='#12669b');bx.set(xlabel='B / Bi',ylabel='T / Ti',xlim=(0,1.16),ylim=(0,1.16),title='Illustrative cooling sequence');bx.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
