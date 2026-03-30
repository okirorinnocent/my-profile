import streamlit as st
from supabase import create_client, Client

# --- 1. CONNECTION LOGIC ---


@st.cache_resource
def init_connection():
    try:
        # Pulling from Streamlit Cloud Secrets
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Okiror Innocent | Portfolio",
                   page_icon="🎓", layout="wide")

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("profile.jpg", caption="Okiror Innocent",
                 use_container_width=True)
    except:
        st.info("👤 Upload 'profile.jpg' to GitHub")

    st.title("Contact")
    st.write("📧: okirorinnocent49@gmail.com")
    st.divider()
    st.info("AI Student @ Seeta University")

# --- 4. MAIN CONTENT ---
st.title("Innocent Okiror")
st.subheader("Aspiring AI Specialist")

tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 My Story", "🚀 Projects", "📊 Skills", "📝 Guestbook"])

with tab1:
    st.header("Education & Journey")
    st.write("Born: 2004 | Schools: Mukongoro Rock P/S & Teso College Aloet.")
    st.write("Currently studying AI at Seeta University.")

with tab2:
    st.header("Projects")
    with st.container(border=True):
        st.write("**Full-Stack Portfolio**")
        st.write("Built using Python, Streamlit, and Supabase.")

with tab3:
    st.header("Skills")
    st.write("Python")
    st.progress(75)
    st.write("SQL")
    st.progress(60)

with tab4:
    st.header("Guestbook")

    # Check if connection exists before showing form
    if supabase is None:
        st.error("⚠️ Database connection not configured in Streamlit Secrets.")
    else:
        with st.form("guestbook_form", clear_on_submit=True):
            name = st.text_input("Name")
            msg = st.text_area("Message")
            submit = st.form_submit_button("Send")

            if submit and name and msg:
                try:
                    # Attempt to insert into the 'guestbook' table
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Message saved!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")

        st.divider()
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                st.write(f"**{r['name']}**: {r['message']}")
        except:
            st.write("No messages yet!")

st.divider()
st.caption("© 2026 Okiror Innocent")
