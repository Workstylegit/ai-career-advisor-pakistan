import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="AI Career Advisor | Pakistan",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------
# 🎓 University Database (Fall 2026 Official Prospectus Data)
# --------------------------
uni_data = pd.DataFrame([
    {
        "University": "NUST Islamabad",
        "Type": "Public / Sector",
        "Programs": "BS CS, BS AI, BS SE, BS Electrical Engg, BS ME, BS Data Science, BBA",
        "Eligibility": "Matric ≥60%, FSc/ICS ≥60%; A‑Levels with IBCC Equivalence",
        "Entry Test": "NET (Compulsory)",
        "Merit Range": "85% – 92%",
        "Fee/Semester (PKR)": "190,000 – 260,000",
        "Admission Period": "15 May – 30 June 2026",
        "Deadline": "15 July 2026",
        "Career Scope": "Top industry, govt, research; Starting 70,000 – 180,000 PKR",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "COMSATS University Islamabad",
        "Type": "Public",
        "Programs": "BS CS, BS AI, BS SE, BS Cyber Security, BBA, BS Electrical",
        "Eligibility": "Matric ≥50%, FSc/ICS ≥50%; A‑Levels with IBCC Equivalence",
        "Entry Test": "CUI Entry / NTS",
        "Merit Range": "75% – 88%",
        "Fee/Semester (PKR)": "90,000 – 130,000",
        "Admission Period": "01 June – 25 July 2026",
        "Deadline": "20 August 2026",
        "Career Scope": "Strong IT & corporate sector; Starting 50,000 – 120,000 PKR",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "FAST‑NUCES Islamabad",
        "Type": "Private",
        "Programs": "BS CS, BS AI, BS SE, BS Data Science",
        "Eligibility": "Matric ≥60%, FSc/ICS ≥60%; A‑Levels with IBCC Equivalence",
        "Entry Test": "FAST Entry Test",
        "Merit Range": "82% – 90%",
        "Fee/Semester (PKR)": "150,000 – 190,000",
        "Admission Period": "20 May – 10 July 2026",
        "Deadline": "20 July 2026",
        "Career Scope": "Leading software industry; Starting 80,000 – 200,000 PKR",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "International Islamic University (IIUI)",
        "Type": "Public",
        "Programs": "BS CS, BS SE, BBA, BS Electrical Engg, BS Social Sciences",
        "Eligibility": "Matric ≥50%, FSc/ICS ≥50%; A‑Levels with IBCC Equivalence",
        "Entry Test": "Not Required",
        "Merit Range": "60% – 75%",
        "Fee/Semester (PKR)": "40,000 – 70,000",
        "Admission Period": "10 June – 30 July 2026",
        "Deadline": "25 August 2026",
        "Career Scope": "Affordable options; Public & private roles; Starting 35,000 – 85,000 PKR",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "Air University Islamabad",
        "Type": "Semi‑Government",
        "Programs": "BS CS, BS SE, BS Electrical Engg, BBA, BS Aerospace",
        "Eligibility": "Matric ≥60%, FSc ≥60%; A‑Levels with IBCC Equivalence",
        "Entry Test": "AU Entry Test",
        "Merit Range": "78% – 86%",
        "Fee/Semester (PKR)": "110,000 – 150,000",
        "Admission Period": "05 June – 20 July 2026",
        "Deadline": "05 August 2026",
        "Career Scope": "Aviation, IT, defense sectors; Starting 55,000 – 130,000 PKR",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "NUTECH Islamabad",
        "Type": "Public",
        "Programs": "BS CS, BS SE, BS Civil, BS Electrical, BS Mechatronics",
        "Eligibility": "Matric ≥55%, FSc ≥55%; A‑Levels with IBCC Equivalence",
        "Entry Test": "NUTECH Entry / NTS",
        "Merit Range": "70% – 82%",
        "Fee/Semester (PKR)": "85,000 – 145,000",
        "Admission Period": "15 June – 25 July 2026",
        "Deadline": "10 August 2026",
        "Career Scope": "Engineering & tech industries; Starting 50,000 – 110,000 PKR",
        "HEC Recognized": "✅ Yes"
    }
])

# --------------------------
# 🖥️ App Interface
# --------------------------
st.title("🎓 AI Career Advisor — For Pakistani Students")
st.markdown("**Source**: Official Fall 2026 University Prospectuses | All universities are HEC‑Recognized")
st.write("Enter your marks, study stream, and budget to see eligible universities, criteria, fees, deadlines & career scope.")

# Inputs
col1, col2, col3 = st.columns(3)
marks = col1.number_input("Intermediate / A‑Level Percentage", min_value=33, max_value=100, value=65)
stream = col2.selectbox("Study Stream", ["FSc Pre‑Engineering", "FSc Pre‑Medical", "ICS / Computer Science", "Commerce", "Arts / Humanities"])
budget = col3.number_input("Max Budget per Semester (in thousands PKR)", min_value=20, max_value=300, value=150)

# Filter logic
if st.button("🔍 Find My Universities", type="primary"):
    def extract_min_pct(text):
        try:
            return int(text.split("≥")[1].split("%")[0])
        except:
            return 50

    def extract_max_fee(text):
        try:
            return int(text.split("–")[1].replace(",", "").strip())
        except:
            return 300000

    df = uni_data.copy()
    df["Min_Req"] = df["Eligibility"].apply(extract_min_pct)
    df["Max_Fee"] = df["Fee/Semester (PKR)"].apply(extract_max_fee)

    results = df[
        (marks >= df["Min_Req"]) &
        (budget * 1000 <= df["Max_Fee"])
    ].drop(columns=["Min_Req", "Max_Fee"]).reset_index(drop=True)

    if not results.empty:
        st.success(f"✅ Found {len(results)} matching universities!")
        st.dataframe(results, use_container_width=True)
    else:
        st.warning("⚠️ No matches found. Try increasing your marks or budget.")

st.info("ℹ️ For reference only — always verify details from official university websites.")
