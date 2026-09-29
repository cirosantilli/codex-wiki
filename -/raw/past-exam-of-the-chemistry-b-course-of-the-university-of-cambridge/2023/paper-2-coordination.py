"""Original chain proposal and hydration connectivities. Python 3.14; PNG to cwd."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,save
fig=plt.figure(figsize=(14,6.2),facecolor='white');gs=fig.add_gridspec(2,4,height_ratios=[.8,1.2])
a=fig.add_subplot(gs[0,:]);a.axis('off');a.set(xlim=(-1,13),ylim=(-1.3,1.9))
a.set_title('Proposed asymmetric Pt–Br chain',fontsize=15)
for x,text in [(0,'Pt(II)'),(4,'Pt(IV)'),(8,'Pt(II)'),(12,'Pt(IV)')]:atom(a,(x,0),text,size=14)
for p,q in [((0,0),(3,0)),((5,0),(8,0)),((8,0),(11,0))]:bond(a,p,q,style='dashed',color='0.5')
for p,q in [((3,0),(4,0)),((4,0),(5,0)),((11,0),(12,0))]:bond(a,p,q,lw=2)
for x in [3,5,11]:atom(a,(x,0),'Br',size=14)
a.text(1.5,.45,'long',ha='center');a.text(4,.65,'short axial Pt(IV)–Br contacts',ha='center',fontsize=11)
a.text(6,-.9,'Each Pt also has an equatorial set of 2 NH₃ + 2 Br; equatorial bonds are not expanded here.',ha='center',fontsize=11)
positions=[(-.95,0),(.95,0),(0,.95),(0,-.95),(.68,.62),(-.68,-.62)]
specs=[('Hexaaqua',[], 'outside: 2 Cl⁻'),('Monochloro',[2],'outside: Cl⁻ + H₂O'),('Dichloro: cis',[1,2],'outside: 2 H₂O'),('Dichloro: trans',[2,3],'outside: 2 H₂O')]
for i,(title,chlorides,extra) in enumerate(specs):
    a=fig.add_subplot(gs[1,i]);a.axis('off');a.set_aspect('equal');a.set(xlim=(-1.6,1.6),ylim=(-1.7,1.65));a.set_title(title,fontsize=13)
    for j,p in enumerate(positions):
        bond(a,(0,0),p,style='dashed' if j==5 else 'solid')
        atom(a,p,'Cl' if j in chlorides else 'OH₂',size=11,color='#b45309' if j in chlorides else '0.2')
    atom(a,(0,0),'Ni',size=14)
    a.text(0,-1.5,extra,ha='center',fontsize=10)
fig.suptitle('Different primary coordination spheres; same overall nickel salt composition',fontsize=14,y=.98)
fig.tight_layout(rect=(0,0,1,.94));save(fig,'paper-2-coordination.png',dpi=145)
