import streamlit as st
from supabase import create_client, Client

# --- 1. SUPABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
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
    # IMPORTANT: Ensure this file is named 'profile.jpg' on GitHub
    try:
        st.image("profile.jpg", caption="Okiror Innocent")
    except:
        st.warning("Profile photo not found on GitHub. Rename it to profile.jpg")

    st.title("Contact Me")
    st.write("📧: okirorinnocent49@gmail.com")
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
        st.write("Born: 2004 | Schools: Mukongoro Rock P/S & Teso College Aloet.")
        try:
            st.image("school.jpg", caption="Memories of the Journey")
        except:
            st.write("(School image not found)")

with tab2:
    st.header("Technical Progress")
    st.write("Python Progress")
    st.progress(75)
    try:
        st.image("study.png", caption="Learning at Seeta University", width=500)
    except:
        st.write("(Study image not found)")

with tab3:
    st.header("Community Guestbook")
    with st.form("guestbook_form", clear_on_submit=True):
        u_name = st.text_input("Name")
        u_msg = st.text_area("Message")
        btn = st.form_submit_button("Send")

        if btn and u_name and u_msg:
            if supabase:
                try:
                    supabase.table("guestbook").insert(
                        {"name": u_name, "message": u_msg}).execute()
                    st.success("Message saved!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")

    st.divider()
    if supabase:
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for r in res.data:
                st.write(f"**{r['name']}**: {r['message']}")
        except:
            st.write("No messages yet!")
