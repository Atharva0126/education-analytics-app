import streamlit as st
import pandas as pd
import plotly.express as px
from data.education_data import load_student_master, load_student_performance

# Page config (Professional UI)
st.set_page_config(
    page_title="Education Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Load data
df_master = load_student_master()
df_performance = load_student_performance()

# App Title
st.markdown(
    "<h1 style='text-align:center;'>🎓 Education Analytics Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data & 🔗 Data Join & Merge Demonstration")

option = st.selectbox(
    "Select Operation",
    ["Inner Merge", "Left Merge", "Right Merge", "Join", "Concat (Vertical)", "Concat (Horizontal)"]
)

if option == "Inner Merge":
    st.dataframe(df_merge_inner)
elif option == "Left Merge":
    st.dataframe(df_merge_left)
elif option == "Right Merge":
    st.dataframe(df_merge_right)
elif option == "Join":
    st.dataframe(df_join)
elif option == "Concat (Vertical)":
    st.dataframe(df_concat_vertical)
elif option == "Concat (Horizontal)":
    st.dataframe(df_concat_horizontal)

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

df_merge_inner = pd.merge(
    df_master,
    df_performance,
    on="Student_ID",
    how="inner"
)

df_merge_left = pd.merge(
    df_master,
    df_performance,
    on="Student_ID",
    how="left"
)

df_merge_right = pd.merge(
    df_master,
    df_performance,
    on="Student_ID",
    how="right"
)

df_join = df_master.set_index("Student_ID").join(
    df_performance.set_index("Student_ID"),
    how="inner"
)

df_concat_vertical = pd.concat(
    [df_master, df_master],
    axis=0,
    ignore_index=True
)

df_concat_horizontal = pd.concat(
    [df_master, df_performance],
    axis=1
)


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
