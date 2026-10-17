"""Original schematic cage geometries; Python 3.14, numpy, matplotlib.

Outputs the PNG basename to the current working directory.
"""
import itertools
import numpy as np
import matplotlib.pyplot as plt

PALETTE = ['#3274a1', '#e18b2b', '#3e9165', '#a55b9b', '#d05d58', '#7a7c4c']

def automorphisms(adj, colours):
    """Small coloured-graph backtracking, independent of point-group labels."""
    n = len(adj)
    candidates = [[j for j in range(n) if colours[j] == colours[i] and sum(adj[j]) == sum(adj[i])] for i in range(n)]
    order = sorted(range(n), key=lambda i: (len(candidates[i]), -sum(adj[i])))
    result = []
    def visit(mapping, used):
        if len(mapping) == n:
            result.append([mapping[i] for i in range(n)])
            return
        i = order[len(mapping)]
        for j in candidates[i]:
            if j in used or any(adj[i][k] != adj[j][v] for k, v in mapping.items()):
                continue
            visit({**mapping, i: j}, used | {j})
    visit({}, set())
    return result

def orbits(adj, colours):
    autos = automorphisms(adj, colours)
    remaining = {i for i,c in enumerate(colours) if c == 'B'}
    groups = []
    while remaining:
        i = min(remaining)
        group = sorted({p[i] for p in autos})
        groups.append(group)
        remaining -= set(group)
    return groups

def cages():
    g = (1 + np.sqrt(5))/2
    ico = np.array([(0,a,b*g) for a in [-1,1] for b in [-1,1]]
                   + [(a,b*g,0) for a in [-1,1] for b in [-1,1]]
                   + [(a*g,0,b) for a in [-1,1] for b in [-1,1]], float)
    adj = np.isclose(np.linalg.norm(ico[:,None,:]-ico[None,:,:],axis=-1), 2)
    p2 = np.where(adj[0])[0][0]
    ec = ['P' if i in [0,p2] else 'B' for i in range(12)]
    angles = np.arange(4)*np.pi/2
    ten = np.vstack([[0,0,1.8], np.column_stack([np.cos(angles), np.sin(angles), np.full(4,.6)]),
                     np.column_stack([np.cos(angles+np.pi/4),np.sin(angles+np.pi/4), np.full(4,-.6)]), [0,0,-1.8]])
    ta = np.zeros((10,10),bool)
    edges = [(0,1+i) for i in range(4)] + [(9,5+i) for i in range(4)]
    edges += [(1+i,1+(i+1)%4) for i in range(4)] + [(5+i,5+(i+1)%4) for i in range(4)]
    edges += [(1+i,5+i) for i in range(4)] + [(1+i,5+(i-1)%4) for i in range(4)]
    for i,j in edges:ta[i,j]=ta[j,i]=True
    fc = ['P']+['BN']+['B']*8
    return (ico,adj,ec), (ten,ta,fc)

def project(points):
    theta = .39
    p = points @ np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]]).T
    return np.column_stack([p[:,0]+.28*p[:,1],p[:,2]+.35*p[:,1]])

def cage(ax, points, adj, colours, title):
    pts = project(points)
    groups = orbits(adj, ['B' if c=='BN' else c for c in colours]) if 'BN' not in colours else orbits(adj,colours)
    # BN is a distinct boron environment and is included explicitly below.
    if 'BN' in colours:groups = [[colours.index('BN')]]+groups
    labels = {i:chr(97+k) for k,g in enumerate(groups) for i in g}
    for i,j in itertools.combinations(range(len(points)),2):
        if adj[i,j]:ax.plot(*pts[[i,j]].T,color='#b9bdc2',lw=1.4,zorder=1)
    for i,(x,y) in enumerate(pts):
        label = 'P' if colours[i]=='P' else labels[i]
        k=next((k for k,g in enumerate(groups) if i in g),None)
        ax.scatter(x,y,s=310,color='#202933' if k is None else PALETTE[k],edgecolor='white',zorder=3)
        ax.text(x,y,label,color='white',ha='center',va='center',weight='bold',fontsize=11,zorder=4)
        if colours[i]=='BN':ax.annotate('B←NEt₃',(x,y),(x+.55,y+.6),fontsize=10,arrowprops={'arrowstyle':'-','color':'#444'})
    sizes = [len(g) for g in groups]
    ax.text(.5,-.03,'B-site classes: '+', '.join(f'{chr(97+i)} × {s}' for i,s in enumerate(sizes)),ha='center',va='top',transform=ax.transAxes,fontsize=9)
    ax.set_title(title,fontsize=12)
    ax.set_aspect('equal');ax.axis('off');ax.margins(.20)

def draw():
    fig,axs=plt.subplots(2,2,figsize=(10.8,8.0),layout='constrained')
    a=axs[0,0]
    pts=np.array([[-1,-.5],[1,-.5],[0,1.1]])
    for i,j in [(0,1),(1,2),(2,0)]:a.plot(*pts[[i,j]].T,color='#444',lw=1.5)
    for x,y in pts:a.text(x,y,'BH₂',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none'},fontsize=12)
    a.plot([-1,0,1],[-.5,-1.05,-.5],'--',color='#ad6027');a.text(0,-1.05,'H',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none'},fontsize=12)
    a.plot([0,0],[1.1,1.85],color='#444');a.text(0,1.9,'L',ha='center',fontsize=12)
    a.text(0,-1.65,'L = CO or NCO⁻ (N-bound)',ha='center',fontsize=11)
    a.set(xlim=(-2,2),ylim=(-1.9,2.25),title='Triborane donor adduct: localized contact model');a.axis('off')
    a=axs[0,1]
    pts=np.array([[-1,-.6],[1,-.6],[.15,.25],[-.2,1.7]])
    for i,j in itertools.combinations(range(4),2):a.plot(*pts[[i,j]].T,color='#777',lw=1.5)
    for i,(x,y) in enumerate(pts):
        a.text(x,y,'BH₂' if i<3 else 'RhH(PPh₃)₂',ha='center',va='center',fontsize=11,bbox={'facecolor':'white','edgecolor':'none'})
    a.plot([-1,0,1],[-.6,-1.2,-.6],'--',color='#ad6027');a.text(0,-1.2,'H',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none'},fontsize=12)
    a.text(0,-1.85,'RhB₃ skeleton; 6 skeletal electron pairs',ha='center',fontsize=10)
    a.set(xlim=(-2,2),ylim=(-2.1,2.5),title='Rhodium as a skeletal vertex');a.axis('off')
    e,f=cages()
    cage(axs[1,0],*e,'E: adjacent P vertices on an icosahedron')
    cage(axs[1,1],*f,'F: one six-signal positional model')
    fig.savefig('paper-1-cluster-skeletons.png',dpi=155,facecolor='white')
    plt.close(fig)

if __name__=='__main__':draw()
