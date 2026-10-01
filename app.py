import base64
import json
from datetime import datetime

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
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
ROLES = [
    "BSc. Computer Science Student",
    "AI & Machine Learning Enthusiast",
    "Python & Streamlit Developer",
]

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

TIMELINE = [
    ("BSc. Computer Science", "Mbarara University of Science and Technology (MUST)", "Now"),
    ("Certificate in Artificial Intelligence", "Seeta University", ""),
    ("UCE & UACE", "Teso College Aloet", ""),
]

# ---------------------------------------------------------------
# ICONS
# Simple Icons removed the LinkedIn logo from its CDN, which is why the
# LinkedIn icon went missing. It is embedded here as an inline SVG instead,
# so it can never break.
# ---------------------------------------------------------------
_LINKEDIN_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="#fff" d="'
    "M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 "
    "107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2"
    "-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 "
    '87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg>'
)
_LINKEDIN_URI = "data:image/svg+xml;base64," + \
    base64.b64encode(_LINKEDIN_SVG.encode()).decode()


def icon_src(slug: str) -> str:
    return _LINKEDIN_URI if slug == "linkedin" else f"https://cdn.simpleicons.org/{slug}/ffffff"


def social_html(labelled: bool = False) -> str:
    """One line per tag, no leading indentation (markdown would treat it as code)."""
    links = []
    for label, url, color, slug in SOCIALS:
        extra = " wa" if slug == "whatsapp" else ""
        text = f"<span>{label}</span>" if labelled else ""
        links.append(
            f'<a class="soc{extra}" href="{url}" target="_blank" rel="noopener" '
            f'title="{label}" style="background:{color}">'
            f'<img src="{icon_src(slug)}" alt="{label}">{text}</a>'
        )
    cls = "socials labelled" if labelled else "socials"
    return f'<div class="{cls}">{"".join(links)}</div>'


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
# PAGE STYLES
# ---------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
.stApp { background: #f1f5f9; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
.block-container { padding-top: 1.2rem; max-width: 1200px; }

@keyframes fadeUp { from {opacity:0; transform:translateY(24px);} to {opacity:1; transform:none;} }
@keyframes grow   { from {transform:scaleX(0);} to {transform:scaleX(1);} }
@keyframes pulse  { 0%{box-shadow:0 0 0 0 rgba(37,211,102,.55);} 70%{box-shadow:0 0 0 12px rgba(37,211,102,0);} 100%{box-shadow:0 0 0 0 rgba(37,211,102,0);} }

/* social icons */
.socials { display:flex; flex-wrap:wrap; gap:12px; }
.soc { display:inline-flex; align-items:center; gap:8px; padding:10px; border-radius:12px; text-decoration:none !important;
    color:#fff !important; font-size:.85rem; font-weight:600; transition: transform .2s ease, box-shadow .2s ease; }
.soc img { width:20px; height:20px; display:block; }
.soc:hover { transform: translateY(-4px) scale(1.06); box-shadow: 0 10px 20px rgba(0,0,0,.3); }
.soc.wa { animation: pulse 2.4s infinite; }
.socials.labelled { flex-direction:column; }
.socials.labelled .soc { padding:10px 14px; }

/* tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
.stTabs [data-baseweb="tab"] { border-radius: 10px; padding: 8px 18px; font-weight:600; transition: background .2s ease; }
.stTabs [data-baseweb="tab"]:hover { background: #e0e7ff; }
.stTabs [data-baseweb="tab-panel"] { animation: fadeUp .6s ease both; }

/* bordered containers become animated cards */
div[data-testid="stVerticalBlockBorderWrapper"] { background:#fff; border-radius:16px; animation: fadeUp .7s ease both;
    transition: transform .25s ease, box-shadow .25s ease; }
div[data-testid="stVerticalBlockBorderWrapper"]:hover { transform: translateY(-4px); box-shadow: 0 16px 30px -12px rgba(15,23,42,.25); }

.tech-tag { display:inline-block; background:#e0e7ff; color:#3730a3; font-size:.75rem; font-weight:600;
    padding:4px 12px; border-radius:999px; margin:0 6px 6px 0; transition: background .2s, color .2s; }
.tech-tag:hover { background:#4338ca; color:#fff; }

/* skill bars */
.skill { margin-bottom: 14px; }
.skill-top { display:flex; justify-content:space-between; font-weight:600; font-size:.9rem; color:#0f172a; margin-bottom:6px; }
.bar { height:10px; background:#e2e8f0; border-radius:999px; overflow:hidden; }
.fill { height:100%; border-radius:999px; background: linear-gradient(90deg, #4338ca, #3b82f6);
    transform-origin:left; animation: grow 1.3s cubic-bezier(.22,1,.36,1) both; }
.group-title { font-weight:800; color:#1e3a8a; margin: 18px 0 10px; font-size:1.05rem; }

/* timeline */
.tl { border-left:3px solid #c7d2fe; margin:12px 0 0 8px; padding-left:24px; }
.tl-item { position:relative; margin-bottom:22px; animation: fadeUp .7s ease both; }
.tl-item::before { content:""; position:absolute; left:-33px; top:5px; width:14px; height:14px; border-radius:50%;
    background:#4338ca; box-shadow:0 0 0 4px #e0e7ff; }
.tl-title { font-weight:800; color:#0f172a; }
.tl-sub { color:#475569; font-size:.95rem; }
.tl-now { display:inline-block; margin-left:8px; font-size:.7rem; font-weight:700; color:#fff; background:#16a34a;
    padding:2px 8px; border-radius:999px; }

/* sidebar */
section[data-testid="stSidebar"] { background:#fff; border-right:1px solid #e2e8f0; }
section[data-testid="stSidebar"] img { border-radius: 16px; }
h2, h3 { color:#0f172a; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
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
# HERO: interactive particle network, typing roles, count-up stats
# (runs in an iframe because Streamlit markdown cannot execute JavaScript)
# ---------------------------------------------------------------
HERO_TEMPLATE = """
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',sans-serif;background:transparent;overflow:hidden}
.hero{position:relative;height:100vh;border-radius:20px;overflow:hidden;color:#fff;
 background:linear-gradient(120deg,#0b1224,#1e3a8a,#4338ca,#0b1224);background-size:300% 300%;
 animation:grad 14s ease infinite;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
@keyframes grad{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes up{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(37,211,102,.55)}70%{box-shadow:0 0 0 12px rgba(37,211,102,0)}100%{box-shadow:0 0 0 0 rgba(37,211,102,0)}}
canvas{position:absolute;inset:0;width:100%;height:100%}
.content{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;padding:0 48px}
.badge{align-self:flex-start;padding:6px 14px;border-radius:999px;font-size:.85rem;font-weight:500;
 background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);margin-bottom:14px;animation:up .8s both}
.name{font-size:clamp(2rem,5.5vw,3.8rem);font-weight:800;line-height:1.1;animation:up .8s .1s both;
 background:linear-gradient(90deg,#fff,#c7d2fe);-webkit-background-clip:text;background-clip:text;color:transparent}
.role{font-size:clamp(1.05rem,2.4vw,1.45rem);font-weight:500;color:#c7d2fe;min-height:2rem;margin-top:8px;animation:up .8s .2s both}
.cursor{display:inline-block;width:2px;height:1.1em;background:#c7d2fe;margin-left:3px;vertical-align:-3px;animation:blink 1s steps(2) infinite}
@keyframes blink{50%{opacity:0}}
.text{max-width:620px;color:#e2e8f0;line-height:1.6;margin:10px 0 20px;animation:up .8s .3s both}
.socials{display:flex;flex-wrap:wrap;gap:12px;animation:up .8s .4s both}
.soc{display:inline-flex;padding:10px;border-radius:12px;transition:transform .2s,box-shadow .2s}
.soc img{width:20px;height:20px;display:block}
.soc:hover{transform:translateY(-4px) scale(1.08);box-shadow:0 10px 22px rgba(0,0,0,.4)}
.soc.wa{animation:pulse 2.4s infinite}
.counters{display:flex;gap:34px;margin-top:26px;animation:up .8s .5s both}
.num{font-size:1.9rem;font-weight:800}
.lbl{font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:#a5b4fc;font-weight:600}
@media(max-width:640px){.content{padding:0 22px}.text{display:none}.counters{gap:20px;margin-top:18px}.num{font-size:1.4rem}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
</style></head><body>
<div class="hero" id="hero">
<canvas id="c"></canvas>
<div class="content">
 <div class="badge">👋 Welcome to my portfolio</div>
 <div class="name">__NAME__</div>
 <div class="role"><span id="typed"></span><span class="cursor"></span></div>
 <p class="text">I build practical software and AI tools, from conversational assistants to machine learning pipelines, at Mbarara University of Science and Technology.</p>
 __SOCIALS__
 <div class="counters">
  <div><div class="num" data-to="__PROJECTS__">0</div><div class="lbl">Projects</div></div>
  <div><div class="num" data-to="__TECHS__">0</div><div class="lbl">Technologies</div></div>
  <div><div class="num" data-to="1">0</div><div class="lbl">AI Certificate</div></div>
 </div>
</div>
</div>
<script>
(function(){
 var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 // typing effect
 var roles=__ROLES__, el=document.getElementById('typed'), r=0, i=0, del=false;
 function type(){
  var w=roles[r];
  el.textContent=w.substring(0,i);
  if(!del&&i===w.length){del=true;return setTimeout(type,1700)}
  if(del&&i===0){del=false;r=(r+1)%roles.length}
  i+=del?-1:1;
  setTimeout(type,del?28:55);
 }
 if(reduce){el.textContent=roles[0]}else{type()}
 // count-up
 document.querySelectorAll('.num').forEach(function(n){
  var to=+n.dataset.to,t0=null;
  function step(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1400,1);n.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(step)}
  if(reduce){n.textContent=to}else{setTimeout(function(){requestAnimationFrame(step)},600)}
 });
 // particle network
 var cv=document.getElementById('c'),ctx=cv.getContext('2d'),W,H,pts=[],mouse={x:null,y:null},dpr=window.devicePixelRatio||1;
 function size(){W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
  var n=Math.max(24,Math.min(70,Math.floor(W*H/14000)));pts=[];
  for(var k=0;k<n;k++)pts.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5})}
 size();window.addEventListener('resize',size);
 var hero=document.getElementById('hero');
 hero.addEventListener('mousemove',function(e){var b=cv.getBoundingClientRect();mouse.x=e.clientX-b.left;mouse.y=e.clientY-b.top});
 hero.addEventListener('mouseleave',function(){mouse.x=mouse.y=null});
 function draw(){
  ctx.clearRect(0,0,W,H);
  for(var a=0;a<pts.length;a++){
   var p=pts[a];p.x+=p.vx;p.y+=p.vy;
   if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;
   ctx.beginPath();ctx.arc(p.x,p.y,1.8,0,6.283);ctx.fillStyle='rgba(199,210,254,.85)';ctx.fill();
   for(var b=a+1;b<pts.length;b++){
    var q=pts[b],dx=p.x-q.x,dy=p.y-q.y,d=Math.sqrt(dx*dx+dy*dy);
    if(d<120){ctx.strokeStyle='rgba(165,180,252,'+(1-d/120)*.35+')';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.stroke()}
   }
   if(mouse.x!==null){var mx=p.x-mouse.x,my=p.y-mouse.y,md=Math.sqrt(mx*mx+my*my);
    if(md<150){ctx.strokeStyle='rgba(255,255,255,'+(1-md/150)*.6+')';ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(mouse.x,mouse.y);ctx.stroke();
     p.x+=mx/md*.6;p.y+=my/md*.6}}
  }
  requestAnimationFrame(draw);
 }
 if(!reduce)draw();
})();
</script></body></html>
"""


def hero_socials() -> str:
    parts = []
    for label, url, color, slug in SOCIALS:
        extra = " wa" if slug == "whatsapp" else ""
        parts.append(
            f'<a class="soc{extra}" href="{url}" target="_blank" rel="noopener" title="{label}" '
            f'style="background:{color}"><img src="{icon_src(slug)}" alt="{label}"></a>'
        )
    return '<div class="socials">' + "".join(parts) + "</div>"


unique_tech = {t for p in PROJECTS for t in p["tech"]}
hero_html = (
    HERO_TEMPLATE.replace("__NAME__", NAME)
    .replace("__SOCIALS__", hero_socials())
    .replace("__ROLES__", json.dumps(ROLES))
    .replace("__PROJECTS__", str(len(PROJECTS)))
    .replace("__TECHS__", str(len(unique_tech)))
)
components.html(hero_html, height=470)

tab_projects, tab_about, tab_skills, tab_guestbook, tab_contact = st.tabs(
    ["🚀 Projects", "🏠 About", "🛠️ Skills", "📝 Guestbook", "📬 Contact"]
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
        items = ""
        for i, (title, place, tag) in enumerate(TIMELINE):
            badge = f'<span class="tl-now">{tag}</span>' if tag else ""
            items += (
                f'<div class="tl-item" style="animation-delay:{i * 0.2:.1f}s">'
                f'<div class="tl-title">{title}{badge}</div><div class="tl-sub">{place}</div></div>'
            )
        st.markdown(f'<div class="tl">{items}</div>', unsafe_allow_html=True)
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
# CONTACT
# ---------------------------------------------------------------
with tab_contact:
    st.header("Let's work together")
    st.write(
        "Looking for a student developer for an AI, data, or web project, an internship, "
        "or a collaboration? Reach out on whichever channel suits you."
    )
    k1, k2, k3 = st.columns(3)
    k1.link_button("💬 Chat on WhatsApp",
                   SOCIALS[2][1], use_container_width=True)
    k2.link_button("✉️ Send an email",
                   f"mailto:{EMAIL}", use_container_width=True)
    k3.link_button("🔗 Connect on LinkedIn",
                   SOCIALS[0][1], use_container_width=True)
    st.write("")
    st.markdown(social_html(), unsafe_allow_html=True)

# ---------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------
st.write("")
st.divider()
st.markdown(social_html(), unsafe_allow_html=True)
st.caption(
    f"© {datetime.now().year} {NAME} | Built with Python & Streamlit @ MUST")
