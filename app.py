import streamlit as st
from supabase import create_client, Client

# --- 1. CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Innocent Okiror | AI Specialist",
                   page_icon="🚀", layout="wide")

# --- 3. SIDEBAR (The Professional Touch) ---
with st.sidebar:
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.title("👤")

    st.markdown("## Okiror Innocent")
    st.info("📍 Kampala, Uganda")
    st.write("---")
    st.markdown("### 🎓 Education")
    st.caption("AI Student @ Seeta University")
    st.caption("Alumnus @ Teso College Aloet")
    st.write("---")
    st.markdown("### 📧 Contact")
    st.write("okirorinnocent49@gmail.com")

# --- 4. HERO SECTION (The Big Impression) ---
col_logo, col_text = st.columns([1, 4])
with col_text:
    st.title("Artificial Intelligence Specialist")
    st.write("Building the future of African Tech through data and code.")
    st.markdown("---")

# --- 5. DASHBOARD METRICS (Visual "Wow" factor) ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Python", "75%", "Learning")
m2.metric("Streamlit", "90%", "Expert")
m3.metric("SQL/Supabase", "65%", "Active")
m4.metric("AI/ML", "40%", "Growing")

# --- 6. INTERACTIVE TABS ---
tab1, tab2, tab3 = st.tabs(["⭐ My Journey", "🛠️ Portfolio", "✉️ Guestbook"])

with tab1:
    st.subheader("The Story of a Tech Pioneer")
    col_a, col_b = st.columns([3, 2])
    with col_a:
        st.write("""
        From the classrooms of **Mukongoro Rock P/S** to the science labs of **Teso College Aloet**, 
        my journey has always been driven by curiosity. 
        
        Now, at **Seeta University**, I am specializing in Artificial Intelligence. 
        I believe that AI isn't just about robots; it's about solving real-world 
        problems in agriculture, education, and finance.
        """)
    with col_b:
        try:
            st.image("school.jpg", caption="Where it all started",
                     use_container_width=True)
        except:
            st.info("Add school.jpg to GitHub to see memories here.")

with tab2:
    st.subheader("Featured Work")
    # Using columns to create "Cards"
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown("### 🌐 Personal Cloud Portfolio")
            st.write(
                "A full-stack application using Supabase for real-time guestbook management.")
            st.button("View on GitHub", key="btn1")

    with c2:
        with st.container(border=True):
            st.markdown("### 📊 Data Analysis Hub")
            st.write("Research projects focused on local data trends in Uganda.")
            st.button("View Project", key="btn2")

with tab3:
    st.subheader("Leave a Legacy")
    # Form with a more modern feel
    with st.form("guestbook", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Who are you?")
        msg = st.text_area(
            "Message", placeholder="Write something inspiring...")
        submit = st.form_submit_button("Post to Guestbook")

        if submit and name and msg:
            if supabase:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Message live on the cloud!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")

    st.write("---")
    st.markdown("### 💬 Recent Shoutouts")
    if supabase:
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                # Using a chat-style bubble for messages
                with st.chat_message("user"):
                    st.write(f"**{r['name']}**")
                    st.write(r['message'])
        except:
            st.write("No messages yet. Be the first!")

# --- 7. FOOTER ---
st.write("---")
st.caption("Designed & Developed by Okiror Innocent | © 2026")
