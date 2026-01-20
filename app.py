import streamlit as st
import time
import pandas as pd
from shah_armor import ShahArmor

# --- INITIALIZE SHAH ARMOR ---
# This checks for debuggers/VMs immediately
armor = ShahArmor()

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Shah Armor | Neural Vault", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a Professional "Cyber" Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c24; padding: 15px; border-radius: 10px; border: 1px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR & AUTHENTICATION ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/shield.png", width=80)
    st.title("Shah Armor Admin")
    st.write(f"Owner: **{armor.owner}**")
    st.markdown("---")
    
    user_key = st.text_input("🔑 License Access Key", type="password")
    
    st.markdown("---")
    st.info(f"Support: {armor.contact}")

# --- MAIN LOGIC GATE ---
if user_key == st.secrets["VALID_KEY"]:
    
    # NAVIGATION TABS
    tab1, tab2, tab3 = st.tabs(["📈 FTR Predictor", "🔒 Black Box Service", "📜 About Shah Armor"])

    # --- TAB 1: FTR PREDICTOR (Your Product) ---
    with tab1:
        st.header("Fractal Temporal Resonance Engine")
        st.write("Analyze chaotic data streams with Quantum-resilient math.")
        
        col_input, col_viz = st.columns([1, 1])
        
        with col_input:
            data_str = st.text_area("Input Stream (Comma Separated Values)", "10.5, 12.1, 11.8, 13.4, 12.9")
            if st.button("Run Resonance Analysis"):
                import engine
                try:
                    data = [float(x.strip()) for x in data_str.split(",")]
                    with st.status("Solving Fractal Equations...", expanded=False):
                        prediction = engine.predict_next(data)
                        time.sleep(1)
                    
                    st.metric("Predicted Value", prediction['prediction'])
                    st.progress(prediction['coherence_index']/100, text=f"Coherence: {prediction['coherence_index']}%")
                except Exception as e:
                    st.error("Data Format Error: Use numbers separated by commas.")

        with col_viz:
            if 'data' in locals():
                st.line_chart(pd.DataFrame(data, columns=["Signal"]))
                st.caption("Visualizing input frequency before FTR processing.")

    # --- TAB 2: BLACK BOX SERVICE (Your New Business) ---
    with tab2:
        st.header("Shah Armor: Black Box Wrapping")
        st.subheader("Turn your Python IP into an unbreakable Binary Vault.")
        
        st.markdown("""
        **What happens when you submit?**
        1. We inject **Sentinel Melt Protocols** into your logic.
        2. We compile your code into a **C-Binary (.pyd/.so)**.
        3. We add a **Hardware ID Lock** so it only runs on authorized PCs.
        """)
        
        with st.form("protection_form"):
            client_name = st.text_input("Your Name / Company")
            client_email = st.text_input("Email for Delivery")
            uploaded_code = st.file_uploader("Upload your Python Script (.py)", type="py")
            security_level = st.select_slider("Select Protection Level", options=["Standard", "High", "Melt-On-Sight"])
            
            submit_btn = st.form_submit_button("Request Black Box Quote")
            
            if submit_btn and uploaded_code:
                st.success(f"File '{uploaded_code.name}' received! Shanawaz Khan will contact you at {client_email} with the secure binary.")
                # Note: In a real app, you would use an email API (like SendGrid) here to notify you.

    # --- TAB 3: ABOUT & COMPETITORS ---
    with tab3:
        st.header("Intelligence Report")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**What we created:**")
            st.write("- **Self-Healing Logic:** Code deletes itself if debugged.")
            st.write("- **BCC Compilation:** Pure machine code execution.")
            st.write("- **Zero-Trace Memory:** Memory is wiped after calculation.")
        
        with col_b:
            st.write("**Competitive Edge:**")
            st.table({
                "Feature": ["Melt Protocol", "VM Detection", "Identity Stamp"],
                "Shah Armor": ["✅ Yes", "✅ Yes", "✅ Yes"],
                "Competitors": ["❌ No", "⚠️ Partial", "❌ No"]
            })

else:
    # ACCESS DENIED SCREEN
    st.warning("🛡️ SHAH ARMOR: System is currently in Vault Mode.")
    st.image("https://img.icons8.com/ios-filled/100/4CAF50/lock.png")
    st.write("Please enter your authorized license key in the sidebar to wake the engine.")
    
    with st.expander("New to Shah Armor?"):
        st.write(f"Shah Armor is a proprietary security layer for high-performance Python code. To purchase a key or protect your own code, contact **{armor.owner}** at **{armor.contact}**.")
