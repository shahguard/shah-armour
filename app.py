import streamlit as st
import time
from shah_armor import ShahArmor

# Secure the environment
armor = ShahArmor()

st.set_page_config(page_title="Shah Armor FTR", page_icon="🛡️")

# Display your branding at the top
st.markdown(f"<p style='text-align: right; color: gray;'>{armor.get_stamp()}</p>", unsafe_allow_html=True)

st.title("🛡️ Shah Armor: FTR Predictor")

# Sidebar for License
st.sidebar.header("Authentication")
user_key = st.sidebar.text_input("Enter Shah Armor Key", type="password")

if user_key == st.secrets["VALID_KEY"]:
    st.sidebar.success("Verified: Shanawaz Khan")
    
    val_input = st.text_input("Enter data points (e.g., 10, 20, 30)", "1.5, 2.3, 1.8")
    
    if st.button("Calculate Fractal Resonance"):
        import engine # Imported only after validation
        data = [float(x.strip()) for x in val_input.split(",")]
        
        with st.spinner("Shah Armor analyzing..."):
            res = engine.predict_next(data)
            time.sleep(1)
            
        st.metric("FTR Prediction", res['prediction'])
        st.write(f"Confidence: {res['coherence_index']}%")
else:
    st.warning("Locked. Provide your Shah Armor key to continue.")
