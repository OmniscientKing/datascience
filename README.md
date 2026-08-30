# UC Admissions After the SAT/ACT Ban

## Driving question

**How did the removal of SAT/ACT requirements affect UC admission rates across
different ethnic groups?**

## Methodology

**Data source.** `uc_admissions_summary_by_ethnicity.csv`, drawn from the
UC Information Center's own published systemwide/campus totals by ethnicity
(2017–2025, freshman and transfer, Applicants/Admits/Enrollees). This file was
chosen over the school-level modeling tables specifically because UC redacts
any school-level ethnicity cell below 5 applicants / 3 admits — summing those
redacted rows undercounts smaller groups by an huge amount. The
ethnicity summary file is UC's own aggregate and is not subject to that
redaction problem.

**Defining the three eras.** UC was barred by a 2020 court injunction from
considering SAT/ACT scores starting with the Fall 2021 admissions cycle, and
the policy was later made permanent (test-blind). Fall 2020 is also
COVID-disrupted (test centers closed, many students couldn't test even where
policy allowed it). To avoid conflating "test-optional because of COVID" with
"test-blind by policy," the dashboard splits the timeline into three eras:

| Era | Years | Testing policy |
|---|---|---|
| Pre-COVID | ≤2019 | SAT/ACT required and considered |
| COVID transition | 2020–2021 | Testing suspended / access disrupted |
| Post-removal | 2022–2025 | Fully test-blind |

**Metric.** Admit rate = admits ÷ applicants, computed by **pooling counts
first, then dividing** (never averaging per-year rates), per the dataset's own
guidance — this avoids small-year noise skewing the average. The "net shift"
view compares the pooled Pre-COVID rate to the pooled Post-removal rate for
each ethnicity, in percentage points.

**Scope and limits.** This shows systemwide (or a selected campus's) admit
rate trends; it is descriptive, not causal. Applicant volumes by ethnicity
also changed over this period, independent of the testing policy, which
affects rates on its own — the per-era applicant/admit tables let a user check
whether a rate change came from more admits, fewer/more applicants, or both.
Race is recorded here only as a reported outcome: California's Prop 209 (1996)
prohibits UC from using race as an admissions input, so these are not
race-conscious admissions decisions, only their demographic result.
"Unknown" and "International" are excluded from the default view since they
don't represent a U.S. racial/ethnic category comparison, but can be
re-added via the ethnicity filter.

## What the dashboard does
1. **Trend line** — admit rate by ethnicity, 2017–2025, with the COVID/removal
   transition window shaded.
2. **Three-era tabs** — applicant/admit volume and admit rate per ethnicity,
   matching Pre-COVID / COVID transition / Post-removal, with a data table.
3. **Net shift chart** — percentage-point change in admit rate per ethnicity,
   Pre-COVID baseline vs. Post-removal.
4. **Auto-generated conclusion** — recomputed live from whatever campus/level/
   ethnicity filters the user has selected, naming the largest gain and the
   largest drop.

All charts are filterable by applicant type (freshman/transfer), campus, and
ethnicity group.

## Conclusions
Through our 

## Running local
Link: https://claude.ai/public/artifacts/71f14a5a-ef4a-474d-9265-1ccabf3411cd
