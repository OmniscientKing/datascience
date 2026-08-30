import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="UC Admissions: Test-Blind Impact", layout="wide", page_icon="🎓")

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("uc_admissions_summary_by_ethnicity.csv")
    piv = (
        df.pivot_table(
            index=["entrant_level", "campus", "fall_term", "ethnicity"],
            columns="count_type",
            values="n",
        )
        .reset_index()
    )
    piv["admit_rate"] = piv["Adm"] / piv["App"]
    piv["yield_rate"] = piv["Enr"] / piv["Adm"]

    def era(year):
        if year <= 2019:
            return "Pre-COVID (≤2019) — SAT/ACT required"
        elif year <= 2021:
            return "COVID transition (2020–2021) — testing suspended"
        else:
            return "Post-removal (2022–2025) — test-blind"

    piv["era"] = piv["fall_term"].apply(era)
    return piv


data = load_data()
ERA_ORDER = [
    "Pre-COVID (≤2019) — SAT/ACT required",
    "COVID transition (2020–2021) — testing suspended",
    "Post-removal (2022–2025) — test-blind",
]
ERA_COLORS = {
    ERA_ORDER[0]: "#4C78A8",
    ERA_ORDER[1]: "#F58518",
    ERA_ORDER[2]: "#54A24B",
}

