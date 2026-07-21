# ==============================================================================
# SMARTWAY VEHICLE CLASSIFICATION
# AI/ML Project by Prince Gajera
# BLOCK 1 - IMPORTS + PAGE CONFIGURATION
# ==============================================================================

import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

# ------------------------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------------------------

st.set_page_config(
    page_title="SmartWay Vehicle Classification",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------------------
# LOAD ML PIPELINE
# ------------------------------------------------------------------------------

MODEL_PATH = Path("models") / "smartway_pipeline.pkl"

try:

    pipeline = joblib.load(MODEL_PATH)

except Exception as e:

    st.error("❌ Unable to load SmartWay ML Pipeline")

    st.exception(e)

    st.stop()

# ------------------------------------------------------------------------------
# PAGE TITLE
# ------------------------------------------------------------------------------

# st.title("🚗 SmartWay Vehicle Classification")

# st.caption(
#     "Predict whether a vehicle qualifies as an EPA SmartWay vehicle using Machine Learning."
# )

# ==============================================================================
# BLOCK 2 - PREMIUM CSS
# ==============================================================================

st.markdown("""
<style>

/* ---------------- Main Background ---------------- */

.stApp{
    background:#0F172A;
}

/* ---------------- Page Width ---------------- */

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* ---------------- Hero Title ---------------- */

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:700;
    color:white;
}

.main-subtitle{
    text-align:center;
    color:#CBD5E1;
    font-size:18px;
}

/* ---------------- Premium Card ---------------- */

.card{

    background:linear-gradient(
    145deg,
    #1E293B,
    #0F172A);

    border-radius:24px;

    padding:28px;

    border:1px solid rgba(255,255,255,.08);

    box-shadow:0 15px 40px rgba(0,0,0,.35);

    margin-bottom:25px;

    transition:.35s;
}

.card:hover{

    transform:translateY(-8px);

    box-shadow:0 25px 60px rgba(37,99,235,.35);

}

/* ---------------- Card Heading ---------------- */

.card h1,
.card h2,
.card h3,
.card h4{

    color:white;

}

.card p{

    color:#CBD5E1;

}

/* ---------------- Section Title ---------------- */

.section-title{

    font-size:32px;

    font-weight:700;

    color:white;

    margin-bottom:10px;

}

.section-sub{

    color:#94A3B8;

    margin-bottom:25px;

}

/* ---------------- Metric Cards ---------------- */

.metric-card{

    background:#172554;

    padding:18px;

    border-radius:18px;

    border:1px solid rgba(255,255,255,.08);

}

/* ---------------- Green Badge ---------------- */

.badge{

    display:inline-block;

    padding:8px 18px;

    border-radius:30px;

    background:#16A34A;

    color:white;

    font-weight:600;

}

/* ---------------- Divider ---------------- */

hr{

    border:none;

    border-top:1px solid rgba(255,255,255,.08);

}

/* ---------------- Selectbox ---------------- */

.stSelectbox>div>div{

    border-radius:14px;

}

/* ---------------- Slider ---------------- */

.stSlider{

    padding-top:10px;

}

</style>
""",unsafe_allow_html=True)

# ==============================================================================
# BLOCK 2 - LOAD MODEL & DROPDOWN OPTIONS
# ==============================================================================

from pathlib import Path
import joblib

# ------------------------------------------------------------------------------
# LOAD TRAINED PIPELINE
# ------------------------------------------------------------------------------

MODEL_PATH = Path("models") / "smartway_pipeline.pkl"

pipeline = joblib.load(MODEL_PATH)

# ------------------------------------------------------------------------------
# DROPDOWN OPTIONS
# ------------------------------------------------------------------------------

YEAR_OPTIONS = list(range(2008, 2019))

FUEL_OPTIONS = [
    "Gasoline",
    "Diesel",
    "Gasoline/Electricity",
    "Electricity",
    "Ethanol",
    "Ethanol/Gas",
    "CNG",
    "Hydrogen"
]

DRIVE_OPTIONS = [
    "2WD",
    "4WD"
]

TRANSMISSION_OPTIONS = [
    "Automatic",
    "Manual",
    "CVT",
    "Semi Automatic"
]

VEHICLE_CLASS_OPTIONS = [
    "Small Car",
    "Midsize Car",
    "Large Car",
    "Small SUV",
    "Standard SUV",
    "Minivan",
    "Pickup",
    "Station Wagon",
    "Van",
    "Special Purpose"
]

STND_OPTIONS = [
    "LEV",
    "ULEV",
    "SULEV",
    "PZEV",
    "TZEV",
    "ZEV"
]

# ==============================================================================
# BLOCK 3 - HERO SECTION
# ==============================================================================

st.markdown("""

<div class="hero">

<h1>
🚗 SmartWay Vehicle Classification
</h1>

<p>

Predict whether a vehicle qualifies as an
EPA SmartWay Vehicle using Machine Learning.

</p>

</div>

""",unsafe_allow_html=True)

# ==============================================================================
# BLOCK 4 - SMARTWAY VEHICLE EXAMPLES
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">

<h1 style="color:white;">
🚘 Popular SmartWay Vehicles
</h1>

<p style="color:#94A3B8;font-size:18px;">
Examples of fuel-efficient and environmentally friendly vehicles
</p>

</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)

