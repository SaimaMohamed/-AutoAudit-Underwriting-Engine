import streamlit as st
import pandas as pd

st.set_page_config(page_title="AutoAudit | Underwriting Engine", layout="wide")

st.title("⚖️ AutoAudit: Policy Underwriting Engine")
st.markdown("### Automated Risk Assessment & Triage for Intact Insurance")

# 1. Configuration: Underwriting Rules
st.sidebar.header("⚙️ Underwriting Rule Configuration")
min_credit = st.sidebar.slider("Min Credit Score", 300, 850, 660)
min_age = st.sidebar.slider("Minimum Age", 16, 100, 21)
allow_prior_claims = st.sidebar.checkbox("Allow Prior Claims for Auto-Approval?", value=False)

# 2. Logic: The Triage Engine
def triage_application(score, age, claims):
    if score >= min_credit and age >= min_age and (not claims or allow_prior_claims):
        return "✅ Auto-Approved", "Low Risk"
    elif score < 500:
        return "❌ Declined", "High Risk"
    else:
        return "⚠️ Manual Review", "Medium Risk"

# 3. User Input Section
st.subheader("📝 New Policy Application")
col1, col2, col3 = st.columns(3)
name = col1.text_input("Applicant Name")
c_score = col2.number_input("Credit Score", 300, 850, 700)
age_input = col3.number_input("Age", 1, 100, 30)
claims_input = st.radio("Has Prior Claims?", [True, False], index=1)

if st.button("Process Application"):
    decision, risk_level = triage_application(c_score, age_input, claims_input)
    
    # 4. Observability: Displaying the result
    st.divider()
    if "Approved" in decision:
        st.success(f"**Result:** {decision} | **Risk Level:** {risk_level}")
    elif "Review" in decision:
        st.warning(f"**Result:** {decision} | **Risk Level:** {risk_level}")
    else:
        st.error(f"**Result:** {decision} | **Risk Level:** {risk_level}")
        
    st.info("💡 This triage logic automates defect prevention by flagging high-risk applications before they are finalized.")
