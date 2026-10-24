"""Python 3.14; root Matplotlib/NumPy versions. Write PNG into CWD."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5.5,4.5),layout='constrained',facecolor='white')
y=np.linspace(-3,3,200);ax.fill_betweenx(y,y/2,1+y/2,color='#dcecf4')
ax.plot(y/2,y,color='#2676a5');ax.plot(1+y/2,y,color='#2676a5')
for s in np.linspace(0,1,6):
 ax.plot(s+y/2,y,color='#76a4b5',lw=.8)
 ax.annotate('',xy=(s+.8,1.6),xytext=(s+.5,1),arrowprops={'arrowstyle':'->','color':'#538090'})
ax.plot([0,1],[0,0],color='#c65a28',lw=4,label='initial data')
ax.axhline(0,color='#666',lw=.5);ax.axvline(0,color='#666',lw=.5)
ax.set(xlim=(-2,3),ylim=(-3,3),xlabel='x',ylabel='y',title='Characteristics: 0 ≤ x − y/2 ≤ 1')
ax.legend(loc='upper left');fig.savefig('2009-characteristic-strip.png',dpi=155,facecolor='white')
