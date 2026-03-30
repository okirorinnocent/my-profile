import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- 1. SUPABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        # These keys MUST be in your Streamlit Cloud Secrets box
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return None


supabase = init_connection()

# --- 2. PAGE SETTINGS ---
st.set_page_config(page_title="Okiror Innocent | AI Portfolio",
                   page_icon="🚀", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    # Using one of your uploaded photos as a profile pic
    st.image("PXL_20260116_070724604.MP~2 (1).jpg", caption="Okiror Innocent")
    st.title("Contact Info")
    st.write("📧: innocent@example.com")
    st.write("📍: Uganda")
    st.divider()
    st.info("Student at Seeta University - AI Certificate (2026)")

# --- 4. MAIN CONTENT ---
st.title("Okiror Innocent: From TCA to AI")
st.write("Welcome to my professional profile. I am an aspiring AI specialist with a background from Teso College Aloet.")

tab1, tab2, tab3 = st.tabs(
    ["🏠 My Story", "📊 Skills & Progress", "📝 Guestbook"])

# --- TAB 1: STORY ---
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Education Background")
        st.write("""
        I was born on **January 27, 2004**. My journey started at **Mukongoro Rock Primary School**. 
        I later spent 6 years at **Teso College Aloet (TCA)** for both my O-Level and A-Level. 
        TCA taught me discipline and the 'Acre' spirit!
        """)
        # Displaying a group/school photo
        st.image("WhatsApp Image 2026-03-04 at 1.41.52 PM (3).jpeg",
                 caption="Memories from the journey", use_container_width=True)

    with col2:
        st.header("Life at Seeta")
        st.write(
            "Currently pursuing an AI Certificate at Seeta University (Feb - April 2026).")
        st.image("PXL_20260105_100654655.MP~4.jpg", use_container_width=True)

    st.divider()
    st.subheader("Gallery")
    # Displaying more of your uploaded photos in a grid
    g1, g2, g3 = st.columns(3)
    with g1:
        st.image("PXL_20260125_134004809~5.jpg", caption="Focus")
    with g2:
        st.image("PXL_20260116_070956790.MP.jpg", caption="The Journey")
    with g3:
        st.image("IMG-20250501-WA0021 (1).jpg", caption="Milestones")

# --- TAB 2: SKILLS ---
with tab_journey if 'tab_journey' in locals() else tab2:
    st.header("AI Technical Path")
    st.write("Here is how I am progressing in my AI studies:")

    st.write("Python Programming")
    st.progress(70)

    st.write("Data Analysis")
    st.progress(50)

    st.write("Streamlit Web Apps")
    st.progress(85)

    st.image("tt (2).jpg", caption="Studying hard at Seeta University", width=400)

# --- TAB 3: GUESTBOOK (SUPABASE) ---
with tab3:
    st.header("Leave me a Message")
    st.write("This data is saved live to my Supabase database!")

    with st.form("message_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            if name and message and supabase:
                data = {"name": name, "message": message}
                supabase.table("guestbook").insert(data).execute()
                st.success(f"Thank you {name}, message sent!")
                st.balloons()
            else:
                st.error("Please fill all fields or check connection.")

    st.divider()
    st.subheader("What others are saying")
    if supabase:
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for row in res.data:
                st.info(f"**{row['name']}**: {row['message']}")
        except:
            st.write("No messages yet!")

st.divider()
st.caption("Built with ❤️ by Okiror Innocent | 2026")
