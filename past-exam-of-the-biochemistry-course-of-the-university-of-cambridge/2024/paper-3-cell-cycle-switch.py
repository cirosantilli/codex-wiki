"""Original ideal-relay diagram. Python 3.14, numpy and matplotlib; PNG output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(8.2, 4.8), facecolor='white')
off, on, low, high = .30, .70, .17, .83
ax.axvspan(off, on, color='#f5e8c9', alpha=.7)
ax.plot([0, on], [low, low], color='#176298', lw=3)
ax.plot([off, 1], [high, high], color='#176298', lw=3)
ax.plot([off, off], [low, high], color='#858585', ls=':', lw=1.5)
ax.plot([on, on], [low, high], color='#858585', ls=':', lw=1.5)
for start, end in [((.08, low), (.57, low)), ((on, low), (on, high)), ((.94, high), (.43, high)), ((off, high), (off, low))]:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=17, color='#b74a2c', lw=2, zorder=4))
ax.text(.44, .05, 'Rising input', ha='center', color='#923a24')
ax.text(.66, .94, 'Falling input after cyclin destruction', ha='center', color='#923a24', fontsize=10)
ax.text(.5, .5, 'Either state persists here:\nhistory matters', ha='center', va='center', fontsize=12)
ax.text(.18, .24, 'Low CDK activity', ha='center', fontsize=10)
ax.text(.82, .72, 'High CDK activity', ha='center', fontsize=10)
ax.set(xlim=(-.02, 1.02), ylim=(0, 1), xlabel='Effective activating input, u (arbitrary units)', ylabel='Switch activity (arbitrary units)')
ax.set_xticks([off, on], [r'$u_{\mathrm{off}}$', r'$u_{\mathrm{on}}$'])
ax.set_yticks([])
ax.spines[['top', 'right']].set_visible(False)
ax.set_title('Distinct activation and reset thresholds', fontsize=15, weight='bold')
fig.text(.5, .025, 'Idealized switch logic; no numerical thresholds or response curves are experimental data.', ha='center', fontsize=9)
fig.tight_layout(rect=(0, .06, 1, 1))
fig.savefig('paper-3-cell-cycle-switch.png', dpi=150, facecolor='white')
plt.close(fig)
