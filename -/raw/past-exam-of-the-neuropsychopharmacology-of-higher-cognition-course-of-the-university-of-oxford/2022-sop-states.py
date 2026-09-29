"""Original SOP-style state illustration, not experimental neuronal data.

Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; existing dependencies.
No associative weight learning is simulated. Fractions are conserved by transfers.
Outputs the same-basename PNG into the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
import numpy as np

stimulus_fraction, d1, d2 = .70, .18, .03
def decay(p):
    i,a,b=p
    result=np.array([i+d2*b,(1-d1)*a,b+d1*a-d2*b])
    assert np.min(result)>=-1e-14 and abs(result.sum()-1)<1e-12
    return result
def present(p):
    i,a,b=p;f=stimulus_fraction*i
    return np.array([i-f,a+f,b])
def trace(before):
    p=present(np.array(before,dtype=float));out=[p.copy()]
    for _ in range(70):p=decay(p);out.append(p.copy())
    return np.array(out)
recent=present(np.array([1.,0,0]))
for _ in range(15):recent=decay(recent)
conditions=[('Unprimed',[1.,0,0],'#1668a6'),('Recently presented',recent,'#cf6a14'),('Associatively primed',[.4,0,.6],'#679344')]
traces=[(name,trace(p),color) for name,p,color in conditions]
assert np.isclose(traces[2][1][0,1], .28, rtol=0, atol=1e-14)
assert stimulus_fraction*recent[0] < stimulus_fraction

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,axs=plt.subplots(1,3,figsize=(9.3,4.3),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.05,1,1]})
fig.subplots_adjust(left=.025,right=.975,bottom=.25,top=.80,wspace=.35)
ax=axs[0];ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
nodes=[(.50,.83,'Inactive  I'),(.21,.32,'Primary  A₁'),(.79,.32,'Secondary  A₂')]
for x,y,label in nodes:
    ax.add_patch(FancyBboxPatch((x-.19,y-.09),.38,.18,boxstyle='round,pad=.015',facecolor='#eef3f8',edgecolor='#34536b'))
    ax.text(x,y,label,ha='center',va='center',fontsize=9)
def arrow(a,b,rad=0,dash=False):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,linewidth=1.3,color='#34536b',connectionstyle=f'arc3,rad={rad}',linestyle='--' if dash else '-'))
arrow((.40,.72),(.24,.43));ax.text(.16,.62,'Direct\nstimulus',ha='center',fontsize=8)
arrow((.42,.32),(.58,.32));ax.text(.50,.43,'Decay',ha='center',fontsize=8)
arrow((.83,.43),(.60,.73),rad=.20);ax.text(.88,.64,'Decay',ha='center',fontsize=8)
arrow((.57,.71),(.74,.43),dash=True);ax.text(.57,.60,'Associative\npriming',ha='center',fontsize=8)
ax.text(.5,.06,'No direct A₂ → A₁ transition',ha='center',fontsize=9)
for name,tr,color in traces:
    axs[1].plot(tr[:,1],color=color,lw=1.8,label=name)
    axs[2].plot(tr[:,2],color=color,lw=1.8,label=name)
for panel,title in [(axs[1],'Primary occupancy'),(axs[2],'Secondary occupancy')]:
    panel.set(xlabel='Steps after probe',ylabel='Element fraction',ylim=(0,.86),xlim=(0,70),title=title)
    panel.grid(alpha=.18)
handles,labels=axs[1].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.5,.105),ncol=3,frameon=False,fontsize=9)
fig.suptitle('Recent and associative priming constrain primary stimulus processing',y=.96,fontsize=13)
fig.text(.5,.075,'Chosen parameters: stimulus fraction 0.70; A₁ decay 0.18; A₂ decay 0.03 per step.',ha='center',fontsize=9)
fig.text(.5,.025,'Calculated fractions only: abstract states, no neural identity claim and no fitted biological data.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False,
    metadata={'Software':'Matplotlib','Description':'Original conserved-fraction SOP-style state illustration'})
plt.close(fig)
