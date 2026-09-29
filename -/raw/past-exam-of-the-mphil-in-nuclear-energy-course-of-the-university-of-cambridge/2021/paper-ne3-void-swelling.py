"""Qualitative illustrations only: no measured steel data or fitted parameters."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(10,4.3),dpi=150)
dose=np.linspace(0,1,600)
def curve(x,onset,tau,slope):
    z=np.maximum(x-onset,0)
    return slope*(z-tau*(1-np.exp(-z/tau)))
ax=axs[0]
ax.axvspan(0,.30,color="#e7edf2")
ax.axvspan(.30,.58,color="#f5eddb")
ax.axvspan(.58,1,color="#e5f0e9")
ax.plot(dose,curve(dose,.30,.09,1),color="#286c9b",lw=2.5)
for x,label in [(.15,"incubation"),(.44,"transition"),(.79,"approximate\nsteady slope")]:
    ax.text(x,.64,label,ha="center",va="center",fontsize=10)
ax.set(xlim=(0,1),ylim=(0,.72),xlabel="accumulated displacement dose (arbitrary scale)",
       ylabel="swelling (arbitrary scale)",title="Typical stages at one set of conditions",
       xticks=[],yticks=[])
ax.spines[["top","right"]].set_visible(False)
ax=axs[1]
temperature=np.linspace(0,1,600)
response=np.exp(-((temperature-.52)/.23)**2)
ax.plot(temperature,response,color="#a35a35",lw=2.5)
ax.text(.13,.22,"limited defect\nmobility",ha="center",fontsize=11)
ax.text(.83,.26,"recovery and\nemission compete",ha="center",fontsize=11)
ax.set(xlim=(0,1),ylim=(0,1.2),xlabel="irradiation temperature",
       ylabel="swelling tendency (arbitrary scale)",
       title="Qualitative temperature window",xticks=[.05,.5,.95],
       xticklabels=["lower","intermediate","higher"],yticks=[])
ax.spines[["top","right"]].set_visible(False)
fig.suptitle("Void swelling: dose evolution and temperature dependence",fontsize=14)
fig.text(.5,.025,"Schematic trends only. Alloy, dose rate and exposure history shift the onset and temperature window.",
         ha="center",fontsize=10)
fig.tight_layout(rect=(0,.07,1,.94))
fig.savefig(Path(__file__).with_suffix(".png").name,facecolor="white")
