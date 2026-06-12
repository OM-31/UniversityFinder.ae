import streamlit as st
import pandas as pd
import pydeck as pdk
from datetime import date

# 1. System Main Configuration
st.set_page_config(
    page_title="UAE University Intelligence Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global Configurations and Compliance Data Assets
LEGAL_TEXT = """
1. Core Technology Statement: This matching application is natively conceptualized, configured, and constructed using Gemini artificial intelligence models. All structural scoring parameters, design parameters, and code components were deployed via machine-learning workflow structures.
2. Verification Mandate: Tuition frames, grade requirements, entrance scoring metrics, and localized coordinate tracks serve as diagnostic reference fields. Users are strictly mandated to complete secondary individual data verification processes directly via live campus registry offices or matching records maintained on the Knowledge and Human Development Authority (KHDA) database archives prior to completing financial or academic commitments.
3. Disclaimers: System engineers assume zero tracking legal liabilities for processing adjustments, administrative changes, fee modifications, or criteria restructurings introduced by institutions over time.
"""

# Enterprise Glassmorphism Design Language
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #09090b 0%, #171721 100%);
        color: #f8fafc;
    }
    section[data-testid="stSidebar"] {
        background-color: rgba(9, 9, 11, 0.9) !important;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 2rem;
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(56, 189, 248, 0.4);
    }
    .main-title {
        font-size: 2.75rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(90deg, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
    }
    .subtitle-text { color: #64748b; font-size: 1.1rem; margin-bottom: 2.5rem; }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #38bdf8 !important;
    }
    .status-likely { color: #34d399; font-weight: bold; }
    .status-possible { color: #fbbf24; font-weight: bold; }
    .status-unlikely { color: #f87171; font-weight: bold; }
    hr { border-color: rgba(255,255,255,0.05); }
    </style>
""", unsafe_allow_html=True)

# Application State Initialization
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# Date Context for Countdowns
CURRENT_DATE = date(2026, 6, 12)

# 2. Comprehensive Metric Framework Dataset
@st.cache_data
def get_dataset():
    return [
        {
            "name": "American University of Sharjah (AUS)",
            "emirat": "Sharjah", "website": "https://www.aus.edu",
            "min_fee": 110876, "lat": 25.3115, "lon": 55.4914,
            "min_grade": 80, "ielts": 6.5, "sat_score": 1100,
            "ranking": "Top 350 Globally (QS)", "acceptance_rate": 25,
            "housing_score": 8, "curriculum": "American Liberal Arts & STEM",
            "deadline_date": date(2026, 7, 15),
            "majors": ["Architecture", "Civil Engineering", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Accounting", "Finance", "Marketing"]
        },
        {
            "name": "University of Sharjah (UOS)",
            "emirat": "Sharjah", "website": "https://www.sharjah.ac.ae",
            "min_fee": 42000, "lat": 25.2882, "lon": 55.4772,
            "min_grade": 70, "ielts": 5.0, "sat_score": 1000,
            "ranking": "Top 600 Globally (QS)", "acceptance_rate": 45,
            "housing_score": 7, "curriculum": "Dual Arab-International Framework",
            "deadline_date": date(2026, 8, 1),
            "majors": ["Medicine", "Dental Surgery", "Pharmacy", "Nursing", "Cyber Security", "Law", "Graphic Design", "Accounting", "Business Administration"]
        },
        {
            "name": "American University in Dubai (AUD)",
            "emirat": "Dubai", "website": "https://www.aud.edu",
            "min_fee": 85000, "lat": 25.0945, "lon": 55.1561,
            "min_grade": 75, "ielts": 6.0, "sat_score": 1050,
            "ranking": "Top 650 Globally (QS)", "acceptance_rate": 30,
            "housing_score": 8, "curriculum": "US Traditional Collegiate Curriculum",
            "deadline_date": date(2026, 7, 30),
            "majors": ["Architecture", "Interior Design", "Business Administration", "Finance", "Accounting", "Journalism"]
        },
        {
            "name": "University of Wollongong in Dubai (UOWD)",
            "emirat": "Dubai", "website": "https://www.uowdubai.ac.ae",
            "min_fee": 58000, "lat": 25.1032, "lon": 55.1636,
            "min_grade": 70, "ielts": 6.0, "sat_score": 1000,
            "ranking": "Top 200 Globally (UOW Australia)", "acceptance_rate": 55,
            "housing_score": 6, "curriculum": "Australian Higher Education Framework",
            "deadline_date": date(2026, 8, 20),
            "majors": ["Business", "Finance", "Accounting", "Computer Science", "Cyber Security", "Software Engineering"]
        },
        {
            "name": "Heriot-Watt University Dubai",
            "emirat": "Dubai", "website": "https://www.hw.ac.uk/dubai",
            "min_fee": 65000, "lat": 25.1012, "lon": 55.4022,
            "min_grade": 75, "ielts": 6.0, "sat_score": 1050,
            "ranking": "Top 300 Globally (QS)", "acceptance_rate": 60,
            "housing_score": 7, "curriculum": "British Specialized Curriculum",
            "deadline_date": date(2026, 9, 1),
            "majors": ["Mechanical Engineering", "Data Science", "Software Engineering", "Business Administration", "Accounting", "Psychology"]
        },
        {
            "name": "University of Birmingham Dubai",
            "emirat": "Dubai", "website": "https://www.birmingham.ac.uk/dubai",
            "min_fee": 115000, "lat": 25.1051, "lon": 55.4044,
            "min_grade": 85, "ielts": 6.5, "sat_score": 1200,
            "ranking": "Top 100 Globally (QS)", "acceptance_rate": 15,
            "housing_score": 8, "curriculum": "UK Russell Group Research Model",
            "deadline_date": date(2026, 7, 1),
            "majors": ["Computer Science", "Artificial Intelligence", "Biomedical Science", "Law", "Finance", "Business Management"]
        },
        {
            "name": "Khalifa University (KU)",
            "emirat": "Abu Dhabi", "website": "https://www.ku.ac.ae",
            "min_fee": 81250, "lat": 24.4608, "lon": 54.3963,
            "min_grade": 80, "ielts": 6.0, "sat_score": 1250,
            "ranking": "Top 200 Globally (QS)", "acceptance_rate": 20,
            "housing_score": 9, "curriculum": "Advanced Research-Intensive STEM",
            "deadline_date": date(2026, 6, 30),
            "majors": ["Aerospace Engineering", "Chemical Engineering", "Computer Engineering", "Computer Science"]
        },
        {
            "name": "New York University Abu Dhabi (NYUAD)",
            "emirat": "Abu Dhabi", "website": "https://nyuad.nyu.edu",
            "min_fee": 230000, "lat": 24.5241, "lon": 54.4344,
            "min_grade": 90, "ielts": 7.5, "sat_score": 1450,
            "ranking": "Top 30 Globally (NYU Track)", "acceptance_rate": 4,
            "housing_score": 10, "curriculum": "Elite Global Liberal Arts Model",
            "deadline_date": date(2026, 11, 1),
            "majors": ["Interactive Media", "Economics", "Political Science", "Computer Science", "Mathematics"]
        }
    ]

universities = get_dataset()
all_majors = sorted(list(set(m for uni in universities for m in uni.get("majors", []))))

# Analytics Variables
avg_market_tuition = sum([u["min_fee"] for u in universities]) / len(universities)

# Calculate Complex Scores Dynamically
for u in universities:
    days_left = (u["deadline_date"] - CURRENT_DATE).days
    u["days_left"] = max(0, days_left)

    housing_pts = (u["housing_score"] / 10) * 40
    acc_pts = ((100 - u["acceptance_rate"]) / 100) * 20
    rank_pts = 40
    u["campus_score"] = int(housing_pts + acc_pts + rank_pts)

# Header Structure
st.markdown('<div class="main-title">UAE University Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Commercial-grade admissions forecasting, structural academic screening, and comparative analytics.</div>', unsafe_allow_html=True)

# 3. Sidebar Diagnostic Submission Interface
with st.sidebar.form(key="screening_form"):
    st.markdown("### Profile Screening Matrix")
    selected_regions = st.multiselect("Target Jurisdictions", ["Sharjah", "Dubai", "Abu Dhabi"], default=["Sharjah", "Dubai", "Abu Dhabi"])
    selected_major = st.selectbox("Intended Major", options=["Select discipline..."] + [m.title() for m in all_majors])
    max_budget = st.slider("Annual Budget Ceiling (AED)", 40000, 250000, 140000, 5000)

    st.markdown("---")
    st.markdown("### Academic Diagnostics")
    user_grade = st.slider("High School Performance (%)", 50, 100, 85)
    user_ielts = st.slider("IELTS Academic Level", 4.0, 9.0, 6.5, 0.5)
    user_sat = st.slider("SAT Score Equivalent", 800, 1600, 1150, 50)

    execute_analysis = st.form_submit_button(label="RUN DIAGNOSTIC SCREENING", use_container_width=True)

# Calculate Scholarship Eligibility Engine for Match Report
def estimate_scholarship(grade, sat):
    if grade >= 95 and sat >= 1400: return "Estimated 40-50% Merit Allocation"
    elif grade >= 90 and sat >= 1250: return "Estimated 25-35% Merit Allocation"
    elif grade >= 85 and sat >= 1100: return "Estimated 10-20% Merit Allocation"
    return "Standard Eligibility Pool"

# 4. Master Navigation Framework
tab_home, tab_match, tab_favorites, tab_map, tab_charts = st.tabs([
    "Executive Dashboard", "AI Admissions Engine", "Saved Favorites Comparison", "Interactive Campus Map", "Rankings & Analytics"
])

# --- TAB 1: EXECUTIVE DASHBOARD ---
with tab_home:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="glass-card"><h4 style='margin:0; color:#94a3b8;'>Indexed Hubs</h4><h2 style='margin:0; color:#38bdf8;'>8</h2></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="glass-card"><h4 style='margin:0; color:#94a3b8;'>Market Avg Tuition</h4><h2 style='margin:0; color:#38bdf8;'>AED {int(avg_market_tuition):,}</h2></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="glass-card"><h4 style='margin:0; color:#94a3b8;'>Total Program Tracks</h4><h2 style='margin:0; color:#38bdf8;'>48+</h2></div>""", unsafe_allow_html=True)

    st.markdown("### Structural Platform Architecture")
    f1, f2 = st.columns(2)
    with f1:
        st.markdown("""
        <div class="glass-card">
            <h4>Admissions Probability Engine & Weakness Detector</h4>
            <p style='color:#94a3b8;'>Processes grade profiles against mandatory benchmarks, flags parameter deficits, and outputs dynamic entry assessments.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
            <h4>Interactive Geospatial Mapping</h4>
            <p style='color:#94a3b8;'>Visualize institutional coordinates and evaluate geographical infrastructure positioning across the United Arab Emirates.</p>
        </div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown("""
        <div class="glass-card">
            <h4>Dynamic Bookmarked Comparison Framework</h4>
            <p style='color:#94a3b8;'>Aggregates individual favorites into an analytical matrix layout to assess competing requirements instantly.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
            <h4>Global Matrix Analytics</h4>
            <p style='color:#94a3b8;'>Delivers isolated analytical charts evaluating selectivity parameters and institutional tuition boundaries safely.</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: AI ADMISSIONS ENGINE (WITH WEAKNESS DETECTOR & FUZZY MATCH) ---
with tab_match:
    if not execute_analysis or selected_major == "Select discipline...":
        st.info("Configure your academic specifications inside the left filter container and click 'RUN DIAGNOSTIC SCREENING' to generate evaluation diagnostics.")
    else:
        st.markdown("### Admissions Probability Index")
        target_mj_lower = selected_major.lower()
        evaluated_unis = []

        for u in universities:
            # 1. Check Region Hard Constraint
            if u["emirat"] not in selected_regions:
                continue

            # 2. Advanced Fuzzy Substring Match for Majors
            major_matched = False
            for m in u["majors"]:
                if target_mj_lower in m.lower() or m.lower() in target_mj_lower:
                    major_matched = True
                    break

            if not major_matched:
                continue

            # 3. Check Budget Hard Constraint
            if max_budget < u["min_fee"]:
                continue

            # Match scoring calculation
            grade_score = min(100, (user_grade / u["min_grade"]) * 100)
            ielts_score = min(100, (user_ielts / u["ielts"]) * 100)
            sat_score = min(100, (user_sat / u["sat_score"]) * 100)
            total_match = (grade_score * 0.4) + (ielts_score * 0.3) + (sat_score * 0.3)
            total_match = min(99, max(10, total_match))

            if total_match >= 90: status, color = "Likely", "status-likely"
            elif total_match >= 75: status, color = "Possible", "status-possible"
            else: status, color = "Unlikely", "status-unlikely"

            # Weakness Detector Tracking Engine
            weaknesses = []
            if user_grade < u["min_grade"]:
                weaknesses.append(f"High School performance profile ({user_grade}%) falls below institutional entrance baseline ({u['min_grade']}%).")
            if user_ielts < u["ielts"]:
                weaknesses.append(f"IELTS Language assessment score ({user_ielts}) is lower than minimum prerequisite framework ({u['ielts']}).")
            if user_sat < u["sat_score"]:
                weaknesses.append(f"SAT Standardized diagnostic equivalent ({user_sat}) registers below historical benchmark standards ({u['sat_score']}).")

            evaluated_unis.append({
                "data": u, "match": total_match, "status": status, "color": color, "weaknesses": weaknesses
            })

        evaluated_unis.sort(key=lambda x: x["match"], reverse=True)

        if not evaluated_unis:
            st.warning("No institutional metrics align with your active filters. Try expanding your Budget Ceiling or selecting additional regions.")
        else:
            st.success(f"Successfully mapped {len(evaluated_unis)} universities offering programs matching your criteria.")
            for item in evaluated_unis:
                u = item["data"]
                match_val = int(item["match"])

                with st.container():
                    st.markdown(f"""
                    <div class="glass-card">
                        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                            <div>
                                <h3 style="margin:0;">{u['name']}</h3>
                                <p style="color:#94a3b8; font-size:0.9rem; margin-top:2px;">{u['emirat']} Region Hub | <b>{u['days_left']} Days Left to Apply</b></p>
                            </div>
                            <div style="text-align:right;">
                                <h2 style="margin:0; color:#38bdf8;">{match_val}% Match</h2>
                                <p class="{item['color']}" style="margin:0;">Simulated Status: {item['status']}</p>
                            </div>
                        </div>
                        <div style="margin-top:1rem; padding: 10px 15px; background: rgba(255,255,255,0.02); border-radius: 8px;">
                            <p style="margin:0; font-size:0.9rem; color:#94a3b8;"><b>Annual Tuition Cost:</b> AED {u['min_fee']:,} | <b>Prerequisites:</b> GPA {u['min_grade']}% | IELTS {u['ielts']} | SAT {u['sat_score']}</p>
                        </div>
                    """, unsafe_allow_html=True)

                    # Weakness Detector Output Layer
                    if item["weaknesses"]:
                        st.markdown("<p style='color:#f87171; font-weight:bold; margin-bottom:4px; font-size:0.9rem;'>WARNING — APPLICATION WEAKNESSES DETECTED:</p>", unsafe_allow_html=True)
                        for w in item["weaknesses"]:
                            st.markdown(f"<p style='color:#fca5a5; font-size:0.88rem; margin:0 0 4px 12px;'>• {w}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown("<p style='color:#34d399; font-weight:bold; margin-top:5px; font-size:0.9rem;'>PROFILE COMPLIANT — All basic entrance baseline requirements met comfortably.</p>", unsafe_allow_html=True)

                    # Additional Data Display
                    st.markdown(f"""
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1.5rem;">
                            <div>
                                <p style="margin:0; font-size:0.8rem; color:#94a3b8; text-transform:uppercase;">Overall Campus Score</p>
                                <p style="margin:0; font-size:1.2rem; font-weight:bold;">{u['campus_score']} / 100</p>
                            </div>
                            <div>
                                <p style="margin:0; font-size:0.8rem; color:#94a3b8; text-transform:uppercase;">Scholarship Estimate</p>
                                <p style="margin:0; font-size:0.95rem; font-weight:bold; color:#34d399;">{estimate_scholarship(user_grade, user_sat)}</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if u['name'] in st.session_state.favorites:
                        if st.button("Remove from Saved Favorites", key=f"rem_{u['name']}"):
                            st.session_state.favorites.remove(u['name'])
                            st.rerun()
                    else:
                        if st.button("Save to Favorites Portfolio", type="primary", key=f"add_{u['name']}"):
                            st.session_state.favorites.append(u['name'])
                            st.rerun()

# --- TAB 3: DYNAMIC SAVED FAVORITES COMPARISON ---
with tab_favorites:
    st.markdown("### Bookmarked Institutional Portfolio Matrix")
    if not st.session_state.favorites:
        st.info("No universities currently saved to portfolio. Browse the 'AI Admissions Engine' to bookmark choices.")
    else:
        saved_unis = [u for u in universities if u["name"] in st.session_state.favorites]

        comparison_records = []
        for s in saved_unis:
            comparison_records.append({
                "Institution Name": s["name"],
                "Jurisdiction Hub": s["emirat"],
                "Annual Tuition (AED)": f"AED {s['min_fee']:,}",
                "Required GPA Threshold": f"{s['min_grade']}%",
                "Mandatory IELTS": s["ielts"],
                "Mandatory SAT": s["sat_score"],
                "Acceptance Rate": f"{s['acceptance_rate']}%",
                "Campus Score Index": f"{s['campus_score']} / 100"
            })

        df_comparison = pd.DataFrame(comparison_records).set_index("Institution Name")
        st.dataframe(df_comparison, use_container_width=True)

        if st.button("Purge Saved Favorites Portfolio"):
            st.session_state.favorites = []
            st.rerun()

# --- TAB 4: GEOSPATIAL MAP ---
with tab_map:
    st.markdown("### Interactive Geographical Node Projection Matrix")
    st.caption("Hover over markers to track structural institutional location mappings.")

    geo_df = pd.DataFrame([
        {"lat": u["lat"], "lon": u["lon"], "name": u["name"], "ranking": u["ranking"]} for u in universities
    ])

    view_state_nodes = pdk.ViewState(latitude=25.1300, longitude=55.2800, zoom=9, pitch=0)

    node_layer = pdk.Layer(
        "ScatterplotLayer",
        data=geo_df,
        get_position="[lon, lat]",
        get_color="[239, 68, 68, 220]",
        get_radius=700,
        pickable=True,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[node_layer],
        initial_view_state=view_state_nodes,
        map_provider="carto",
        map_style="dark",
        tooltip={
            "html": """
            <div style='font-family:sans-serif; font-size:12px; padding:10px; color:#fff; background-color:#020617; border:1px solid #1e293b; border-radius:6px; line-height:1.4;'>
                <b>{name}</b><br>
                <span style='color:#38bdf8;'>Tracking Bracket: {ranking}</span>
            </div>
            """
        }
    ))

# --- TAB 5: RANKINGS & ANALYTICS DASHBOARD ---
with tab_charts:
    st.markdown("### System-Wide Analytics Projections")

    df_analytics = pd.DataFrame(universities)

    col_c1, col_c2 = st.columns(2, gap="large")
    with col_c1:
        st.markdown("#### Annual Fixed Academic Tuition Fees (AED)")
        df_tuit = df_analytics[["name", "min_fee"]].sort_values("min_fee", ascending=True).set_index("name")
        st.bar_chart(df_tuit, color="#f87171")

        st.markdown("#### Acceptance Selectivity Rate (%)")
        df_acc = df_analytics[["name", "acceptance_rate"]].sort_values("acceptance_rate", ascending=True).set_index("name")
        st.bar_chart(df_acc, color="#fbbf24")

    with col_c2:
        st.markdown("#### Overall Campus Infrastructure Score (Out of 100)")
        df_camp = df_analytics[["name", "campus_score"]].sort_values("campus_score", ascending=True).set_index("name")
        st.bar_chart(df_camp, color="#34d399")

# Corporate Legal Disclaimer Framework
st.markdown("<br><br><br>", unsafe_allow_html=True)
with st.expander("LEGAL DISCLAIMER & COMPLIANCE NOTICE"):
    st.markdown(f"<div style='font-size:0.85rem; color:#94a3b8; line-height:1.6; font-family:sans-serif;'>{LEGAL_TEXT}</div>", unsafe_allow_html=True)
