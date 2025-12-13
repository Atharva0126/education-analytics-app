import streamlit as st
import pandas as pd
import plotly.express as px
from data.education_data import load_data

# Page config (Professional UI)
st.set_page_config(
    page_title="Education Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Load data
df = load_data()

# App Title
st.markdown(
    "<h1 style='text-align:center;'>🎓 Education Analytics Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")

course_filter = st.sidebar.multiselect(
    "Select Course",
    options=df["Course"].unique(),
    default=df["Course"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Course"].isin(course_filter)) &
    (df["Gender"].isin(gender_filter))
]

# KPI Section
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", filtered_df.shape[0])
col2.metric("Average Score", round(filtered_df["Score"].mean(), 2))
col3.metric("Top Score", filtered_df["Score"].max())
col4.metric("Institutes", filtered_df["Institute"].nunique())

st.markdown("---")

# Data Table
st.subheader("📋 Student Data")
st.dataframe(filtered_df, use_container_width=True)

# Charts
st.subheader("📊 Visual Insights")

col5, col6 = st.columns(2)

with col5:
    fig_course = px.bar(
        filtered_df,
        x="Course",
        y="Score",
        color="Course",
        title="Average Score by Course",
        barmode="group"
    )
    st.plotly_chart(fig_course, use_container_width=True)

with col6:
    fig_gender = px.box(
        filtered_df,
        x="Gender",
        y="Score",
        color="Gender",
        title="Score Distribution by Gender"
    )
    st.plotly_chart(fig_gender, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Built with Streamlit & Pandas | Portfolio Project</p>",
    unsafe_allow_html=True
)
