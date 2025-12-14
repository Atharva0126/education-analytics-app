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
# LOAD RAW DATA
# =========================
df_master = load_student_master()
df_performance = load_student_performance()

# =========================
# RAW DATA VIEW (DEFAULT)
# =========================
st.subheader("📌 Raw Data Tables")

show_raw_data = st.checkbox(
    "Show / Hide Raw Data Tables",
    value=True
)

if show_raw_data:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧑 Student Master Table")
        st.dataframe(df_master, use_container_width=True)

    with col2:
        st.markdown("### 📊 Student Performance Table")
        st.dataframe(df_performance, use_container_width=True)

st.divider()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🔎 Filters")

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=df_master["Gender"].unique(),
    default=df_master["Gender"].unique()
)

selected_institute = st.sidebar.multiselect(
    "Institute",
    options=df_master["Institute"].unique(),
    default=df_master["Institute"].unique()
)

selected_course = st.sidebar.multiselect(
    "Course",
    options=df_performance["Course"].unique(),
    default=df_performance["Course"].unique()
)

score_range = st.sidebar.slider(
    "Score Range",
    min_value=int(df_performance["Score"].min()),
    max_value=int(df_performance["Score"].max()),
    value=(int(df_performance["Score"].min()), int(df_performance["Score"].max()))
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
# DATA OPERATIONS
# =========================
df_merge_inner = pd.merge(filtered_master, filtered_performance, on="Student_ID", how="inner")
df_merge_left = pd.merge(filtered_master, filtered_performance, on="Student_ID", how="left")
df_merge_right = pd.merge(filtered_master, filtered_performance, on="Student_ID", how="right")

df_join = filtered_master.set_index("Student_ID").join(
    filtered_performance.set_index("Student_ID"),
    how="inner"
)

df_concat = pd.concat(
    [filtered_performance, filtered_performance],
    axis=0,
    ignore_index=True
)





# =========================
# OPERATION SELECTOR
# =========================
st.subheader("🔄 Data Operations")

operation = st.selectbox(
    "Select Operation",
    [
        "Inner Merge",
        "Left Merge",
        "Right Merge",
        "Join",
        "Concat"
    ]
)

# =========================
# DISPLAY RESULTS
# =========================
if operation == "Inner Merge":
    st.dataframe(df_merge_inner, use_container_width=True)

elif operation == "Left Merge":
    st.dataframe(df_merge_left, use_container_width=True)

elif operation == "Right Merge":
    st.dataframe(df_merge_right, use_container_width=True)

elif operation == "Join":
    st.dataframe(df_join, use_container_width=True)

elif operation == "Concat":
    st.dataframe(df_concat, use_container_width=True)



# =========================
# FOOTER
# =========================
st.markdown(
    "---\n"
    "**Built by Atharva Pawar | Data Science Portfolio Project**",
    unsafe_allow_html=True
)
