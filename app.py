import streamlit as st
import pandas as pd
from database import setup_database, add_student, get_students
from services import calculate_grade, calculate_statistics

# Bazanı avtomatik işə salırıq
setup_database()

st.title("🎓 Student Performance Dashboard")

st.sidebar.header("Add New Student")
with st.sidebar.form("student_form"):
    student_name = st.text_input("Student Name")
    student_score = st.number_input("Score", min_value=0, max_value=100, step=1)
    submit_button = st.form_submit_button("Add Student")
    
    if submit_button:
        if student_name.strip() == "":
            st.sidebar.error("Adı boş buraxmaq olmaz!")
        else:
            grade = calculate_grade(student_score)
            add_student(student_name, student_score, grade)
            st.sidebar.success("Tələbə uğurla əlavə olundu!")
            st.rerun()

search_query = st.text_input("🔍 Search Student by Name", "")
students_data = get_students(search_query)

stats = calculate_statistics(students_data)
st.subheader("📊 Performance Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", stats["total_students"])
col2.metric("Average Score", stats["average_score"])
col3.metric("Highest Score", stats["highest_score"])
col4.metric("Lowest Score", stats["lowest_score"])

st.markdown("---")

st.subheader("📋 Student List")
if students_data:
    df = pd.DataFrame(students_data)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Heç bir tələbə tapılmadı.")
