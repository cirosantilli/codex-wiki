"""Original conceptual two-event trench log, not copied from a published log.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; opaque basename PNG to CWD.
Geometries are schematic: A is displaced twice, B once, C not at all.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    plt.rcParams.update({'font.size':10})
    fig,ax=plt.subplots(figsize=(10.8,5.7),layout='constrained')
    # One fault dipping right. Unit boundaries intersect it at different heights.
    fx=lambda y:.25+(1.55-y)*.36
    ax.add_patch(Polygon([(-3,-1.8),(5,-1.8),(5,.25),(fx(.25),.25),(fx(1.45),1.45),(-3,1.45)],facecolor='#d5dadd',edgecolor='none'))
    for y in (-.45,.05,.55):
        ax.plot([-3,fx(y)],[y,y],color='#557887',lw=2)
        yr=y-1.05;ax.plot([fx(yr),5],[yr,yr],color='#557887',lw=2)
    # First-event colluvium, already displaced and truncated by second faulting.
    ax.add_patch(Polygon([(fx(-.5),-.5),(3.6,-.5),(fx(.18),.18)],facecolor='#c59f69',edgecolor='0.3',hatch='..'))
    # B seals first-event evidence but is offset by the second event.
    ax.add_patch(Polygon([(-3,.85),(fx(.85),.85),(fx(1.15),1.15),(-3,1.15)],facecolor='#c6d7ad',edgecolor='0.3'))
    ax.add_patch(Polygon([(fx(.25),.25),(5,.25),(5,.55),(fx(.55),.55)],facecolor='#c6d7ad',edgecolor='0.3'))
    # Second-event colluvial wedge above displaced B, below continuous C.
    ax.add_patch(Polygon([(fx(.55),.55),(4,.55),(fx(1.55),1.55)],facecolor='#e3bc87',edgecolor='0.3',hatch='//'))
    ax.plot([fx(-1.8),fx(1.55)],[-1.8,1.55],color='#a42f21',lw=3)
    # C drapes the entire relief and seals the second fault tip.
    lower=[(-3,1.55),(.25,1.55),(4,.55),(5,.55)]
    upper=[(-3,1.9),(.25,1.9),(4,.9),(5,.9)]
    ax.add_patch(Polygon(lower+upper[::-1],facecolor='#f1e8ba',edgecolor='0.3'))
    ax.text(-2.6,1.67,'C: continuous sealing layer')
    ax.text(-2.6,.94,'B: soil / marker bed');ax.text(-2.6,.25,'A: older bedded deposits')
    ax.annotate('W1: older wedge; cut by event 2',xy=(1.45,-.3),xytext=(2.3,-1.3),arrowprops={'arrowstyle':'->'},ha='center')
    ax.annotate('W2: younger wedge',xy=(1.6,.95),xytext=(3.3,1.9),arrowprops={'arrowstyle':'->'},ha='center')
    ax.annotate('Event 2 tip, buried by C',xy=(.25,1.55),xytext=(-2.3,2.5),arrowprops={'arrowstyle':'->'})
    ax.text(-2.7,-1.3,'Footwall');ax.text(3.9,-1.65,'Hanging wall ↓')
    ax.text(-2.9,-2.3,'Sequence: A → event 1 → W1 → B → event 2 → W2 → C\nOffsets and cross-cutting relations constrain events; wedge count alone does not.')
    ax.set(xlim=(-3.1,5.2),ylim=(-2.6,2.8),title='Original schematic trench wall: two normal-faulting events, not to scale')
    ax.axis('off')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
