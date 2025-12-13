import pandas as pd

# =========================
# TABLE 1: STUDENT MASTER
# (Primary Table)
# =========================
def load_student_master():
    """
    SQL Equivalent:
    SELECT Student_ID, Student_Name, Age, Gender, Institute FROM student_master;
    """
    return pd.DataFrame([
        {"Student_ID": 301, "Student_Name": "Atharva Pawar", "Age": 21, "Gender": "Male", "Institute": "FinX Institute"},
        {"Student_ID": 302, "Student_Name": "Riya Sharma", "Age": 22, "Gender": "Female", "Institute": "IIT Bombay"},
        {"Student_ID": 303, "Student_Name": "Kunal Mehta", "Age": 23, "Gender": "Male", "Institute": "NMIMS"},
        {"Student_ID": 304, "Student_Name": "Snehal Patil", "Age": 21, "Gender": "Female", "Institute": "SP Jain"},
        {"Student_ID": 305, "Student_Name": "Rohit Jain", "Age": 24, "Gender": "Male", "Institute": "VIT"},
        {"Student_ID": 306, "Student_Name": "Neha Verma", "Age": 22, "Gender": "Female", "Institute": "BITS Pilani"},
        {"Student_ID": 307, "Student_Name": "Aman Khan", "Age": 23, "Gender": "Male", "Institute": "Manipal"},
        {"Student_ID": 308, "Student_Name": "Pooja Nair", "Age": 21, "Gender": "Female", "Institute": "Mumbai University"},
        {"Student_ID": 309, "Student_Name": "Sahil Desai", "Age": 24, "Gender": "Male", "Institute": "Symbiosis"},
        {"Student_ID": 310, "Student_Name": "Isha Kulkarni", "Age": 22, "Gender": "Female", "Institute": "COEP"},
        # EXTRA ROW → Missing in performance table (NaN demo)
        {"Student_ID": 311, "Student_Name": "Varun Kulkarni", "Age": 23, "Gender": "Male", "Institute": "NIT Trichy"}
    ])


# =========================
# TABLE 2: STUDENT PERFORMANCE
# (One-to-Many Relationship)
# =========================
def load_student_performance():
    """
    SQL Equivalent:
    SELECT Student_ID, Course, Score FROM student_performance;
    """
    return pd.DataFrame([
        {"Student_ID": 301, "Course": "Data Science", "Score": 88},
        {"Student_ID": 301, "Course": "AI & ML", "Score": 85},      # Same student, second course
        {"Student_ID": 302, "Course": "AI & ML", "Score": 92},
        {"Student_ID": 303, "Course": "Cyber Security", "Score": 81},
        {"Student_ID": 304, "Course": "Data Analytics", "Score": 85},
        {"Student_ID": 305, "Course": "Cloud Computing", "Score": 78},
        {"Student_ID": 306, "Course": "AI & ML", "Score": 90},
        {"Student_ID": 307, "Course": "Data Science", "Score": 83},
        {"Student_ID": 308, "Course": "Statistics", "Score": 87},
        {"Student_ID": 309, "Course": "Business Analytics", "Score": 80},
        {"Student_ID": 310, "Course": "AI & ML", "Score": 91},
        # EXTRA ROW → Missing in master table (NaN demo)
        {"Student_ID": 312, "Course": "Data Science", "Score": 76}
    ])
