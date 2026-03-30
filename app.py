import streamlit as st
from supabase import create_client, Client
import requests

# --- SUPABASE CONNECTION SETUP ---


@st.cache_resource
def init_connection():
    try:
        url = st.secrets["https://oggnhlnsfgfcfgppuvuh.supabase.co"]
        key = st.secrets["sb_publishable_u0f65Ghe6cQjFubMF0Q1wQ_--Q9FJM8"]
        return create_client(url, key)
    except FileNotFoundError:
        st.warning(
            "⚠️ **Database secrets not found!** Complete Step 2 for the Guestbook to work.")
        return None
    except Exception as e:
        st.error(f"⚠️ **Supabase connection error:** {e}")
        return None


supabase = init_connection()

# --- IMAGE URL DICTIONARY (USER: REPLACE THESE!) ---
# This dictionary stores links to all your hosted photos.
# You MUST upload your 9 images online and replace these placeolder text with the real URLs.
# Without real URLs, placeholders will be shown.
image_urls = {
    # image_0.png - Your professional/coding look
    "profile": "https://via.placeholder.com/300?text=Okiror+Innocent",
    # image_1.png - Clear, well-lit photo
    "balcony": "https://via.placeholder.com/400x300?text=Balcony+Photo",
    # image_2.png - Group photo on rock
    "hike": "https://via.placeholder.com/400x300?text=Hike+with+Friends",
    # image_3.png - Group in school uniform
    "tca_group": "https://via.placeholder.com/400x300?text=Teso+College+Aloet",
    # image_4.png - Studious pose
    "study_denim": "https://via.placeholder.com/400x300?text=Study+In+Denim",
    # image_5.png - Close-up study pose
    "study_close": "https://via.placeholder.com/400x300?text=Study+Close-up",
    # image_6.png - Professional school uniform photo
    "tca_scarf": "https://via.placeholder.com/400x300?text=Teso+College+Alumnus",
    # image_7.png - Casual photo
    "yellow_jersey": "https://via.placeholder.com/400x300?text=Relaxing",
    # image_8.png - Blessings/Milestone photo
    "blessing": "https://via.placeholder.com/400x300?text=Confirmation+Day"
}

# Simple function to check if an image URL is valid and valid placeholder if not


def display_image(url_key, caption=None, width=None):
    url = image_urls[url_key]
    # In a real scenario, st.image handles placeholders if the URL is broken.
    if caption:
        st.image(url, caption=caption,
                 use_column_width=width is None, width=width)
    else:
        st.image(url, use_column_width=width is None, width=width)


# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Okiror Innocent | Portfolio",
                   page_icon="🎓", layout="wide")

# --- MAIN CONTENT ---
st.title("Welcome! I'm Okiror Innocent, from Uganda.")
st.write("Join me as I explore the exciting world of Artificial Intelligence.")

# --- CREATE TABS ---
tab_home, tab_journey, tab_guestbook = st.tabs([
    "🏠 My Story",
    "📊 My Learning Journey",
    "📝 Guestbook"
])

# --- TAB 1: MY STORY (Education & Lifestyle) ---
with tab_home:
    st.header("Who I Am")
    col1, col2 = st.columns([1, 2])
    with col1:
        # 📸 IMAGE_0.png - Your main profile image
        display_image("profile", caption="Okiror Innocent", width=250)

    with col2:
        st.write("""
            Born on **January 27, 2004**, I am a student transitioning into the tech space.
            I started with **no coding background**, and my dream is to specialize in Artificial Intelligence.
            
            Beyond academics, I enjoy a balanced life. You can often find me focused, 
            or sometimes just enjoying a nice day on a **balcony** or being active with friends.
        """)
        col_pic1, col_pic2 = st.columns(2)
        with col_pic1:
            # 📸 IMAGE_1.png - Balcony photo
            display_image("balcony", caption="Enjoying the moment")
        with col_pic2:
            # 📸 IMAGE_7.png - Yellow jersey photo
            display_image("yellow_jersey",
                          caption="Finding a moment of relaxation")

    st.divider()

    st.header("Academic Foundation & Key Milestones")

    col3, col4 = st.columns([2, 1])
    with col3:
        st.write("""
            My formal education began with a strong foundation in PLE at **Mukongoro Rock Primary School**.
            
            I then proudly joined **Teso College Aloet (TCA)** for my entire secondary education,
            from Senior 1 to Senior 6, completing both my UCE and UACE. Those years at TCA 
            helped mold me into the driven person I am today.
        """)
        st.success("**Teso College Aloet** (Alumnus)")

        col_tca1, col_tca2 = st.columns(2)
        with col_tca1:
            # 📸 IMAGE_3.png - TCA group photo
            display_image("tca_group", caption="Proud TCA students in uniform")
        with col_tca2:
            # 📸 IMAGE_6.png - TCA with scarf
            display_image("tca_scarf", caption="Ready for a successful future")

    with col4:
        st.write("""
            Looking ahead, I have been blessed with opportunities and milestone moments.
            The spiritual support from family and mentors, symbolized by my **confirmation**,
            keeps me grounded as I pursue my ambitions.
        """)
        # 📸 IMAGE_8.png - Blessing photo
        display_image("blessing", caption="Receiving blessings and guidance")

