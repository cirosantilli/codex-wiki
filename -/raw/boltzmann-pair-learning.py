"""Exact two-visible-unit Boltzmann learning; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

states = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
pair = states[:,0]*states[:,1]
q = np.array([3,1,1,3])/8

def model(j):
    weights = np.exp(j*pair)
    return weights / weights.sum()

def likelihood(j):
    return q @ np.log(model(j))

for j in (-.7, 0, .25, .5493061443340549, 1.1):
    assert np.isclose(np.exp(j*pair).sum(),4*np.cosh(j))
    assert np.isclose(model(j) @ pair, np.tanh(j))
    step = 1e-5
    derivative = (likelihood(j+step)-likelihood(j-step))/(2*step)
    assert abs(derivative - (.5-np.tanh(j))) < 1e-9
assert np.allclose(model(np.log(3)/2),q)
assert likelihood(.25) > likelihood(0)

plt.rcParams.update({'font.size': 11, 'axes.spines.top':False, 'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),gridspec_kw={'width_ratios':[1.1,1]})
fig.patch.set_facecolor('white')
x=np.arange(4)
for offset, values, label, color in [(-.26,q,'Data','#294e76'),(0,model(0),'Initial J = 0','#b0bdc9'),(.26,model(.25),'After step J = 1/4','#dc6b20')]:
    ax.bar(x+offset,values,width=.24,label=label,color=color)
ax.set(xticks=x,xticklabels=['(+,+)','(+,−)','(−,+)','(−,−)'],ylabel='Probability',ylim=(0,.46),xlabel='Visible state',title='Enumerate all four states')
ax.legend(frameon=False,fontsize=9,loc='upper center',ncol=1)
ax.grid(axis='y',alpha=.16)
j=np.linspace(-.15,1.25,250)
bx.plot(j,np.tanh(j),label=r'Free model: $\langle x_1x_2\rangle_-=\tanh J$',color='#294e76',lw=2)
bx.axhline(.5,color='#6d7f36',ls='--',label=r'Clamped data: $\langle x_1x_2\rangle_+=1/2$')
bx.annotate('',xy=(0,.5),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#dc6b20','lw':2})
bx.text(.025,.22,'Initial gradient\n= 1/2',color='#a94912',fontsize=10)
opt=np.log(3)/2
bx.scatter([opt],[.5],s=55,color='#6d7f36',zorder=4)
bx.axvline(opt,color='#6d7f36',ls=':',alpha=.7)
bx.text(opt+.045,.31,r'$J_* = \frac{\log 3}{2}$'+'\n≈ 0.5493',fontsize=12)
bx.scatter([.25],[np.tanh(.25)],color='#dc6b20',zorder=4)
bx.set(xlabel='Coupling J',ylabel='Mean pair product',ylim=(-.22,.94),title='Learning closes the correlation gap')
bx.legend(loc='upper left',frameon=False,fontsize=9)
bx.grid(alpha=.16)
fig.suptitle('Boltzmann learning: observed association minus generated association',fontsize=14)
fig.text(.5,.025,r'$E=-Jx_1x_2$, $\beta=1$, $Z=4\cosh J$.  One ascent step: $J=0+(1/2)(1/2)=1/4$.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.065,1,.93),w_pad=2)
fig.savefig(Path(__file__).stem+'.png',dpi=120,facecolor='white')
