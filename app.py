import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- 1. SUPABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        # Check if secrets exist before trying to connect
        if "SUPABASE_URL" not in st.secrets:
            st.error("Missing SUPABASE_URL in secrets!")
            return None

        url = st.secrets["https://oggnhlnsfgfcfgppuvuh.supabase.co"]
        key = st.secrets["sb_publishable_u0f65Ghe6cQjFubMF0Q1wQ_--Q9FJM8"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return None


supabase = init_connection()

# --- 2. PAGE SETTINGS ---
st.set_page_config(page_title="Okiror Innocent | Portfolio",
                   page_icon="🎓", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    # Using your uploaded profile-style photo
    st.image("PXL_20260116_070724604.MP~2 (1).jpg", caption="Okiror Innocent")
    st.title("Contact Me")
    st.write("📧: innocent@example.com")
    st.write("📍: Uganda")
    st.divider()
    st.info("AI Student @ Seeta University")

# --- 4. MAIN CONTENT ---
st.title("Okiror Innocent")
st.subheader("Aspiring AI Specialist | TCA Alumnus")

tab1, tab2, tab3 = st.tabs(["🏠 My Story", "📊 AI Journey", "📝 Guestbook"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Education & Background")
        st.write("""
        I was born on **January 27, 2004**. My education started at **Mukongoro Rock Primary School**. 
        I then attended **Teso College Aloet (TCA)** from Senior 1 to Senior 6. 
        TCA built my character and academic strength.
        """)
        st.image("WhatsApp Image 2026-03-04 at 1.41.52 PM (3).jpeg",
                 caption="Memories of the Journey")

    with col2:
        st.header("Current Focus")
        st.write(
            "I am currently enrolled at **Seeta University** for an Artificial Intelligence Certificate.")
        st.image("PXL_20260105_100654655.MP~4.jpg",
                 caption="Learning at Seeta")

with tab2:
    st.header("Technical Progress")
    st.write("Current progress in my AI Certificate program:")
    st.write("Python")
    st.progress(70)
    st.write("Machine Learning")
    st.progress(45)

    # Displaying your study-focused photos
    c1, c2 = st.columns(2)
    with c1:
        st.image("tt (2).jpg", caption="Coding Session")
    with c2:
        st.image("PXL_20260125_134004809~5.jpg", caption="Deep Focus")

with tab3:
    st.header("Community Guestbook")
    with st.form("guestbook_form", clear_on_submit=True):
        u_name = st.text_input("Name")
        u_msg = st.text_area("Message")
        btn = st.form_submit_button("Send to Innocent")

        if btn and u_name and u_msg:
            if supabase:
                try:
                    supabase.table("guestbook").insert(
                        {"name": u_name, "message": u_msg}).execute()
                    st.success("Message saved! Refresh to see it below.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Supabase not connected. Check your Secrets.")

    st.divider()
    st.subheader("Recent Messages")
    if supabase:
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                st.write(f"**{r['name']}**: {r['message']}")
        except:
            st.write("No messages yet. Be the first!")

st.divider()
st.caption("© 2026 Okiror Innocent")
