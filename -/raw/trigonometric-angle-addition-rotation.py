"""Original geometric angle-addition diagram; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig,(left,right)=plt.subplots(1,2,figsize=(10.6,4.8),
                             gridspec_kw={"width_ratios":[1,1.05]},
                             layout="constrained")
x,y=np.pi/6,np.pi/4
theta=np.linspace(0,2*np.pi,601)
left.plot(np.cos(theta),np.sin(theta),color="#999999",lw=1.3)
left.axhline(0,color="#bbbbbb",lw=.8);left.axvline(0,color="#bbbbbb",lw=.8)
for angle,colour,label in [(x,"#2855a6",r"$x=\pi/6$"),
                            (x+y,"#087e8b",r"$x+y=5\pi/12$")]:
    left.annotate("",xy=(np.cos(angle),np.sin(angle)),xytext=(0,0),
                  arrowprops={"arrowstyle":"-|>","color":colour,"lw":2.5})
    left.text(1.03*np.cos(angle),1.07*np.sin(angle),label,color=colour,fontsize=12,
              ha="left" if angle==x else "center")
arc=np.linspace(x,x+y,80)
left.plot(.6*np.cos(arc),.6*np.sin(arc),color="#c45b12",lw=2.4)
left.annotate("",xy=(.6*np.cos(arc[-1]),.6*np.sin(arc[-1])),
              xytext=(.6*np.cos(arc[-6]),.6*np.sin(arc[-6])),
              arrowprops={"arrowstyle":"-|>","color":"#c45b12","lw":2})
left.text(.59,.70,r"Rotate by $y=\pi/4$",color="#c45b12",fontsize=11,ha="center")
left.plot([0,np.cos(x+y)],[np.sin(x+y),np.sin(x+y)],":",color="#087e8b")
left.plot([np.cos(x+y),np.cos(x+y)],[0,np.sin(x+y)],":",color="#087e8b")
left.set(xlim=(-1.15,1.25),ylim=(-1.12,1.32),aspect="equal",
         xticks=[-1,0,1],yticks=[-1,0,1],title="Angles add; coordinates mix")
right.axis("off");right.set(xlim=(0,1),ylim=(0,1))
lines=[
(.92,"Horizontal coordinate","#2855a6",14),
(.79,r"$\cos(x+y)=\cos x\cos y-\sin x\sin y$","#333333",14),
(.67,r"$=(\sqrt{6}-\sqrt{2})/4\ \approx 0.258819$","#2855a6",14),
(.48,"Vertical coordinate","#087e8b",14),
(.35,r"$\sin(x+y)=\sin x\cos y+\cos x\sin y$","#333333",14),
(.23,r"$=(\sqrt{6}+\sqrt{2})/4\ \approx 0.965926$","#087e8b",14),
(.06,r"$0.258819^2+0.965926^2\ \approx 1$","#555555",13),
]
for ypos,text,colour,size in lines:right.text(.5,ypos,text,ha="center",
                                           color=colour,fontsize=size)
fig.suptitle("A 30° direction rotated by 45° gives a 75° direction",fontsize=17)
fig.supxlabel("All formulas use the corresponding radian angles; values are rounded only in the numerical labels",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
