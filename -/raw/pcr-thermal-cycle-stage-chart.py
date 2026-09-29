"""Draw an illustrative thermal schedule, not measured thermocycler data.

Tested with Python 3.14 / matplotlib 3.10.7; run from _media.
Writes pcr-thermal-cycle-stage-chart.png in the CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    holds = [(20, 94, '#b44435', 'Denaturation', 'separate strands'),
             (25, 55, '#2166ac', 'Annealing', 'pair primers'),
             (45, 72, '#16704a', 'Extension', 'copy from 3′ ends')]
    cursor = 0
    for cycle in range(3):
        previous = None
        for duration, temp, color, _, _ in holds:
            if previous is not None:
                ax.plot([cursor, cursor], [previous, temp], color='#7a818c', lw=1.3, ls='--')
            elif cycle:
                ax.plot([cursor, cursor], [72, temp], color='#7a818c', lw=1.3, ls='--')
            ax.axvspan(cursor, cursor + duration, color=color, alpha=0.08, lw=0)
            ax.plot([cursor, cursor + duration], [temp, temp], color=color, lw=4, solid_capstyle='butt')
            ax.text(cursor + duration/2, temp + 2.2, f'{duration} s', ha='center', va='bottom', fontsize=11, color=color)
            cursor += duration
            previous = temp
        ax.text(cycle * 90 + 45, 45.5, f'Cycle {cycle + 1}', ha='center', fontsize=12, weight='bold')
        if cycle < 2:
            ax.axvline(cursor, color='#c4c8cf', lw=1)
    ax.set(xlim=(0, 270), ylim=(43, 104), xlabel='Cumulative stipulated hold time (seconds)', ylabel='Temperature (°C)', xticks=range(0, 271, 30), yticks=[55, 72, 94])
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#e3e5e9', lw=0.7)
    ax.set_axisbelow(True)
    fig.suptitle('PCR thermal cycle: three temperatures, three jobs', fontsize=16, weight='bold', y=0.97)
    ax.set_title('Illustrative holds at 94, 55 and 72 °C; durations are assumptions', fontsize=12, pad=14)
    handles = [Patch(facecolor=color, label=f'{name}: {job}') for _, _, color, name, job in holds]
    fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, 0.09), ncol=1, frameon=False, fontsize=11)
    fig.text(0.5, 0.025, 'Ramps, initial separation and final extension omitted • Vertical jumps are schematic • Not a measured trace', ha='center', fontsize=10, color='#344054')
    fig.subplots_adjust(left=0.1, right=0.97, top=0.81, bottom=0.34)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
