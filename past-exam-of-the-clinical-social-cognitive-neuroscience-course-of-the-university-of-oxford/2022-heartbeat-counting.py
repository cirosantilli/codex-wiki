"""Original counterexample to interpreting a heartbeat-counting score as detection.

Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7, existing pyproject dependencies.
All values are calculated examples, not measurements from people.
Writes its same-basename white opaque PNG into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def score(recorded,reported):
 recorded=np.asarray(recorded,dtype=float)
 assert np.all(recorded>0)
 return 1-np.abs(recorded-reported)/recorded
assert score(60,60)==1
assert np.isclose(score(90,60),2/3)
assert score(30,60)==0
assert score(20,60)==-1 # No unasserted clipping to [0,1].
actual=np.arange(30,121);reported=60;scores=score(actual,reported)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,(ax,b)=plt.subplots(1,2,figsize=(9.2,4.3),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.1,1]})
fig.subplots_adjust(left=.075,right=.98,bottom=.22,top=.80,wspace=.28)
ax.plot(actual,scores,lw=2,color='#176b9e');ax.scatter([30,60,90],[0,1,2/3],color='#b95816',s=28,zorder=4)
ax.set(xlim=(28,122),ylim=(-.045,1.12),xlabel='Actual beats in one minute, N',ylabel='Score  A = 1 − |N − 60| / N')
ax.grid(alpha=.18);ax.annotate('Perfect score\nwithout detecting beats',xy=(60,1),xytext=(73,.96),fontsize=9,arrowprops={'arrowstyle':'->','color':'#42627a'})
ax.set_title('Fixed estimate: always report 60',fontsize=11)
b.axis('off');b.set(xlim=(0,1),ylim=(0,1))
def box(x,y,w,h,text):
 b.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.015',facecolor='#edf3f8',edgecolor='#42627a'))
 b.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=9,linespacing=1.4)
box(.02,.70,.96,.23,'Actual count N = 60\nReported count C = 60')
box(.01,.22,.45,.24,'Detect all beats\n→ report 60')
box(.54,.22,.45,.24,'Estimate 60 bpm\n→ report 60')
for end in [(.23,.48),(.77,.48)]:b.add_patch(FancyArrowPatch((.5,.68),end,arrowstyle='-|>',mutation_scale=12,color='#42627a'))
b.text(.5,.08,'Same observations and score;\ndifferent latent reporting strategies',ha='center',va='center',fontsize=10)
fig.suptitle('A perfect counting score does not identify heartbeat detection',fontsize=13,y=.97)
fig.text(.5,.09,'Calculated counterexample, not participant data. The fixed-rate estimator receives no heartbeat signal.',ha='center',fontsize=9)
fig.text(.5,.035,'Unclipped score shown for N = 30…120; sufficiently large overcounts can produce negative values.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,dpi=100,metadata={'Software':'Matplotlib','Description':'Original calculated heartbeat-counting identifiability counterexample'})
plt.close(fig)
