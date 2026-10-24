"""An original DAG counterexample to constant edge shifts; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

points = {'s':(0,0), 'u':(1.5,1.4), 't':(3,0)}
edges = [('s','t',1), ('s','u',-2), ('u','t',2)]
fig, axes = plt.subplots(1,2,figsize=(8.8,3.6),dpi=100,facecolor='white')
for ax,shift in zip(axes,[0,3]):
    for a,b,weight in edges:
        first,second=points[a],points[b]
        winning = (a,b)!=('s','t') if shift==0 else (a,b)==('s','t')
        color = '#238b45' if winning else '#64748b'
        ax.add_patch(FancyArrowPatch(first,second,arrowstyle='-|>',shrinkA=15,shrinkB=15,
                                    mutation_scale=13,linewidth=2.8 if winning else 1.3,color=color))
        x,y=(first[0]+second[0])/2,(first[1]+second[1])/2
        if a=='s' and b=='u': x-=.16; y+=.1
        elif a=='u': x+=.16; y+=.1
        else: y-=.16
        ax.text(x,y,str(weight+shift),ha='center',va='center',fontsize=12,
                bbox=dict(facecolor='white',edgecolor='none',pad=1))
    for name,point in points.items():
        ax.add_patch(Circle(point,.14,facecolor='white',edgecolor='#334155',linewidth=1.3,zorder=3))
        ax.text(*point,name,ha='center',va='center',fontsize=12,zorder=4)
    direct,via=1+shift,2*shift
    ax.text(1.5,-.48,f'Direct cost: {direct}; via u: {via}',ha='center',fontsize=11)
    ax.set_title('Original weights' if shift==0 else 'Add 3 to each edge',fontsize=13)
    ax.set(xlim=(-.4,3.4),ylim=(-.8,1.85),aspect='equal')
    ax.axis('off')
fig.suptitle('A constant edge shift can change the shortest path',fontsize=14,y=.97)
fig.text(.5,.045,'Green edges show the shortest route in each weighted graph.',
         ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.985,top=.81,bottom=.12,wspace=.18)
fig.savefig(Path.cwd()/'functional-main-2015-edge-weight-shift.png',
            facecolor='white',transparent=False)
