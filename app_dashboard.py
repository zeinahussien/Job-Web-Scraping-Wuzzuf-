import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Wuzzuf Job Market Intelligence", page_icon="📊", layout="wide"
)

def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

@st.cache_data
def load_data():
    df = pd.read_csv("wuzzuf_jobs_cleaned.csv")
    return df

df = load_data()

st.sidebar.markdown("## Control Center")
st.sidebar.markdown("Filter live intelligence harvested across Egypt's tech sectors.")

search_query = st.sidebar.text_input("Search Job Title / Company", "")

tracks = sorted(df["track"].dropna().unique().tolist())
selected_track = st.sidebar.selectbox("Filter by Track", ["All Tracks"] + tracks)

work_modes = sorted(df["work_mode"].dropna().unique().tolist())
selected_mode = st.sidebar.selectbox("Filter by Work Mode", ["All Modes"] + work_modes)

filtered_df = df.copy()
if selected_track != "All Tracks":
    filtered_df = filtered_df[filtered_df["track"] == selected_track]
if selected_mode != "All Modes":
    filtered_df = filtered_df[filtered_df["work_mode"] == selected_mode]
if search_query:
    filtered_df = filtered_df[
        filtered_df["job_title"].str.contains(search_query, case=False, na=False) |
        filtered_df["company"].str.contains(search_query, case=False, na=False)
    ]

st.title("Wuzzuf Job Market Intelligence")
st.markdown("Real-time analytics engine tracking demand, roles, and hiring trends in Egypt's engineering sector.")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Listings", len(filtered_df))
col2.metric("Hiring Companies", filtered_df["company"].nunique())
col3.metric("Remote Share", f"{(len(filtered_df[filtered_df['work_mode'] == 'Remote']) / len(filtered_df) * 100 if len(filtered_df) > 0 else 0):.1f}%")
col4.metric("Unique Tracks", filtered_df["track"].nunique())

st.markdown("---")

chart_col1, chart_col2 = st.columns(2)

pastel_colors = ["#b4f8c8", "#a0e7e5", "#ffaebc", "#ffc6ff", "#fdffb6", "#caffbf", "#9bf6ff"]

with chart_col1:
    st.subheader("Top Hiring Companies")
    if not filtered_df.empty:
        top_companies = filtered_df["company"].value_counts().head(8).reset_index()
        top_companies.columns = ["Company", "Openings"]
        fig_comp = px.bar(
            top_companies,
            x="Openings",
            y="Company",
            orientation="h",
            color="Openings",
            color_continuous_scale=["#a0e7e5", "#b4f8c8", "#fdffb6"],
            template="plotly_dark"
        )
        fig_comp.update_layout(
            yaxis={"categoryorder": "total ascending"},
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_comp, use_container_width=True)
    else:
        st.info("No data available for current filters.")

with chart_col2:
    st.subheader("Work Mode Distribution")
    if not filtered_df.empty:
        mode_counts = filtered_df["work_mode"].value_counts().reset_index()
        mode_counts.columns = ["Work Mode", "Count"]
        fig_mode = px.pie(
            mode_counts,
            names="Work Mode",
            values="Count",
            hole=0.4,
            template="plotly_dark",
            color_discrete_sequence=pastel_colors
        )
        fig_mode.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_mode, use_container_width=True)
    else:
        st.info("No data available for current filters.")

st.markdown("---")

st.subheader("Live Job Feed Explorer")
st.markdown("Click any job link below to view the official Wuzzuf posting.")

display_df = filtered_df[['track', 'job_title', 'company', 'location', 'work_mode', 'job_experience', 'job_url']]
st.dataframe(display_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #a0a0a0;'>Engineered with Python, Pandas, Plotly & Streamlit.</p>", unsafe_allow_html=True)