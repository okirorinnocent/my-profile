import pandas as pd
import streamlit as st
from supabase import Client, create_client

# --- 1. DATABASE CONNECTION ---


@st.cache_resource
def init_connection():
    try:
        url = st.secrets["SUPABASE_URL"].strip()
        key = st.secrets["SUPABASE_KEY"].strip()
        return create_client(url, key)
    except Exception:
        return None


supabase = init_connection()

# --- 2. PAGE CONFIGURATION & CUSTOM STYLING ---
st.set_page_config(
    page_title="Innocent Okiror | CS & AI Portfolio",
    page_icon="🎓",
    layout="wide",
)

# Custom CSS for a refined, classic theme
st.markdown(
    """
    <style>
    /* Main Background & Accent Colors */
    .stApp {
        background-color: #f8fafc;
    }

    /* Project Card Custom Styling */
    .project-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Tech Tag Badges */
    .tech-tag {
        display: inline-block;
        background-color: #e0e7ff;
        color: #3730a3;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 9999px;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    /* Classic Header Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        color: #0f172a;
        font-weight: 800;
        font-size: 2.5rem;
    }
    .sub-title {
        color: #475569;
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- 3. SIDEBAR (PROFILE, SOCIALS, DOWNLOADS) ---
with st.sidebar:
    try:
        st.image("profile.png", use_container_width=True)
    except Exception:
        st.markdown(
            "<h1 style='text-align: center;'>👤</h1>", unsafe_allow_html=True
        )

    st.markdown("## **Innocent Okiror**")
    st.caption("👨‍💻 Computer Science Student @ MUST")
    st.caption("🤖 AI & Software Engineering")
    st.divider()

    st.markdown("### 📞 Contacts & Profiles")
    st.write("📩 okirorinnocent49@gmail.com")
    st.write("📍 Mbarara / Kumi, Uganda")

    # Badges
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/innocent-okiror-2793443b0)"
    )
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)"
    )
    st.markdown(
        "[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/256726278320)"
    )
    st.markdown(
        "[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/innocent_okiror)"
    )

    st.divider()

    # Resume Download
    try:
        with open("my_cv.pdf", "rb") as file:
            st.download_button(
                label="📄 Download My CV",
                data=file,
                file_name="Innocent_Okiror_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except Exception:
        st.caption(
            "⚠️ Add 'my_cv.pdf' to your root directory to enable CV download."
        )

    st.divider()
    st.info(
        "💡 **Mission:** Developing scalable software and AI solutions to solve real-world problems in East Africa."
    )

# --- 4. MAIN HEADER ---
st.markdown(
    '<div class="main-title">Innocent Okiror</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">BSc. Computer Science Student | Mbarara University of Science and Technology</div>',
    unsafe_allow_html=True,
)

# Highlights Banner
h1, h2, h3 = st.columns(3)
with h1:
    st.metric(label="Institution", value="MUST", delta="BSc. CS")
with h2:
    st.metric(
        label="Focus Area",
        value="Software & AI",
        delta="Python / SQL / Web / C / Java",
    )
with h3:
    st.metric(label="Certification", value="Seeta Univ.", delta="AI TOOLS")

st.divider()

# --- 5. TAB NAVIGATION ---
tab_projects, tab_about, tab_skills, tab_guestbook = st.tabs(
    [
        "🚀 Projects & Portfolio",
        "🏠 About & Background",
        "🛠️ Technical Skills",
        "📝 Guestbook",
    ]
)

# ==========================================
# TAB 1: FEATURED PROJECTS SECTION
# ==========================================
with tab_projects:
    st.header("Featured Projects")
    st.caption(
        "Explore my latest software applications, web apps, and machine learning models."
    )

    projects = [
        {
            "title": "OKIROR'S AI — Intelligent Workspace Companion",
            "category": "Artificial Intelligence",
            "desc": "A custom dark-themed conversational AI workspace assistant powered by Google's Gemini models, featuring customizable persona instructions, custom CSS contrast styling, and session history management.",
            "tech": [
                "Python",
                "Streamlit",
                "Google GenAI SDK",
                "CSS Custom Styling",
            ],
            "github": "https://github.com/okirorinnocent/4G",
            "demo": "https://evbmr2bmurgs3snobraabe.streamlit.app/",
            "status": "Completed",
        },
        {
            "title": "Weather Prediction ML Pipeline",
            "category": "Artificial Intelligence",
            "desc": "An interactive Machine Learning web app built with Streamlit and Joblib that dynamically loads trained weather model artifacts (.pkl) to deliver real-time weather forecasting and feature inference.",
            "tech": [
                "Python",
                "Streamlit",
                "Scikit-Learn",
                "Joblib",
                "Matplotlib",
                "NumPy",
            ],
            "github": "https://github.com/okirorinnocent/model",
            "demo": "https://p4x9y2gikjoog9i4evnrkq.streamlit.app/",
            "status": "Completed",
        },
        {
            "title": "CASMI26 Molecule ID & Mass Spectra Predictor",
            "category": "Artificial Intelligence",
            "desc": "An end-to-end Machine Learning pipeline built with Streamlit and Random Forest to process Parquet mass spectrometry data and predict SMILES molecular structures.",
            "tech": [
                "Python",
                "Streamlit",
                "Scikit-Learn",
                "Pandas",
                "PyArrow",
                "NumPy",
            ],
            "github": "https://github.com/okirorinnocent/KASUN",
            "demo": "https://mxyli76bszrcffkapu7bik.streamlit.app/",
            "status": "Completed",
        },
    ]

    # Search & Filter Controls
    f_col1, f_col2 = st.columns([2, 1])
    with f_col1:
        search_query = st.text_input(
            "🔍 Search projects by keyword or tech...", ""
        )
    with f_col2:
        category_filter = st.selectbox(
            "Filter Category",
            [
                "All Categories",
                "Web Development",
                "Artificial Intelligence",
                "Database Engineering",
            ],
        )

    st.write("")  # Spacing

    # Display Filtered Projects in Grid
    filtered_projects = [
        p
        for p in projects
        if (
            category_filter == "All Categories"
            or p["category"] == category_filter
        )
        and (
            search_query.lower() in p["title"].lower()
            or search_query.lower() in " ".join(p["tech"]).lower()
        )
    ]

    if not filtered_projects:
        st.info("No projects match your search criteria.")

    for proj in filtered_projects:
        with st.container(border=True):
            col_info, col_links = st.columns([3, 1])

            with col_info:
                st.subheader(f"📌 {proj['title']}")
                st.caption(
                    f"**Category:** {proj['category']} | **Status:** `{proj['status']}`"
                )
                st.write(proj["desc"])

                # Render Tech Tags
                tags_html = "".join(
                    [
                        f'<span class="tech-tag">{t}</span>'
                        for t in proj["tech"]
                    ]
                )
                st.markdown(tags_html, unsafe_allow_html=True)

            with col_links:
                st.write("")
                st.write("")
                if proj["github"]:
                    st.link_button(
                        "💻 View GitHub",
                        proj["github"],
                        use_container_width=True,
                    )
                if proj["demo"]:
                    st.link_button(
                        "🚀 Live Demo", proj["demo"], use_container_width=True
                    )


# ==========================================
# TAB 2: ABOUT & BACKGROUND
# ==========================================
with tab_about:
    col_text, col_img = st.columns([2, 1])

    with col_text:
        st.header("My Journey")
        st.write(
            """
            I am currently pursuing a degree in **Computer Science at Mbarara University of Science and Technology (MUST)**.
            My educational foundation was built at **Teso College Aloet**, where I developed analytical discipline and logical thinking.

            Having earned a certification in **Artificial Intelligence** from **Seeta University**, I am blending administrative precision with advanced computing concepts.
            My goal is to design software architectures, Cyber Security and AI models(Machine Learning & Datascience) that enhance data integrity, automate workflows, and empower businesses in Uganda and across the globe.
            """
        )

        st.subheader("🎓 Education & Credentials")
        st.markdown(
            """
            - **BSc. Computer Science** — *Mbarara University of Science and Technology (MUST)*
            - **Certificate in Artificial Intelligence** — *Seeta University*
            - **Both Uganda Certificate of Education & Uganda Advanced Certificate of Education (UACE)** — *Teso College Aloet*
            """
        )

    with col_img:
        try:
            st.image(
                "school.png",
                caption="Academic Roots",
                use_container_width=True,
            )
        except Exception:
            st.info("🎓 Mbarara University of Science and Technology (MUST)")


# ==========================================
# TAB 3: TECHNICAL SKILLS & PROFICIENCY
# ==========================================
with tab_skills:
    st.header("Technical Competencies")

    sk1, sk2, sk3 = st.columns(3)
    with sk1:
        with st.container(border=True):
            st.markdown("#### 💻 Languages")
            st.markdown("- Python\n- C")
    with sk2:
        with st.container(border=True):
            st.markdown("#### 🛠️ Frameworks & Tools")
            st.markdown(
                "- Streamlit\n- Pandas & NumPy\n- Supabase \n- Git & GitHub"
            )
    with sk3:
        with st.container(border=True):
            st.markdown("#### 🤖 Core Domains")
            st.markdown(
                "- Software Engineering\n- AI Workflow Automation\n- Data Analysis"
            )

    st.divider()
    st.subheader("Proficiency Matrix")
    skills_df = pd.DataFrame(
        {
            "Skillset": [
                "Python Programming",
                "C Programming",
                "Web Apps (Streamlit)",
                "AI Tools",
                "Office Suite",
                "Prompt Engineering",
                "Information Literacy",
                "Cloud & IoT Concepts",
                "Productivity Tools",
                "Learning Strategies",
            ],
            "Proficiency Level (%)": [
                30,
                30,
                50,
                82,
                60,
                85,
                70,
                45,
                85,
                45,
            ],
        }
    )
    st.bar_chart(
        skills_df,
        x="Skillset",
        y="Proficiency Level (%)",
        color="#1d4ed8",
    )


# ==========================================
# TAB 4: GUESTBOOK
# ==========================================
# with tab_guestbook:
    st.header("Community Guestbook")
    st.write(
        "Feel free to leave a note or feedback. Messages are sent directly to my Supabase database."
    )

    if not supabase:
        st.warning(
            "⚠️ Database connection keys (`SUPABASE_URL`, `SUPABASE_KEY`) are missing in Streamlit secrets."
        )
    else:
        with st.form("guestbook_form", clear_on_submit=True):
            name_input = st.text_input("Your Name / Organization")
            message_input = st.text_area("Your Message")
            submitted = st.form_submit_button("Submit Message")

            if submitted and name_input and message_input:
                try:
                    supabase.table("guestbook").insert(
                        {"name": name_input, "message": message_input}
                    ).execute()
                    st.success("Thank you! Your message has been logged.")
                    st.balloons()
                except Exception as err:
                    st.error(f"Error submitting message: {err}")

# --- 6. FOOTER ---
st.divider()
st.caption(
    "© 2026 Innocent Okiror Contact +256763212490/+256726278320 | Built with Python, Streamlit  @ MUST"
)
