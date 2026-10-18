"""Original toy TD calculation, not dopamine data or a reproduced source figure.

Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; existing dependencies.
The baseline is fixed at zero; each trial starts with an unpredicted cue.
Output is written to CWD with the generator's basename.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

alpha, gamma, trials = .20, .90, 80
v = np.zeros(5)
errors=[]
for trial in range(trials):
    delta=[gamma*v[1]]  # fixed reset baseline is not learned
    for state in range(1,4):
        reward=float(state==3)
        e=reward+gamma*v[state+1]-v[state]
        delta.append(e)
        v[state]+=alpha*e
    errors.append(delta)
errors=np.array(errors)
asymptotic=np.array([gamma**2,gamma,1.0])
assert np.allclose(v[1:4],asymptotic,atol=5e-6)
assert np.allclose(errors[0],[0,0,0,1])
omission=-v[3]
assert omission < -.99999 and abs(1-v[3]) < 1e-6

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,axs=plt.subplots(1,2,figsize=(8.8,4.1),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.3,1]})
fig.subplots_adjust(left=.08,right=.97,bottom=.25,top=.80,wspace=.38)
t=np.arange(1,trials+1)
axs[0].plot(t,errors[:,0],label='First informative cue',color='#1668a6',lw=2)
axs[0].plot(t,errors[:,3],label='Expected reward delivery',color='#cf6a14',lw=2)
axs[0].set(xlabel='Training trial',ylabel='Calculated prediction error',ylim=(-.03,1.08),xlim=(1,trials))
axs[0].legend(frameon=False,fontsize=9)
axs[0].grid(alpha=.20)
axs[1].bar([1,2,3],v[1:4],color=['#b9d7ed','#70aed7','#2175ae'],width=.55)
axs[1].plot([1,2,3],asymptotic,'k_',markersize=20,label='Analytic limit')
axs[1].set(xlabel='Post-cue state',ylabel='Learned state value',xticks=[1,2,3],ylim=(0,1.13))
for i,y in enumerate(v[1:4],1):axs[1].text(i,y+.025,f'{y:.3f}',ha='center',fontsize=9)
axs[1].legend(frameon=False,fontsize=9,loc='upper left')
fig.suptitle('Learning can shift an error from an outcome to its prediction',y=.96,fontsize=13)
fig.text(.5,.115,r'$\alpha=0.2,\ \gamma=0.9$; reward = 1; terminal value = 0; reset baseline held at 0.',ha='center',fontsize=9)
fig.text(.5,.065,f'After learning: expected delivery error ≈ 0; unexpected omission error ≈ {omission:.3f}.',ha='center',fontsize=9)
fig.text(.5,.02,'Original illustrative computation only: no fitted parameters or neuronal measurements.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False,
    metadata={'Software':'Matplotlib','Description':'Original deterministic temporal-difference learning illustration'})
plt.close(fig)
