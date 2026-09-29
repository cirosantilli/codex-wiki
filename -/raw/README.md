# Codex Wiki

This repository contains a Codex-generated knowledge written in OurBigBook markup, created with a decent amount of human guidance.

The human readable readme is index.bigb.

The agent guidelines are at AGENTS.md.

Google Analytics 4 can be enabled at deployment time by adding a `googleAnalyticsMeasurementId` property such as `"G-XXXXXXXXXX"` to `ourbigbook.json`. If the property is absent, the generated pages do not load Google Analytics.

Figure generators use the Python environment declared in `pyproject.toml`, tested with Python 3.14.4. To reproduce the figures:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
export MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
find past-exam-of-the-mathematics-course-of-the-university-of-cambridge -name '*.py' -exec python {} \;
```

## Natural Sciences exam stubs

Each course's exams have their own top-level directory, for example
`past-exam-of-the-soft-condensed-matter-course-of-the-university-of-cambridge/`.
The study year is included only where the course name needs disambiguation,
as with Natural Sciences mathematics in years 1 and 2 and year-1 physics.
The catalogue's `source_path` retains the exam archive's
`tex/nst/PART/COURSE/` path; `path` specifies the wiki directory relative to
the repository root. Each course has an `index.bigb`, linked from its entry in
`university-of-cambridge.bigb`. A single-paper year uses `YEAR.bigb`;
multiple-paper years use `YEAR/index.bigb` and `YEAR/paper-N.bigb`.
Years appear newest first.

The existing 98 mathematics paper files were moved without changing their
contents. Mathematics has separate Part IA and Part IB course entries.

Run from the repository root:

```sh
python3 tools/import-nst-exam-stubs.py
python3 tools/import-nst-exam-stubs.py --check
ourbigbook .
```

Use `--tex-root PATH` for a different exam archive location. The importer
requires only the Python standard library. It extracts section labels,
question numbers, lettered parts, and nested Roman or numeric parts. It
handles restarted enumerations and the transcription's explicit numbering
macros. It emits no statements, mathematical expressions, diagrams, or
solutions, and never overwrites an existing paper. `--check` compares the
header trees while allowing future solution prose.

`nst-exam-catalog.json` records course placement, source links and explicit
solution-coverage exclusions. Review this evidence before adding new papers:

* Theories of Quantum Matter: all eight currently transcribed papers have
  worked solutions and are excluded.
* Thermal and Statistical Physics: the 2022 released paper includes worked
  solutions and is excluded; the other available years are included.
* Physics B, 2017: selected final answers are available, but these sheets do
  not cover every question. Both papers are included and link to the sheets.
* Examiner commentary is not assumed to be a complete worked solution.
  Exact solution coverage inside the restricted Cambridge teaching system
  remains unverified.

The Cambridge release is available at
https://www.whatdotheyknow.com/request/natural_science_tripos_physics_e .
Links use the original 509-page PDF's page positions, as recorded in
`pdf/nst/sullivan-2022/README.md` in the exam archive. Ten older Quantum
Condensed Matter papers link to the official course archive; their direct
PDF URLs remain unverified.
