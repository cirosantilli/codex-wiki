"""Original schematic interpretations, without source-map pixels. Python 3.14.4."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
fig, axs=plt.subplots(2,2,figsize=(11,6.5),layout="constrained")
a=axs[0,0]
a.plot([.12,.28,.44,.53,.65,.83,.97],[.83,.75,.68,.62,.42,.20,.04],color="#b63232",lw=2,label="strike-slip interpretation")
a.plot([.03,.18,.34,.45,.51],[.56,.61,.65,.69,.68],color="#793a95",lw=2,label="reverse interpretation")
for x,y in [(.15,.60),(.29,.64),(.40,.68)]:
 a.fill([x-.018,x+.018,x],[y+.005,y+.005,y+.05],color="#793a95")
a.annotate("",(.73,.27),(.62,.43),arrowprops={"arrowstyle":"->","lw":2})
a.annotate("",(.62,.29),(.73,.13),arrowprops={"arrowstyle":"->","lw":2})
a.text(.77,.43,"left-lateral",rotation=42)
a.text(.16,.81,"hanging wall",color="#793a95")
a.text(.19,.47,"footwall / basin",color="#793a95")
a.plot([.45,.45,.49,.51],[.42,.64,.69,.95],color="#2383a4",lw=2)
a.annotate("offset / diverted channel",(.47,.67),(.03,.27),arrowprops={"arrowstyle":"->"},fontsize=9)
a.annotate("",(.58,.38),(.58,.04),arrowprops={"arrowstyle":"->","color":"#228443","lw":2})
a.annotate("",(.58,.77),(.58,.98),arrowprops={"arrowstyle":"->","color":"#228443","lw":2})
a.text(.60,.09,r"$\sigma_1$ N–S",color="#228443")
a.set(xlim=(0,1),ylim=(1,0),xlabel="Fraction from left edge",ylabel="Fraction from top edge",title="3(b): Attachment A, approximate trace positions")
a.legend(loc="lower right",fontsize=7)
a=axs[0,1]
a.plot([0,4],[1.1,1.1],color=".4")
a.plot([.8,3.1],[.2,1.6],color="#793a95",lw=3)
a.annotate("",(1.8,1.05),(1.2,.69),arrowprops={"arrowstyle":"->","lw":2})
a.annotate("",(2.3,.58),(2.9,.94),arrowprops={"arrowstyle":"->","lw":2})
a.text(.1,1.35,"S: hanging wall up")
a.text(2.1,.2,"N: footwall")
a.text(.1,-.05,"E–W reverse strand takes up N–S shortening")
a.set(xlim=(0,4),ylim=(-.2,2),title="3(b): schematic reverse-fault section")
a.axis("off")
a=axs[1,0]
x=[.04,.22,.43,.55,.59,.62,.72,.88,.98]
y=[.56,.52,.60,.64,.57,.43,.49,.64,.61]
a.plot(x,y,color="#b63232",lw=2)
a.text(.15,.24,"mountain footwall")
a.text(.20,.86,"basin hanging wall")
a.annotate("stepped trace",(.60,.52),(.72,.24),arrowprops={"arrowstyle":"->"})
a.annotate("fan-surface scarp",(.38,.58),(.03,.73),arrowprops={"arrowstyle":"->"})
a.annotate("triangular mountain-front facets",(.78,.48),(.43,.08),arrowprops={"arrowstyle":"->"},fontsize=9)
a.set(xlim=(0,1),ylim=(1,0),xlabel="Fraction from left edge",ylabel="Fraction from top edge",title="4(b): Attachment B, mountain front and scarp")
a=axs[1,1]
a.plot([.1,.45],[.35,.35],color="#b63232",lw=3)
a.plot([.55,.9],[.65,.65],color="#b63232",lw=3)
a.plot([.45,.55],[.35,.65],color="#276792",lw=2,label="breached relay: linking fault")
a.fill([.35,.45,.65,.55],[.35,.35,.65,.65],color="#e7ce96",alpha=.8)
a.text(.02,.1,"Unbreached: tilted relay ramp")
a.text(.02,.91,"Breached: connecting oblique fault")
a.annotate("",(.28,.50),(.28,.28),arrowprops={"arrowstyle":"->"})
a.annotate("",(.75,.82),(.75,.59),arrowprops={"arrowstyle":"->"})
a.text(.04,.76,"plan view; arrows mark downthrown side",fontsize=8)
a.set(xlim=(0,1),ylim=(1,0),title="4(b)(iv): two stages of a normal-fault relay")
a.axis("off")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
