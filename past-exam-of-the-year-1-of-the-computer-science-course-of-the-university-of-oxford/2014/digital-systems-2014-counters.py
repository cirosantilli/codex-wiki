"""Oxford 2014 Q3 circuits; writes the opaque PNG to the working directory.

Tested with Python 3.14.4, matplotlib 3.10.7 (root pyproject.toml).
Named signal stubs with the same blue label are physically connected nets.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle

INK='#1c3040'; BLUE='#125e83'; PALE='#eff6fa'
fig,ax=plt.subplots(figsize=(12,8.3),dpi=120,facecolor='white')
ax.set(xlim=(0,15),ylim=(0,10.4));ax.axis('off');ax.set_facecolor('white')
def wire(points):
    xs,ys=zip(*points);ax.plot(xs,ys,color=INK,lw=1.5,zorder=1)
def label(x,y,s,**kw):ax.text(x,y,s,color=BLUE,fontsize=12,va='center',**kw)
def box(x,y,w,h,title):
    ax.add_patch(Rectangle((x,y-h/2),w,h,facecolor=PALE,edgecolor=INK,lw=1.5,zorder=2))
    ax.text(x+w/2,y,title,ha='center',va='center',fontsize=12,color=INK,zorder=3)
def flop(x,y,out):
    box(x,y,2.2,1.35,'D flip-flop')
    label(x+.15,y+.32,'D');label(x+2.02,y+.32,'Q',ha='right')
    ax.add_patch(Polygon([(x+.38,y-.675),(x+.52,y-.49),(x+.66,y-.675)],closed=False,fill=False,ec=INK,lw=1.3,zorder=3))
    wire([(x+.52,y-.675),(x+.52,y-1.05)])
    ax.text(x+.52,y-1.22,'CLK',color=BLUE,fontsize=10,ha='center')
    wire([(x+1.65,y-.675),(x+1.65,y-1.05)])
    ax.text(x+1.65,y-1.22,'E',color=BLUE,fontsize=11,ha='center')
    wire([(x+2.2,y+.32),(x+3,y+.32)]);label(x+3.1,y+.32,out)
def gate(x,y,name,inputs,out):
    box(x,y,1.12,1.0,name)
    offsets=[0] if len(inputs)==1 else [.23,-.23]
    for s,o in zip(inputs,offsets):
        wire([(x-.55,y+o),(x,y+o)]);label(x-.66,y+o,s,ha='right')
    wire([(x+1.12,y),(x+1.65,y)]);label(x+1.75,y,out)
ax.text(7.5,10.03,'Gray counter and SOS sequencer',ha='center',fontsize=20,color=INK)
ax.text(.5,9.4,'(b) Two-bit enabled Gray counter',fontsize=14,weight='bold',color=INK)
flop(2.1,8.15,'G');wire([(1.15,8.47),(2.1,8.47)]);label(1.03,8.47,'H',ha='right')
flop(9.9,8.15,'H')
# A conventional inverter symbol feeding the second flip-flop.
wire([(6.6,8.47),(7.35,8.47)]);label(6.48,8.47,'G',ha='right')
ax.add_patch(Polygon([(7.35,8.09),(7.35,8.85),(8.03,8.47)],facecolor='white',edgecolor=INK,lw=1.5))
ax.add_patch(Circle((8.12,8.47),.09,facecolor='white',edgecolor=INK,lw=1.5))
wire([(8.21,8.47),(9.9,8.47)])
ax.text(7.5,6.45,'D(G) = H       D(H) = NOT G       E = 0: hold       E = 1: advance',ha='center',fontsize=12,color=INK)
ax.text(7.5,6.05,'Reset G,H to 00; both flip-flops use the same active clock edge.',ha='center',fontsize=11,color=INK)
ax.plot([.45,14.55],[5.68,5.68],color='#bdccd5',lw=1)
ax.text(.5,5.25,'(c) Synchronous cascade and output decoder',fontsize=14,weight='bold',color=INK)
box(1.2,3.5,3,1.65,'Modulo-six\ncounter')
wire([(.6,3.87),(1.2,3.87)]);label(.49,3.87,'CLK',ha='right')
wire([(.6,3.05),(1.2,3.05)]);label(.49,3.05,'1',ha='right')
ax.text(1.35,3.88,'CLK',fontsize=9,color=INK,zorder=4)
ax.text(1.35,3.07,'EN',fontsize=9,color=INK,zorder=4)
for y,s in [(4.0,'A'),(3.5,'B'),(3.,'C')]:
    wire([(4.2,y),(4.68,y)]);label(4.78,y,s)
gate(6.15,3.6,'AND',['A','C'],'E')
box(10.,3.5,3.,1.65,'Gray counter\nfrom (b)')
wire([(9.35,3.88),(10.,3.88)]);label(9.25,3.88,'CLK',ha='right')
wire([(9.35,3.05),(10.,3.05)]);label(9.25,3.05,'E',ha='right')
for y,s in [(3.95,'G'),(3.1,'H')]:
    wire([(13.,y),(13.65,y)]);label(13.75,y,s)
# Gates use named input/output stubs to keep the feedback wiring legible.
gate(1.8,1.42,'XOR',['G','B'],'X')
gate(6.15,1.42,'AND',['H','X'],'Z')
gate(10.5,1.42,'OR',['C','Z'],'Y')
ax.text(7.5,.42,'E = A AND C       Y = C OR (H AND (G XOR B))       Reset A,B,C,G,H to 0',ha='center',fontsize=12,color=INK)
ax.text(7.5,.02,'Repeated blue labels are connected nets; CLK is shared by both counters.',ha='center',fontsize=10.5,color=INK)
fig.subplots_adjust(left=.025,right=.985,bottom=.04,top=.98)
out=Path('digital-systems-2014-counters.png')
fig.savefig(out,facecolor='white',transparent=False,metadata={'Software':'codex-wiki matplotlib generator'})
plt.close(fig)
print(out)
