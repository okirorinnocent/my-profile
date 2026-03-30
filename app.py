import streamlit as st
from supabase import create_client, Client
import pandas as pd

# --- 1. SAFE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        # Using .strip() to clean up any invisible spaces in your secrets
        url = st.secrets["SUPABASE_URL"].strip()
        key = st.secrets["SUPABASE_KEY"].strip()
        return create_client(url, key)
    except Exception as e:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Okiror | AI Portfolio",
                   page_icon="🤖", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.title("👤")
    st.header("Innocent Okiror")
    st.markdown("### **AI Specialist**")
    st.divider()
    st.write("📧 okirorinnocent49@gmail.com")
    st.write("📍 Kampala, Uganda")
    st.write("🎓 Seeta University")

# --- 4. HERO SECTION ---
# Using columns to create a clean, modern header
col_title, col_stats = st.columns([2, 1])

with col_title:
    st.title("Innocent Okiror")
    st.markdown("#### *Developing the future of AI in East Africa*")
    st.write(
        "Alumnus of Teso College Aloet (TCA). Passionate about Data Science and Machine Learning.")

with col_stats:
    # Outstanding visual metrics
    st.metric(label="Python Skills", value="95%", delta="Top Tier")

st.divider()

# --- 5. DASHBOARD TILES ---
# This replaces the old "Worst" design with a modern grid
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.subheader("🐍 Core")
    st.write("Python Expert")
with m2:
    st.subheader("🌐 Web")
    st.write("Streamlit Pro")
with m3:
    st.subheader("🗄️ Cloud")
    st.write("Supabase DB")
with m4:
    st.subheader("🧠 Research")
    st.write("AI/ML Focus")

# --- 6. INTERACTIVE TABS ---
tab1, tab2, tab3 = st.tabs(
    ["🚀 Portfolio Gallery", "📊 Skills Matrix", "💬 Community Wall"])

with tab1:
    st.header("Featured Projects")
    p1, p2 = st.columns(2)
    with p1:
        with st.container(border=True):
            st.markdown("### ⚡ AI-Powered Portfolio")
            st.write(
                "A high-speed web application integrated with cloud databases.")
            st.caption("Status: Live & Optimized")
    with p2:
        with st.container(border=True):
            st.markdown("### 📈 Data Insights Engine")
            st.write("Researching educational trends using advanced visualization.")
            st.caption("Status: In Development")

with tab2:
    st.header("Proficiency Breakdown")
    # A bar chart makes the site look much more professional
    skills = pd.DataFrame({
        "Skill": ["Coding", "Mathematics", "UI Design", "Data Analysis"],
        "Level": [90, 85, 75, 80]
    })
    st.bar_chart(skills, x="Skill", y="Level", color="#007BFF")

with tab3:
    st.header("Public Guestbook")

    if supabase is None:
        st.error("🔑 Database Connection missing! Check your Streamlit Secrets.")
    else:
        with st.form("guest_form", clear_on_submit=True):
            name = st.text_input("Name")
            msg = st.text_area("Your Message")
            btn = st.form_submit_button("Post Message 🚀")

            if btn and name and msg:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Message live on the cloud!")
                    st.balloons()
                    st.rerun()
                except Exception as e:
                    st.error(f"Database Error: {e}")

        st.divider()
        st.subheader("Recent Transmissions")
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                with st.chat_message("user"):
                    st.write(f"**{r['name']}**: {r['message']}")
        except:
            st.write("Waiting for the first message...")

# --- 7. FOOTER ---
st.divider()
st.caption("© 2026 Okiror Innocent | Built for Performance & Style")
