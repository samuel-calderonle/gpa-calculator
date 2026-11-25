import streamlit as st
from streamlit_local_storage import LocalStorage
from gpa_calculator import calculate_gpa, weight_boost

# --- PAGE SETUP ---
st.set_page_config(page_title="GPA Tracker", page_icon="🎓")
st.title("🌴 High School GPA Calculator")

localS = LocalStorage()

# Load saved classes from this browser's localStorage
saved_courses = localS.getItem("gpa_courses")
if "courses" not in st.session_state:
    st.session_state.courses = saved_courses if isinstance(saved_courses, list) else []
elif not st.session_state.courses and isinstance(saved_courses, list) and saved_courses:
    st.session_state.courses = saved_courses

# --- ADD A CLASS ---
st.subheader("Add a Class")
with st.form("add_class_form", clear_on_submit=True):
    name = st.text_input("Class Name", placeholder="e.g., ENC 1101 (Dual Enrollment)")

    grade = st.select_slider(
        "Grade",
        options=["F", "D", "C", "B", "A"],
        value="A"
    )

    c1, c2 = st.columns(2)
    level = c1.selectbox("Level", options=list(weight_boost.keys()))
    credits = c2.number_input(
        "Credits",
        min_value=0.5,
        max_value=20.0,
        value=1.0,
        step=0.5
    )

    submitted = st.form_submit_button("Add Class", use_container_width=True)

    if submitted:
        if not name.strip():
            st.warning("Please enter a class name.")
        else:
            st.session_state.courses.append({
                "name": name.strip(),
                "grade": grade,
                "level": level,
                "credits": float(credits)
            })
            localS.setItem("gpa_courses", st.session_state.courses)

# --- LIVE GPA DISPLAY (Placed after form so it always shows the latest update) ---
unweighted, weighted = calculate_gpa(st.session_state.courses)

st.divider()
col1, col2 = st.columns(2)
col1.metric("Unweighted GPA", f"{unweighted:.3f}")
col2.metric("Weighted GPA", f"{weighted:.3f}")
st.divider()

# --- CLASS LIST ---
if st.session_state.courses:
    st.subheader("Your Classes")
    for idx, course in enumerate(st.session_state.courses):
        row1, row2, row3, row4, row5 = st.columns([3, 1, 2, 1.5, 1])
        row1.write(f"**{course['name']}**")
        row2.write(f"`{course['grade']}`")
        row3.write(course["level"])
        row4.write(f"{course['credits']} cr")

        if row5.button("✕", key=f"del_{idx}", help="Remove class"):
            st.session_state.courses.pop(idx)
            localS.setItem("gpa_courses", st.session_state.courses)
            st.rerun()
else:
    st.info("No classes added yet. Add your first class above!")
