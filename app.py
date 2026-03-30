import streamlit as st
from supabase import create_client, Client
import pandas as pd

# --- 1. CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Innocent | AI Specialist",
                   page_icon="🤖", layout="wide")

# --- 3. COOL BACKGROUND & GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    
    /* Glassmorphism Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Style for Headers */
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px 10px 0px 0px;
        color: white;
        padding: 0px 20px;
    }
    </style>
    """, unsafe_view_as_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("# 👤 Profile")
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.info("Upload 'profile.jpg' to GitHub")

    st.markdown("### **Innocent Okiror**")
    st.caption("AI & Machine Learning Student")
    st.write("---")
    st.write("📧 okirorinnocent49@gmail.com")
    st.write("📍 Kampala, Uganda")

# --- 5. HERO SECTION ---
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.title("Innocent Okiror")
    st.subheader("Building Intelligent Solutions for Tomorrow")
    st.write("Specializing in Deep Learning and Full-Stack AI Deployment. Alumnus of Teso College Aloet.")

with col_h2:
    # Outstanding visual: Animated Skill Metrics
    st.metric(label="Python Mastery", value="92%", delta="Top 10%")

# --- 6. INTERACTIVE DASHBOARD ---
st.write("## Technical Landscape")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Cloud DB", "Supabase", "Active")
m2.metric("Frontend", "Streamlit", "Expert")
m3.metric("Backend", "Python", "90%")
m4.metric("University", "Seeta Uni", "Year 2")

st.write("---")

tab1, tab2, tab3 = st.tabs(["🚀 Projects", "📊 Performance", "📝 Guestbook"])

with tab1:
    st.header("Innovation Gallery")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown("### 🧬 AI Portfolio Engine")
            st.write(
                "A high-performance portfolio with glassmorphism UI and Supabase integration.")
            st.code("Python | CSS | SQL", language="python")
    with c2:
        with st.container(border=True):
            st.markdown("### 📈 Data Analytics Bot")
            st.write("Analyzing local education data using NumPy and Pandas.")
            st.code("Pandas | Matplotlib", language="python")

with tab2:
    st.header("Growth Metrics")
    chart_data = pd.DataFrame({
        "Skills": ["Coding", "Mathematics", "Logic", "Design", "Research"],
        "Level": [90, 85, 80, 70, 65]
    })
    st.bar_chart(chart_data, x="Skills", y="Level", color="#00d2ff")

with tab3:
    st.header("Connect with the Community")
    if not supabase:
        st.error("🔑 Connection keys missing! Go to Streamlit Settings > Secrets.")
    else:
        # Styled Form
        with st.form("guestbook", clear_on_submit=True):
            st.write("Leave your mark on my journey:")
            name = st.text_input("Full Name")
            msg = st.text_area("Your Message")
            btn = st.form_submit_button("Blast Off 🚀")

            if btn and name and msg:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Message received by the AI!")
                    st.balloons()
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

        # Display message wall
        st.write("---")
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(4).execute()
            for r in res.data:
                with st.chat_message("assistant"):
                    st.write(f"**{r['name']}**")
                    st.write(r['message'])
        except:
            st.write("The guestbook is waiting for its first entry.")

# --- 7. FOOTER ---
st.markdown("---")
st.caption("© 2026 Okiror Innocent | Built with Python & Pure Grit")
