import streamlit as st
from supabase import create_client, Client

# --- 1. CONNECTION LOGIC (With Error Handling) ---


@st.cache_resource
def init_connection():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Okiror Innocent | AI Specialist",
                   page_icon="🤖", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("profile.jpg", use_container_width=True)
    except:
        st.title("👤")
    st.header("Innocent Okiror")
    st.info("📍 Kampala, Uganda")
    st.write("---")
    st.caption("AI Student @ Seeta University")
    st.write("📧 okirorinnocent49@gmail.com")

# --- 4. HERO SECTION ---
st.title("Artificial Intelligence Specialist 🚀")
st.markdown("#### Transforming the future through Data & Machine Learning")
st.divider()

# --- 5. THE "WOW" METRICS ---
# These make your site look like a high-end dashboard
col1, col2, col3, col4 = st.columns(4)
col1.metric("Python Skills", "80%", "+5%")
col2.metric("Streamlit", "95%", "Expert")
col3.metric("SQL/DB", "70%", "Active")
col4.metric("AI Research", "50%", "Growing")

# --- 6. CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["📖 My Story", "💻 Projects", "💬 Guestbook"])

with tab1:
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Educational Journey")
        st.write("""
        From **Teso College Aloet** to **Seeta University**, my focus has been on 
        bridging the gap between technology and local community needs. 
        I specialize in building intelligent systems that simplify complex data.
        """)
    with c2:
        try:
            st.image("school.jpg", use_container_width=True)
        except:
            st.info("Add school.jpg to GitHub")

with tab2:
    st.subheader("Featured Portfolio")
    # Using 'border=True' creates a modern card look
    with st.container(border=True):
        st.markdown("### 🌐 AI-Powered Portfolio")
        st.write(
            "A full-stack web application hosted on Streamlit Cloud with a Supabase backend.")
        st.button("View Source Code", key="p1")

with tab3:
    st.subheader("Community Messages")

    # Check if keys are working before showing the form
    if supabase is None:
        st.warning(
            "🔗 Please configure your Supabase Keys in Streamlit Secrets to enable the Guestbook.")
    else:
        with st.form("guestbook_form", clear_on_submit=True):
            name = st.text_input("Your Name")
            message = st.text_area("Your Message")
            submit = st.form_submit_button("Post Message")

            if submit and name and message:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name, "message": message}).execute()
                    st.success("Success! Your message is saved.")
                    st.balloons()
                except Exception as e:
                    st.error(
                        "Connection Error: Please check your API Keys in Secrets.")

        st.divider()
        # Display messages in a clean way
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for entry in res.data:
                with st.chat_message("user"):
                    st.write(f"**{entry['name']}**")
                    st.write(entry['message'])
        except:
            st.write("No messages yet. Be the first!")

# --- 7. FOOTER ---
st.divider()
st.center = st.caption("© 2026 | Okiror Innocent | Built with ❤️ and Python")
