"""Exact serialized buffer-state rules; writes matching PNG to the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
This teaching model excludes cancellation, failures and concurrent I/O.
"""
from collections import deque
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def successors(state, bound=2):
    if state is None:
        return [('reserve', (0, 0, 1))]
    v, dirty, refs = state
    result = []
    if refs < bound:
        result.append(('acquire or pin', (v, dirty, refs + 1)))
    if v and refs:
        result.append(('release or unpin', (v, dirty, refs - 1)))
        result.append(('modify', (1, 1, refs)))
    if not v and refs:
        result.append(('fill', (1, 0, refs)))
    if v and dirty:
        result.append(('writeback', (1, 0, refs)))
    if v and not dirty and not refs:
        result.append(('evict', None))
    return result


def reachable():
    seen = {None}
    queue = deque([None])
    edges = []
    while queue:
        source = queue.popleft()
        for action, target in successors(source):
            edges.append((source, action, target))
            if target not in seen:
                seen.add(target)
                queue.append(target)
    assert len(seen) == 9
    for source, action, target in edges:
        if target is not None:
            v, dirty, refs = target
            assert 0 <= dirty <= v <= 1 and 0 <= refs <= 2
            assert v or refs > 0
        if action == 'evict':
            assert source == (1, 0, 0)
    return seen, edges


def main():
    states, edges = reachable()
    fig, ax = plt.subplots(figsize=(10, 5.7), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    fig.subplots_adjust(left=.015, right=.985, top=.86, bottom=.05)
    fig.suptitle('One cached block: contents and lifetime are separate', fontsize=16, y=.96)
    fig.text(.5, .895, 'Exact rules of the serialized model; all I/O succeeds', ha='center', fontsize=11)
    boxes = [(.12, 'Absent\nno key', '#f0f0f0'),
             (.37, 'Reserved\nv = 0, D = 0\nr ≥ 1', '#f4ebc7'),
             (.62, 'Valid clean\nv = 1, D = 0', '#d9eaf2'),
             (.87, 'Valid dirty\nv = 1, D = 1', '#f6d9c6')]
    for x, text, color in boxes:
        ax.add_patch(FancyBboxPatch((x-.1, .62), .2, .22, boxstyle='round,pad=0.008', facecolor=color, edgecolor='#46515a'))
        ax.text(x, .73, text, ha='center', va='center', fontsize=12)
    def arrow(start, end, label, pos, rad=0):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=13,
                                     connectionstyle=f'arc3,rad={rad}', lw=1.6, color='#334754'))
        ax.text(*pos, label, ha='center', va='center', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='none', pad=2))
    arrow((.225,.74),(.265,.74),'reserve\nr ← 1',(.245,.91))
    arrow((.475,.74),(.515,.74),'fill\nv ← 1',(.495,.91))
    arrow((.725,.79),(.765,.79),'modify\nr > 0',(.745,.91))
    arrow((.765,.64),(.725,.64),'writeback\nD ← 0',(.745,.52),rad=-.5)
    arrow((.57,.61),(.12,.61),'evict only if r = 0',(.33,.43),rad=-.55)
    ax.text(.87,.40,'No dirty → absent edge:\nwrite back before reuse.',ha='center',fontsize=11)
    ax.axhline(.30, color='#c7cdd2', lw=1)
    ax.text(.5,.255,'Reference transitions keep v and D unchanged',ha='center',fontsize=12,weight='bold')
    ax.text(.5,.17,'acquire / pin:  r → r + 1       release / unpin:  r → r − 1  (v = 1, r > 0)',ha='center',fontsize=12)
    ax.text(.5,.085,'r counts holders and pins. Any r > 0 forbids eviction, even when clean.',ha='center',fontsize=11)
    ax.text(.5,.015,'Writeback retains an internal reference during I/O; its net change to r is zero.',ha='center',fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)
    print(json.dumps({'reachable_states': len(states), 'transitions': len(edges),
                      'states': sorted([s for s in states if s is not None]),
                      'absent_state': True, 'invariants_passed': True}))


if __name__ == '__main__':
    main()
