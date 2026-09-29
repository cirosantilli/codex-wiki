from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
image=np.zeros((12,16));image[8:11,2:5]=1.;image[4:6,7:11]=.6;image[1:3,13:15]=.85
freq=300+50*np.arange(12);duration=.04;fs=24000;ts=np.arange(round(duration*fs))/fs
basis=np.sin(2*np.pi*ts[:,None]*freq[None,:])
coeff=[]
for j in range(16):
 signal=basis@image[:,j]
 recovered=2*basis.T@signal/len(ts)
 assert np.max(np.abs(recovered-image[:,j]))<1e-12
 coeff.append(recovered)
fig,ax=plt.subplots(1,2,figsize=(9.3,3.9),layout="constrained")
ax[0].imshow(image,origin="lower",cmap="gray",vmin=0,vmax=1,extent=(-.5,15.5,-.5,11.5),interpolation="nearest",aspect="equal")
ax[0].set(xlabel="Horizontal image column → scan order",ylabel="Vertical image row → increasing frequency",title="Original toy camera image",xticks=[0,4,8,12,15],yticks=[0,3,6,9,11])
arr=np.stack(coeff,axis=1)
ax[1].imshow(arr,origin="lower",cmap="gray",vmin=0,vmax=1,extent=(0,.64,275,875),interpolation="nearest",aspect="auto")
ax[1].set(xlabel="Time within one column scan (s)",ylabel="Tone frequency (Hz)",title="Encoded oscillator amplitudes",yticks=[300,450,600,750,850])
fig.suptitle("Brightness sets amplitude; this is an ideal code, not measured hearing",fontsize=11)
fig.savefig(Path.cwd()/"2022-substitution-encoder.png",dpi=110,transparent=False)