# ---------------------------------------------------------------------------
# Header / Banner
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div style="padding:28px 32px;border-radius:14px;
                background:linear-gradient(120deg,#0b3d91,#1e6fd9 60%,#54A24B);
                color:white;margin-bottom:18px;">
        <div style="font-size:2.1rem;font-weight:700;">
            UC Admissions After the SAT/ACT Ban
        </div>
        <div style="font-size:1.05rem;opacity:0.92;margin-top:6px;">
            Tracking systemwide freshman &amp; transfer admissions by ethnicity, 2017–2025
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Intro / background
# ---------------------------------------------------------------------------
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Background")
        st.markdown(
            """
Standardized test scores (SAT/ACT) were once a core input in University of California
admissions decisions. A 2020 court injunction barred UC from considering SAT/ACT scores
starting with the **Fall 2021** cycle, and the UC Board of Regents subsequently made the
policy permanent (test-blind) through the period covered by this data.

That policy shift, layered on top of the COVID-19 disruption to testing access in 2020,
created a natural before/after comparison.
            """
        )
    with col2:
        st.subheader("Driving Question")
        st.info(
            "**How did the removal of SAT/ACT requirements affect UC admission rates "
            "across different ethnic groups?**"
        )

st.divider()

# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
st.subheader("Explore the data")
c1, c2, c3 = st.columns(3)
with c1:
    level = st.radio("Applicant type", ["freshman", "transfer"], horizontal=True)
with c2:
    campus = st.selectbox("Campus", sorted(data["campus"].unique()), index=sorted(data["campus"].unique()).index("Systemwide"))
with c3:
    ethnicities = sorted(data["ethnicity"].unique())
    default_eth = [e for e in ethnicities if e not in ("Unknown", "International")]
    selected_eth = st.multiselect("Ethnicities", ethnicities, default=default_eth)

filtered = data[
    (data.entrant_level == level) & (data.campus == campus) & (data.ethnicity.isin(selected_eth))
].copy()

if filtered.empty:
    st.warning("No data for this combination — pick at least one ethnicity.")
    st.stop()

# ---------------------------------------------------------------------------
# 1) Admit rate trend line — the core answer to the driving question
# ---------------------------------------------------------------------------
st.markdown("### Admit rate by ethnicity, 2017–2025")
fig_line = px.line(
    filtered.sort_values("fall_term"),
    x="fall_term",
    y="admit_rate",
    color="ethnicity",
    markers=True,
    labels={"fall_term": "Fall term", "admit_rate": "Admit rate", "ethnicity": "Ethnicity"},
)
fig_line.update_yaxes(tickformat=".0%")
fig_line.add_vrect(x0=2019.5, x1=2021.5, fillcolor="orange", opacity=0.12, line_width=0,
                    annotation_text="Testing suspended → removed", annotation_position="top left")
fig_line.update_layout(height=460, legend_title="Ethnicity", hovermode="x unified")
st.plotly_chart(fig_line, use_container_width=True)
st.caption(
    "Shaded band marks the COVID disruption (2020) through the first fully test-blind "
    "cycle (2021). Fall 2020 is COVID-distorted; treat it as transitional, not baseline."
)

st.divider()

# ---------------------------------------------------------------------------
# 2) Three-era comparison — matches the wireframe's 3-panel layout
# ---------------------------------------------------------------------------
st.markdown("### Applicants vs. Admits, by era")
era_tabs = st.tabs(["Pre-COVID (≤2019)", "COVID transition (2020–2021)", "Post-removal (2022–2025)"])

for tab, era_name in zip(era_tabs, ERA_ORDER):
    with tab:
        era_df = (
            filtered[filtered.era == era_name]
            .groupby("ethnicity")[["App", "Adm", "Enr"]]
            .sum()
            .reset_index()
        )
        era_df["admit_rate"] = era_df["Adm"] / era_df["App"]

        colA, colB = st.columns(2)
        with colA:
            fig_bar = go.Figure()
            fig_bar.add_bar(name="Applicants", x=era_df["ethnicity"], y=era_df["App"], marker_color="#9ecae1")
            fig_bar.add_bar(name="Admits", x=era_df["ethnicity"], y=era_df["Adm"], marker_color=ERA_COLORS[era_name])
            fig_bar.update_layout(barmode="group", height=380, title="Applicant & admit volume (summed across era)",
                                   yaxis_title="Students")
            st.plotly_chart(fig_bar, use_container_width=True)
        with colB:
            fig_rate = px.bar(
                era_df.sort_values("admit_rate", ascending=False),
                x="ethnicity",
                y="admit_rate",
                color="ethnicity",
                text_auto=".1%",
            )
            fig_rate.update_yaxes(tickformat=".0%", title="Admit rate")
            fig_rate.update_layout(height=380, showlegend=False, title="Admit rate by ethnicity (pooled counts)")
            st.plotly_chart(fig_rate, use_container_width=True)

        st.dataframe(
            era_df.rename(columns={"App": "Applicants", "Adm": "Admits", "Enr": "Enrolled"})
            .assign(**{"Admit rate": lambda d: (d["admit_rate"] * 100).round(1).astype(str) + "%"})
            .drop(columns="admit_rate")
            .sort_values("Applicants", ascending=False),
            use_container_width=True,
            hide_index=True,
        )

st.divider()

# ---------------------------------------------------------------------------
# 3) Change table: Pre-COVID -> Post-removal shift per ethnicity
# ---------------------------------------------------------------------------
st.markdown("### Net shift: Pre-COVID baseline → Post-removal")
pre = (
    filtered[filtered.era == ERA_ORDER[0]].groupby("ethnicity")[["App", "Adm"]].sum()
)
post = (
    filtered[filtered.era == ERA_ORDER[2]].groupby("ethnicity")[["App", "Adm"]].sum()
)
shift = pre.join(post, lsuffix="_pre", rsuffix="_post").dropna()
shift["rate_pre"] = shift["Adm_pre"] / shift["App_pre"]
shift["rate_post"] = shift["Adm_post"] / shift["App_post"]
shift["pct_point_change"] = (shift["rate_post"] - shift["rate_pre"]) * 100
shift = shift.reset_index().sort_values("pct_point_change", ascending=False)

fig_shift = px.bar(
    shift,
    x="ethnicity",
    y="pct_point_change",
    color="pct_point_change",
    color_continuous_scale="RdYlGn",
    text_auto=".1f",
    labels={"pct_point_change": "Change in admit rate (pct. points)", "ethnicity": "Ethnicity"},
)
fig_shift.update_layout(height=420, coloraxis_showscale=False)
st.plotly_chart(fig_shift, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# 4) Conclusions — computed live from current filters
# ---------------------------------------------------------------------------
st.markdown("### Conclusions")
if not shift.empty:
    biggest_gain = shift.iloc[0]
    biggest_drop = shift.iloc[-1]
    overall_pre = pre["Adm"].sum() / pre["App"].sum()
    overall_post = post["Adm"].sum() / post["App"].sum()
    st.markdown(
        f"""
For **{level} applicants at {campus}**, comparing the pre-COVID baseline (≤2019, SAT/ACT
required) to the post-removal era (2022–2025, test-blind):

- Overall pooled admit rate moved from **{overall_pre:.1%}** to **{overall_post:.1%}**
  ({'+' if overall_post >= overall_pre else ''}{(overall_post-overall_pre)*100:.1f} points).
- **{biggest_gain['ethnicity']}** saw the largest increase in admit rate:
  {biggest_gain['rate_pre']:.1%} → {biggest_gain['rate_post']:.1%}
  ({biggest_gain['pct_point_change']:+.1f} points).
- **{biggest_drop['ethnicity']}** saw the largest decrease:
  {biggest_drop['rate_pre']:.1%} → {biggest_drop['rate_post']:.1%}
  ({biggest_drop['pct_point_change']:+.1f} points).

These are systemwide/campus **admit-rate** shifts, not causal proof that removing
SAT/ACT alone drove the change — application volumes also shifted across ethnic groups
over this period, which affects rates independent of admissions policy. Use the
per-era tables above to check whether a rate change was driven by more admits, fewer
applicants, or both.
        """
    )
else:
    st.write("Select ethnicities with data in both eras to generate a conclusion.")

st.caption(
    "Source: UC Information Center, systemwide/campus admissions summary by ethnicity, "
    "Fall 2017–2025. 'Unknown' and 'International' excluded by default. Race is reported "
    "as an outcome only — California's Prop 209 (1996) bars its use as an admissions input."
)
