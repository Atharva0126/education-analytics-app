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
# CREATE OPERATIONS
# =========================
df_merge_inner = pd.merge(
    filtered_master, filtered_performance,
    on="Student_ID", how="inner"
)

df_merge_left = pd.merge(
    filtered_master, filtered_performance,
    on="Student_ID", how="left"
)

df_merge_right = pd.merge(
    filtered_master, filtered_performance,
    on="Student_ID", how="right"
)

df_join = filtered_master.set_index("Student_ID").join(
    filtered_performance.set_index("Student_ID"),
    how="inner"
)

df_concat_vertical = pd.concat(
    [filtered_performance, filtered_performance],
    axis=0,
    ignore_index=True
)

df_concat_horizontal = pd.concat(
    [
        filtered_master.reset_index(drop=True),
        filtered_performance.reset_index(drop=True)
    ],
    axis=1
)

df_left_merge_filled = df_merge_left.fillna({
    "Course": "Not Enrolled",
    "Score": 0
})

# =========================
# OPERATION SELECTOR
# =========================
operation = st.selectbox(
    "📌 Select Data Operation",
    [
        "Inner Merge",
        "Left Merge",
        "Right Merge",
        "Join",
        "Concat (Vertical)",
        "Concat (Horizontal)",
        "Left Merge (NaN Handled)"
    ]
)

# =========================
# DISPLAY RESULTS
# =========================
if operation == "Inner Merge":
    st.subheader("🔗 INNER MERGE")
    st.dataframe(df_merge_inner, use_container_width=True)

elif operation == "Left Merge":
    st.subheader("⬅️ LEFT MERGE")
    st.dataframe(df_merge_left, use_container_width=True)

elif operation == "Right Merge":
    st.subheader("➡️ RIGHT MERGE")
    st.dataframe(df_merge_right, use_container_width=True)

elif operation == "Join":
    st.subheader("🔑 JOIN (Index-Based)")
    st.dataframe(df_join, use_container_width=True)

elif operation == "Concat (Vertical)":
    st.subheader("⬇️ CONCAT – VERTICAL (UNION ALL)")
    st.dataframe(df_concat_vertical, use_container_width=True)

elif operation == "Concat (Horizontal)":
    st.subheader("➡️ CONCAT – HORIZONTAL")
    st.dataframe(df_concat_horizontal, use_container_width=True)

elif operation == "Left Merge (NaN Handled)":
    st.subheader("🧹 LEFT MERGE WITH NaN HANDLING")
    st.dataframe(df_left_merge_filled, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown(
    "---\n"
    "**Built by Atharva Pawar | Data Science Portfolio Project**",
    unsafe_allow_html=True
)
