import streamlit as st
import pandas as pd
from data.education_data import load_student_master, load_student_performance

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Education Data Operations Dashboard",
    layout="wide"
)

st.title("🎓 Education Data – Join, Merge & Concat Dashboard")

# =========================
# LOAD DATA
# =========================
df_master = load_student_master()
df_performance = load_student_performance()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🔎 Filters")

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df_master["Gender"].unique(),
    default=df_master["Gender"].unique()
)

selected_institute = st.sidebar.multiselect(
    "Select Institute",
    options=df_master["Institute"].unique(),
    default=df_master["Institute"].unique()
)

selected_course = st.sidebar.multiselect(
    "Select Course",
    options=df_performance["Course"].unique(),
    default=df_performance["Course"].unique()
)

score_range = st.sidebar.slider(
    "Select Score Range",
    int(df_performance["Score"].min()),
    int(df_performance["Score"].max()),
    (0, 100)
)

# =========================
# APPLY FILTERS
# =========================
filtered_master = df_master[
    (df_master["Gender"].isin(selected_gender)) &
    (df_master["Institute"].isin(selected_institute))
]

filtered_performance = df_performance[
    (df_performance["Course"].isin(selected_course)) &
    (df_performance["Score"].between(score_range[0], score_range[1]))
]

# =========================
# CREATE OPER
