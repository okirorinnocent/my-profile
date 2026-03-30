import streamlit as st
from supabase import create_client, Client

# --- 1. SUPABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        # Note: Using st.secrets is correct for hosting on Streamlit Cloud
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return None


# Initialize connection
supabase = init_connection()

# --- 2. PAGE SETTINGS ---
st.set_page_config(
    page_title="Okiror Innocent | AI Specialist",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 3. CUSTOM CSS (To make it look high-end) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    .stProgress > div > div > div > div { background-color: #007BFF; }
    </style>
    """, unsafe_view_as_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.info("👤 (Place 'profile.jpg' in your GitHub repo)")

    st.title("Innocent Okiror")
    st.markdown("📍 **Kampala, Uganda**")
    st.markdown("🎓 **AI Student @ Seeta University**")

    st.divider()
    st.subheader("Connect with Me")
    st.write(
        "📧: [okirorinnocent49@gmail.com](mailto:okirorinnocent49@gmail.com)")
    st.write("🔗: [LinkedIn](https://linkedin.com)")
    st.write("💻: [GitHub](https://github.com)")

    st.divider()
    if st.button("Download CV (PDF)"):
        st.toast("CV link coming soon!")

# --- 5. HEADER SECTION ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("Hi, I'm Innocent! 👋")
    st.markdown(
        "### Creating the future through **Artificial Intelligence** & **Data Science**.")
    st.write("Alumnus of Teso College Aloet (TCA) | Dedicated to solving local problems with global tech.")

# --- 6. MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 My Story", "🚀 Projects", "📊 Skills", "📝 Guestbook"])

with tab1:
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.header("Education & Journey")
        st.write("""
        Born in 2004, my journey began at **Mukongoro Rock P/S** and led me to the prestigious **Teso College Aloet**. 
        Today, I am specializing in AI at **Seeta University**, focusing on how machine learning can transform industries in East Africa.
        """)

        # Professional Timeline
        st.subheader("The Timeline")
        st.write("🗓️ **2023 - Present:** Bachelor's in AI, Seeta University")
        st.write("🗓️ **2017 - 2022:** Secondary Education @ TCA")

    with col_b:
        try:
            st.image("school.jpg", caption="TCA Memories",
                     use_container_width=True)
        except:
            st.info("Upload school.jpg to see memories here.")

with tab2:
    st.header("Featured AI Projects")
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        with st.container(border=True):
            st.subheader("Streamlit-Supabase Web App")
            st.write("A full-stack portfolio with real-time database integration.")
            st.code("Python | Streamlit | SQL", language="text")
            st.link_button("View Code", "https://github.com")

    with p_col2:
        with st.container(border=True):
            st.subheader("AI Research Project")
            st.write("Analyzing local data trends using Python and Pandas.")
            st.code("Pandas | NumPy | Matplotlib", language="text")
            st.link_button("View Report", "https://github.com")

with tab3:
    st.header("Technical Mastery")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.write("🐍 **Python Development**")
        st.progress(75)

        st.write("🗄️ **Database Management (Supabase/SQL)**")
        st.progress(60)

    with col_s2:
        st.write("🤖 **Machine Learning Basics**")
        st.progress(45)

        st.write("🌐 **Web Deployment**")
        st.progress(85)

with tab4:
    st.header("Community Guestbook")
    st.write("Leave a message for me below!")

    with st.form("guestbook_form", clear_on_submit=True):
        u_name = st.text_input("Full Name")
        u_msg = st.text_area("Your Message")
        btn = st.form_submit_button("Send to Innocent")

        if btn and u_name and u_msg:
            if supabase:
                try:
                    supabase.table("guestbook").insert(
                        {"name": u_name, "message": u_msg}).execute()
                    st.success("Your message has been saved to the cloud!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Failed to save: {e}")

    st.divider()
    st.subheader("Recent Messages")
    if supabase:
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                with st.chat_message("user"):
                    st.write(f"**{r['name']}** says:")
                    st.write(r['message'])
        except:
            st.write("Be the first to leave a message!")

# --- 7. FOOTER ---
st.divider()
st.center = st.write("© 2026 Okiror Innocent | Built with ❤️ and AI")