# --- TAB 2: MY LEARNING JOURNEY ---
with tab_journey:
    st.header("Seeta University: AI Studies")
    st.write(f"""
        In **2026**, my passion for data and learning led me to enroll at **Seeta University**.
        I am currently in the intense and rewarding process of earning my 
        **Certificate in Artificial Intelligence** (Feb 2026 - April 2026).
    """)

    col5, col6 = st.columns([1, 2])
    with col5:
        st.info("**Seeta University**")
        st.write("**AI Certificate Candidate**")
        # 📸 IMAGE_4.png - Study denim photo
        display_image("study_denim", caption="Focused during my AI studies")

    with col6:
        st.write(
            "This rigorous program is teaching me how to build intelligent systems.")
        # 📸 IMAGE_5.png - Study close-up photo
        display_image(
            "study_close", caption="AI Concepts: The foundation of the future.")

    st.divider()

    # Learning Progress and Exploration
    st.header("Learning Path & Exploration")

    col7, col8 = st.columns([2, 1])
    with col7:
        st.write("I believe in constant improvement and learning new technologies.")
        st.write("**Python Programming**")
        st.progress(75)  # Adjust based on your real progress
        st.write("**Data Science Principles**")
        st.progress(55)  # Adjust
        st.write("**Streamlit (Web Development)**")
        st.progress(90)  # Adjust
        st.write("**Database Integration (Supabase)**")
        st.progress(60)  # Adjust

    with col8:
        st.write("""
            I am a natural explorer and enjoy teamwork and shared adventures.
            Working with peers is crucial to success.
        """)
        # 📸 IMAGE_2.png - Hike photo
        display_image(
            "hike", caption="Connecting with others through shared experiences")


# --- TAB 3: GUESTBOOK (SUPABASE LIVE SAVING) ---
with tab_guestbook:
    st.header("Leave a Message in my Guestbook!")

    if supabase:
        with st.form("guestbook_form", clear_on_submit=True):
            st.write("Share your thoughts or a piece of advice!")
            name = st.text_input("Full Name", placeholder="Your Name")
            msg = st.text_area(
                "Your Message", placeholder="Type your message here...")
            submitted = st.form_submit_button("Send to Supabase")

            if submitted:
                if name and msg:
                    data = {"name": name, "message": msg}
                    try:
                        # Pushes name and message to your 'guestbook' table in Supabase
                        supabase.table("guestbook").insert(data).execute()
                        st.success(
                            f"Success! Thanks, {name}, for your message.")
                        st.balloons()
                    except Exception as e:
                        st.error(f"Error saving to database: {e}")
                else:
                    st.warning("Please fill in both fields.")

        # --- DISPLAY MESSAGES FROM SUPABASE ---
        st.divider()
        st.subheader("Recent Community Messages")

        try:
            # Fetches the latest 5 messages, ordered by time
            response = supabase.table("guestbook").select(
                "*").order("created_at", desc=True).limit(5).execute()

            # Displays messages only if some exist
            if response.data:
                for record in response.data:
                    st.markdown(f"**{record['name']}**: {record['message']}")
                    st.caption(f"📅 Sent: {record['created_at'][:10]}")
            else:
                st.write("No messages yet. Be the first to leave one!")

        except Exception as e:
            st.write("Could not retrieve messages at this time.")

    else:
        st.warning(
            "Guestbook functionality requires a valid Supabase connection (Check Step 2).")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Okiror Innocent | Built with Python & Streamlit")
