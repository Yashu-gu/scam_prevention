import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Cyber-Fraud Scam Shield",
    page_icon="🚨",
    layout="wide"
)

# Initialize Session State
if "scam_detected" not in st.session_state:
    st.session_state.scam_detected = False

st.title("🛡️ Cyber-Fraud Scam Shield: Live Defense Center")
st.markdown("### Real-Time Digital Arrest & Coercion Interception System")

# Layout: Two columns (Control Center vs Live Status)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 📥 Simulate Incoming Chat / Screen Content")
    user_input_text = st.text_area(
        "Paste suspicious text or chat log to test threat detection:",
        value="CBI Officer Notice: Digital arrest warrant issued for illegal package. Pay fine immediately via UPI to avoid police action.",
        height=120
    )
    
    # Trigger simulation buttons
    run_btn = st.button("🔍 Scan Screen Content Now", type="primary")
    
    if run_btn:
        # Simple threat matching logic for the demo
        text_lower = user_input_text.lower()
        threat_keywords = ["cbi", "police", "arrest", "warrant", "upi", "fine", "pay"]
        matches = [kw for kw in threat_keywords if kw in text_lower]
        
        score = len(matches) * 15  # Scaled score calculation
        if score > 100: score = 100
        
        if score >= 60 or "arrest" in text_lower:
            st.session_state.scam_detected = True
        else:
            st.session_state.scam_detected = False
            st.success("✅ Content looks safe. No active scam patterns found.")

with col2:
    st.markdown("#### ⚡ System Status")
    st.metric(label="Monitoring Engine", value="Active (ADB / OCR)")
    st.metric(label="Guardian API", value="Connected (Twilio)")
    
    # Emergency Manual Help / SOS Button
    st.markdown("---")
    st.markdown("#### 🆘 Panic / Help Button")
    if st.button("🚨 PRESS FOR IMMEDIATE HELP", type="secondary", use_container_width=True):
        st.session_state.scam_detected = True

# 🚨 POP-UP ALERT OVERLAY (Triggered when Scam Detected or Panic Button Pressed)
if st.session_state.scam_detected:
    st.error("### 🛑 CRITICAL WARNING: DIGITAL ARREST / FRAUD DETECTED!")
    
    # Styled warning container
    with st.container():
        st.warning(
            "**WARNING:** High-pressure psychological coercion or fake authority threat detected on screen. "
            "**DO NOT transfer any money, do not share OTPs, and do not disconnect.**"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("📞 Call Family Guardian Now", type="primary", use_container_width=True):
                st.toast("Emergency WhatsApp & SMS alert successfully dispatched to Guardian (+91 98765 43210)!")
        with c2:
            if st.button("❌ Dismiss Warning (I am safe)", use_container_width=True):
                st.session_state.scam_detected = False
                st.rerun()

# Footer notes for hackathon pitch
st.markdown("---")
st.markdown("*Hackathon MVP: Privacy-first local processing keeping user data completely secure.*")