vehicles=[

("🔋","Tesla Model 3","Electric Vehicle"),

("🌿","Toyota Prius","Hybrid Vehicle"),

("⚡","Hyundai Ioniq","Hybrid / Electric"),

("🍃","Honda Insight","Hybrid Sedan")

]

for col,data in zip([c1,c2,c3,c4],vehicles):

    icon,name,desc=data

    with col:

        st.markdown(f"""

<div class="card" style="text-align:center;height:250px;">

<h1 style="font-size:60px;">
{icon}
</h1>

<h3>
{name}
</h3>

<p>
{desc}
</p>

<br>

<div class="badge">
✓ SmartWay Certified
</div>

</div>

""",unsafe_allow_html=True)

# ==============================================================================
# BLOCK 5 - PREMIUM VEHICLE INFORMATION
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="card">

<div class="section-title">

🚗 Vehicle Information

</div>

<div class="section-sub">

Select your vehicle specifications

</div>

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ------------------------------------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------------------------------------

with col1:

    year = st.selectbox(
        "📅 Model Year",
        YEAR_OPTIONS,
        key="year"
    )

    fuel = st.selectbox(
        "⛽ Fuel Type",
        FUEL_OPTIONS,
        key="fuel"
    )

    drive = st.selectbox(
        "🛞 Drive Type",
        DRIVE_OPTIONS,
        key="drive"
    )

# ------------------------------------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------------------------------------

with col2:

    vehicle_class = st.selectbox(
        "🚙 Vehicle Class",
        VEHICLE_CLASS_OPTIONS,
        key="vehicle_class"
    )

    transmission = st.selectbox(
        "⚙️ Transmission",
        TRANSMISSION_OPTIONS,
        key="transmission"
    )

# ------------------------------------------------------------------------------
# LIVE PREVIEW
# ------------------------------------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown(f"""
<div class="metric-card">
<h4>📅 Year</h4>
<h2>{year}</h2>
</div>
""", unsafe_allow_html=True)

with p2:
    st.markdown(f"""
<div class="metric-card">
<h4>⛽ Fuel</h4>
<h2>{fuel}</h2>
</div>
""", unsafe_allow_html=True)

with p3:
    st.markdown(f"""
<div class="metric-card">
<h4>🚙 Class</h4>
<h2>{vehicle_class}</h2>
</div>
""", unsafe_allow_html=True)

with p4:
    st.markdown(f"""
<div class="metric-card">
<h4>⚙️ Drive</h4>
<h2>{drive}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BLOCK 6 - PREMIUM ENGINE INFORMATION
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="card">

<div class="section-title">

⚙️ Engine Information

</div>

<div class="section-sub">

Engine performance and fuel economy

</div>

