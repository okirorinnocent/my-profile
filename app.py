from datetime import datetime

import pandas as pd
import streamlit as st
from supabase import Client, create_client

st.set_page_config(
    page_title="Innocent Okiror | CS & AI Portfolio",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------------
# CONTENT: edit here, not in the layout code
# ---------------------------------------------------------------
NAME = "Innocent Okiror"
EMAIL = "okirorinnocent49@gmail.com"
LOCATION = "Mbarara / Kumi, Uganda"

# (label, url, brand colour, simple-icons slug)
SOCIALS = [
    ("LinkedIn", "https://www.linkedin.com/in/innocent-okiror-2793443b0",
     "#0A66C2", "linkedin"),
    ("GitHub", "https://github.com/okirorinnocent", "#181717", "github"),
    ("WhatsApp", "https://wa.me/256726278320", "#25D366", "whatsapp"),
    ("X", "https://x.com/innocent_okiror", "#000000", "x"),
    ("Email", f"mailto:{EMAIL}", "#EA4335", "gmail"),
]

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

SKILLS = {
    "Strongest": {"Prompt Engineering": 85, "Productivity Tools": 85, "AI Tools": 82},
    "Growing": {
        "Information Literacy": 70,
        "Office Suite": 60,
        "Web Apps (Streamlit)": 50,
        "Cloud & IoT Concepts": 45,
    },
    "Foundations": {"Python Programming": 30, "C Programming": 30},
}

# ---------------------------------------------------------------
# DATABASE
# ---------------------------------------------------------------


@st.cache_resource
def init_connection() -> Client | None:
    try:
        return create_client(
            st.secrets["SUPABASE_URL"].strip(
            ), st.secrets["SUPABASE_KEY"].strip()
        )
    except Exception:
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
# STYLES + ANIMATIONS
# ---------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
.stApp { background: #f1f5f9; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
.block-container { padding-top: 1.5rem; max-width: 1200px; }

/* ---------- keyframes ---------- */
@keyframes fadeUp   { from {opacity:0; transform:translateY(24px);} to {opacity:1; transform:none;} }
@keyframes gradient { 0%{background-position:0% 50%;} 50%{background-position:100% 50%;} 100%{background-position:0% 50%;} }
@keyframes float    { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-8px);} }
@keyframes roleFade { 0%{opacity:0; transform:translateY(12px);} 6%,30%{opacity:1; transform:none;} 36%,100%{opacity:0; transform:translateY(-12px);} }
@keyframes grow     { from {transform:scaleX(0);} to {transform:scaleX(1);} }
@keyframes pulse    { 0%{box-shadow:0 0 0 0 rgba(37,211,102,.5);} 70%{box-shadow:0 0 0 12px rgba(37,211,102,0);} 100%{box-shadow:0 0 0 0 rgba(37,211,102,0);} }

/* ---------- hero ---------- */
.hero {
    position: relative; overflow: hidden; border-radius: 20px; padding: 56px 48px; margin-bottom: 28px;
    background: linear-gradient(120deg, #0f172a, #1e3a8a, #4338ca, #0f172a);
    background-size: 300% 300%; animation: gradient 14s ease infinite, fadeUp .9s ease both;
    color: #fff; box-shadow: 0 20px 40px -15px rgba(30,58,138,.5);
}
.hero::after {
    content:""; position:absolute; right:-80px; top:-80px; width:300px; height:300px; border-radius:50%;
    background: radial-gradient(circle, rgba(255,255,255,.18), transparent 70%); animation: float 6s ease-in-out infinite;
}
.hero-badge { display:inline-block; padding:6px 14px; border-radius:999px; font-size:.85rem; font-weight:500;
    background: rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.25); margin-bottom:16px; }
