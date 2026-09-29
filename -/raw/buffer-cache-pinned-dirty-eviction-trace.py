"""Exact two-slot buffered partial-write trace; writes matching PNG to CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Serialized successful I/O; request completion refreshes recency, pin does not.
Backing values are toy contents, not measurements or durability guarantees.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

EVENTS = [('read', 'A', None), ('write', 'A', 11), ('pin', 'A', None),
          ('read', 'B', None), ('read', 'C', None), ('read', 'A', None),
          ('write', 'A', 12), ('read', 'C', None), ('unpin', 'A', None),
          ('read', 'B', None)]


def simulate(capacity=2, with_pin=True):
    slots = [None] * capacity
    recent = []
    backing = {'A': 10, 'B': 20, 'C': 30}
    rows = []
    counts = dict(hits=0, misses=0, reads=0, writes=0)
    for action, key, value in EVENTS:
        if not with_pin and action in ('pin', 'unpin'):
            continue
        slot = next((i for i, entry in enumerate(slots) if entry and entry['key'] == key), None)
        result, io, victim, observed = '—', '—', '—', None
        if action in ('pin', 'unpin'):
            assert slot is not None
            slots[slot]['refs'] += 1 if action == 'pin' else -1
            assert slots[slot]['refs'] >= 0
        else:
            hit = slot is not None
            counts['hits' if hit else 'misses'] += 1
            result = 'HIT' if hit else 'MISS'
            if not hit:
                slot = next((i for i, entry in enumerate(slots) if entry is None), None)
                if slot is None:
                    candidates = [k for k in recent if any(e and e['key'] == k and e['refs'] == 0 for e in slots)]
                    if not candidates:
                        return {'blocked_on': f'{action} {key}', 'counts': counts, 'rows': rows}
                    victim = candidates[0]
                    slot = next(i for i, entry in enumerate(slots) if entry['key'] == victim)
                    old = slots[slot]
                    if old['dirty']:
                        backing[victim] = old['value']
                        counts['writes'] += 1
                        io = f'write {victim}={old["value"]}; read {key}'
                    recent.remove(victim)
                if io == '—':
                    io = f'read {key}'
                counts['reads'] += 1
                slots[slot] = dict(key=key, value=backing[key], dirty=False, refs=0)
            entry = slots[slot]
            entry['refs'] += 1
            if action == 'write':
                entry.update(value=value, dirty=True)
            observed = entry['value']
            entry['refs'] -= 1
            if key in recent:
                recent.remove(key)
            recent.append(key)
        live_keys = [e['key'] for e in slots if e]
        assert len(live_keys) == len(set(live_keys))
        assert set(live_keys) == set(recent)
        assert all(e['refs'] >= 0 and (e['dirty'] or e['value'] == backing[e['key']]) for e in slots if e)
        rows.append(dict(event=action+' '+key+(f'={value}' if action == 'write' else ''),
                         result=result, victim=victim, io=io, observed=observed,
                         slots=[dict(e) if e else None for e in slots],
                         lru=list(recent), backing=dict(backing)))
    return dict(counts=counts, rows=rows, backing=backing, resident_keys=recent)


def main():
    trace = simulate()
    assert trace['counts'] == dict(hits=4, misses=4, reads=4, writes=1)
    assert trace['backing']['A'] == 12 and trace['resident_keys'] == ['C', 'B']
    assert trace['rows'][4]['victim'] == 'B' and trace['rows'][-1]['victim'] == 'A'
    fig, ax = plt.subplots(figsize=(10.8, 6.2), dpi=120)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    fig.subplots_adjust(left=.02, right=.98, top=.82, bottom=.17)
    fig.suptitle('Two-slot buffer cache: a pin changes the eviction victim', fontsize=16, y=.96)
    fig.text(.5, .89, 'Partial writes; successful serialized I/O; oldest eligible key is evicted', ha='center', fontsize=11)
    data = []
    for n, row in enumerate(trace['rows'], 1):
        def fmt(entry):
            return 'empty' if entry is None else f'{entry["key"]}={entry["value"]}  {"D" if entry["dirty"] else "C"}  r={entry["refs"]}'
        data.append([str(n), row['event'], row['result'], row['victim'],
                     fmt(row['slots'][0]), fmt(row['slots'][1]), row['io']])
    table = ax.table(cellText=data, colLabels=['Step', 'Operation', 'Lookup', 'Evict', 'Slot 0 after', 'Slot 1 after', 'Device I/O'],
                     cellLoc='center', loc='center', colWidths=[.055,.16,.085,.065,.20,.20,.235])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.9)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#c4cbd0')
        if row == 0:
            cell.set_facecolor('#e6edf2')
            cell.set_text_props(weight='bold')
        else:
            cell.set_facecolor('#ffffff' if row % 2 else '#f6f8fa')
            if col == 2:
                cell.set_facecolor('#dcefe2' if data[row-1][2] == 'HIT' else '#f6e0cf' if data[row-1][2] == 'MISS' else '#f0f0f0')
            if col in (4, 5) and 'D ' in data[row-1][col]:
                cell.set_facecolor('#fff0dd')
    fig.text(.5,.105,'C = clean, D = dirty; r counts retained references after each step.',ha='center',fontsize=11)
    fig.text(.5,.06,'8 data requests: 4 hits, 4 misses  •  4 device reads, 1 device write  •  no storage flush',ha='center',fontsize=11,weight='bold')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)
    print(json.dumps({'trace': trace, 'capacity_sweep': [dict(capacity=n, with_pin=pin, result=simulate(n,pin)) for n in (1,2,3) for pin in (False,True)]}))


if __name__ == '__main__':
    main()
