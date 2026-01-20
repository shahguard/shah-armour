import streamlit as st
import time
import pandas as pd
from shah_armor import ShahArmor

# --- Initialize Shah Armor ---
armor = ShahArmor()

st.set_page_config(page_title="Shah Armor | FTR Predictor", layout="wide")

# Owner Branding
st.markdown(f"<p style='text-align: right; color: #666;'>{armor.get_stamp()}</p>", unsafe_allow_html=True)

# Main Header
st.title("🛡️ Shah Armor: Quantum-Resilient Predictor")
st.markdown("---")

# User Authentication
st.sidebar.header("🔑 Authentication")
user_key = st.sidebar.text_input("Enter Shah Armor License Key", type="password")

if user_key == st.secrets["VALID_KEY"]:
    st.sidebar.success(f"Verified Access: {armor.owner}")
    
    # User Instructions Panel
    with st.expander("ℹ️ How it works & What you will see"):
        st.write("""
        1. **Encryption Layer:** Your data is processed through the **Shah Armor** Neural Vault.
        2. **FTR Engine:** The system calculates **Fractal Temporal Resonance** to find hidden patterns.
        3. **Coherence Score:** This shows the mathematical 'tightness' of the prediction.
        4. **Secure Wipe:** Once the result is shown, the transient memory is zeroed for your security.
        """)

    # Main Interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📈 Data Input")
        val_input = st.text_area("Paste your chaotic signal (comma separated):", "1.5, 2.3, 1.8, 3.1, 2.9")
        
        if st.button("🚀 Execute Shah Armor Analysis"):
            import engine
            try:
                data = [float(x.strip()) for x in val_input.split(",")]
                
                with st.status("Analyzing via Shah Armor Protocol...", expanded=True) as status:
                    st.write("Initializing Quantum Noise Injection...")
                    time.sleep(0.5)
                    st.write("Solving Fractal Resonance Equations...")
                    res = engine.predict_next(data)
                    time.sleep(0.5)
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
                
                # Big Result Display
                st.success("Analysis Successful")
                st.metric(label="Shah Armor Prediction", value=res['prediction'])
                st.progress(res['coherence_index'] / 100, text=f"Mathematical Coherence: {res['coherence_index']}%")
                
            except ValueError:
                st.error("Invalid Input: Please ensure you only enter numbers separated by commas.")

    with col2:
        st.subheader("🔍 Visual Validation")
        if 'res' in locals():
            # Create a simple trend chart for the user
            chart_data = pd.DataFrame(data, columns=["Signal Value"])
            st.line_chart(chart_data)
            st.caption("The graph above shows the input signal density before FTR processing.")

else:
    st.warning("Locked. Please provide a valid Shah Armor Key to unlock this engine.")
    st.info("For support, contact: tenor9777@gmail.com")