.hero-name { font-size: clamp(2.2rem, 5vw, 3.6rem); font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
.hero-roles { position: relative; height: 2.2rem; font-size: 1.35rem; font-weight: 500; color: #c7d2fe; }
.hero-roles span { position:absolute; left:0; opacity:0; animation: roleFade 9s infinite; }
.hero-roles span:nth-child(2) { animation-delay: 3s; }
.hero-roles span:nth-child(3) { animation-delay: 6s; }
.hero-text { max-width: 640px; color: #e2e8f0; margin: 8px 0 22px; line-height: 1.6; }

/* ---------- social icons ---------- */
.socials { display:flex; flex-wrap:wrap; gap:12px; }
.soc { display:inline-flex; align-items:center; gap:8px; padding:10px; border-radius:12px; text-decoration:none !important;
    color:#fff !important; font-size:.85rem; font-weight:600; transition: transform .2s ease, box-shadow .2s ease; }
.soc img { width:20px; height:20px; display:block; }
.soc:hover { transform: translateY(-4px) scale(1.06); box-shadow: 0 10px 20px rgba(0,0,0,.3); }
.soc.wa { animation: pulse 2.4s infinite; }
.socials.labelled { flex-direction:column; }
.socials.labelled .soc { padding:10px 14px; }

/* ---------- stat cards ---------- */
.stats { display:grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap:16px; margin-bottom: 8px; }
.stat { background:#fff; border-radius:16px; padding:20px; border:1px solid #e2e8f0; animation: fadeUp .8s ease both;
    transition: transform .25s ease, box-shadow .25s ease; }
.stat:nth-child(2){animation-delay:.1s;} .stat:nth-child(3){animation-delay:.2s;} .stat:nth-child(4){animation-delay:.3s;}
.stat:hover { transform: translateY(-6px); box-shadow: 0 16px 28px -10px rgba(30,64,175,.35); }
.stat .lbl { font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:#64748b; font-weight:600; }
.stat .val { font-size:1.6rem; font-weight:800; color:#0f172a; margin:4px 0; }
.stat .sub { font-size:.85rem; color:#4338ca; font-weight:500; }

/* ---------- tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
.stTabs [data-baseweb="tab"] { border-radius: 10px; padding: 8px 18px; font-weight:600; transition: background .2s ease; }
.stTabs [data-baseweb="tab"]:hover { background: #e0e7ff; }
.stTabs [data-baseweb="tab-panel"] { animation: fadeUp .6s ease both; }

/* ---------- bordered containers become animated cards ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] { background:#fff; border-radius:16px; animation: fadeUp .7s ease both;
    transition: transform .25s ease, box-shadow .25s ease; }
div[data-testid="stVerticalBlockBorderWrapper"]:hover { transform: translateY(-4px); box-shadow: 0 16px 30px -12px rgba(15,23,42,.25); }

.tech-tag { display:inline-block; background:#e0e7ff; color:#3730a3; font-size:.75rem; font-weight:600;
    padding:4px 12px; border-radius:999px; margin:0 6px 6px 0; transition: background .2s, color .2s; }
.tech-tag:hover { background:#4338ca; color:#fff; }

/* ---------- skill bars ---------- */
.skill { margin-bottom: 14px; }
.skill-top { display:flex; justify-content:space-between; font-weight:600; font-size:.9rem; color:#0f172a; margin-bottom:6px; }
.bar { height:10px; background:#e2e8f0; border-radius:999px; overflow:hidden; }
.fill { height:100%; border-radius:999px; background: linear-gradient(90deg, #4338ca, #3b82f6);
    transform-origin:left; animation: grow 1.3s cubic-bezier(.22,1,.36,1) both; }
.group-title { font-weight:800; color:#1e3a8a; margin: 18px 0 10px; font-size:1.05rem; }

/* ---------- sidebar ---------- */
section[data-testid="stSidebar"] { background:#fff; border-right:1px solid #e2e8f0; }
section[data-testid="stSidebar"] img { border-radius: 16px; }

h2, h3 { color:#0f172a; }

@media (max-width: 640px) { .hero { padding: 36px 22px; } }
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
</style>
""",
    unsafe_allow_html=True,
)


def social_html(labelled: bool = False) -> str:
    """HTML must stay on one line per tag with no leading indentation (markdown would treat it as code)."""
    links = []
    for label, url, color, slug in SOCIALS:
        extra = " wa" if slug == "whatsapp" else ""
        text = f"<span>{label}</span>" if labelled else ""
        links.append(
            f'<a class="soc{extra}" href="{url}" target="_blank" rel="noopener" '
            f'title="{label}" style="background:{color}">'
            f'<img src="https://cdn.simpleicons.org/{slug}/ffffff" alt="{label}">{text}</a>'
        )
    cls = "socials labelled" if labelled else "socials"
    return f'<div class="{cls}">{"".join(links)}</div>'


# ---------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------
with st.sidebar:
    try:
        st.image("profile.png", use_container_width=True)
    except FileNotFoundError:
        st.markdown("<h1 style='text-align:center;'>👤</h1>",
                    unsafe_allow_html=True)

    st.markdown(f"## {NAME}")
    st.caption("👨‍💻 Computer Science Student @ MUST")
    st.caption("🤖 AI & Software Engineering")
    st.caption(f"📍 {LOCATION}")
    st.divider()

    st.markdown("##### Connect with me")
    st.markdown(social_html(labelled=True), unsafe_allow_html=True)
    st.write("")

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
        pass

    st.divider()
    st.info("💡 **Mission:** Building scalable software and AI solutions for real-world problems in East Africa.")

# ---------------------------------------------------------------
# HERO
# ---------------------------------------------------------------
hero = (
    '<div class="hero">'
    '<div class="hero-badge">👋 Welcome to my portfolio</div>'
    f'<div class="hero-name">{NAME}</div>'
    '<div class="hero-roles">'
    "<span>BSc. Computer Science Student</span>"
    "<span>AI &amp; Machine Learning Enthusiast</span>"
    "<span>Python &amp; Streamlit Developer</span>"
    "</div>"
    '<p class="hero-text">I build practical software and AI tools, from conversational assistants '
    "to machine learning pipelines, at Mbarara University of Science and Technology.</p>"
    f"{social_html()}"
    "</div>"
)
st.markdown(hero, unsafe_allow_html=True)

stats = [
    ("Institution", "MUST", "BSc. Computer Science"),
    ("Focus", "Software & AI", "Python · C · SQL"),
    ("Certification", "Seeta University", "AI Tools"),
    ("Projects", f"{len(PROJECTS)} live", "Deployed demos"),
]
st.markdown(
    '<div class="stats">'
    + "".join(
        f'<div class="stat"><div class="lbl">{a}</div><div class="val">{b}</div><div class="sub">{c}</div></div>'
        for a, b, c in stats
    )
    + "</div>",
    unsafe_allow_html=True,
)
st.write("")

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
                st.write("")
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

    st.subheader("Proficiency")
    st.caption("Self-assessed, and updated as I learn.")
    cols = st.columns(len(SKILLS))
    delay = 0.0
    for col, (group, items) in zip(cols, SKILLS.items()):
        html = f'<div class="group-title">{group}</div>'
        for skill, level in items.items():
            html += (
                f'<div class="skill"><div class="skill-top"><span>{skill}</span><span>{level}%</span></div>'
                f'<div class="bar"><div class="fill" style="width:{level}%;animation-delay:{delay:.1f}s"></div></div></div>'
            )
            delay += 0.15
        col.markdown(html, unsafe_allow_html=True)

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
            submitted = st.form_submit_button("Submit")

        if submitted:
            if not name.strip() or not message.strip():
                st.warning("Please fill in both your name and a message.")
            else:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name.strip(), "message": message.strip()}
                    ).execute()
                    load_messages.clear()
                    st.success("Thank you! Your message has been posted.")
                    st.balloons()
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
                    # plain text: visitors can't inject HTML
                    st.write(row["message"])
                    when = pd.to_datetime(
                        row.get("created_at"), errors="coerce")
                    stamp = when.strftime("%d %b %Y") if pd.notna(when) else ""
                    st.caption(f"— {row['name']}" +
                               (f" · {stamp}" if stamp else ""))

# ---------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------
st.write("")
st.divider()
st.markdown(social_html(), unsafe_allow_html=True)
st.caption(
    f"© {datetime.now().year} {NAME} | Built with Python & Streamlit @ MUST")
