import streamlit as st
from supabase import create_client, Client

# --- CONNECTION ---
# This version is simplified to avoid hidden errors


def get_supabase():
    try:
        return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except:
        return None


supabase = get_supabase()

# --- PAGE STYLE ---
st.set_page_config(page_title="Innocent Okiror | AI Specialist", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Innocent Okiror")
    st.info("🎓 AI Student @ Seeta University")
    st.write("📧 okirorinnocent49@gmail.com")
    st.divider()
    st.write("Alumnus: Teso College Aloet")

# --- MAIN INTERFACE ---
st.title("Artificial Intelligence Specialist 🚀")
st.markdown("### Portfolio & Professional Hub")
st.divider()

# Outstanding Feature: Quick Stats
c1, c2, c3 = st.columns(3)
c1.metric("Python", "90%", "Expert")
c2.metric("AI Research", "55%", "Growing")
c3.metric("Web Apps", "80%", "Active")

tab1, tab2 = st.tabs(["📖 My Journey", "✍️ Guestbook"])

with tab1:
    st.subheader("Education & Background")
    st.write("Born in 2004. Educated at Mukongoro Rock P/S and Teso College Aloet.")
    st.write(
        "Currently pursuing a degree in Artificial Intelligence at Seeta University.")

with tab2:
    st.subheader("Community Guestbook")

    # Check if we have a connection
    if not supabase:
        st.error("Connection keys are missing in Streamlit Secrets!")
    else:
        with st.form("guestbook_form", clear_on_submit=True):
            name = st.text_input("Name")
            msg = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")

            if submitted and name and msg:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name, "message": msg}).execute()
                    st.success("Sent! Refreshing...")
                    st.balloons()
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

        # Display last 5 messages
        st.divider()
        try:
            res = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()
            for row in res.data:
                with st.chat_message("user"):
                    st.write(f"**{row['name']}**: {row['message']}")
        except:
            st.info("No messages yet.")
