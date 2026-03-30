import streamlit as st
from supabase import create_client, Client

# --- 1. CONNECTION LOGIC ---


@st.cache_resource
def init_connection():
    try:
        # These must match the names in your Streamlit Secrets exactly
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(
            "Missing Secrets: Please check SUPABASE_URL and SUPABASE_KEY in Streamlit settings.")
        return None


supabase = init_connection()

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Okiror Innocent | Portfolio",
    page_icon="🎓",
    layout="wide"
)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    try:
        # use_container_width ensures it fits the sidebar perfectly
        st.image("profile.jpg", caption="Okiror Innocent",
                 use_container_width=True)
    except:
        st.info("👤 (Upload 'profile.jpg' to your GitHub repository)")

    st.title("Contact Details")
    st.write("📧: okirorinnocent49@gmail.com")
    st.write("📍: Kampala, Uganda")
    st.divider()
    st.info("AI Student @ Seeta University")
    st.write("Alumnus: Teso College Aloet")

# --- 4. HEADER ---
st.title("Innocent Okiror")
st.markdown("### Aspiring AI Specialist & Data Scientist")
st.write("---")

# --- 5. MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 My Story", "🚀 AI Projects", "📊 Skills", "📝 Guestbook"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Education & Journey")
        st.write("""
        Born in 2004, my academic path started at **Mukongoro Rock P/S**, followed by 
        high school at **Teso College Aloet (TCA)**. 
        
        Currently, I am diving deep into the world of **Artificial Intelligence at Seeta University**. 
        My goal is to use machine learning to build solutions that impact my community.
        """)
    with col2:
        try:
            st.image("school.jpg", caption="Educational Journey",
                     use_container_width=True)
        except:
            st.warning("School image not found on GitHub.")

with tab2:
    st.header("Projects & Research")

    # Using 'expander' to make it look professional
    with st.expander("🌐 Streamlit-Supabase Portfolio", expanded=True):
        st.write(
            "Developed a full-stack portfolio app with a real-time database connection.")
        st.code("Tech: Python, Streamlit, Supabase SQL")

    with st.expander("📊 Data Analysis Project"):
        st.write("Analyzing local trends using Python libraries.")
        st.code("Tech: Pandas, NumPy")

with tab3:
    st.header("Technical Mastery")

    # Progress bars for visual impact
    st.write("Python Programming")
    st.progress(75)

    st.write("Web Development (Streamlit)")
    st.progress(85)

    st.write("Machine Learning Concepts")
    st.progress(45)

    st.write("SQL & Database Management")
    st.progress(60)

with tab4:
    st.header("Community Guestbook")
    st.write("Leave a message or some feedback below!")

    with st.form("guestbook_form", clear_on_submit=True):
        u_name = st.text_input("Your Name")
        u_msg = st.text_area("Your Message")
        btn = st.form_submit_button("Submit Message")

        if btn and u_name and u_msg:
            if supabase:
                try:
                    supabase.table("guestbook").insert(
                        {"name": u_name, "message": u_msg}).execute()
                    st.success("Message sent successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error saving message: {e}")

    st.divider()
    st.subheader("Recent Messages")
    if supabase:
        try:
            # Fetches last 5 messages
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            if res.data:
                for r in res.data:
                    st.markdown(f"**{r['name']}**: {r['message']}")
                    st.caption(
                        f"Sent on: {r.get('created_at', 'Recently')[:10]}")
            else:
                st.write("No messages yet. Be the first to say hi!")
        except Exception as e:
            st.write("Unable to load messages.")

# --- 6. FOOTER ---
st.divider()
st.caption("© 2026 Okiror Innocent | Built with Python & Supabase")
