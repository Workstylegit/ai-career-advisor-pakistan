import streamlit as st

# Page setup
st.set_page_config(page_title="AI Career Advisor | Pakistan", layout="wide")
st.title("🎓 AI Career Advisor — Islamabad, Pakistan")
st.markdown("**Source**: Official Fall 2026 University Prospectuses | All HEC‑Recognized")

# University data (no pandas needed)
universities = [
    {
        "University": "NUST Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Electrical Engg, BBA",
        "Min_Percent": 60,
        "Max_Fee": 260000,
        "Merit_Range": "85% – 92%",
        "Admission": "15 May – 30 June 2026",
        "Deadline": "15 July 2026",
        "Career": "70,000 – 180,000 PKR starting",
        "HEC": "✅ Yes"
    },
    {
        "University": "COMSATS University Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Cyber Security, BBA",
        "Min_Percent": 50,
        "Max_Fee": 130000,
        "Merit_Range": "75% – 88%",
        "Admission": "01 June – 25 July 2026",
        "Deadline": "20 August 2026",
        "Career": "50,000 – 120,000 PKR starting",
        "HEC": "✅ Yes"
    },
    {
        "University": "FAST‑NUCES Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Data Science",
        "Min_Percent": 60,
        "Max_Fee": 190000,
        "Merit_Range": "82% – 90%",
        "Admission": "20 May – 10 July 2026",
        "Deadline": "20 July 2026",
        "Career": "80,000 – 200,000 PKR starting",
        "HEC": "✅ Yes"
    },
    {
        "University": "International Islamic University (IIUI)",
        "Programs": "BS CS, BS SE, BBA, BS Electrical Engg",
        "Min_Percent": 50,
        "Max_Fee": 70000,
        "Merit_Range": "60% – 75%",
        "Admission": "10 June – 30 July 2026",
        "Deadline": "25 August 2026",
        "Career": "35,000 – 85,000 PKR starting",
        "HEC": "✅ Yes"
    },
    {
        "University": "Air University Islamabad",
        "Programs": "BS CS, BS SE, BS Electrical Engg, BBA",
        "Min_Percent": 60,
        "Max_Fee": 150000,
        "Merit_Range": "78% – 86%",
        "Admission": "05 June – 20 July 2026",
        "Deadline": "05 August 2026",
        "Career": "55,000 – 130,000 PKR starting",
        "HEC": "✅ Yes"
    }
]

# Inputs
marks = st.number_input("Your Intermediate / A‑Level Percentage", min_value=33, max_value=100, value=65)
stream = st.selectbox("Your Study Stream", ["FSc Pre‑Engineering", "FSc Pre‑Medical", "ICS / Computer Science", "Commerce", "Arts / Humanities"])
budget = st.number_input("Max Budget per Semester (thousands PKR)", min_value=20, max_value=300, value=150)

# Filter & show results
if st.button("🔍 Find My Universities", type="primary"):
    matches = []
    for uni in universities:
        if marks >= uni["Min_Percent"] and (budget * 1000) <= uni["Max_Fee"]:
            matches.append(uni)

    if matches:
        st.success(f"✅ Found {len(matches)} matching universities!")
        for u in matches:
            st.subheader(u["University"])
            st.write(f"**Programs**: {u['Programs']}")
            st.write(f"**Merit Range**: {u['Merit_Range']} | **Max Fee**: {u['Max_Fee']:,} PKR")
            st.write(f"**Admission**: {u['Admission']} | **Deadline**: {u['Deadline']}")
            st.write(f"**Career Scope**: {u['Career']} | **HEC Recognized**: {u['HEC']}")
            st.divider()
    else:
        st.warning("⚠️ No matches found. Try increasing your marks or budget.")

st.info("ℹ️ For reference only — always verify details from official university websites.")
