"""Original stipulated gating model; Python 3.14, numpy and matplotlib.

No experimental data. PNG output is a literal basename in the current directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

phase = np.linspace(0, 24, 241)
baseline = 1 + 0.25*np.cos(2*np.pi*phase/24)
fixed_gain = np.full_like(phase, 0.5)
gated_gain = 0.5 + 0.35*np.cos(2*np.pi*(phase-6)/24)
pulse_phase = np.array([0., 6., 12., 18.])
fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.3), sharex=True, layout='constrained')
fig.patch.set_facecolor('white')
for col, gain in enumerate([fixed_gain, gated_gain]):
    top, bottom = axes[:,col]
    top.plot(phase, baseline, color='#6e7781', ls='--', label='Untreated baseline')
    top.plot(phase, baseline+gain, color='#277b83', label='With identical stimulus')
    top.scatter(pulse_phase, np.interp(pulse_phase,phase,baseline+gain), color='#277b83', s=32)
    top.set(ylim=(0.55,2.25), title=['Constant sensitivity','Circadian gating'][col])
    bottom.plot(phase, gain, color='#98581d', lw=2)
    bottom.scatter(pulse_phase,np.interp(pulse_phase,phase,gain), color='#98581d', s=32)
    bottom.set(ylim=(0,1.0), xlabel='Internal phase (h)')
    for ax in [top,bottom]:
        ax.set_xticks([0,6,12,18,24])
        ax.set_xlim(0,24)
        ax.grid(alpha=0.2)
        ax.spines[['top','right']].set_visible(False)
axes[0,0].set_ylabel('Absolute response (arbitrary units)')
axes[1,0].set_ylabel('Response above baseline')
axes[0,0].legend(fontsize=8.5, loc='upper right')
fig.suptitle('Same stimulus, different internal phase\nIllustrative response curves for separate timed treatments', fontsize=14)
fig.savefig('paper-plm1-clock-gating.png', dpi=160, facecolor='white')
plt.close(fig)
