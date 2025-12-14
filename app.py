import streamlit as st
import pandas as pd
from data.education_data import load_student_master, load_student_performance

st.set_page_config(
    page_title="Education Data Join & Merge Demo",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
df_master = load_student_master()
df_performance = load_student_performance()

# =========================
# CREATE ALL OPERATIONS
# (DEFINE BEFORE USE)
# =========================

# MERGE OPERATIONS
df_merge_inner = pd.merge(df_master, df_performance, on="Student_ID", how="inner")
df_merge_left = pd.merge(df_master, df_performance, on="Student_ID", how="left")
df_merge_right = pd.merge(df_master, df_performance, on="Student_ID", how="right")

# JOIN (Index-based)
df_join = df_master.set_index("Student_ID").join(
    df_performance.set_index("Student_ID"),
    how="inner"
)

# CONCAT OPERATIONS
df_concat_vertical = pd.concat(
    [df_performance, df_performance],
    axis=0,
    ignore_index=True
)

df_concat_horizontal = pd.concat(
    [df_master.reset_index(drop=True),
     df_performance.reset_index(drop=True)],
    axis=1
)

# HANDLE NaN (Optional)
df_left_merge_filled = df_merge_left.fillna({
    "Course": "Not Enrolled",
    "Score": 0
})

# =========================
# STREAMLIT UI
# =========================
st.title("🎓 Education Data Join, Merge & Concat Demo")

option = st.selectbox(
    "Select Data Operation",
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

if option == "Inner Merge":
    st.subheader("INNER MERGE")
    st.dataframe(df_merge_inner, use_container_width=True)

elif option == "Left Merge":
    st.subheader("LEFT MERGE")
    st.dataframe(df_merge_left, use_container_width=True)

elif option == "Right Merge":
    st.subheader("RIGHT MERGE")
    st.dataframe(df_merge_right, use_container_width=True)

elif option == "Join":
    st.subheader("JOIN (Index Based)")
    st.dataframe(df_join, use_container_width=True)

elif option == "Concat (Vertical)":
    st.subheader("CONCAT VERTICAL (UNION ALL)")
    st.dataframe(df_concat_vertical, use_container_width=True)

elif option == "Concat (Horizontal)":
    st.subheader("CONCAT HORIZONTAL")
    st.dataframe(df_concat_horizontal, use_container_width=True)

elif option == "Left Merge (NaN Handled)":
    st.subheader("LEFT MERGE WITH NaN HANDLING")
    st.dataframe(df_left_merge_filled, use_container_width=True)
