"""Compute and draw every vertex and lowering edge of B2's vector tensor square."""
from pathlib import Path
from collections import defaultdict, deque
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

labels=['1','2','0',r'\bar{2}',r'\bar{1}'];weights=[(1,0),(0,1),(0,0),(0,-1),(-1,0)];colors=[1,2,2,1]
def f(v,i):return v+1 if v<4 and colors[v]==i else None
def e(v,i):return v-1 if v>0 and colors[v-1]==i else None
def length(v,i,op):
    n=0
    while (w:=op(v,i)) is not None:n+=1;v=w
    return n
def tf(v,i):
    a,b=v
    if length(a,i,f)>length(b,i,e):
        a=f(a,i)
    else:b=f(b,i)
    return None if a is None or b is None else (a,b)
vertices=[(a,b) for a in range(5) for b in range(5)]
edges=[(v,w,i) for v in vertices for i in [1,2] if (w:=tf(v,i)) is not None]
incoming={w for v,w,i in edges};highest=[v for v in vertices if v not in incoming]
assert highest==[(0,0),(0,1),(0,4)]
components=[]
for top in highest:
    seen={top};q=deque([top]);depth={top:0}
    while q:
        v=q.popleft()
        for x,w,i in edges:
            if x==v and w not in seen:seen.add(w);depth[w]=depth[v]+1;q.append(w)
    components.append((seen,depth))
assert [len(c) for c,d in components]==[14,10,1]
assert set.union(*(c for c,d in components))==set(vertices)
fig=plt.figure(figsize=(12,7.6),dpi=100,facecolor='white')
chain=fig.add_axes([.08,.84,.84,.12]);chain.axis('off');chain.set(xlim=(-.4,4.4),ylim=(-.55,.55))
for j,label in enumerate(labels):chain.text(j,0,rf'${label}$',ha='center',va='center',fontsize=15,bbox=dict(boxstyle='circle',fc='white',ec='#253746',pad=.35))
for j,i in enumerate(colors):
    col='#2468a2' if i==1 else '#c53b36';chain.annotate('',xy=(j+.81,0),xytext=(j+.19,0),arrowprops=dict(arrowstyle='->',color=col,lw=1.7));chain.text(j+.5,.23,str(i),ha='center',color=col,fontsize=12)
chain.set_title(r'$B_2$ defining crystal (dimension 5); tensor square below',fontsize=14)
panels=[(.045,.095,.45,.68),(.54,.095,.4,.68),(.905,.79,.08,.08)]
titles=[r'$L(2\omega_1)$: symmetric traceless (14)',r'$L(2\omega_2)$: adjoint (10)',r'$L(0)$: (1)']
fills=['#e3f1e7','#eee7f5','#fff0c9'];cols={1:'#2468a2',2:'#c53b36'}
for k,((comp,depth),panel) in enumerate(zip(components,panels)):
    ax=fig.add_axes(panel);levels=defaultdict(list)
    for v in sorted(comp):levels[depth[v]].append(v)
    pos={v:(j-(len(vs)-1)/2,-d) for d,vs in levels.items() for j,v in enumerate(vs)}
    for v,w,i in edges:
        if v in comp:
            ax.annotate('',xy=pos[w],xytext=pos[v],arrowprops=dict(arrowstyle='->',color=cols[i],lw=1.5,shrinkA=16,shrinkB=16),zorder=1)
    for v,(x,y) in pos.items():
        label=rf'${labels[v[0]]}\!\otimes\!{labels[v[1]]}$'
        ax.text(x,y,label,ha='center',va='center',fontsize=12,bbox=dict(boxstyle='round,pad=.22',fc=fills[k],ec='#596770',lw=.8),zorder=3)
    width=max(len(v) for v in levels.values());ax.set(xlim=(-width/2-.15,width/2+.15),ylim=(-max(depth.values())-.5,.7));ax.axis('off');ax.set_title(titles[k],fontsize=12,pad=5)
fig.text(.5,.025,'Every ordered pair appears once. Blue arrows: color 1; red arrows: color 2. Arrows point downward.',ha='center',fontsize=11)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