""", unsafe_allow_html=True)

left, right = st.columns(2)

# ------------------------------------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------------------------------------

with left:

    displ = st.slider(
        "🔧 Engine Size (Litres)",
        min_value=0.5,
        max_value=8.5,
        value=2.0,
        step=0.1,
        key="engine_size"
    )

    cyl = st.selectbox(
        "🛞 Number of Cylinders",
        [2,3,4,5,6,8,10,12,16],
        key="cyl"
    )

    city_mpg = st.number_input(
        "🏙️ City MPG",
        1,
        200,
        25,
        key="city"
    )

# ------------------------------------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------------------------------------

with right:

    hwy_mpg = st.number_input(
        "🛣️ Highway MPG",
        1,
        250,
        32,
        key="highway"
    )

    cmb_mpg = st.number_input(
        "🚘 Combined MPG",
        1,
        220,
        28,
        key="combined"
    )

# ------------------------------------------------------------------------------
# LIVE ENGINE DASHBOARD
# ------------------------------------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown(f"""
<div class="metric-card">

<h4>⚙️ Engine</h4>

<h2>{displ:.1f} L</h2>

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="metric-card">

<h4>🛞 Cylinders</h4>

<h2>{cyl}</h2>

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class="metric-card">

<h4>🏙️ City MPG</h4>

<h2>{city_mpg}</h2>

