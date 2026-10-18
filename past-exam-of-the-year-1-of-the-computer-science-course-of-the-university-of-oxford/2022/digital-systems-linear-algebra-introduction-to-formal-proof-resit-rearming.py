"""Original Moore-state/timing solution; Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7, as pinned in the root pyproject. Writes its PNG to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
from matplotlib.path import Path as MplPath


def main():
    fig,(ax,bx)=plt.subplots(1,2,figsize=(9.8,4.1),dpi=100,gridspec_kw={'width_ratios':[1,1.15]})
    fig.patch.set_facecolor('white')
    positions={'R':(0,1.4),'P':(2,1.4),'D':(2,-.5),'Z':(0,-.5)}
    labels={'R':'R\n00 / z=0','P':'P\n10 / z=1','D':'D\n11 / z=0','Z':'Z\n01 / z=0'}
    for key,(x,y) in positions.items():
        ax.add_patch(Circle((x,y),.4,facecolor='#d9ebf8' if key=='P' else '#f3f4f5',edgecolor='#275777',linewidth=1.4))
        ax.text(x,y,labels[key],ha='center',va='center',fontsize=9)
    def edge(fr,to,text,offset=(0,0),rad=0):
        p=np.array(positions[fr]);q=np.array(positions[to]);d=(q-p)/np.linalg.norm(q-p);start=p+.41*d;end=q-.42*d
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=11,color='#333333',connectionstyle=f'arc3,rad={rad}'))
        mid=(p+q)/2+np.array(offset);ax.text(*mid,text,fontsize=10,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
    edge('R','P','1',(0,.16));edge('P','D','1',(.18,0));edge('P','Z','0',(-.08,.08));edge('D','Z','0',(0,-.3),.2);edge('Z','D','1',(0,.3),.2);edge('Z','R','0',(-.18,0))
    for points,at,label in [([(-.22,1.74),(-.7,2.7),(.7,2.7),(.22,1.74)],(0,2.45),'0'), ([(2.35,-.32),(3.4,.6),(3.4,-1.6),(2.35,-.68)],(3.2,-.5),'1')]:
        path=MplPath(points,[MplPath.MOVETO,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4])
        ax.add_patch(FancyArrowPatch(path=path,arrowstyle='-|>',mutation_scale=10,color='#333333'))
        ax.text(*at,label,fontsize=10,ha='center')
    ax.annotate('reset',xy=(-.38,1.4),xytext=(-1.1,1.4),ha='center',va='center',fontsize=9,arrowprops={'arrowstyle':'->'})
    ax.set(xlim=(-1.4,3.5),ylim=(-1.6,2.8));ax.set_aspect('equal');ax.axis('off');ax.set_title('State code / output; arrows labelled by a',fontsize=10)
    inputs=[1,1,0,1,0,0,1,0,0,1];q1=q0=0;outputs=[]
    for bit in inputs:
        q1,q0=bit,int(bool(q1 or (q0 and bit)));outputs.append(int(bool(q1 and not q0)))
    assert outputs==[1,0,0,0,0,0,1,0,0,1]
    edges=np.arange(1,len(inputs)+2)
    bx.step(edges,np.r_[inputs,inputs[-1]]+2,where='post',color='#666666',label='a',linewidth=1.8)
    bx.step(edges,np.r_[outputs,outputs[-1]],where='post',color='#21618c',label='z',linewidth=2)
    for n in range(1,11):bx.axvline(n,color='#dddddd',linewidth=.7,zorder=0)
    bx.set(xlim=(.6,11),ylim=(-.25,3.4),xticks=np.arange(1,11),yticks=[0,1,2,3],yticklabels=['0','1','0','1'],xlabel='Sampling edge (values shown after update)')
    bx.text(.25,.5,'z',va='center',ha='center',fontsize=11);bx.text(.25,2.5,'a',va='center',ha='center',fontsize=11)
    bx.spines[['top','right']].set_visible(False);bx.set_title('A high cannot retrigger before two zeros',fontsize=10)
    fig.suptitle('One-clock pulses, with reset into the ready state',fontsize=12)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,
                metadata={'Software':'NumPy/Matplotlib; original Oxford 2022 resit answer figure'})
    plt.close(fig)


if __name__=='__main__':main()
