"""Python 3.14; Matplotlib in ../pyproject.toml. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
pos={"root":(0,0),"u":(1.2,1),"d":(1.2,-1),"uu":(2.65,1.65),"ud":(2.65,.5),"du":(2.65,-.5),"dd":(2.65,-1.65)}
edges=[("root","u","3/4"),("root","d","1/4"),("u","uu","3/4"),("u","ud","1/4"),("d","du","3/4"),("d","dd","1/4")]
labels={"root":"S = 100\nWait\nValue 575/49","u":"S = 110\nShout\nValue 115/7","d":"S = 90\nWait\nValue 0","uu":"S = 121\nPayoff 20","ud":"S = 99\nPayoff 9\nEarlier shout","du":"S = 99\nPayoff 0\nNo shout","dd":"S = 81\nPayoff 0"}
fig,ax=plt.subplots(figsize=(10,5.2),facecolor="white")
for a,b,prob in edges:
 x,y=pos[a];xx,yy=pos[b]
 ax.plot([x,xx],[y,yy],color=".6",lw=1.5)
 ax.text((x+xx)/2,(y+yy)/2+.12,prob,fontsize=9,ha="center",bbox=dict(fc="white",ec="none",pad=1))
for key,(x,y) in pos.items():
 ax.text(x,y,labels[key],ha="center",va="center",fontsize=10,bbox=dict(boxstyle="round,pad=.4",facecolor="#fff0cf" if key=="u" else "white",edgecolor="C0",lw=1.4))
ax.set(xlim=(-.55,3.2),ylim=(-2.2,2.2),title="Shout decisions preserve path history even when stock prices recombine")
ax.axis("off")
fig.tight_layout();fig.savefig("2008-shout-tree.png",dpi=150,facecolor="white")