</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown(f"""
<div class="metric-card">

<h4>🛣️ Highway MPG</h4>

<h2>{hwy_mpg}</h2>

</div>
""",unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# FUEL EFFICIENCY STATUS
# ------------------------------------------------------------------------------

if cmb_mpg >= 40:

    st.success("🟢 Excellent Fuel Efficiency")

elif cmb_mpg >= 30:

    st.info("🔵 Good Fuel Efficiency")

elif cmb_mpg >= 20:

    st.warning("🟡 Average Fuel Efficiency")

else:

    st.error("🔴 Poor Fuel Efficiency")

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BLOCK 7 - ENVIRONMENTAL INTELLIGENCE
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="card">

<div class="section-title">

🌍 Environmental Intelligence

</div>

<div class="section-sub">

Analyze your vehicle's environmental impact

</div>

""", unsafe_allow_html=True)

left, right = st.columns(2)

# ------------------------------------------------------------------------------
# LEFT SIDE
# ------------------------------------------------------------------------------

with left:

    air_pollution = st.slider(
        "🌫 Air Pollution Score",
        0,
        10,
        7,
        key="air"
    )

    greenhouse = st.slider(
        "🌱 Greenhouse Gas Score",
        0,
        10,
        7,
        key="green"
    )

# ------------------------------------------------------------------------------
# RIGHT SIDE
# ------------------------------------------------------------------------------

with right:

    stnd = st.selectbox(
        "📄 Emission Standard",
        STND_OPTIONS,
        key="stnd"
    )

    eco_score = int((air_pollution + greenhouse) / 2 * 10)

    st.metric(
        "🌍 Eco Score",
        f"{eco_score}/100"
    )

# ------------------------------------------------------------------------------
# ECO STATUS
# ------------------------------------------------------------------------------

if eco_score >= 85:

    eco_status = "🟢 Excellent"

elif eco_score >= 70:

    eco_status = "🟢 Good"

elif eco_score >= 50:

    eco_status = "🟡 Average"

else:

    eco_status = "🔴 Poor"

st.progress(eco_score / 100)

st.markdown(f"""
<div class="metric-card">

<h2 style="text-align:center;">{eco_status}</h2>

<p style="text-align:center;">
Environmental Performance Rating
</p>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ENVIRONMENT SUMMARY
# ------------------------------------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(f"""
<div class="metric-card">

<h4>🌫 Pollution</h4>

<h2>{air_pollution}/10</h2>

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="metric-card">

<h4>🌱 Greenhouse</h4>

<h2>{greenhouse}/10</h2>

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class="metric-card">

<h4>📄 Standard</h4>

<h2>{stnd}</h2>

</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BLOCK 8 - LIVE VEHICLE DASHBOARD
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="card">

<div class="section-title">

🚗 Live Vehicle Dashboard

</div>

<div class="section-sub">

Real-time summary of your selected vehicle

</div>

""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# VEHICLE NAME
# ------------------------------------------------------------------------------

vehicle_name = f"{year} {vehicle_class}"

st.markdown(f"""

<h2 style="text-align:center;color:white;margin-top:10px;">
{vehicle_name}
</h2>

""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# METRIC CARDS
# ------------------------------------------------------------------------------

m1,m2,m3,m4 = st.columns(4)

with m1:

    st.metric(
        "⛽ Fuel",
        fuel
    )

with m2:

    st.metric(
        "⚙️ Engine",
        f"{displ:.1f} L"
    )

with m3:

    st.metric(
        "🛞 Cylinders",
        cyl
    )

with m4:

    st.metric(
        "📈 Combined MPG",
        cmb_mpg
    )

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# SECOND ROW
# ------------------------------------------------------------------------------

m5,m6,m7,m8 = st.columns(4)

with m5:

    st.metric(
        "🚙 Drive",
        drive
    )

with m6:

    st.metric(
        "⚙️ Transmission",
        transmission
    )

with m7:

    st.metric(
        "🌍 Eco Score",
        f"{eco_score}/100"
    )

with m8:

    efficiency = round((city_mpg + hwy_mpg) / 2)

    st.metric(
        "🚀 Avg MPG",
        efficiency
    )

# ------------------------------------------------------------------------------
# SMARTWAY CHANCE (UI ONLY)
# ------------------------------------------------------------------------------

chance = min(
    100,
    int(
        eco_score * 0.6 +
        cmb_mpg * 1.2
    )
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""

<h3 style="color:white;">

🎯 Estimated SmartWay Chance

</h3>

""", unsafe_allow_html=True)

st.progress(chance/100)

if chance >= 85:

    st.success(f"🟢 Excellent ({chance}%)")

elif chance >= 70:

    st.info(f"🔵 Good ({chance}%)")

elif chance >= 50:

    st.warning(f"🟡 Average ({chance}%)")

else:

    st.error(f"🔴 Low ({chance}%)")

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BLOCK 9 - AI PREDICTION ENGINE
# ==============================================================================

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button(
    "🚀 Analyze Vehicle",
    use_container_width=True,
    type="primary"
)

if analyze:

    # --------------------------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------------------------

    input_data = pd.DataFrame({

        "Air Pollution Score": [air_pollution],
        "City MPG": [city_mpg],
        "Cmb MPG": [cmb_mpg],
        "Cyl": [cyl],
        "Displ": [displ],
        "Drive": [drive],
        "Fuel": [fuel],
        "Greenhouse Gas Score": [greenhouse],
        "Hwy MPG": [hwy_mpg],
        "Stnd": [stnd],
        "Trans": [transmission],
        "Veh Class": [vehicle_class],
        "Year": [year]

    })

    # --------------------------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------------------------

    prediction = pipeline.predict(input_data)[0]

    probability = pipeline.predict_proba(input_data)[0]

    confidence = round(max(probability) * 100, 2)

    # Save values for next block
    st.session_state["prediction"] = prediction
    st.session_state["probability"] = probability
    st.session_state["confidence"] = confidence
    st.session_state["input_data"] = input_data

    # --------------------------------------------------------------------------
    # SUCCESS MESSAGE
    # --------------------------------------------------------------------------

    st.success("✅ Vehicle analyzed successfully!")

# ==============================================================================
# BLOCK 10 - AI RESULT DASHBOARD
# ==============================================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    confidence = st.session_state["confidence"]

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <div class="section-title">
    🤖 AI Prediction Result
    </div>

    <div class="section-sub">
    Machine Learning Prediction using Random Forest Pipeline
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    if prediction == "Yes":

        st.balloons()

        st.success("## ✅ SmartWay Certified Vehicle")

        status = "🟢 Excellent"

    else:

        st.error("## ❌ Not a SmartWay Vehicle")

        status = "🔴 Needs Improvement"

    # --------------------------------------------------------
    # Confidence
    # --------------------------------------------------------

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence/100)

    st.markdown("---")

    # --------------------------------------------------------
    # Vehicle Summary
    # --------------------------------------------------------

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("Fuel", fuel)

    with c2:
        st.metric("Engine", f"{displ:.1f} L")

    with c3:
        st.metric("Combined MPG", cmb_mpg)

    with c4:
        st.metric("Eco Score", f"{eco_score}/100")

    st.markdown("---")

    # --------------------------------------------------------
    # AI Explanation
    # --------------------------------------------------------

    st.subheader("🧠 Why AI Predicted This")

    reasons=[]

    if cmb_mpg>=30:
        reasons.append("✅ High Combined Fuel Economy")
    else:
        reasons.append("❌ Combined MPG is comparatively low")

    if city_mpg>=25:
        reasons.append("✅ Good City Mileage")
    else:
        reasons.append("⚠️ City Mileage can be improved")

    if hwy_mpg>=35:
        reasons.append("✅ Excellent Highway Mileage")
    else:
        reasons.append("⚠️ Highway Mileage is average")

    if greenhouse>=7:
        reasons.append("🌱 Low Greenhouse Emissions")
    else:
        reasons.append("❌ Greenhouse emissions are high")

    if air_pollution>=7:
        reasons.append("🌍 Good Air Pollution Score")
    else:
        reasons.append("⚠️ Air Pollution Score is low")

    if displ<=2.5:
        reasons.append("⚙️ Smaller Engine improves efficiency")
    else:
        reasons.append("⚠️ Large Engine consumes more fuel")

    if fuel in ["Electricity","Gasoline/Electricity"]:
        reasons.append("🔋 Eco-Friendly Fuel Type")

    elif fuel=="Gasoline":
        reasons.append("⛽ Conventional Fuel Vehicle")

    for r in reasons:
        st.write(r)

    st.markdown("---")

    # --------------------------------------------------------
    # Overall Rating
    # --------------------------------------------------------

    st.subheader("📊 Overall Vehicle Rating")

    st.info(status)

    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BLOCK 11 - DOWNLOAD REPORT
