"""Original functional beam-clock diagram; Python 3.14, Matplotlib 3.10.7.

Run from _media; writes cesium-beam-clock-feedback.png to CWD.
Magnetic-selector layout follows the functions in Sullivan et al. (2001), Fig. 1.
This is not a reproduction of the apparatus drawing or a dimensional design.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(11.5, 5.4), layout='constrained')
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 12), ylim=(0, 6))
    ax.axis('off')
    navy, orange, green = '#225b91', '#ce6327', '#28784a'

    def arrow(a, b, color=navy, style='-|>', lw=1.7):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=13,
                                    color=color, lw=lw))

    def box(x, y, w, h, label, color=navy, fill='#f0f6fb', size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03',
                                   fc=fill, ec=color, lw=1.5))
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center', fontsize=size)

    ax.text(6, 5.75, 'Functional cesium beam clock',
            ha='center', fontsize=14, weight='bold')
    ax.add_patch(FancyBboxPatch((0.2, 2.95), 11.55, 2.25,
                               boxstyle='round,pad=0.02', fc='white', ec='#aaaaaa', ls='--'))
    ax.text(0.35, 5.02, 'Vacuum beam path', fontsize=10, color='#555555')
    ax.add_patch(FancyBboxPatch((3.3, 3.15), 4.7, 1.7,
                               boxstyle='round,pad=0.02', fc='#f4f8f2', ec='#91ac8b'))
    ax.text(5.65, 4.63, 'Weak static magnetic field', ha='center', fontsize=10, color=green)
    arrow((0.65, 3.92), (11.15, 3.92), color='#aaaaaa', lw=1)
    box(0.45, 3.5, 1.1, 0.85, 'Oven +\nslits')
    box(1.95, 3.5, 1.05, 0.85, 'State\nselector A')
    box(3.7, 3.4, 0.65, 1.0, '1', color=orange, fill='#fff0e3')
    box(6.95, 3.4, 0.65, 1.0, '2', color=orange, fill='#fff0e3')
    box(8.4, 3.5, 1.05, 0.85, 'State\nselector B')
    box(10.05, 3.5, 1.35, 0.85, 'Hot-wire\ndetector')
    for left, right in [(1.55, 1.95), (3.0, 3.7), (4.35, 6.95), (7.6, 8.4), (9.45, 10.05)]:
        arrow((left, 3.92), (right, 3.92))
    ax.text(5.65, 4.18, 'Drive-free flight', ha='center', fontsize=11)
    ax.text(5.65, 3.51, r'$T=L/v$', ha='center', fontsize=12)
    ax.text(5.65, 3.14, r'Two microwave regions: $\tau=\ell/v$ each',
            ha='center', va='bottom', fontsize=10)
    box(3.55, 1.2, 3.0, 0.85, 'Tunable oscillator\n+ microwave synthesis', size=11)
    arrow((4.02, 2.05), (4.02, 3.35), color=orange)
    arrow((6.05, 2.55), (7.27, 2.55), color=orange)
    arrow((6.05, 2.05), (6.05, 2.55), color=orange)
    arrow((7.27, 2.55), (7.27, 3.35), color=orange)
    ax.text(5.35, 2.80, 'Common phase reference', ha='center', fontsize=10, color=orange)
    box(8.1, 1.2, 3.3, 0.85, 'Compare signals at two frequencies\nAdjust the center until equal',
        color=green, fill='#f0f8f1', size=10)
    arrow((10.72, 3.5), (10.72, 2.1), color=green)
    arrow((8.1, 1.62), (6.6, 1.62), color=green)
    ax.text(7.3, 1.88, 'Feedback', color=green, ha='center', fontsize=10)
    box(0.45, 1.2, 2.05, 0.85, 'Count calibrated\noscillator cycles', size=10)
    arrow((3.5, 1.62), (2.55, 1.62))
    ax.text(6, 0.55, 'Schematic; not to scale.',
            ha='center', fontsize=10, color='#555555')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
