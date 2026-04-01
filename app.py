import streamlit as st
from supabase import create_client, Client
import pandas as pd

# --- 1. DATABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        url = st.secrets["SUPABASE_URL"].strip()
        key = st.secrets["SUPABASE_KEY"].strip()
        return create_client(url, key)
    except:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Okiror Innocent | Portfolio",
                   page_icon="🎓", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.title("👤")
    st.header("Innocent Okiror")
    st.write("---")
    st.markdown("### 📞 Contact")
    st.write("okirorinnocent49@gmail.com")
    st.write("📍 Kampala, Uganda")
    st.divider()
    st.info("AI Student @ Seeta University")

# --- 4. MAIN HEADER ---
st.title("Innocent Okiror")
st.subheader("Professional Office Specialist | Aspiring AI Researcher")
st.write("Welcome to my digital space. I combine administrative excellence with a passion for future technologies.")

# --- 5. SKILLS DASHBOARD ---
st.write("### 🛠️ Core Competencies")
c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("#### ☁️ Google Workspace")
        st.caption("Docs, Sheets, Slides, Forms")
        st.progress(95)

with c2:
    with st.container(border=True):
        st.markdown("#### 💻 Microsoft Office")
        st.caption("Word, Excel, PowerPoint")
        st.progress(90)

with c3:
    with st.container(border=True):
        st.markdown("#### 🗄️ Data & AI")
        st.caption("Database Mgmt & AI Certificate (In Progress)")
        st.progress(60)

# --- 6. CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["🏠 My Story", "🚀 AI Journey", "📝 Guestbook"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("About Me")
        st.write("""
        I am a dedicated professional with a strong background in office productivity and data management. 
        My journey started at **Teso College Aloet**, where I developed a disciplined approach to learning. 
        
        Currently, I am expanding my horizons at **Seeta University**, pursuing a certificate in **Artificial Intelligence**. 
        My goal is to integrate AI tools into everyday business workflows to improve efficiency.
        """)
    with col2:
        try:
            st.image("school.jpg", caption="Educational Roots",
                     use_container_width=True)
        except:
            st.write("(School Image)")

with tab2:
    st.header("AI Training & Progress")
    st.info("I am currently undergoing certification in AI to understand how machine learning can solve local problems.")

    skills_data = pd.DataFrame({
        "Skillset": ["Excel/Data", "PowerPoint", "MS Word", "Google Suite", "AI Fundamentals"],
        "Proficiency": [85, 90, 95, 95, 40]
    })
    st.bar_chart(skills_data, x="Skillset", y="Proficiency", color="#1E3A8A")

with tab3:
    st.header("Community Wall")
    # I added a small note here so users know their message was sent successfully
    st.write(
        "Leave a private message for me below. Your message is sent directly to my database.")

    if not supabase:
        st.error("Connection keys not found in Secrets.")
    else:
        with st.form("guest_form", clear_on_submit=True):
            name = st.text_input("Name")
            msg = st.text_area("Leave a message")
            submit = st.form_submit_button("Post to Wall")

            if submit and name and msg:
                try:
                    # ONLY INSERTING DATA: The "Select" code is gone.
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Message saved! Thank you for your feedback.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")

# --- 7. FOOTER ---
st.divider()
st.caption("© 2026 Innocent Okiror | Built with Streamlit & Supabase")
