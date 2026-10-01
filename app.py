from datetime import datetime

import pandas as pd
import streamlit as st
from supabase import Client, create_client

# set_page_config must be the first Streamlit call
st.set_page_config(
    page_title="Innocent Okiror | CS & AI Portfolio",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------------
# CONTENT (edit here, not in the layout code)
# ---------------------------------------------------------------
PROFILE = {
    "name": "Innocent Okiror",
    "email": "okirorinnocent49@gmail.com",
    "location": "Mbarara / Kumi, Uganda",
    "github": "https://github.com/okirorinnocent",
    "linkedin": "https://www.linkedin.com/in/innocent-okiror-2793443b0",
    "whatsapp": "https://wa.me/256726278320",
    "x": "https://x.com/innocent_okiror",
}

PROJECTS = [
    {
        "title": "OKIROR'S AI: Intelligent Workspace Companion",
        "category": "Artificial Intelligence",
        "desc": "A dark-themed conversational AI assistant powered by Google Gemini, with customizable persona instructions and session history management.",
        "tech": ["Python", "Streamlit", "Google GenAI SDK", "CSS"],
        "github": "https://github.com/okirorinnocent/4G",
        "demo": "https://evbmr2bmurgs3snobraabe.streamlit.app/",
        "status": "Completed",
    },
    {
        "title": "Weather Prediction ML Pipeline",
        "category": "Machine Learning",
        "desc": "A Streamlit app that loads trained model artifacts (.pkl) with Joblib to deliver weather forecasts and feature inference.",
        "tech": ["Python", "Streamlit", "Scikit-Learn", "Joblib", "Matplotlib", "NumPy"],
        "github": "https://github.com/okirorinnocent/model",
        "demo": "https://p4x9y2gikjoog9i4evnrkq.streamlit.app/",
        "status": "Completed",
    },
    {
        "title": "CASMI26 Molecule ID & Mass Spectra Predictor",
        "category": "Machine Learning",
        "desc": "An end-to-end pipeline using Random Forest to process Parquet mass spectrometry data and predict SMILES molecular structures.",
        "tech": ["Python", "Streamlit", "Scikit-Learn", "Pandas", "PyArrow", "NumPy"],
        "github": "https://github.com/okirorinnocent/KASUN",
        "demo": "https://mxyli76bszrcffkapu7bik.streamlit.app/",
        "status": "Completed",
    },
]

# Self-assessed levels out of 100, grouped so the chart tells a story
SKILLS = {
    "Strongest": {
        "Prompt Engineering": 85,
        "Productivity Tools": 85,
        "AI Tools": 82,
    },
    "Growing": {
        "Information Literacy": 70,
        "Office Suite": 60,
        "Web Apps (Streamlit)": 50,
        "Cloud & IoT Concepts": 45,
    },
    "Foundations": {
        "Python Programming": 30,
        "C Programming": 30,
    },
}

# ---------------------------------------------------------------
# DATABASE
# ---------------------------------------------------------------


@st.cache_resource
def init_connection() -> Client | None:
    try:
        return create_client(
            st.secrets["SUPABASE_URL"].strip(),
            st.secrets["SUPABASE_KEY"].strip(),
        )
    except Exception as err:  # missing secrets or bad URL
        st.session_state["db_error"] = str(err)
        return None


@st.cache_data(ttl=60, show_spinner=False)
def load_messages(limit: int = 20) -> pd.DataFrame:
    client = init_connection()
    if client is None:
        return pd.DataFrame()
    rows = (
        client.table("guestbook")
        .select("name, message, created_at")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
        .data
    )
    return pd.DataFrame(rows)


supabase = init_connection()

# ---------------------------------------------------------------
# STYLING (works in light and dark mode)
# ---------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title { font-weight: 800; font-size: 2.5rem; line-height: 1.2; }
    .sub-title  { opacity: .75; font-size: 1.15rem; margin-bottom: 1.5rem; }
    .tech-tag {
        display: inline-block; background: #e0e7ff; color: #3730a3;
        font-size: .75rem; font-weight: 600; padding: 4px 10px;
        border-radius: 9999px; margin: 0 6px 6px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------
with st.sidebar:
    try:
        st.image("profile.png", use_container_width=True)
    except FileNotFoundError:
        st.markdown("<h1 style='text-align:center;'>👤</h1>",
                    unsafe_allow_html=True)

    st.markdown(f"## {PROFILE['name']}")
    st.caption("👨‍💻 Computer Science Student @ MUST")
    st.caption("🤖 AI & Software Engineering")
    st.divider()

    st.markdown("### 📞 Contact")
    st.write(f"📩 {PROFILE['email']}")
    st.write(f"📍 {PROFILE['location']}")

    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("GitHub", PROFILE["github"], use_container_width=True)
    st.link_button("WhatsApp", PROFILE["whatsapp"], use_container_width=True)
    st.link_button("X (Twitter)", PROFILE["x"], use_container_width=True)

    st.divider()
    try:
        with open("my_cv.pdf", "rb") as f:
            st.download_button(
                "📄 Download My CV",
                data=f,
                file_name="Innocent_Okiror_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        pass  # visitors shouldn't see setup notes; hide the button instead

    st.divider()
    st.info(
        "💡 **Mission:** Building scalable software and AI solutions "
        "for real-world problems in East Africa."
    )

# ---------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------
st.markdown(
    f'<div class="main-title">{PROFILE["name"]}</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">BSc. Computer Science Student | '
    "Mbarara University of Science and Technology</div>",
    unsafe_allow_html=True,
)

h1, h2, h3, h4 = st.columns(4)
h1.metric("Institution", "MUST", "BSc. CS")
h2.metric("Focus", "Software & AI", "Python / C")
h3.metric("Certification", "Seeta Univ.", "AI Tools")
h4.metric("Projects", len(PROJECTS), "live demos")

st.divider()

tab_projects, tab_about, tab_skills, tab_guestbook = st.tabs(
    ["🚀 Projects", "🏠 About", "🛠️ Skills", "📝 Guestbook"]
)

# ---------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------
with tab_projects:
    st.header("Featured Projects")

    categories = ["All"] + sorted({p["category"] for p in PROJECTS})
    c1, c2 = st.columns([2, 1])
    query = c1.text_input("🔍 Search by keyword or tech", "").strip().lower()
    category = c2.selectbox("Category", categories)

    def matches(p: dict) -> bool:
        haystack = " ".join([p["title"], p["desc"], *p["tech"]]).lower()
        return query in haystack and category in ("All", p["category"])

    shown = [p for p in PROJECTS if matches(p)]
    if not shown:
        st.info("No projects match your search.")

    for p in shown:
        with st.container(border=True):
            info, links = st.columns([3, 1])
            with info:
                st.subheader(p["title"])
                st.caption(f"**{p['category']}** | `{p['status']}`")
                st.write(p["desc"])
                st.markdown(
                    "".join(
                        f'<span class="tech-tag">{t}</span>' for t in p["tech"]),
                    unsafe_allow_html=True,
                )
            with links:
                st.link_button(
                    "💻 GitHub", p["github"], use_container_width=True)
                st.link_button(
                    "🚀 Live Demo", p["demo"], use_container_width=True)

# ---------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------
with tab_about:
    text, img = st.columns([2, 1])
    with text:
        st.header("My Journey")
        st.write(
            """
            I am pursuing a degree in **Computer Science at Mbarara University of
            Science and Technology (MUST)**. My foundation was built at
            **Teso College Aloet**, where I developed analytical discipline and
            logical thinking.

            After earning a **Certificate in Artificial Intelligence** from
            **Seeta University**, I now focus on software architecture, cyber
            security, and machine learning, with the goal of building systems that
            protect data, automate workflows, and empower businesses in Uganda and
            beyond.
            """
        )
        st.subheader("🎓 Education & Credentials")
        st.markdown(
            """
            - **BSc. Computer Science**, *Mbarara University of Science and Technology*
            - **Certificate in Artificial Intelligence**, *Seeta University*
            - **UCE & UACE**, *Teso College Aloet*
            """
        )
    with img:
        try:
            st.image("school.png", caption="Academic Roots",
                     use_container_width=True)
        except FileNotFoundError:
            st.info("🎓 Mbarara University of Science and Technology")

# ---------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------
with tab_skills:
    st.header("Technical Competencies")

    s1, s2, s3 = st.columns(3)
    with s1.container(border=True):
        st.markdown("#### 💻 Languages")
        st.markdown("- Python\n- C\n- SQL (Supabase)")
    with s2.container(border=True):
        st.markdown("#### 🛠️ Tools")
        st.markdown(
            "- Streamlit\n- Pandas & NumPy\n- Scikit-Learn\n- Git & GitHub")
    with s3.container(border=True):
        st.markdown("#### 🤖 Domains")
        st.markdown(
            "- Software Engineering\n- Machine Learning\n- Data Analysis")

    st.divider()
    st.subheader("Proficiency")
    st.caption("Self-assessed, and updated as I learn.")
    for group, items in SKILLS.items():
        st.markdown(f"**{group}**")
        for skill, level in items.items():
            st.progress(level / 100, text=f"{skill}: {level}%")

# ---------------------------------------------------------------
# GUESTBOOK
# ---------------------------------------------------------------
with tab_guestbook:
    st.header("Community Guestbook")

    if supabase is None:
        st.warning("The guestbook is temporarily unavailable.")
    else:
        with st.form("guestbook_form", clear_on_submit=True):
            name = st.text_input("Your name / organization", max_chars=60)
            message = st.text_area("Your message", max_chars=500)
            honeypot = st.text_input(
                "Leave this empty", key="hp", label_visibility="collapsed")
            submitted = st.form_submit_button("Submit")

        if submitted:
            if honeypot:  # bots fill hidden-looking fields
                st.stop()
            if not name.strip() or not message.strip():
                st.warning("Please fill in both your name and a message.")
            else:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name.strip(), "message": message.strip()}
                    ).execute()
                    load_messages.clear()
                    st.success("Thank you! Your message has been posted.")
                except Exception:
                    st.error(
                        "Could not submit your message. Please try again later.")

        st.subheader("Recent messages")
        try:
            df = load_messages()
        except Exception:
            df = pd.DataFrame()
            st.caption("Could not load messages right now.")

        if df.empty:
            st.caption("No messages yet. Be the first!")
        else:
            for _, row in df.iterrows():
                with st.container(border=True):
                    # st.write/caption are safe: no raw HTML from visitors
                    st.write(row["message"])
                    when = pd.to_datetime(
                        row.get("created_at"), errors="coerce")
                    stamp = when.strftime("%d %b %Y") if pd.notna(when) else ""
                    st.caption(
                        f"— {row['name']} {('· ' + stamp) if stamp else ''}")

# ---------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------
st.divider()
st.caption(
    f"© {datetime.now().year} {PROFILE['name']} | "
    "Built with Python & Streamlit @ MUST"
)