# ==============================================================================

if "prediction" in st.session_state:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <div class="section-title">
    📄 Download Prediction Report
    </div>

    <div class="section-sub">
    Export the vehicle analysis report
    </div>

    """, unsafe_allow_html=True)

    report = pd.DataFrame({

        "Feature":[

            "Year",
            "Fuel",
            "Drive",
            "Vehicle Class",
            "Transmission",
            "Engine Size",
            "Cylinder",
            "City MPG",
            "Highway MPG",
            "Combined MPG",
            "Air Pollution Score",
            "Greenhouse Score",
            "Emission Standard",
            "Eco Score",
            "Prediction",
            "Confidence"

        ],

        "Value":[

            year,
            fuel,
            drive,
            vehicle_class,
            transmission,
            displ,
            cyl,
            city_mpg,
            hwy_mpg,
            cmb_mpg,
            air_pollution,
            greenhouse,
            stnd,
            eco_score,
            prediction,
            f"{confidence:.2f}%"

        ]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        "📥 Download Report",

        csv,

        file_name="SmartWay_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.markdown("</div>", unsafe_allow_html=True)    

# ==============================================================================
# BLOCK 12 - PROFESSIONAL FOOTER
# ==============================================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:1px solid rgba(255,255,255,.08);">
""", unsafe_allow_html=True)

left, center, right = st.columns([1,2,1])

with center:

    st.markdown("""
    <div style="text-align:center;">

    <h2 style="color:white;">
    🚗 SmartWay Vehicle Classification
    </h2>

    <p style="color:#94A3B8;font-size:18px;">
    AI Powered Vehicle Environmental Analysis System
    </p>

    <br>

    <p style="color:#CBD5E1;">
    Developed with ❤️ using
    <b>Python • Streamlit • Scikit-learn • Machine Learning</b>
    </p>

    <br>

    <p style="color:#64748B;">
    © 2026 Prince Gajera
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)    